from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
# Translation system removed
import os
from functools import wraps
import pymysql

# Install PyMySQL as MySQLdb
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/onda_db_s'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration pour l'upload de fichiers
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'}

# Configuration removed

# Créer le dossier d'upload s'il n'existe pas
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Translation system completely removed

def save_uploaded_file(file, prefix=''):
    """Sauvegarde un fichier uploadé et retourne l'URL"""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Ajouter timestamp pour éviter les conflits
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        filename = f"{prefix}{timestamp}{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return f"uploads/{filename}"
    return None

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    cuisine_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    rating = db.Column(db.Float, default=0.0)
    image_url = db.Column(db.String(200))
    is_open = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # taxi, bus, tram, etc.
    city = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, default=0.0)
    contact_info = db.Column(db.String(100))
    image_url = db.Column(db.String(200))
    available = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)

class Shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50))  # mall, souk, market, etc.
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    opening_hours = db.Column(db.String(100))
    image_url = db.Column(db.String(200))
    is_open = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(200))

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # CREATE, UPDATE, DELETE
    entity_type = db.Column(db.String(50), nullable=False)  # User, Restaurant, Transport, Shopping
    entity_id = db.Column(db.Integer, nullable=True)  # ID of the affected entity
    entity_name = db.Column(db.String(200), nullable=True)  # Name of the affected entity
    description = db.Column(db.Text, nullable=False)  # Description of the action
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', backref=db.backref('activity_logs', lazy=True))

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(10), nullable=False)
    airline = db.Column(db.String(100), nullable=False)
    airport_id = db.Column(db.Integer, db.ForeignKey('airport.id'), nullable=False)
    destination = db.Column(db.String(100), nullable=False)  # Destination city
    flight_type = db.Column(db.String(20), nullable=False)  # 'departure' or 'arrival'
    scheduled_time = db.Column(db.DateTime, nullable=False)
    actual_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default='Scheduled')  # Scheduled, Delayed, Cancelled, Boarding, Departed, Arrived
    gate = db.Column(db.String(10), nullable=True)
    terminal = db.Column(db.String(10), nullable=True)
    aircraft_type = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    airport = db.relationship('Airport', backref=db.backref('flights', lazy=True))

# Nouveaux modèles pour les candidats
class CallForTenders(db.Model):
    """Modèle pour les appels d'offres"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    reference = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)  # Travaux, Services, Fournitures
    budget_min = db.Column(db.Float, nullable=True)
    budget_max = db.Column(db.Float, nullable=True)
    publication_date = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='active')  # active, closed, cancelled
    requirements = db.Column(db.Text)  # Conditions de participation
    contact_person = db.Column(db.String(100))
    contact_email = db.Column(db.String(120))
    contact_phone = db.Column(db.String(20))
    document_url = db.Column(db.String(200))  # Lien vers le PDF
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    creator = db.relationship('User', backref=db.backref('tenders', lazy=True))
    
    @property
    def is_active(self):
        return self.status == 'active' and self.deadline > datetime.utcnow()

class JobOffer(db.Model):
    """Modèle pour les offres d'emploi"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    reference = db.Column(db.String(50), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contract_type = db.Column(db.String(50), nullable=False)  # CDI, CDD, Stage, etc.
    experience_level = db.Column(db.String(50), nullable=False)  # Junior, Senior, Expert
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    benefits = db.Column(db.Text)
    salary_min = db.Column(db.Float, nullable=True)
    salary_max = db.Column(db.Float, nullable=True)
    publication_date = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='active')  # active, closed, cancelled
    contact_person = db.Column(db.String(100))
    contact_email = db.Column(db.String(120))
    contact_phone = db.Column(db.String(20))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    creator = db.relationship('User', backref=db.backref('job_offers', lazy=True))
    
    @property
    def is_active(self):
        return self.status == 'active' and self.deadline > datetime.utcnow()

