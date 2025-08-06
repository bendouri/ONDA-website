#!/usr/bin/env python3
"""
Database initialization script for ONDA website
This script creates the MySQL database and populates it with sample data
"""

import mysql.connector
from mysql.connector import Error
from app import app, db, User, Airport, Restaurant, Transport, Shopping, News
from werkzeug.security import generate_password_hash

def create_database():
    """Create the MySQL database if it doesn't exist"""
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='onda_db_S'  # Default XAMPP MySQL password is empty
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS onda_db_S CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("Database 'onda_db' created successfully or already exists")
            
            cursor.close()
            connection.close()
            
    except Error as e:
        print(f"Error creating database: {e}")
        return False
    
    return True

def populate_sample_data():
    """Populate the database with sample data"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully")
        
        # Create admin user if not exists
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                email='admin@onda.ma',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
            print("Admin user created (username: admin, password: admin123)")
        
        # Create sample regular user
        if not User.query.filter_by(username='user').first():
            user = User(
                username='user',
                email='user@example.com',
                password_hash=generate_password_hash('user123'),
                is_admin=False
            )
            db.session.add(user)
            print("Sample user created (username: user, password: user123)")
        
        # Add airports
        if not Airport.query.first():
            airports_data = [
                {
                    "name": "Casablanca - Mohammed V",
                    "city": "Casablanca",
                    "code": "CMN",
                    "lat": 33.367,
                    "lon": -7.589,
                    "description": "Principal aéroport international du Maroc, situé à Nouaceur, à 30 km au sud-est de Casablanca."
                },
                {
                    "name": "Marrakech - Ménara",
                    "city": "Marrakech",
                    "code": "RAK",
                    "lat": 31.605,
                    "lon": -8.036,
                    "description": "Aéroport international desservant la ville impériale de Marrakech et la région touristique."
                },
                {
                    "name": "Agadir - Al Massira",
                    "city": "Agadir",
                    "code": "AGA",
                    "lat": 30.325,
                    "lon": -9.413,
                    "description": "Aéroport international d'Agadir, porte d'entrée vers les plages du sud du Maroc."
                },
                {
                    "name": "Fès - Saïs",
                    "city": "Fès",
                    "code": "FEZ",
                    "lat": 33.927,
                    "lon": -4.978,
                    "description": "Aéroport international de Fès, desservant la capitale spirituelle du Maroc."
                },
                {
                    "name": "Rabat - Salé",
                    "city": "Rabat",
                    "code": "RBA",
                    "lat": 34.05,
                    "lon": -6.75,
                    "description": "Aéroport international de la capitale administrative du Maroc."
                },
                {
                    "name": "Tanger - Ibn Battouta",
                    "city": "Tanger",
                    "code": "TNG",
                    "lat": 35.726,
                    "lon": -5.917,
                    "description": "Aéroport international de Tanger, porte d'entrée vers l'Europe."
                },
                {
                    "name": "Oujda - Angads",
                    "city": "Oujda",
                    "code": "OUD",
                    "lat": 34.787,
                    "lon": -1.923,
                    "description": "Aéroport international d'Oujda, dans l'est du Maroc."
                },
                {
                    "name": "Laâyoune - Hassan Ier",
                    "city": "Laâyoune",
                    "code": "EUN",
                    "lat": 27.151,
                    "lon": -13.219,
                    "description": "Aéroport international de Laâyoune, dans le sud du Maroc."
                }
            ]
            
            for airport_data in airports_data:
                airport = Airport(
                    name=airport_data["name"],
                    city=airport_data["city"],
                    code=airport_data["code"],
                    latitude=airport_data["lat"],
                    longitude=airport_data["lon"],
                    description=airport_data["description"]
                )
                db.session.add(airport)
            print(f"Added {len(airports_data)} airports")
        
        # Add restaurants
        if not Restaurant.query.first():
            restaurants_data = [
                {
                    "name": "La Sqala",
                    "city": "Casablanca",
                    "cuisine": "Marocaine",
                    "rating": 4.5,
                    "address": "Boulevard des Almohades, Casablanca",
                    "phone": "+212 522 26 09 60",
                    "description": "Restaurant traditionnel marocain dans un cadre authentique avec vue sur l'océan."
                },
                {
                    "name": "Rick's Café",
                    "city": "Casablanca",
                    "cuisine": "Internationale",
                    "rating": 4.2,
                    "address": "248 Boulevard Sour Jdid, Casablanca",
                    "phone": "+212 522 27 42 07",
                    "description": "Restaurant inspiré du film Casablanca, cuisine internationale raffinée."
                },
                {
                    "name": "Nomad",
                    "city": "Marrakech",
                    "cuisine": "Moderne",
                    "rating": 4.7,
                    "address": "1 Rue Amesfah, Marrakech",
                    "phone": "+212 524 38 16 09",
                    "description": "Cuisine moderne marocaine avec une vue panoramique sur la médina."
                },
                {
                    "name": "Le Jardin",
                    "city": "Marrakech",
                    "cuisine": "Française",
                    "rating": 4.3,
                    "address": "32 Souk Jeld, Sidi Abdelaziz, Marrakech",
                    "phone": "+212 524 37 82 95",
                    "description": "Restaurant français dans un magnifique jardin au cœur de la médina."
                },
                {
                    "name": "Pure Passion Restaurant",
                    "city": "Agadir",
                    "cuisine": "Fruits de mer",
                    "rating": 4.4,
                    "address": "Promenade de la Plage, Agadir",
                    "phone": "+212 528 84 10 90",
                    "description": "Spécialités de fruits de mer frais avec vue sur l'océan Atlantique."
                }
            ]
            
            for rest_data in restaurants_data:
                restaurant = Restaurant(
                    name=rest_data["name"],
                    city=rest_data["city"],
                    cuisine_type=rest_data["cuisine"],
                    rating=rest_data["rating"],
                    location=rest_data["address"],
                    phone=rest_data["phone"],
                    description=rest_data["description"],
                    is_open=True
                )
                db.session.add(restaurant)
            print(f"Added {len(restaurants_data)} restaurants")
        
        # Add transport options
        if not Transport.query.first():
            transport_data = [
                {
                    "name": "Casa Taxi",
                    "type": "Taxi",
                    "city": "Casablanca",
                    "description": "Service de taxi officiel de Casablanca, disponible 24h/24.",
                    "price_range": "10-50 MAD",
                    "contact_info": "+212 522 20 20 20"
                },
                {
                    "name": "Tramway de Casablanca",
                    "type": "Tramway",
                    "city": "Casablanca",
                    "description": "Réseau de tramway moderne reliant les principaux quartiers de Casablanca.",
                    "price_range": "6 MAD",
                    "contact_info": "www.casatramway.ma"
                },
                {
                    "name": "Bus CTM",
                    "type": "Bus",
                    "city": "Marrakech",
                    "description": "Service de bus longue distance et urbain.",
                    "price_range": "5-200 MAD",
                    "contact_info": "+212 524 43 44 02"
                },
                {
                    "name": "InDrive",
                    "type": "VTC",
                    "city": "Rabat",
                    "description": "Service de transport avec chauffeur via application mobile.",
                    "price_range": "15-80 MAD",
                    "contact_info": "Application mobile InDrive"
                }
            ]
            
            for trans_data in transport_data:
                # Extract price from price_range (take the higher value)
                price_str = trans_data["price_range"].split("-")[-1].replace(" MAD", "")
                try:
                    price = float(price_str)
                except:
                    price = 20.0  # default price
                    
                transport = Transport(
                    name=trans_data["name"],
                    type=trans_data["type"],
                    city=trans_data["city"],
                    description=trans_data["description"],
                    price=price,
                    contact_info=trans_data["contact_info"],
                    available=True
                )
                db.session.add(transport)
            print(f"Added {len(transport_data)} transport options")
        
        # Add shopping centers
        if not Shopping.query.first():
            shopping_data = [
                {
                    "name": "Morocco Mall",
                    "city": "Casablanca",
                    "type": "Centre commercial",
                    "description": "Le plus grand centre commercial du Maroc avec plus de 350 boutiques.",
                    "address": "Boulevard de la Corniche, Casablanca",
                    "opening_hours": "10h00 - 22h00"
                },
                {
                    "name": "Souk de Marrakech",
                    "city": "Marrakech",
                    "type": "Souk traditionnel",
                    "description": "Marché traditionnel au cœur de la médina de Marrakech.",
                    "address": "Médina de Marrakech",
                    "opening_hours": "9h00 - 19h00"
                },
                {
                    "name": "Mega Mall",
                    "city": "Rabat",
                    "type": "Centre commercial",
                    "description": "Centre commercial moderne avec cinéma et restaurants.",
                    "address": "Avenue Mohammed VI, Rabat",
                    "opening_hours": "10h00 - 22h00"
                }
            ]
            
            for shop_data in shopping_data:
                shopping = Shopping(
                    name=shop_data["name"],
                    city=shop_data["city"],
                    type=shop_data["type"],
                    description=shop_data["description"],
                    location=shop_data["address"],
                    opening_hours=shop_data["opening_hours"],
                    is_open=True
                )
                db.session.add(shopping)
            print(f"Added {len(shopping_data)} shopping centers")
        
        # Add sample news
        if not News.query.first():
            news_data = [
                {
                    "title": "Nouveau terminal à l'aéroport Mohammed V",
                    "content": "L'ONDA annonce l'ouverture prochaine d'un nouveau terminal à l'aéroport Mohammed V de Casablanca, qui permettra d'augmenter la capacité d'accueil de 5 millions de passagers supplémentaires par an.",
                    "author": "ONDA Communication",
                    "is_published": True
                },
                {
                    "title": "Modernisation des aéroports régionaux",
                    "content": "Un programme de modernisation des aéroports régionaux est en cours, incluant l'amélioration des infrastructures et des services aux passagers dans 8 aéroports du royaume.",
                    "author": "ONDA Communication",
                    "is_published": True
                }
            ]
            
            for news_item in news_data:
                news = News(
                    title=news_item["title"],
                    content=news_item["content"],
                    author=news_item["author"],
                    is_published=news_item["is_published"]
                )
                db.session.add(news)
            print(f"Added {len(news_data)} news articles")
        
        # Commit all changes
        db.session.commit()
        print("All sample data has been successfully added to the database!")

def main():
    """Main function to initialize the database"""
    print("Initializing ONDA database...")
    
    # Step 1: Create database
    if create_database():
        print("✓ Database created successfully")
    else:
        print("✗ Failed to create database")
        return
    
    # Step 2: Populate with sample data
    try:
        populate_sample_data()
        print("✓ Sample data added successfully")
        print("\n" + "="*50)
        print("DATABASE INITIALIZATION COMPLETE!")
        print("="*50)
        print("Admin credentials:")
        print("  Username: admin")
        print("  Password: admin123")
        print("\nUser credentials:")
        print("  Username: user")
        print("  Password: user123")
        print("\nYou can now start the Flask application with: python app.py")
        print("="*50)
    except Exception as e:
        print(f"✗ Error populating database: {e}")

if __name__ == "__main__":
    main()
