from app import app, db
from app import CallForTenders, JobOffer, User, Airport
from datetime import datetime, timedelta
import random

def generate_reference(prefix, length=6):
    """Génère une référence aléatoire"""
    import string
    chars = string.ascii_uppercase + string.digits
    return f"{prefix}-{''.join(random.choice(chars) for _ in range(length))}"

def create_sample_tenders():
    """Crée des exemples d'appels d'offres"""
    # Catégories d'appels d'offres
    categories = ["Travaux", "Services", "Fournitures", "Études", "Maintenance"]
    
    # Aéroports
    airports = Airport.query.all()
    
    # Utilisateurs admin
    admin_users = User.query.filter_by(is_admin=True).all()
    
    if not admin_users:
        print("Aucun utilisateur admin trouvé. Créez d'abord un utilisateur admin.")
        return
    
    # Données d'exemple pour les appels d'offres
    tenders_data = [
        {
            "title": "Fourniture de matériel informatique",
            "category": "Fournitures",
            "description": "Fourniture et installation de matériel informatique pour les bureaux de l'aéroport.",
            "budget_min": 500000,
            "budget_max": 800000,
            "days_until_deadline": 30,
            "status": "active"
        },
        {
            "title": "Travaux de rénovation des terminaux",
            "category": "Travaux",
            "description": "Rénovation complète des terminaux passagers, incluant électricité, plomberie et finitions.",
            "budget_min": 2000000,
            "budget_max": 3500000,
            "days_until_deadline": 45,
            "status": "active"
        },
        {
            "title": "Services de nettoyage",
            "category": "Services",
            "description": "Prestation de services de nettoyage pour les espaces communs et les bureaux.",
            "budget_min": 300000,
            "budget_max": 500000,
            "days_until_deadline": 15,
            "status": "active"
        },
        {
            "title": "Étude de faisabilité pour extension de piste",
            "category": "Études",
            "description": "Réalisation d'une étude de faisabilité pour l'extension de la piste d'atterrissage.",
            "budget_min": 800000,
            "budget_max": 1200000,
            "days_until_deadline": 60,
            "status": "active"
        },
        {
            "title": "Maintenance des systèmes de climatisation",
            "category": "Maintenance",
            "description": "Contrat de maintenance annuelle pour les systèmes de climatisation des terminaux.",
            "budget_min": 400000,
            "budget_max": 600000,
            "days_until_deadline": 20,
            "status": "active"
        }
    ]
    
    for data in tenders_data:
        deadline = datetime.utcnow() + timedelta(days=data['days_until_deadline'])
        
        tender = CallForTenders(
            title=data['title'],
            reference=generate_reference('AO'),
            description=data['description'],
            category=data['category'],
            budget_min=data['budget_min'],
            budget_max=data['budget_max'],
            publication_date=datetime.utcnow(),
            deadline=deadline,
            status=data['status'],
            requirements="Soumissionnaire doit être inscrit au registre du commerce et avoir une expérience d'au moins 3 ans dans le domaine.",
            contact_person="Service des Marchés Publics",
            contact_email="marches@onda.ma",
            contact_phone="+212 5XX-XXXXXX",
            document_url="/static/documents/cahier_charges.pdf",
            created_by=random.choice(admin_users).id
        )
        db.session.add(tender)
    
    try:
        db.session.commit()
        print("Appels d'offres d'exemple ajoutés avec succès!")
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de l'ajout des appels d'offres: {e}")