class JobApplication(db.Model):
    """Modèle pour les candidatures"""
    id = db.Column(db.Integer, primary_key=True)
    job_offer_id = db.Column(db.Integer, db.ForeignKey('job_offer.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable pour candidatures publiques
    
    # Informations personnelles
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    
    # Informations professionnelles
    education_level = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    current_position = db.Column(db.String(100))
    skills = db.Column(db.Text)
    languages = db.Column(db.Text)
    
    # Pièces jointes (URLs vers les fichiers)
    cv_url = db.Column(db.String(200))  # Optionnel dans le modèle, obligatoire dans la validation
    cover_letter_url = db.Column(db.String(200))
    diploma_url = db.Column(db.String(200))
    other_documents_url = db.Column(db.String(500))  # JSON array of URLs
    
    # Lettre de motivation
    motivation_letter = db.Column(db.Text)
    
    # Statut et dates
    status = db.Column(db.String(20), default='pending')  # pending, reviewed, accepted, rejected
    tracking_code = db.Column(db.String(20), unique=True)  # Code de suivi unique
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
    reviewed_at = db.Column(db.DateTime)
    reviewed_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.Column(db.Text)  # Notes internes RH
    
    # Relationships
    job_offer = db.relationship('JobOffer', backref=db.backref('applications', lazy=True))
    applicant = db.relationship('User', foreign_keys=[user_id], backref=db.backref('applications', lazy=True))
    reviewer = db.relationship('User', foreign_keys=[reviewed_by])

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Accès administrateur requis.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(required_role):
    """Décorateur pour vérifier les rôles utilisateur"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Connexion requise.', 'error')
                return redirect(url_for('login'))
            if not current_user.has_role(required_role):
                flash(f'Accès {required_role} requis.', 'error')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def log_activity(action, entity_type, entity_id=None, entity_name=None, description=None):
    """Log admin activity"""
    if current_user.is_authenticated:
        activity = ActivityLog(
            user_id=current_user.id,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            entity_name=entity_name,
            description=description or f"{action} {entity_type.lower()} {entity_name or ''}".strip()
        )
        db.session.add(activity)
        db.session.commit()

# Routes
@app.route('/')
def index():
    airports = Airport.query.filter_by(is_active=True).all()
    latest_news = News.query.filter_by(is_published=True).order_by(News.created_at.desc()).limit(3).all()
    return render_template('index.html', airports=airports, news=latest_news)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/offres-emploi')
def offres_emploi():
    """Page publique des offres d'emploi"""
    search = request.args.get('search', '')
    department = request.args.get('department', '')
    contract_type = request.args.get('contract_type', '')
    
    query = JobOffer.query.filter_by(status='active')
    
    if search:
        query = query.filter(JobOffer.title.contains(search) | 
                            JobOffer.description.contains(search))
    
    if department:
        query = query.filter_by(department=department)
    
    if contract_type:
        query = query.filter_by(contract_type=contract_type)
    
    jobs = query.order_by(JobOffer.publication_date.desc()).all()
    departments = db.session.query(JobOffer.department).distinct().all()
    departments = [dept[0] for dept in departments if dept[0]]
    contract_types = db.session.query(JobOffer.contract_type).distinct().all()
    contract_types = [ct[0] for ct in contract_types if ct[0]]
    
    return render_template('offres_emploi.html', jobs=jobs, departments=departments, 
                         contract_types=contract_types, search=search, 
                         selected_department=department, selected_contract_type=contract_type)

@app.route('/appels-offres')
def appels_offres():
    """Page publique des appels d'offres"""
    search = request.args.get('search', '')
    category = request.args.get('category', '')
    
    query = CallForTenders.query.filter_by(status='active')
    
    if search:
        query = query.filter(CallForTenders.title.contains(search) | 
                            CallForTenders.description.contains(search))
    
    if category:
        query = query.filter_by(category=category)
    
    tenders = query.order_by(CallForTenders.publication_date.desc()).all()
    categories = db.session.query(CallForTenders.category).distinct().all()
    categories = [cat[0] for cat in categories if cat[0]]
    
    return render_template('appels_offres.html', tenders=tenders, categories=categories, 
                         search=search, selected_category=category)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/transport')
def transport():
    city = request.args.get('city', '')
    transport_type = request.args.get('type', '')
    
    query = Transport.query.filter_by(is_active=True)
    if city:
        query = query.filter_by(city=city)
    if transport_type:
        query = query.filter_by(type=transport_type)
    
    transports = query.all()
    cities = db.session.query(Transport.city).distinct().all()
    types = db.session.query(Transport.type).distinct().all()
    
    return render_template('transport.html', 
                         transports=transports, 
                         cities=[c[0] for c in cities],
                         types=[t[0] for t in types])

@app.route('/food')
def food():
    city = request.args.get('city', '')
    cuisine = request.args.get('cuisine', '')
    
    query = Restaurant.query.filter_by(is_active=True)
    if city:
        query = query.filter_by(city=city)
    if cuisine:
        query = query.filter_by(cuisine_type=cuisine)
    
    restaurants = query.all()
    cities = db.session.query(Restaurant.city).distinct().all()
    cuisines = db.session.query(Restaurant.cuisine_type).distinct().all()
    
    return render_template('food.html', 
                         restaurants=restaurants,
                         cities=[c[0] for c in cities],
                         cuisines=[c[0] for c in cuisines if c[0]])

@app.route('/shopping')
def shopping():
    city = request.args.get('city', '')
    shop_type = request.args.get('type', '')
    
    query = Shopping.query.filter_by(is_active=True)
    if city:
        query = query.filter_by(city=city)
    if shop_type:
        query = query.filter_by(type=shop_type)
    
    shops = query.all()
    cities = db.session.query(Shopping.city).distinct().all()
    types = db.session.query(Shopping.type).distinct().all()
    
    return render_template('shopping.html', 
                         shops=shops,
                         cities=[c[0] for c in cities],
                         types=[t[0] for t in types if t[0]])

@app.route('/documents')
def documents():
    return render_template('documents.html')

# Flights route moved to line 813 with complete destinations list

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            contact = Contact(
                name=request.form['name'],
                email=request.form['email'],
                subject=request.form['subject'],
                message=request.form['message']
            )
            db.session.add(contact)
            db.session.commit()
            flash('Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            db.session.rollback()
            flash('Une erreur est survenue lors de l\'envoi de votre message. Veuillez réessayer.', 'error')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, is_admin=True).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            
            # Log the login activity
            log_activity('login', 'admin', user.id, user.username, f'Connexion admin réussie pour {user.username}')
            
            flash('Connexion admin réussie!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Identifiants admin incorrects', 'error')
    
    return render_template('admin_login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # Clear session variables
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # User dashboard - show user-specific information
    user_stats = {
        'flights_searched': 0,  # Could be tracked in future
        'bookings': 0,  # Could be tracked in future
        'profile_complete': bool(current_user.email)
    }
    return render_template('dashboard.html', stats=user_stats)

# Fonction pour générer un code de suivi unique
def generate_tracking_code():
    """Générer un code de suivi unique pour une candidature"""
    import random
    import string
    
    while True:
        # Générer un code de 8 caractères (lettres majuscules + chiffres)
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        
        # Vérifier que le code n'existe pas déjà
        existing = JobApplication.query.filter_by(tracking_code=code).first()
        if not existing:
            return code

# Fonction pour sauvegarder les fichiers uploadés
def save_uploaded_file(file, prefix=''):
    """Sauvegarder un fichier uploadé de manière sécurisée"""
    if file and file.filename:
        # Générer un nom de fichier unique
        import uuid
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_id = str(uuid.uuid4())[:8]
        filename = f"{prefix}{timestamp}_{unique_id}_{file.filename}"
        
        # Créer le dossier uploads s'il n'existe pas
        import os
        upload_folder = app.config.get('UPLOAD_FOLDER', 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        # Sauvegarder le fichier
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        
        # Retourner l'URL relative
        return f"uploads/{filename}"
    return None

# Routes publiques pour les candidats
@app.route('/appels-offres/<int:tender_id>')
def appel_offre_detail(tender_id):
    """Détail d'un appel d'offre - accès public"""
    tender = CallForTenders.query.get_or_404(tender_id)
    return render_template('appel_offre_detail.html', tender=tender)



@app.route('/offres-emploi/<int:job_id>')
def offre_emploi_detail(job_id):
    """Détail d'une offre d'emploi - accès public"""
    job = JobOffer.query.get_or_404(job_id)
    return render_template('offre_emploi_detail.html', job=job)

@app.route('/postuler/<int:job_id>', methods=['GET', 'POST'])
def postuler(job_id):
    """Formulaire de candidature pour une offre d'emploi - accès public"""
    job = JobOffer.query.get_or_404(job_id)
    
    if request.method == 'POST':
        try:
            print("=== DEBUT TRAITEMENT CANDIDATURE ===")
            print(f"Données reçues: {dict(request.form)}")
            print(f"Fichiers reçus: {list(request.files.keys())}")
            
            # Validation des champs obligatoires
            required_fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'birth_date', 'nationality', 'education_level', 'experience_years']
            for field in required_fields:
                value = request.form.get(field)
                print(f"Champ {field}: '{value}'")
                if not value:
                    print(f"ERREUR: Champ {field} manquant")
                    flash(f'Le champ {field} est obligatoire.', 'error')
                    return render_template('postuler.html', job=job)
            
            # Gérer les fichiers uploadés
            cv_url = ''
            cover_letter_url = ''
            diploma_url = ''
            
            # Upload CV (obligatoire)
            if 'cv_file' in request.files and request.files['cv_file'].filename:
                cv_file = request.files['cv_file']
                cv_url = save_uploaded_file(cv_file, 'cv_')
            else:
                flash('Le CV est obligatoire.', 'error')
                return render_template('postuler.html', job=job)
            
            # Upload lettre de motivation (optionnel)
            if 'cover_letter_file' in request.files and request.files['cover_letter_file'].filename:
                cover_file = request.files['cover_letter_file']
                cover_letter_url = save_uploaded_file(cover_file, 'cover_')
            
            # Upload diplôme (optionnel)
            if 'diploma_file' in request.files and request.files['diploma_file'].filename:
                diploma_file = request.files['diploma_file']
                diploma_url = save_uploaded_file(diploma_file, 'diploma_')
            
            # Générer un code de suivi unique
            tracking_code = generate_tracking_code()
            
            # Créer une nouvelle candidature (sans user_id)
            candidature = JobApplication(
                job_offer_id=job_id,
                user_id=None,  # Pas d'utilisateur connecté
                first_name=request.form.get('first_name').strip(),
                last_name=request.form.get('last_name').strip(),
                email=request.form.get('email').strip(),
                phone=request.form.get('phone').strip(),
                address=request.form.get('address').strip(),
                birth_date=datetime.strptime(request.form.get('birth_date'), '%Y-%m-%d').date(),
                nationality=request.form.get('nationality').strip(),
                education_level=request.form.get('education_level'),
                experience_years=int(request.form.get('experience_years', 0)),
                current_position=request.form.get('current_position', '').strip(),
                skills=request.form.get('skills', '').strip(),
                languages=request.form.get('languages', '').strip(),
                cv_url=cv_url,
                cover_letter_url=cover_letter_url,
                diploma_url=diploma_url,
                motivation_letter=request.form.get('motivation_letter', '').strip(),
                tracking_code=tracking_code,
                status='pending'
            )
            
            # Sauvegarder en base
            print(f"DEBUT SAUVEGARDE: Candidature pour {candidature.first_name} {candidature.last_name}")
            db.session.add(candidature)
            print("CANDIDATURE AJOUTEE A LA SESSION")
            db.session.commit()
            print(f"CANDIDATURE SAUVEGARDEE AVEC ID: {candidature.id}")
            
            # Log de l'activité (désactivé temporairement)
            # log_activity('CREATE', 'JobApplication', candidature.id, 
            #             f'{candidature.first_name} {candidature.last_name}',
            #             f'Nouvelle candidature publique pour {job.title}')
            
            flash(f'Votre candidature a été soumise avec succès ! Votre code de suivi est : <strong>{tracking_code}</strong>. Conservez ce code pour suivre l’état de votre candidature.', 'success')
            return redirect(url_for('suivi_candidature', code=tracking_code))
            
        except Exception as e:
            db.session.rollback()
            print(f"ERREUR CANDIDATURE: {str(e)}")
            import traceback
            traceback.print_exc()
            flash(f'Erreur technique: {str(e)}', 'error')
            return render_template('postuler.html', job=job)
    
    # GET request - afficher le formulaire
    return render_template('postuler.html', job=job)

# Route pour le suivi des candidatures
@app.route('/suivi-candidature')
def suivi_candidature_form():
    """Formulaire de recherche de candidature"""
    return render_template('suivi_candidature.html')

@app.route('/suivi-candidature/<code>')
def suivi_candidature(code):
    """Afficher les détails d'une candidature par son code"""
    candidature = JobApplication.query.filter_by(tracking_code=code.upper()).first()
    
    if not candidature:
        flash('Code de suivi invalide. Vérifiez votre code et réessayez.', 'error')
        return redirect(url_for('suivi_candidature_form'))
    
    return render_template('candidature_detail.html', candidature=candidature)

@app.route('/rechercher-candidature', methods=['POST'])
def rechercher_candidature():
    """Rechercher une candidature par code"""
    code = request.form.get('tracking_code', '').strip().upper()
    
    if not code:
        flash('Veuillez saisir un code de suivi.', 'error')
        return redirect(url_for('suivi_candidature_form'))
    
    return redirect(url_for('suivi_candidature', code=code))

@app.route('/admin')
@admin_required
def admin_dashboard():
    stats = {
        'airports': Airport.query.count(),
        'restaurants': Restaurant.query.count(),
        'transports': Transport.query.count(),
        'shops': Shopping.query.count(),
        'contacts': Contact.query.filter_by(is_read=False).count(),
        'users': User.query.count()
    }
    
    # Get recent activity logs
    recent_activities = ActivityLog.query.order_by(ActivityLog.created_at.desc()).limit(10).all()
    
    # Get unread contacts for sidebar badge
    unread_contacts = Contact.query.filter_by(is_read=False).all()
    
    return render_template('admin/dashboard.html', stats=stats, recent_activities=recent_activities, contacts=unread_contacts)

# Admin Management Routes
@app.route('/admin/users', methods=['GET', 'POST'])
@admin_required
def admin_users():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        is_admin = 'is_admin' in request.form
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Nom d\'utilisateur déjà existant', 'error')
        elif User.query.filter_by(email=email).first():
            flash('Email déjà utilisé', 'error')
        else:
            new_user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password),
                is_admin=is_admin
            )
            db.session.add(new_user)
            db.session.commit()
            log_activity('CREATE', 'User', new_user.id, new_user.username, f'Nouvel utilisateur créé: {new_user.username}')
            flash('Utilisateur ajouté avec succès', 'success')
        
        return redirect(url_for('admin_users'))
    
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/admin/users/<int:user_id>/delete', methods=['POST'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_admin and user.id == current_user.id:
        return jsonify({'success': False, 'message': 'Impossible de supprimer votre propre compte admin'})
    
    username = user.username
    db.session.delete(user)
    db.session.commit()
    log_activity('DELETE', 'User', user_id, username, f'Utilisateur supprimé: {username}')
    return jsonify({'success': True})



