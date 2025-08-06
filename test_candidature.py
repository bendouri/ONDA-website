#!/usr/bin/env python3
"""Script pour tester la sauvegarde des candidatures"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, db, JobApplication, JobOffer, User
    
    print("=== TEST CANDIDATURE COMPLÈTE ===")
    
    with app.app_context():
        # 1. Vérifier les utilisateurs
        users = User.query.all()
        print(f"Utilisateurs disponibles: {len(users)}")
        for user in users:
            print(f"  - {user.username} (ID: {user.id}, Admin: {user.is_admin})")
        
        # 2. Créer une offre d'emploi si nécessaire
        job = JobOffer.query.first()
        if not job:
            print("Création d'une offre d'emploi test...")
            job = JobOffer(
                title='Développeur Web',
                reference='DEV001',
                department='IT',
                location='Casablanca',
                deadline=datetime(2025, 12, 31).date(),
                contract_type='CDI',
                experience_level='Intermédiaire',
                description='Poste de développeur web',
                requirements='Bac+3 en informatique',
                status='active',
                created_by=1
            )
            db.session.add(job)
            db.session.commit()
            print(f"✅ Offre créée avec ID: {job.id}")
        else:
            print(f"✅ Offre existante: {job.title} (ID: {job.id})")
        
        # 3. Créer une candidature test
        print("Création d'une candidature test...")
        
        # Récupérer l'utilisateur normal
        user_normal = User.query.filter_by(is_admin=False).first()
        print(f"Utilisateur normal: {user_normal.username} (ID: {user_normal.id})")
        
        # Vérifier si une candidature existe déjà
        existing = JobApplication.query.filter_by(
            job_offer_id=job.id,
            user_id=user_normal.id
        ).first()
        
        if existing:
            print(f"Candidature existante trouvée: ID {existing.id}")
        else:
            candidature = JobApplication(
                job_offer_id=job.id,
                user_id=user_normal.id,
                first_name='Test',
                last_name='Candidat',
                email='test@example.com',
                phone='0123456789',
                address='123 Rue Test, Casablanca',
                birth_date=datetime(1990, 1, 1).date(),
                nationality='Marocaine',
                education_level='Bac+5',
                experience_years=3,
                current_position='Développeur Junior',
                skills='PHP, Python, JavaScript',
                languages='Français, Anglais, Arabe',
                cv_url='http://example.com/cv.pdf',
                cover_letter_url='http://example.com/lettre.pdf',
                motivation_letter='Je suis très motivé pour ce poste...',
                status='pending'
            )
            
            print("Ajout de la candidature...")
            db.session.add(candidature)
            
            print("Sauvegarde en base...")
            db.session.commit()
            
            print(f"✅ Candidature créée avec ID: {candidature.id}")
        
        # 4. Vérifier le total des candidatures
        total = JobApplication.query.count()
        print(f"Total candidatures en base: {total}")
        
        # 5. Lister toutes les candidatures
        candidatures = JobApplication.query.all()
        print("Liste des candidatures:")
        for c in candidatures:
            print(f"  - ID: {c.id}, Nom: {c.first_name} {c.last_name}")
            print(f"    Email: {c.email}, Offre: {c.job_offer_id}")
            print(f"    Statut: {c.status}, Date: {c.applied_at}")
        
        print("=== TEST TERMINÉ ===")
        
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()