def create_sample_job_offers():
    """Crée des exemples d'offres d'emploi"""
    # Données pour les offres d'emploi
    job_data = [
        {
            "title": "Ingénieur Aéronautique",
            "department": "Technique",
            "location": "Casablanca",
            "contract_type": "CDI",
            "experience_level": "Senior",
            "description": "Nous recherchons un ingénieur aéronautique expérimenté pour rejoindre notre équipe technique.",
            "requirements": "Diplôme d'ingénieur en aéronautique, minimum 5 ans d'expérience, connaissances en réglementation aérienne.",
            "benefits": "Assurance santé, tickets restaurant, formation continue",
            "salary_min": 25000,
            "salary_max": 35000,
            "days_until_deadline": 30,
            "status": "active"
        },
        {
            "title": "Contrôleur Aérien",
            "department": "Contrôle Aérien",
            "location": "Marrakech",
            "contract_type": "CDI",
            "experience_level": "Confirmé",
            "description": "Poste de contrôleur aérien à l'aéroport de Marrakech-Ménara.",
            "requirements": "Formation en contrôle aérien, certification OACI, anglais courant, résistance au stress.",
            "benefits": "Assurance santé, primes de vol, horaires variables",
            "salary_min": 30000,
            "salary_max": 45000,
            "days_until_deadline": 25,
            "status": "active"
        },
        {
            "title": "Agent d'escale",
            "department": "Exploitation",
            "location": "Agadir",
            "contract_type": "CDD",
            "experience_level": "Débutant accepté",
            "description": "Agent d'escale pour l'accueil et l'information des passagers.",
            "requirements": "Bac+2 minimum, anglais obligatoire, espagnol apprécié, bon relationnel.",
            "benefits": "Formation assurée, tickets restaurant, avantages voyage",
            "salary_min": 7000,
            "salary_max": 9000,
            "days_until_deadline": 15,
            "status": "active"
        },
        {
            "title": "Chef de Projet IT",
            "department": "Systèmes d'Information",
            "location": "Rabat",
            "contract_type": "CDI",
            "experience_level": "Expert",
            "description": "Direction des projets informatiques stratégiques de l'office.",
            "requirements": "Diplôme d'ingénieur en informatique, 10 ans d'expérience dont 5 en gestion de projet, certification PMP un plus.",
            "benefits": "Salaire compétitif, voiture de fonction, télétravail partiel",
            "salary_min": 50000,
            "salary_max": 70000,
            "days_until_deadline": 40,
            "status": "active"
        },
        {
            "title": "Stagiaire en Communication",
            "department": "Communication",
            "location": "Tanger",
            "contract_type": "Stage",
            "experience_level": "Étudiant",
            "description": "Stage en communication et relations publiques.",
            "requirements": "Étudiant en communication, maîtrise des réseaux sociaux, créativité.",
            "benefits": "Indemnité de stage, expérience enrichissante, possibilité d'embauche",
            "salary_min": 3000,
            "salary_max": 3500,
            "days_until_deadline": 10,
            "status": "active"
        }
    ]
    
    # Utilisateurs admin
    admin_users = User.query.filter_by(is_admin=True).all()
    
    if not admin_users:
        print("Aucun utilisateur admin trouvé. Créez d'abord un utilisateur admin.")
        return
    
    for data in job_data:
        deadline = datetime.utcnow() + timedelta(days=data['days_until_deadline'])
        
        job = JobOffer(
            title=data['title'],
            reference=generate_reference('EMP'),
            department=data['department'],
            location=data['location'],
            contract_type=data['contract_type'],
            experience_level=data['experience_level'],
            description=data['description'],
            requirements=data['requirements'],
            benefits=data['benefits'],
            salary_min=data['salary_min'],
            salary_max=data['salary_max'],
            publication_date=datetime.utcnow(),
            deadline=deadline,
            status=data['status'],
            contact_person="Service des Ressources Humaines",
            contact_email="recrutement@onda.ma",
            contact_phone=f"+212 5{random.randint(10, 99)}-{random.randint(100000, 999999)}",
            created_by=random.choice(admin_users).id
        )
        db.session.add(job)
    
    try:
        db.session.commit()
        print("Offres d'emploi d'exemple ajoutées avec succès!")
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de l'ajout des offres d'emploi: {e}")

if __name__ == "__main__":
    with app.app_context():
        print("Ajout des appels d'offres...")
        create_sample_tenders()
        print("\nAjout des offres d'emploi...")
        create_sample_job_offers()
        print("\nTerminé !")