@app.route('/admin/users/<int:user_id>/edit', methods=['GET'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'success': True,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_admin': user.is_admin
        }
    })

@app.route('/admin/users/<int:user_id>/update', methods=['POST'])
@admin_required
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    
    user.username = request.form.get('username')
    user.email = request.form.get('email')
    user.is_admin = 'is_admin' in request.form
    
    # Only update password if provided
    new_password = request.form.get('password')
    if new_password:
        user.password_hash = generate_password_hash(new_password)
    
    db.session.commit()
    log_activity('UPDATE', 'User', user.id, user.username, f'Utilisateur modifié: {user.username}')
    flash('Utilisateur modifié avec succès', 'success')
    return redirect(url_for('admin_users'))

@app.route('/admin/transport', methods=['GET', 'POST'])
@admin_required
def admin_transport():
    if request.method == 'POST':
        name = request.form.get('name')
        transport_type = request.form.get('type')
        city = request.form.get('city')
        price = float(request.form.get('price'))
        description = request.form.get('description')
        available = 'available' in request.form
        
        new_transport = Transport(
            name=name,
            type=transport_type,
            city=city,
            price=price,
            description=description,
            available=available
        )
        db.session.add(new_transport)
        db.session.commit()
        log_activity('CREATE', 'Transport', new_transport.id, new_transport.name, f'Nouveau transport ajouté: {new_transport.name}')
        flash('Transport ajouté avec succès', 'success')
        
        return redirect(url_for('admin_transport'))
    
    transports = Transport.query.all()
    return render_template('admin/transport.html', transports=transports)

@app.route('/admin/transport/<int:transport_id>/delete', methods=['POST'])
@admin_required
def delete_transport(transport_id):
    transport = Transport.query.get_or_404(transport_id)
    transport_name = transport.name
    db.session.delete(transport)
    db.session.commit()
    log_activity('DELETE', 'Transport', transport_id, transport_name, f'Transport supprimé: {transport_name}')
    return jsonify({'success': True})

@app.route('/admin/transport/<int:transport_id>/edit', methods=['GET'])
@admin_required
def edit_transport(transport_id):
    transport = Transport.query.get_or_404(transport_id)
    return jsonify({
        'success': True,
        'transport': {
            'id': transport.id,
            'name': transport.name,
            'type': transport.type,
            'city': transport.city,
            'price': transport.price,
            'description': transport.description,
            'available': transport.available
        }
    })

@app.route('/admin/transport/<int:transport_id>/update', methods=['POST'])
@admin_required
def update_transport(transport_id):
    transport = Transport.query.get_or_404(transport_id)
    
    transport.name = request.form.get('name')
    transport.type = request.form.get('type')
    transport.city = request.form.get('city')
    transport.price = float(request.form.get('price'))
    transport.description = request.form.get('description')
    transport.available = 'available' in request.form
    
    db.session.commit()
    log_activity('UPDATE', 'Transport', transport.id, transport.name, f'Transport modifié: {transport.name}')
    flash('Transport modifié avec succès', 'success')
    return redirect(url_for('admin_transport'))

@app.route('/admin/restaurants', methods=['GET', 'POST'])
@admin_required
def admin_restaurants():
    if request.method == 'POST':
        name = request.form.get('name')
        cuisine_type = request.form.get('cuisine_type')
        city = request.form.get('city')
        location = request.form.get('location')
        rating = float(request.form.get('rating'))
        description = request.form.get('description')
        is_open = 'is_open' in request.form
        
        new_restaurant = Restaurant(
            name=name,
            cuisine_type=cuisine_type,
            city=city,
            location=location,
            rating=rating,
            description=description,
            is_open=is_open
        )
        db.session.add(new_restaurant)
        db.session.commit()
        log_activity('CREATE', 'Restaurant', new_restaurant.id, new_restaurant.name, f'Nouveau restaurant ajouté: {new_restaurant.name}')
        flash('Restaurant ajouté avec succès', 'success')
        
        return redirect(url_for('admin_restaurants'))
    
    restaurants = Restaurant.query.all()
    return render_template('admin/restaurants.html', restaurants=restaurants)

