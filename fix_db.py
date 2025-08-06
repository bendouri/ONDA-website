#!/usr/bin/env python3
"""Script pour forcer la création des tables"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, db, JobApplication, JobOffer, User
    
    print("=== RÉPARATION BASE DE DONNÉES ===")
    
    with app.app_context():
        print("1. Suppression de l'ancienne base...")
        db.drop_all()
        
        print("2. Création des nouvelles tables...")
        db.create_all()
        
        print("3. Vérification des tables...")
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tables créées: {tables}")
        
        print("4. Test d'insertion d'une candidature...")
        
        # Créer un utilisateur test si nécessaire
        test_user = User.query.filter_by(email='test@test.com').first()
        if not test_user:
            from werkzeug.security import generate_password_hash
            test_user = User(
                username='testuser',
                email='test@test.com',
                password_hash=generate_password_hash('test123')
            )
            db.session.add(test_user)
            db.session.commit()
            print("Utilisateur test créé")
        
        # Créer une offre test si nécessaire
        test_job = JobOffer.query.first()
        if not test_job:
            test_job = JobOffer(
                title='Test Job',
                reference='TEST001',
                department='IT',
                location='Rabat',
                deadline=datetime.now().date(),
                contract_type='CDI',
                status='active',
                created_by=test_user.id
            )
            db.session.add(test_job)
            db.session.commit()
            print("Offre test créée")
        
        # Tester l'insertion d'une candidature
        test_application = JobApplication(
            job_offer_id=test_job.id,
            user_id=test_user.id,
            first_name='Test',
            last_name='User',
            email='test@test.com',
            phone='0123456789',
            address='Test Address',
            birth_date=datetime(1990, 1, 1).date(),
            nationality='Marocaine',
            education_level='Bac+5',
            experience_years=3,
            cv_url='http://test.com/cv.pdf',
            status='pending'
        )
        
        db.session.add(test_application)
        db.session.commit()
        
        print(f"✅ Candidature test créée avec ID: {test_application.id}")
        
        # Vérifier le nombre total
        count = JobApplication.query.count()
        print(f"Total candidatures: {count}")
        
        print("=== RÉPARATION TERMINÉE ===")
        
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()
