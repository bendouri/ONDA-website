#!/usr/bin/env python3
"""Créer un nouvel utilisateur pour tester"""

import os
import sys
from werkzeug.security import generate_password_hash

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, db, User
    
    with app.app_context():
        # Créer un nouvel utilisateur
        new_user = User(
            username='candidat',
            email='candidat@test.com',
            password_hash=generate_password_hash('candidat123'),
            is_admin=False
        )
        
        # Vérifier s'il existe déjà
        existing = User.query.filter_by(username='candidat').first()
        if existing:
            print("Utilisateur 'candidat' existe déjà")
        else:
            db.session.add(new_user)
            db.session.commit()
            print("✅ Nouvel utilisateur créé:")
            print("   Username: candidat")
            print("   Password: candidat123")
            print("   Email: candidat@test.com")
        
        # Lister tous les utilisateurs
        users = User.query.all()
        print(f"\nTotal utilisateurs: {len(users)}")
        for user in users:
            print(f"  - {user.username} (ID: {user.id}, Admin: {user.is_admin})")
            
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()