@app.route('/admin/restaurants/<int:restaurant_id>/delete', methods=['POST'])
@admin_required
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    restaurant_name = restaurant.name
    db.session.delete(restaurant)
    db.session.commit()
    log_activity('DELETE', 'Restaurant', restaurant_id, restaurant_name, f'Restaurant supprimé: {restaurant_name}')
    return jsonify({'success': True})

@app.route('/admin/restaurants/<int:restaurant_id>/edit', methods=['GET'])
@admin_required
def edit_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    return jsonify({
        'success': True,
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'cuisine_type': restaurant.cuisine_type,
            'city': restaurant.city,
            'location': restaurant.location,
            'rating': restaurant.rating,
            'description': restaurant.description,
            'is_open': restaurant.is_open
        }
    })

@app.route('/admin/restaurants/<int:restaurant_id>/update', methods=['POST'])
@admin_required
def update_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    
    restaurant.name = request.form.get('name')
    restaurant.cuisine_type = request.form.get('cuisine_type')
    restaurant.city = request.form.get('city')
    restaurant.location = request.form.get('location')
    restaurant.rating = float(request.form.get('rating'))
    restaurant.description = request.form.get('description')
    restaurant.is_open = 'is_open' in request.form
    
    db.session.commit()
    log_activity('UPDATE', 'Restaurant', restaurant.id, restaurant.name, f'Restaurant modifié: {restaurant.name}')
    flash('Restaurant modifié avec succès', 'success')
    return redirect(url_for('admin_restaurants'))

@app.route('/admin/shopping', methods=['GET', 'POST'])
@admin_required
def admin_shopping():
    if request.method == 'POST':
        name = request.form.get('name')
        shopping_type = request.form.get('type')
        city = request.form.get('city')
        location = request.form.get('location')
        description = request.form.get('description')
        opening_hours = request.form.get('opening_hours')
        is_open = 'is_open' in request.form
        
        new_shopping = Shopping(
            name=name,
            type=shopping_type,
            city=city,
            location=location,
            description=description,
            opening_hours=opening_hours,
            is_open=is_open
        )
        db.session.add(new_shopping)
        db.session.commit()
        log_activity('CREATE', 'Shopping', new_shopping.id, new_shopping.name, f'Nouveau centre commercial ajouté: {new_shopping.name}')
        flash('Centre commercial ajouté avec succès', 'success')
        
        return redirect(url_for('admin_shopping'))
    
    shopping_centers = Shopping.query.all()
    return render_template('admin/shopping.html', shopping_centers=shopping_centers)

@app.route('/admin/shopping/<int:shopping_id>/delete', methods=['POST'])
@admin_required
def delete_shopping(shopping_id):
    shopping = Shopping.query.get_or_404(shopping_id)
    shopping_name = shopping.name
    db.session.delete(shopping)
    db.session.commit()
    log_activity('DELETE', 'Shopping', shopping_id, shopping_name, f'Centre commercial supprimé: {shopping_name}')
    return jsonify({'success': True})

@app.route('/admin/shopping/<int:shopping_id>/edit', methods=['GET'])
@admin_required
def edit_shopping(shopping_id):
    shopping = Shopping.query.get_or_404(shopping_id)
    return jsonify({
        'success': True,
        'shopping': {
            'id': shopping.id,
            'name': shopping.name,
            'type': shopping.type,
            'city': shopping.city,
            'location': shopping.location,
            'description': shopping.description,
            'opening_hours': shopping.opening_hours,
            'is_open': shopping.is_open
        }
    })

@app.route('/admin/shopping/<int:shopping_id>/update', methods=['POST'])
@admin_required
def update_shopping(shopping_id):
    shopping = Shopping.query.get_or_404(shopping_id)
    
    shopping.name = request.form.get('name')
    shopping.type = request.form.get('type')
    shopping.city = request.form.get('city')
    shopping.location = request.form.get('location')
    shopping.description = request.form.get('description')
    shopping.opening_hours = request.form.get('opening_hours')
    shopping.is_open = 'is_open' in request.form
    
    db.session.commit()
    log_activity('UPDATE', 'Shopping', shopping.id, shopping.name, f'Centre commercial modifié: {shopping.name}')
    flash('Centre commercial modifié avec succès', 'success')
    return redirect(url_for('admin_shopping'))

# Admin Contacts Management
@app.route('/admin/contacts', methods=['GET'])
@admin_required
def admin_contacts():
    contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    return render_template('admin/contacts.html', contacts=contacts)

