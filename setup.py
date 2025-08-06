#!/usr/bin/env python3
"""
ONDA Website Setup Script
This script helps set up the Flask application with MySQL database
"""

import os
import sys
import subprocess
import mysql.connector
from mysql.connector import Error

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def check_mysql_connection():
    """Check if MySQL server is running and accessible"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Default XAMPP password
        )
        if connection.is_connected():
            print("✅ MySQL connection successful")
            connection.close()
            return True
    except Error as e:
        print(f"❌ MySQL connection failed: {e}")
        print("Please make sure XAMPP MySQL server is running")
        return False

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing Python packages...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        'static/uploads',
        'static/css',
        'static/js',
        'static/images',
        'templates/admin',
        'instance'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def setup_database():
    """Set up the database"""
    print("🗄️  Setting up database...")
    try:
        subprocess.check_call([sys.executable, 'init_db.py'])
        print("✅ Database setup completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Database setup failed: {e}")
        return False

def create_env_file():
    """Create environment file template"""
    env_content = """# ONDA Website Environment Variables
# Copy this file to .env and update the values

# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Database Configuration
DATABASE_URL=mysql://root:@localhost/onda_db

# Email Configuration (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Upload Configuration
MAX_CONTENT_LENGTH=16777216
"""
    
    with open('.env.example', 'w', encoding='utf-8') as f:
        f.write(env_content)
    print("✅ Created .env.example file")

def main():
    """Main setup function"""
    print("🚀 ONDA Website Setup")
    print("=" * 50)
    
    # Check prerequisites
    if not check_python_version():
        return False
    
    if not check_mysql_connection():
        print("\n💡 To start MySQL with XAMPP:")
        print("1. Open XAMPP Control Panel")
        print("2. Start Apache and MySQL services")
        print("3. Run this setup script again")
        return False
    
    # Create directories
    print("\n📁 Creating directories...")
    create_directories()
    
    # Install requirements
    print("\n📦 Installing dependencies...")
    if not install_requirements():
        return False
    
    # Create environment file
    print("\n⚙️  Creating configuration files...")
    create_env_file()
    
    # Setup database
    print("\n🗄️  Initializing database...")
    if not setup_database():
        return False
    
    print("\n" + "=" * 50)
    print("🎉 SETUP COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print("\n📋 Next steps:")
    print("1. Start XAMPP MySQL server (if not already running)")
    print("2. Run: python app.py")
    print("3. Open browser to: http://localhost:5000")
    print("\n🔐 Default admin credentials:")
    print("   Username: admin")
    print("   Password: admin123")
    print("\n👤 Default user credentials:")
    print("   Username: user")
    print("   Password: user123")
    print("\n📚 Access phpMyAdmin at: http://localhost/phpmyadmin")
    print("   Database name: onda_db")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
