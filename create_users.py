#!/usr/bin/env python3
"""Script pour créer les utilisateurs admin et test"""

import os
import sys
from datetime import datetime

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, db, User
    from werkzeug.security import generate_password_hash
    
    print("=== CRÉATION DES UTILISATEURS ===")
    
    with app.app_context():
        # Supprimer les anciens utilisateurs
        User.query.delete()
        db.session.commit()
        
        # Créer utilisateur admin
        admin_user = User(
            username='admin',
            email='admin@onda.ma',
            password_hash=generate_password_hash('admin123'),
            is_admin=True
        )
        db.session.add(admin_user)
        
        # Créer utilisateur normal
        normal_user = User(
            username='user',
            email='user@onda.ma',
            password_hash=generate_password_hash('user123'),
            is_admin=False
        )
        db.session.add(normal_user)
        
        db.session.commit()
        
        print("✅ Utilisateurs créés avec succès !")
        print("📋 INFORMATIONS DE CONNEXION :")
        print("=" * 40)
        print("👤 ADMIN :")
        print("   Username: admin")
        print("   Email: admin@onda.ma")
        print("   Password: admin123")
        print()
        print("👤 USER :")
        print("   Username: user")
        print("   Email: user@onda.ma")
        print("   Password: user123")
        print("=" * 40)
        
        # Vérifier
        total_users = User.query.count()
        admin_count = User.query.filter_by(is_admin=True).count()
        print(f"Total utilisateurs: {total_users}")
        print(f"Admins: {admin_count}")
        
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()