@app.route('/admin/contacts/<int:contact_id>/read', methods=['POST'])
@admin_required
def mark_contact_read(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    contact.is_read = True
    db.session.commit()
    log_activity('UPDATE', 'Contact', contact.id, contact.name, f'Message de contact marqué comme lu: {contact.subject}')
    return jsonify({'success': True})

@app.route('/admin/contacts/<int:contact_id>/delete', methods=['DELETE'])
@admin_required
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    contact_name = contact.name
    contact_subject = contact.subject
    db.session.delete(contact)
    db.session.commit()
    log_activity('DELETE', 'Contact', contact_id, contact_name, f'Message de contact supprimé: {contact_subject}')
    return jsonify({'success': True})

# Admin Appels d'Offres Management
@app.route('/admin/call-for-tenders', methods=['GET', 'POST'])
@admin_required
def admin_call_for_tenders():
    if request.method == 'POST':
        try:
            # Validation des champs requis
            required_fields = ['title', 'reference', 'description', 'category', 'deadline', 'publication_date', 'status']
            for field in required_fields:
                if not request.form.get(field):
                    flash(f'Le champ {field} est requis.', 'error')
                    return redirect(url_for('admin_call_for_tenders'))
            
            # Gérer l'upload du document
            document_url = ''
            if 'document_file' in request.files:
                document_file = request.files['document_file']
                if document_file.filename:
                    document_url = save_uploaded_file(document_file, 'tender_doc_')
                    print(f"DEBUG: Document appel d'offre uploadé: {document_url}")
            
            # Ajouter un nouvel appel d'offre
            new_tender = CallForTenders(
                title=request.form.get('title'),
                reference=request.form.get('reference'),
                description=request.form.get('description'),
                category=request.form.get('category'),
                budget_min=float(request.form['budget_min']) if request.form.get('budget_min') else None,
                budget_max=float(request.form['budget_max']) if request.form.get('budget_max') else None,
                deadline=datetime.strptime(request.form['deadline'], '%Y-%m-%d'),
                publication_date=datetime.strptime(request.form['publication_date'], '%Y-%m-%d'),
                status=request.form.get('status', 'active'),
                contact_email=request.form.get('contact_email', ''),
                contact_phone=request.form.get('contact_phone', ''),
                document_url=document_url,
                created_by=current_user.id
            )
            db.session.add(new_tender)
            db.session.commit()
            log_activity('CREATE', 'CallForTenders', new_tender.id, new_tender.title, f'Appel d\'offre créé: {new_tender.title}')
            flash('Appel d\'offre créé avec succès', 'success')
            return redirect(url_for('admin_call_for_tenders'))
            
        except ValueError as e:
            flash(f'Erreur de format de données: {str(e)}', 'error')
            return redirect(url_for('admin_call_for_tenders'))
        except Exception as e:
            flash(f'Erreur lors de la création: {str(e)}', 'error')
            return redirect(url_for('admin_call_for_tenders'))
    
    tenders = CallForTenders.query.order_by(CallForTenders.created_at.desc()).all()
    return render_template('admin/call_for_tenders.html', tenders=tenders)

@app.route('/admin/call-for-tenders/<int:tender_id>/edit', methods=['GET', 'POST'])
@admin_required
def admin_edit_tender(tender_id):
    tender = CallForTenders.query.get_or_404(tender_id)
    
    if request.method == 'POST':
        try:
            tender.title = request.form.get('title', tender.title)
            tender.reference = request.form.get('reference', tender.reference)
            tender.description = request.form.get('description', tender.description)
            tender.category = request.form.get('category', tender.category)
            tender.budget_min = float(request.form['budget_min']) if request.form.get('budget_min') else tender.budget_min
            tender.budget_max = float(request.form['budget_max']) if request.form.get('budget_max') else tender.budget_max
            tender.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d') if request.form.get('deadline') else tender.deadline
            tender.publication_date = datetime.strptime(request.form['publication_date'], '%Y-%m-%d') if request.form.get('publication_date') else tender.publication_date
            tender.status = request.form.get('status', tender.status)
            tender.contact_email = request.form.get('contact_email', tender.contact_email)
            tender.contact_phone = request.form.get('contact_phone', tender.contact_phone)
            tender.document_url = request.form.get('document_url', tender.document_url)
            
            db.session.commit()
            log_activity('UPDATE', 'CallForTenders', tender.id, tender.title, f'Appel d\'offre modifié: {tender.title}')
            flash('Appel d\'offre modifié avec succès', 'success')
            return redirect(url_for('admin_call_for_tenders'))
            
        except Exception as e:
            flash(f'Erreur lors de la modification: {str(e)}', 'error')
            return redirect(url_for('admin_call_for_tenders'))
    
    return render_template('admin/edit_tender.html', tender=tender)

@app.route('/admin/call-for-tenders/<int:tender_id>/delete', methods=['POST'])
@admin_required
def admin_delete_tender(tender_id):
    tender = CallForTenders.query.get_or_404(tender_id)
    tender_title = tender.title
    
    try:
        db.session.delete(tender)
        db.session.commit()
        log_activity('DELETE', 'CallForTenders', tender_id, tender_title, f'Appel d\'offre supprimé: {tender_title}')
        flash('Appel d\'offre supprimé avec succès', 'success')
    except Exception as e:
        flash(f'Erreur lors de la suppression: {str(e)}', 'error')
    
    return redirect(url_for('admin_call_for_tenders'))

@app.route('/admin/candidatures', methods=['GET'])
@admin_required
def admin_candidatures():
    """Interface admin pour gérer toutes les candidatures"""
    print("DEBUG: Route admin_candidatures appelée")
    
    # Récupérer toutes les candidatures (simplifié)
    candidatures = JobApplication.query.order_by(JobApplication.applied_at.desc()).all()
    print(f"DEBUG: Nombre de candidatures trouvées: {len(candidatures)}")
    
    for c in candidatures:
        print(f"DEBUG: Candidature ID {c.id} - {c.first_name} {c.last_name}")
    
    # Statistiques
    stats = {
        'total': JobApplication.query.count(),
        'pending': JobApplication.query.filter_by(status='pending').count(),
        'reviewed': JobApplication.query.filter_by(status='reviewed').count(),
        'accepted': JobApplication.query.filter_by(status='accepted').count(),
        'rejected': JobApplication.query.filter_by(status='rejected').count()
    }
    
    return render_template('admin/candidatures.html', candidatures=candidatures, stats=stats)

@app.route('/admin/candidatures/<int:candidature_id>/view', methods=['GET'])
@admin_required
def admin_view_candidature(candidature_id):
    """Voir le détail d'une candidature"""
    candidature = JobApplication.query.get_or_404(candidature_id)
    return render_template('admin/view_candidature.html', candidature=candidature)

@app.route('/admin/candidatures/<int:candidature_id>/update-status', methods=['POST'])
@admin_required
def admin_update_candidature_status(candidature_id):
    """Mettre à jour le statut d'une candidature"""
    candidature = JobApplication.query.get_or_404(candidature_id)
    
    try:
        new_status = request.form.get('status')
        notes = request.form.get('notes', '')
        
        if new_status in ['pending', 'reviewed', 'accepted', 'rejected']:
            candidature.status = new_status
            candidature.notes = notes
            candidature.reviewed_at = datetime.utcnow()
            candidature.reviewed_by = current_user.id
            
            db.session.commit()
            log_activity('UPDATE', 'JobApplication', candidature.id, 
                        f'{candidature.first_name} {candidature.last_name}', 
                        f'Statut candidature modifié: {new_status}')
            flash(f'Statut de la candidature mis à jour: {new_status}', 'success')
        else:
            flash('Statut invalide', 'error')
            
    except Exception as e:
        flash(f'Erreur lors de la mise à jour: {str(e)}', 'error')
    
    return redirect(url_for('admin_candidatures'))

# Route de compatibilité
@app.route('/admin/appels-offres', methods=['GET', 'POST'])
@admin_required
def admin_appels_offres():
    return redirect(url_for('admin_call_for_tenders'))

@app.route('/admin/appels-offres/<int:tender_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_appel_offre(tender_id):
    tender = CallForTenders.query.get_or_404(tender_id)
    
    if request.method == 'POST':
        tender.title = request.form['title']
        tender.reference = request.form['reference']
        tender.description = request.form['description']
        tender.category = request.form['category']
        tender.budget_min = float(request.form['budget_min']) if request.form['budget_min'] else None
        tender.budget_max = float(request.form['budget_max']) if request.form['budget_max'] else None
        tender.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d')
        tender.publication_date = datetime.strptime(request.form['publication_date'], '%Y-%m-%d')
        tender.status = request.form['status']
        tender.contact_email = request.form.get('contact_email', '')
        tender.contact_phone = request.form.get('contact_phone', '')
        tender.document_url = request.form.get('document_url', '')
        tender.updated_at = datetime.utcnow()
        
        db.session.commit()
        log_activity('UPDATE', 'CallForTenders', tender.id, tender.title, f'Appel d\'offre modifié: {tender.title}')
        flash('Appel d\'offre modifié avec succès', 'success')
        return redirect(url_for('admin_call_for_tenders'))
    
    return render_template('admin/edit_appel_offre.html', tender=tender)

@app.route('/admin/appels-offres/<int:tender_id>/delete', methods=['DELETE'])
@admin_required
def delete_appel_offre(tender_id):
    tender = CallForTenders.query.get_or_404(tender_id)
    tender_title = tender.title
    db.session.delete(tender)
    db.session.commit()
    log_activity('DELETE', 'CallForTenders', tender_id, tender_title, f'Appel d\'offre supprimé: {tender_title}')
    return jsonify({'success': True})

# Admin Offres d'Emploi Management
@app.route('/admin/job-offers', methods=['GET', 'POST'])
@admin_required
def admin_job_offers():
    if request.method == 'POST':
        try:
            # Validation des champs requis
            required_fields = ['title', 'reference', 'department', 'location', 'contract_type', 'deadline']
            for field in required_fields:
                if not request.form.get(field):
                    flash(f'Le champ {field} est requis.', 'error')
                    return redirect(url_for('admin_job_offers'))
            
            new_job = JobOffer(
                title=request.form.get('title'),
                reference=request.form.get('reference'),
                department=request.form.get('department'),
                location=request.form.get('location'),
                deadline=datetime.strptime(request.form['deadline'], '%Y-%m-%d'),
                contract_type=request.form.get('contract_type'),
                experience_level=request.form.get('experience_level', ''),
                description=request.form.get('description', ''),
                requirements=request.form.get('requirements', ''),
                contact_email=request.form.get('contact_email', ''),
                contact_phone=request.form.get('contact_phone', ''),
                status=request.form.get('status', 'active'),
                created_by=current_user.id
            )
            db.session.add(new_job)
            db.session.commit()
            log_activity('CREATE', 'JobOffer', new_job.id, new_job.title, f'Offre d\'emploi créée: {new_job.title}')
            flash('Offre d\'emploi créée avec succès', 'success')
            return redirect(url_for('admin_job_offers'))
            
        except ValueError as e:
            flash(f'Erreur de format de données: {str(e)}', 'error')
            return redirect(url_for('admin_job_offers'))
        except Exception as e:
            flash(f'Erreur lors de la création: {str(e)}', 'error')
            return redirect(url_for('admin_job_offers'))
    
    jobs = JobOffer.query.order_by(JobOffer.created_at.desc()).all()
    return render_template('admin/job_offers.html', jobs=jobs)

@app.route('/admin/job-offers/<int:job_id>/edit', methods=['GET', 'POST'])
@admin_required
def admin_edit_job_offer(job_id):
    job = JobOffer.query.get_or_404(job_id)
    
    if request.method == 'POST':
        try:
            job.title = request.form.get('title', job.title)
            job.reference = request.form.get('reference', job.reference)
            job.department = request.form.get('department', job.department)
            job.location = request.form.get('location', job.location)
            job.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%d') if request.form.get('deadline') else job.deadline
            job.contract_type = request.form.get('contract_type', job.contract_type)
            job.experience_level = request.form.get('experience_level', job.experience_level)
            job.description = request.form.get('description', job.description)
            job.requirements = request.form.get('requirements', job.requirements)
            job.contact_email = request.form.get('contact_email', job.contact_email)
            job.contact_phone = request.form.get('contact_phone', job.contact_phone)
            job.status = request.form.get('status', job.status)
            
            db.session.commit()
            log_activity('UPDATE', 'JobOffer', job.id, job.title, f'Offre d\'emploi modifiée: {job.title}')
            flash('Offre d\'emploi modifiée avec succès', 'success')
            return redirect(url_for('admin_job_offers'))
            
        except Exception as e:
            flash(f'Erreur lors de la modification: {str(e)}', 'error')
            return redirect(url_for('admin_job_offers'))
    
    return render_template('admin/edit_job_offer.html', job=job)

@app.route('/admin/job-offers/<int:job_id>/delete', methods=['POST'])
@admin_required
def admin_delete_job_offer(job_id):
    job = JobOffer.query.get_or_404(job_id)
    job_title = job.title
    
    try:
        db.session.delete(job)
        db.session.commit()
        log_activity('DELETE', 'JobOffer', job_id, job_title, f'Offre d\'emploi supprimée: {job_title}')
        flash('Offre d\'emploi supprimée avec succès', 'success')
    except Exception as e:
        flash(f'Erreur lors de la suppression: {str(e)}', 'error')
    
    return redirect(url_for('admin_job_offers'))

# Route de compatibilité
@app.route('/admin/offres-emploi', methods=['GET', 'POST'])
@admin_required
def admin_offres_emploi():
    return redirect(url_for('admin_job_offers'))

@app.route('/admin/offres-emploi/<int:job_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_offre_emploi(job_id):
    job = JobOffer.query.get_or_404(job_id)
    
    if request.method == 'POST':
        job.title = request.form['title']
        job.reference = request.form['reference']
        job.department = request.form['department']
        job.location = request.form['location']
        job.contract_type = request.form['contract_type']
        job.experience_level = request.form['experience_level']
        job.description = request.form['description']
        job.requirements = request.form['requirements']
        job.benefits = request.form.get('benefits', '')
        job.salary_min = float(request.form['salary_min']) if request.form['salary_min'] else None
        job.salary_max = float(request.form['salary_max']) if request.form['salary_max'] else None
        job.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%dT%H:%M')
        job.status = request.form['status']
        job.contact_person = request.form.get('contact_person', '')
        job.contact_email = request.form.get('contact_email', '')
        job.contact_phone = request.form.get('contact_phone', '')
        job.updated_at = datetime.utcnow()
        
        db.session.commit()
        log_activity('UPDATE', 'JobOffer', job.id, job.title, f'Offre d\'emploi modifiée: {job.title}')
        flash('Offre d\'emploi modifiée avec succès', 'success')
        return redirect(url_for('admin_offres_emploi'))
    
    return render_template('admin/edit_offre_emploi.html', job=job)

@app.route('/admin/offres-emploi/<int:job_id>/delete', methods=['DELETE'])
@admin_required
def delete_offre_emploi(job_id):
    job = JobOffer.query.get_or_404(job_id)
    job_title = job.title
    db.session.delete(job)
    db.session.commit()
    log_activity('DELETE', 'JobOffer', job_id, job_title, f'Offre d\'emploi supprimée: {job_title}')
    return jsonify({'success': True})



# Admin Flights Management
@app.route('/admin/flights', methods=['GET', 'POST'])
@admin_required
def admin_flights():
    if request.method == 'POST':
        # Add new flight
        new_flight = Flight(
            flight_number=request.form['flight_number'],
            airline=request.form['airline'],
            airport_id=request.form['airport_id'],
            destination=request.form['destination'],
            flight_type=request.form['flight_type'],
            scheduled_time=datetime.strptime(request.form['scheduled_date'] + ' ' + request.form['scheduled_time'], '%Y-%m-%d %H:%M'),
            status=request.form['status'],
            gate=request.form['gate'] if request.form['gate'] else None,
            terminal=request.form['terminal'] if request.form['terminal'] else None,
            aircraft_type=request.form['aircraft_type'] if request.form['aircraft_type'] else None
        )
        db.session.add(new_flight)
        db.session.commit()
        log_activity('CREATE', 'Flight', new_flight.id, new_flight.flight_number, f'Nouveau vol ajouté: {new_flight.flight_number}')
        flash('Vol ajouté avec succès', 'success')
        return redirect(url_for('admin_flights'))
    
    flights = Flight.query.order_by(Flight.scheduled_time.desc()).all()
    airports = Airport.query.filter_by(is_active=True).all()
    return render_template('admin/flights.html', flights=flights, airports=airports)

@app.route('/admin/flights/<int:flight_id>/delete', methods=['DELETE'])
@admin_required
def delete_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    flight_number = flight.flight_number
    db.session.delete(flight)
    db.session.commit()
    log_activity('DELETE', 'Flight', flight_id, flight_number, f'Vol supprimé: {flight_number}')
    return jsonify({'success': True})

@app.route('/admin/flights/<int:flight_id>/edit', methods=['GET'])
@admin_required
def edit_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    return jsonify({
        'success': True,
        'flight': {
            'id': flight.id,
            'flight_number': flight.flight_number,
            'airline': flight.airline,
            'airport_id': flight.airport_id,
            'destination': flight.destination,
            'flight_type': flight.flight_type,
            'scheduled_date': flight.scheduled_time.strftime('%Y-%m-%d'),
            'scheduled_time': flight.scheduled_time.strftime('%H:%M'),
            'status': flight.status,
            'gate': flight.gate or '',
            'terminal': flight.terminal or '',
            'aircraft_type': flight.aircraft_type or ''
        }
    })

@app.route('/admin/flights/<int:flight_id>/update', methods=['POST'])
@admin_required
def update_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    
    flight.flight_number = request.form['flight_number']
    flight.airline = request.form['airline']
    flight.airport_id = request.form['airport_id']
    flight.destination = request.form['destination']
    flight.flight_type = request.form['flight_type']
    flight.scheduled_time = datetime.strptime(request.form['scheduled_date'] + ' ' + request.form['scheduled_time'], '%Y-%m-%d %H:%M')
    flight.status = request.form['status']
    flight.gate = request.form['gate'] if request.form['gate'] else None
    flight.terminal = request.form['terminal'] if request.form['terminal'] else None
    flight.aircraft_type = request.form['aircraft_type'] if request.form['aircraft_type'] else None
    
    db.session.commit()
    log_activity('UPDATE', 'Flight', flight.id, flight.flight_number, f'Vol modifié: {flight.flight_number}')
    flash('Vol modifié avec succès', 'success')
    return redirect(url_for('admin_flights'))

# Additional route handlers
@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/bagages')
def bagages():
    return render_template('bagages.html')

@app.route('/surete')
def surete():
    return render_template('surete.html')

@app.route('/user_dashboard')
@login_required
def user_dashboard():
    return render_template('user_dashboard.html')

# Public Flights Route
@app.route('/flights')
def flights():
    # Complete list of world capitals and major cities
    destinations = [
        # Europe
        'Paris', 'London', 'Madrid', 'Rome', 'Berlin', 'Amsterdam', 'Brussels', 'Vienna', 'Prague', 'Budapest',
        'Warsaw', 'Stockholm', 'Copenhagen', 'Helsinki', 'Oslo', 'Dublin', 'Lisbon', 'Athens', 'Zurich', 'Geneva',
        'Milan', 'Barcelona', 'Munich', 'Frankfurt', 'Hamburg', 'Lyon', 'Marseille', 'Nice', 'Venice', 'Florence',
        
        # Middle East & Asia
        'Istanbul', 'Dubai', 'Doha', 'Abu Dhabi', 'Kuwait City', 'Riyadh', 'Jeddah', 'Muscat', 'Manama', 'Amman',
        'Beirut', 'Damascus', 'Baghdad', 'Tehran', 'Ankara', 'Tel Aviv', 'Jerusalem', 'Yerevan', 'Tbilisi', 'Baku',
        'Tokyo', 'Beijing', 'Shanghai', 'Hong Kong', 'Singapore', 'Bangkok', 'Kuala Lumpur', 'Jakarta', 'Manila', 'Seoul',
        'New Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Karachi', 'Lahore', 'Islamabad', 'Dhaka', 'Colombo',
        
        # Africa
        'Cairo', 'Alexandria', 'Tunis', 'Algiers', 'Tripoli', 'Khartoum', 'Addis Ababa', 'Nairobi', 'Kampala', 'Dar es Salaam',
        'Lagos', 'Abuja', 'Accra', 'Abidjan', 'Dakar', 'Bamako', 'Ouagadougou', 'Niamey', 'Conakry', 'Freetown',
        'Monrovia', 'Yaoundé', 'Douala', 'Libreville', 'Brazzaville', 'Kinshasa', 'Luanda', 'Windhoek', 'Gaborone', 'Pretoria',
        'Cape Town', 'Johannesburg', 'Durban', 'Harare', 'Lusaka', 'Lilongwe', 'Maputo', 'Antananarivo', 'Port Louis',
        
        # Americas
        'New York', 'Los Angeles', 'Chicago', 'Miami', 'Boston', 'Washington DC', 'San Francisco', 'Las Vegas', 'Atlanta', 'Dallas',
        'Houston', 'Philadelphia', 'Phoenix', 'San Diego', 'Denver', 'Seattle', 'Detroit', 'Minneapolis', 'Tampa', 'Orlando',
        'Toronto', 'Montreal', 'Vancouver', 'Ottawa', 'Calgary', 'Edmonton', 'Winnipeg', 'Quebec City', 'Halifax',
        'Mexico City', 'Guadalajara', 'Monterrey', 'Cancun', 'Tijuana', 'León', 'Puebla', 'Juárez', 'Mérida',
        'Havana', 'Kingston', 'Santo Domingo', 'San Juan', 'Port-au-Prince', 'Nassau', 'Bridgetown', 'Port of Spain',
        'Caracas', 'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Quito', 'Guayaquil', 'Lima', 'Arequipa', 'Cusco',
        'La Paz', 'Santa Cruz', 'Asunción', 'Montevideo', 'Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza', 'Santiago', 'Valparaíso',
        'São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza', 'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Porto Alegre',
        
        # Oceania
        'Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Canberra', 'Gold Coast', 'Newcastle', 'Wollongong',
        'Auckland', 'Wellington', 'Christchurch', 'Hamilton', 'Tauranga', 'Dunedin', 'Palmerston North',
        'Suva', 'Nadi', 'Port Moresby', 'Honiara', 'Port Vila', 'Nuku\'alofa', 'Apia', 'Papeete'
    ]
    
    # Sort destinations alphabetically
    destinations.sort()
    
    # Get search parameters
    selected_airport = request.args.get('airport_id', '')
    selected_destination = request.args.get('destination', '')
    selected_date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    selected_type = request.args.get('type', 'departure')
    
    # Get all airports
    airports = Airport.query.filter_by(is_active=True).all()
    
    # Build query for flights
    query = Flight.query
    
    # Filter by airport if selected
    if selected_airport:
        query = query.filter(Flight.airport_id == selected_airport)
    
    # Filter by destination if selected
    if selected_destination:
        query = query.filter(Flight.destination == selected_destination)
    
    # Filter by flight type
    query = query.filter(Flight.flight_type == selected_type)
    
    # Filter by date
    if selected_date:
        try:
            search_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            query = query.filter(db.func.date(Flight.scheduled_time) == search_date)
        except ValueError:
            pass
    
    # Order by scheduled time
    flights = query.order_by(Flight.scheduled_time.asc()).all()
    
    return render_template('flights.html', 
                         flights=flights,
                         airports=airports,
                         destinations=destinations,
                         selected_airport=selected_airport,
                         selected_destination=selected_destination,
                         selected_date=selected_date,
                         selected_type=selected_type)

# API Routes
@app.route('/api/airports')
def api_airports():
    airports = Airport.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': a.id,
        'name': a.name,
        'city': a.city,
        'code': a.code,
        'latitude': a.latitude,
        'longitude': a.longitude,
        'description': a.description
    } for a in airports])

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '')
    category = request.args.get('category', 'all')
    
    results = []
    
    if category in ['all', 'restaurants']:
        restaurants = Restaurant.query.filter(
            Restaurant.name.contains(query),
            Restaurant.is_active == True
        ).limit(10).all()
        results.extend([{
            'type': 'restaurant',
            'id': r.id,
            'name': r.name,
            'city': r.city,
            'description': r.description
        } for r in restaurants])
    
    if category in ['all', 'transport']:
        transports = Transport.query.filter(
            Transport.name.contains(query),
            Transport.is_active == True
        ).limit(10).all()
        results.extend([{
            'type': 'transport',
            'id': t.id,
            'name': t.name,
            'city': t.city,
            'description': t.description
        } for t in transports])
    
    if category in ['all', 'shopping']:
        shops = Shopping.query.filter(
            Shopping.name.contains(query),
            Shopping.is_active == True
        ).limit(10).all()
        results.extend([{
            'type': 'shopping',
            'id': s.id,
            'name': s.name,
            'city': s.city,
            'description': s.description
        } for s in shops])
    
    return jsonify(results)

