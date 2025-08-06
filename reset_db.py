#!/usr/bin/env python3
"""
Script to completely reset the ONDA database
This will drop all tables and recreate them with the new structure
"""

import mysql.connector
from mysql.connector import Error
from app import app, db, User, Airport, Restaurant, Transport, Shopping, News, Contact, ActivityLog, Flight
from werkzeug.security import generate_password_hash

def reset_database():
    """Drop and recreate the database with new structure"""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Drop the existing database
            print("Dropping existing database...")
            cursor.execute("DROP DATABASE IF EXISTS onda_db_S")
            
            # Create the database again
            cursor.execute("CREATE DATABASE onda_db_S CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✓ Database 'onda_db_S' recreated successfully")
            
            cursor.close()
            connection.close()
            
        # Now create tables using SQLAlchemy
        with app.app_context():
            print("Creating database tables...")
            db.create_all()
            print("✓ Database tables created successfully")
            
            # Add admin user
            if not User.query.filter_by(username='admin').first():
                admin = User(
                    username='admin',
                    email='admin@onda.ma',
                    password_hash=generate_password_hash('admin123'),
                    is_admin=True
                )
                db.session.add(admin)
                print("✓ Admin user created")
            
            # Add regular user
            if not User.query.filter_by(username='user').first():
                user = User(
                    username='user',
                    email='user@onda.ma',
                    password_hash=generate_password_hash('user123'),
                    is_admin=False
                )
                db.session.add(user)
                print("✓ Regular user created")
            
            # Add all ONDA airports
            airports_data = [
                {
                    "name": "Agadir Al Massira",
                    "city": "Agadir",
                    "code": "AGA",
                    "lat": 30.3281,
                    "lon": -9.4131,
                    "description": "Aéroport international d'Agadir, porte d'entrée vers le sud du Maroc."
                },
                {
                    "name": "Al Hoceima Chérif El Idrissi",
                    "city": "Al Hoceima",
                    "code": "AHU",
                    "lat": 35.1769,
                    "lon": -3.8394,
                    "description": "Aéroport d'Al Hoceima dans la région du Rif."
                },
                {
                    "name": "Béni Mellal",
                    "city": "Béni Mellal",
                    "code": "BEM",
                    "lat": 32.3944,
                    "lon": -6.3158,
                    "description": "Aéroport de Béni Mellal dans la région de Béni Mellal-Khénifra."
                },
                {
                    "name": "Bouarfa",
                    "city": "Bouarfa",
                    "code": "UAR",
                    "lat": 32.5019,
                    "lon": -1.9639,
                    "description": "Aéroport de Bouarfa dans la région de l'Oriental."
                },
                {
                    "name": "Casablanca Mohammed V",
                    "city": "Casablanca",
                    "code": "CMN",
                    "lat": 33.3675,
                    "lon": -7.5897,
                    "description": "Principal aéroport international du Maroc, situé à Casablanca."
                },
                {
                    "name": "Dakhla",
                    "city": "Dakhla",
                    "code": "VIL",
                    "lat": 23.7183,
                    "lon": -15.9319,
                    "description": "Aéroport de Dakhla dans les provinces du Sud."
                },
                {
                    "name": "Errachidia Moulay Ali Chérif",
                    "city": "Errachidia",
                    "code": "ERH",
                    "lat": 31.9475,
                    "lon": -4.3983,
                    "description": "Aéroport d'Errachidia dans la région de Drâa-Tafilalet."
                },
                {
                    "name": "Essaouira Mogador",
                    "city": "Essaouira",
                    "code": "ESU",
                    "lat": 31.3975,
                    "lon": -9.6817,
                    "description": "Aéroport d'Essaouira, ville côtière historique."
                },
                {
                    "name": "Fès Saïs",
                    "city": "Fès",
                    "code": "FEZ",
                    "lat": 33.9275,
                    "lon": -4.9778,
                    "description": "Aéroport de Fès, capitale spirituelle du Maroc."
                },
                {
                    "name": "Guelmim",
                    "city": "Guelmim",
                    "code": "GLN",
                    "lat": 28.9867,
                    "lon": -10.0567,
                    "description": "Aéroport de Guelmim, porte du Sahara."
                },
                {
                    "name": "Laâyoune Hassan 1er",
                    "city": "Laâyoune",
                    "code": "EUN",
                    "lat": 27.1517,
                    "lon": -13.2194,
                    "description": "Aéroport de Laâyoune dans les provinces du Sud."
                },
                {
                    "name": "Marrakech Ménara",
                    "city": "Marrakech",
                    "code": "RAK",
                    "lat": 31.6069,
                    "lon": -8.0363,
                    "description": "Aéroport international desservant la ville impériale de Marrakech."
                },
                {
                    "name": "Nador El Aroui",
                    "city": "Nador",
                    "code": "NDR",
                    "lat": 34.9889,
                    "lon": -3.0283,
                    "description": "Aéroport de Nador dans la région de l'Oriental."
                },
                {
                    "name": "Ouarzazate",
                    "city": "Ouarzazate",
                    "code": "OZZ",
                    "lat": 30.9392,
                    "lon": -6.9094,
                    "description": "Aéroport d'Ouarzazate, porte du désert."
                },
                {
                    "name": "Oujda Angads",
                    "city": "Oujda",
                    "code": "OUD",
                    "lat": 34.7867,
                    "lon": -1.9239,
                    "description": "Aéroport d'Oujda dans la région de l'Oriental."
                },
                {
                    "name": "Rabat-Salé",
                    "city": "Rabat",
                    "code": "RBA",
                    "lat": 34.0514,
                    "lon": -6.7517,
                    "description": "Aéroport de la capitale administrative du Maroc."
                },
                {
                    "name": "Tanger Ibn Battouta",
                    "city": "Tanger",
                    "code": "TNG",
                    "lat": 35.7267,
                    "lon": -5.9169,
                    "description": "Aéroport international de Tanger, porte de l'Europe."
                },
                {
                    "name": "Tétouan Sania R'mel",
                    "city": "Tétouan",
                    "code": "TTU",
                    "lat": 35.5944,
                    "lon": -5.3200,
                    "description": "Aéroport de Tétouan dans la région de Tanger-Tétouan-Al Hoceima."
                },
                {
                    "name": "Zagora",
                    "city": "Zagora",
                    "code": "ZAG",
                    "lat": 30.3306,
                    "lon": -5.8667,
                    "description": "Aéroport de Zagora dans la vallée du Drâa."
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
            print(f"✓ Added {len(airports_data)} airports")
            
            # Add sample restaurants
            restaurants_data = [
                {
                    "name": "La Sqala",
                    "city": "Casablanca",
                    "cuisine": "Marocaine",
                    "rating": 4.5,
                    "location": "Boulevard des Almohades, Casablanca",
                    "description": "Restaurant traditionnel marocain dans un cadre authentique."
                },
                {
                    "name": "Rick's Café",
                    "city": "Casablanca",
                    "cuisine": "Internationale",
                    "rating": 4.2,
                    "location": "248 Boulevard Sour Jdid, Casablanca",
                    "description": "Restaurant inspiré du film Casablanca."
                },
                {
                    "name": "Nomad",
                    "city": "Marrakech",
                    "cuisine": "Moderne",
                    "rating": 4.7,
                    "location": "1 Rue Amesfah, Marrakech",
                    "description": "Cuisine moderne marocaine avec vue panoramique."
                }
            ]
            
            for rest_data in restaurants_data:
                restaurant = Restaurant(
                    name=rest_data["name"],
                    city=rest_data["city"],
                    cuisine_type=rest_data["cuisine"],
                    rating=rest_data["rating"],
                    location=rest_data["location"],
                    description=rest_data["description"],
                    is_open=True
                )
                db.session.add(restaurant)
            print(f"✓ Added {len(restaurants_data)} restaurants")
            
            # Add sample transport
            transport_data = [
                {
                    "name": "Casa Taxi",
                    "type": "Taxi",
                    "city": "Casablanca",
                    "description": "Service de taxi officiel de Casablanca.",
                    "price": 25.0
                },
                {
                    "name": "Tramway de Casablanca",
                    "type": "Tramway",
                    "city": "Casablanca",
                    "description": "Réseau de tramway moderne.",
                    "price": 6.0
                },
                {
                    "name": "Bus CTM",
                    "type": "Bus",
                    "city": "Rabat",
                    "description": "Transport en bus confortable.",
                    "price": 15.0
                }
            ]
            
            for trans_data in transport_data:
                transport = Transport(
                    name=trans_data["name"],
                    type=trans_data["type"],
                    city=trans_data["city"],
                    description=trans_data["description"],
                    price=trans_data["price"],
                    available=True
                )
                db.session.add(transport)
            print(f"✓ Added {len(transport_data)} transport options")
            
            # Add sample shopping
            shopping_data = [
                {
                    "name": "Morocco Mall",
                    "city": "Casablanca",
                    "type": "Centre commercial",
                    "description": "Le plus grand centre commercial du Maroc.",
                    "location": "Boulevard de la Corniche, Casablanca",
                    "opening_hours": "10h00 - 22h00"
                },
                {
                    "name": "Souk de Marrakech",
                    "city": "Marrakech",
                    "type": "Souk traditionnel",
                    "description": "Marché traditionnel au cœur de la médina.",
                    "location": "Médina de Marrakech",
                    "opening_hours": "9h00 - 19h00"
                }
            ]
            
            for shop_data in shopping_data:
                shopping = Shopping(
                    name=shop_data["name"],
                    city=shop_data["city"],
                    type=shop_data["type"],
                    description=shop_data["description"],
                    location=shop_data["location"],
                    opening_hours=shop_data["opening_hours"],
                    is_open=True
                )
                db.session.add(shopping)
            print(f"✓ Added {len(shopping_data)} shopping centers")
            
            # Add sample news
            news_data = [
                {
                    "title": "Nouveau terminal à l'aéroport Mohammed V",
                    "content": "L'ONDA annonce l'ouverture prochaine d'un nouveau terminal.",
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
            print(f"✓ Added {len(news_data)} news items")
            
            # Add sample flights
            from datetime import datetime, timedelta
            today = datetime.now()
            
            # Get airport IDs for sample flights
            casablanca_airport = Airport.query.filter_by(code='CMN').first()
            rabat_airport = Airport.query.filter_by(code='RBA').first()
            
            if casablanca_airport and rabat_airport:
                sample_flights = [
                    # Departures from Casablanca
                    Flight(
                        flight_number='AT101',
                        airline='Royal Air Maroc',
                        airport_id=casablanca_airport.id,
                        destination='Paris',
                        flight_type='departure',
                        scheduled_time=today.replace(hour=8, minute=30),
                        status='Scheduled',
                        gate='A12',
                        terminal='T1',
                        aircraft_type='Boeing 737'
                    ),
                    Flight(
                        flight_number='AT205',
                        airline='Royal Air Maroc',
                        airport_id=casablanca_airport.id,
                        destination='Madrid',
                        flight_type='departure',
                        scheduled_time=today.replace(hour=14, minute=15),
                        status='Boarding',
                        gate='B7',
                        terminal='T1',
                        aircraft_type='Airbus A320'
                    ),
                    Flight(
                        flight_number='EK751',
                        airline='Emirates',
                        airport_id=casablanca_airport.id,
                        destination='Dubai',
                        flight_type='departure',
                        scheduled_time=today.replace(hour=23, minute=45),
                        status='Scheduled',
                        gate='C3',
                        terminal='T1',
                        aircraft_type='Boeing 777'
                    ),
                    # Arrivals to Casablanca
                    Flight(
                        flight_number='AF1395',
                        airline='Air France',
                        airport_id=casablanca_airport.id,
                        destination='Paris',
                        flight_type='arrival',
                        scheduled_time=today.replace(hour=11, minute=20),
                        status='Arrived',
                        gate='A5',
                        terminal='T1',
                        aircraft_type='Airbus A319'
                    ),
                    Flight(
                        flight_number='IB1125',
                        airline='Iberia',
                        airport_id=casablanca_airport.id,
                        destination='Madrid',
                        flight_type='arrival',
                        scheduled_time=today.replace(hour=16, minute=30),
                        status='Delayed',
                        gate='B12',
                        terminal='T1',
                        aircraft_type='Airbus A321'
                    ),
                    # Flights from Rabat
                    Flight(
                        flight_number='AT301',
                        airline='Royal Air Maroc',
                        airport_id=rabat_airport.id,
                        destination='Tunis',
                        flight_type='departure',
                        scheduled_time=today.replace(hour=10, minute=0),
                        status='Departed',
                        gate='1',
                        terminal='T1',
                        aircraft_type='Boeing 737'
                    ),
                    Flight(
                        flight_number='TU671',
                        airline='Tunisair',
                        airport_id=rabat_airport.id,
                        destination='Tunis',
                        flight_type='arrival',
                        scheduled_time=today.replace(hour=18, minute=45),
                        status='Scheduled',
                        gate='2',
                        terminal='T1',
                        aircraft_type='Airbus A320'
                    )
                ]
                
                for flight in sample_flights:
                    db.session.add(flight)
                
                print("✓ Added sample flights")
            
            db.session.commit()
            print("✓ Database reset completed successfully!")
            print("\nLogin credentials:")
            print("Admin: username='admin', password='admin123'")
            print("User: username='user', password='user123'")
            
    except Error as e:
        print(f"✗ Error resetting database: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Resetting ONDA database...")
    reset_database()
