#!/usr/bin/env python3
"""Script pour déboguer les candidatures"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, db, JobApplication, JobOffer, User
    
    print("=== DEBUG CANDIDATURE ===")
    
    with app.app_context():
        # 1. Vérifier les utilisateurs
        users = User.query.all()
        print(f"Utilisateurs: {len(users)}")
        for user in users:
            print(f"  - {user.username} (ID: {user.id})")
        
        # 2. Vérifier les offres
        jobs = JobOffer.query.all()
        print(f"Offres d'emploi: {len(jobs)}")
        for job in jobs:
            print(f"  - {job.title} (ID: {job.id})")
        
        # 3. Créer une candidature test SIMPLE
        if jobs and users:
            job = jobs[0]
            user = User.query.filter_by(is_admin=False).first()
            
            print(f"Test avec Job ID: {job.id}, User ID: {user.id}")
            
            # Vérifier si candidature existe déjà
            existing = JobApplication.query.filter_by(
                job_offer_id=job.id,
                user_id=user.id
            ).first()
            
            if existing:
                print(f"Candidature existante trouvée: ID {existing.id}")
            else:
                print("Création d'une nouvelle candidature...")
                
                candidature = JobApplication(
                    job_offer_id=job.id,
                    user_id=user.id,
                    first_name='Debug',
                    last_name='Test',
                    email='debug@test.com',
                    phone='0123456789',
                    address='Test Address',
                    birth_date=datetime(1990, 1, 1).date(),
                    nationality='Test',
                    education_level='Bac+3',
                    experience_years=2,
                    current_position='Test Position',
                    skills='Test Skills',
                    languages='Test Languages',
                    cv_url='',
                    cover_letter_url='',
                    diploma_url='',
                    motivation_letter='Test motivation',
                    status='pending'
                )
                
                try:
                    db.session.add(candidature)
                    db.session.commit()
                    print(f"✅ Candidature créée avec ID: {candidature.id}")
                except Exception as e:
                    print(f"❌ Erreur lors de la création: {e}")
                    db.session.rollback()
        
        # 4. Lister toutes les candidatures
        candidatures = JobApplication.query.order_by(JobApplication.applied_at.desc()).all()
        print(f"\nTotal candidatures: {len(candidatures)}")
        for c in candidatures:
            print(f"  - ID {c.id}: {c.first_name} {c.last_name} ({c.applied_at})")
        
        print("=== FIN DEBUG ===")
        
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()