def init_db():
    """Initialize database with sample data"""
    db.create_all()
    
    # Create admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@onda.ma',
            password_hash=generate_password_hash('admin123'),
            is_admin=True
        )
        db.session.add(admin)
    
    # Add sample airports
    if not Airport.query.first():
        airports_data = [
            {"name": "Casablanca - Mohammed V", "city": "Casablanca", "code": "CMN", "lat": 33.367, "lon": -7.589},
            {"name": "Marrakech - Ménara", "city": "Marrakech", "code": "RAK", "lat": 31.605, "lon": -8.036},
            {"name": "Agadir - Al Massira", "city": "Agadir", "code": "AGA", "lat": 30.325, "lon": -9.413},
            {"name": "Fès - Saïs", "city": "Fès", "code": "FEZ", "lat": 33.927, "lon": -4.978},
            {"name": "Rabat - Salé", "city": "Rabat", "code": "RBA", "lat": 34.05, "lon": -6.75},
            {"name": "Tanger - Ibn Battouta", "city": "Tanger", "code": "TNG", "lat": 35.726, "lon": -5.917},
        ]
        
        for airport_data in airports_data:
            airport = Airport(
                name=airport_data["name"],
                city=airport_data["city"],
                code=airport_data["code"],
                latitude=airport_data["lat"],
                longitude=airport_data["lon"],
                description=f"Aéroport international de {airport_data['city']}"
            )
            db.session.add(airport)
    
    # Add sample restaurants
    if not Restaurant.query.first():
        restaurants_data = [
            {"name": "La Sqala", "city": "Casablanca", "cuisine": "Marocaine", "rating": 4.5},
            {"name": "Rick's Café", "city": "Casablanca", "cuisine": "Internationale", "rating": 4.2},
            {"name": "Nomad", "city": "Marrakech", "cuisine": "Moderne", "rating": 4.7},
            {"name": "Le Jardin", "city": "Marrakech", "cuisine": "Française", "rating": 4.3},
        ]
        
        for rest_data in restaurants_data:
            restaurant = Restaurant(
                name=rest_data["name"],
                city=rest_data["city"],
                cuisine_type=rest_data["cuisine"],
                rating=rest_data["rating"],
                description=f"Restaurant {rest_data['cuisine'].lower()} à {rest_data['city']}"
            )
            db.session.add(restaurant)
    
    db.session.commit()

