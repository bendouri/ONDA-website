#!/usr/bin/env python3
"""Script de test pour vérifier la base de données"""

from app import app, db, JobApplication, JobOffer, User
from sqlalchemy import inspect

def test_database():
    with app.app_context():
        print("=== TEST BASE DE DONNÉES ===")
        
        # Vérifier les tables
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tables existantes: {tables}")
        
        # Vérifier la table JobApplication
        if 'job_application' in tables:
            print("✅ Table JobApplication existe")
            
            # Compter les candidatures
            count = JobApplication.query.count()
            print(f"Nombre de candidatures: {count}")
            
            # Afficher les candidatures
            candidatures = JobApplication.query.all()
            for c in candidatures:
                print(f"- ID: {c.id}, Nom: {c.first_name} {c.last_name}, Email: {c.email}")
                
        else:
            print("❌ Table JobApplication manquante !")
            print("Création de la table...")
            db.create_all()
            print("Table créée !")
        
        # Vérifier les autres tables importantes
        print(f"\nTable JobOffer: {'✅' if 'job_offer' in tables else '❌'}")
        print(f"Table User: {'✅' if 'user' in tables else '❌'}")
        
        # Compter les offres et utilisateurs
        if 'job_offer' in tables:
            job_count = JobOffer.query.count()
            print(f"Nombre d'offres d'emploi: {job_count}")
            
        if 'user' in tables:
            user_count = User.query.count()
            print(f"Nombre d'utilisateurs: {user_count}")

if __name__ == '__main__':
    test_database()