# Route pour servir les fichiers uploadés
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Servir les fichiers uploadés publiquement"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route pour télécharger les documents d'appels d'offres
@app.route('/tender/<int:tender_id>/document')
def download_tender_document(tender_id):
    """Télécharger le document d'un appel d'offre"""
    tender = CallForTenders.query.get_or_404(tender_id)
    
    if not tender.document_url:
        flash('Aucun document disponible pour cet appel d\'offre.', 'warning')
        return redirect(url_for('appel_offre_detail', tender_id=tender_id))
    
    # Extraire le nom du fichier de l'URL
    filename = tender.document_url.split('/')[-1]
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# Route pour créer/mettre à jour les tables
@app.route('/init-db')
def init_database():
    """Initialiser la base de données - À utiliser une seule fois"""
    try:
        db.create_all()
        flash('Base de données initialisée avec succès!', 'success')
        return "Base de données créée avec succès!"
    except Exception as e:
        return f"Erreur lors de la création de la base de données: {str(e)}"

# Route pour nettoyer les données avant migration
@app.route('/clean-db')
def clean_database():
    """Nettoyer les données avant migration"""
    try:
        from sqlalchemy import text
        with db.engine.connect() as connection:
            # Supprimer les candidatures avec cv_url NULL
            result = connection.execute(text("""
                DELETE FROM job_application WHERE cv_url IS NULL OR cv_url = '';
            """))
            connection.commit()
            return f"Nettoyage réussi ! {result.rowcount} enregistrements supprimés."
    except Exception as e:
        import traceback
        return f"Erreur de nettoyage: {str(e)}<br><pre>{traceback.format_exc()}</pre>"

# Route pour migrer le schéma de la base de données
@app.route('/migrate-db')
def migrate_database():
    """Migrer le schéma de la base de données pour ajouter tracking_code"""
    try:
        # Exécuter la migration SQL directement avec la nouvelle syntaxe
        from sqlalchemy import text
        with db.engine.connect() as connection:
            # Permettre user_id NULL pour les candidatures publiques
            connection.execute(text("""
                ALTER TABLE job_application 
                MODIFY COLUMN user_id INT NULL;
            """))
            
            # Ajouter le champ tracking_code
            connection.execute(text("""
                ALTER TABLE job_application 
                ADD COLUMN tracking_code VARCHAR(20) UNIQUE;
            """))
            
            connection.commit()
        return "Migration réussie ! user_id peut être NULL et tracking_code ajouté."
    except Exception as e:
        import traceback
        return f"Erreur de migration: {str(e)}<br><pre>{traceback.format_exc()}</pre>"

# Route de test pour candidature simple
@app.route('/test-candidature')
def test_candidature():
    """Tester la création d'une candidature simple"""
    try:
        # Trouver une offre d'emploi
        job = JobOffer.query.first()
        if not job:
            return "Aucune offre d'emploi trouvée pour tester"
        
        # Créer une candidature de test
        test_candidature = JobApplication(
            job_offer_id=job.id,
            user_id=None,
            first_name="Test",
            last_name="Candidat",
            email="test@example.com",
            phone="0123456789",
            address="123 Rue Test",
            birth_date=datetime(1990, 1, 1).date(),
            nationality="Marocaine",
            education_level="Master",
            experience_years=3,
            current_position="Développeur",
            skills="Python, Flask",
            languages="Français, Anglais",
            cv_url="test_cv.pdf",
            cover_letter_url="test_cover.pdf",
            diploma_url="test_diploma.pdf",
            motivation_letter="Lettre de motivation test",
            status='pending'
        )
        
        # Sauvegarder
        db.session.add(test_candidature)
        db.session.commit()
        
        return f"Candidature de test créée avec succès ! ID: {test_candidature.id}"
        
    except Exception as e:
        db.session.rollback()
        import traceback
        return f"Erreur: {str(e)}<br><pre>{traceback.format_exc()}</pre>"

# Route de test pour vérifier la base de données
@app.route('/test-db')
def test_database():
    """Tester la connexion à la base de données"""
    try:
        # Test de connexion
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        
        # Test de création d'une candidature factice
        job = JobOffer.query.first()
        if job:
            test_app = JobApplication(
                job_offer_id=job.id,
                user_id=None,
                first_name="Test",
                last_name="User",
                email="test@test.com",
                phone="0123456789",
                address="Test Address",
                birth_date=datetime(1990, 1, 1).date(),
                nationality="Test",
                education_level="Master",
                experience_years=5,
                cv_url="test_cv.pdf",
                status="pending"
            )
            
            db.session.add(test_app)
            db.session.commit()
            db.session.delete(test_app)
            db.session.commit()
            
            return f"Test réussi ! Tables: {tables}"
        else:
            return f"Pas d'offre d'emploi pour tester. Tables: {tables}"
            
    except Exception as e:
        import traceback
        return f"Erreur de test: {str(e)}<br><pre>{traceback.format_exc()}</pre>"

if __name__ == '__main__':
    with app.app_context():
        print("Création des tables de base de données...")
        db.create_all()
        print("Tables créées avec succès !")
        
        # Vérifier si la table JobApplication existe
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tables existantes: {tables}")
        
        if 'job_application' in tables:
            print("✅ Table JobApplication existe")
        else:
            print("❌ Table JobApplication manquante !")
            
        # Initialiser avec des données de test
        init_db()
            
    app.run(debug=True, host='0.0.0.0', port=5000)
