from app import app, db
from app import Flight, Airport
from datetime import datetime, timedelta
import random

def create_sample_flights():
    # Vérifier si des aéroports existent
    airports = Airport.query.all()
    if not airports:
        print("Aucun aéroport trouvé. Veuillez d'abord ajouter des aéroports.")
        return
    
    # Aéroports de destinations internationales
    destinations = [
        "Paris (CDG)", "Londres (LHR)", "Madrid (MAD)", "New York (JFK)", 
        "Dubai (DXB)", "Istanbul (IST)", "Casablanca (CMN)", "Dakar (DSS)"
    ]
    
    # Compagnies aériennes
    airlines = ["Royal Air Maroc", "Air France", "Emirates", "Turkish Airlines", 
               "Iberia", "British Airways", "Qatar Airways", "Lufthansa"]
    
    # Types d'avions
    aircrafts = ["Boeing 737-800", "Airbus A320", "Boeing 787 Dreamliner", 
                "Airbus A350", "Boeing 777-300ER"]
    
    # Statuts de vol
    statuses = ['Scheduled', 'On Time', 'Delayed', 'Boarding', 'Departed', 'Arrived']
    
    # Créer des vols pour les 4 jours
    current_date = datetime(2025, 8, 4)
    end_date = datetime(2025, 8, 7)
    
    while current_date <= end_date:
        # Créer 10 vols par jour (5 départs, 5 arrivées)
        for i in range(5):
            # Vols au départ (departures)
            flight_num = f"AT{random.randint(200, 999)}"
            departure_time = current_date.replace(hour=random.randint(6, 22), minute=random.choice([0, 15, 30, 45]))
            
            flight = Flight(
                flight_number=flight_num,
                airline=random.choice(airlines),
                airport_id=random.choice(airports).id,
                destination=random.choice(destinations),
                flight_type='departure',
                scheduled_time=departure_time,
                actual_time=departure_time + timedelta(minutes=random.randint(-15, 45)),
                status=random.choices(statuses, weights=[5, 50, 10, 15, 10, 10])[0],
                gate=f"{random.choice(['A', 'B', 'C'])}{random.randint(1, 30)}",
                terminal=random.choice(['1', '2', '3']),
                aircraft_type=random.choice(aircrafts)
            )
            db.session.add(flight)
            
            # Vols à l'arrivée (arrivals)
            flight_num = f"AT{random.randint(200, 999)}"
            arrival_time = current_date.replace(hour=random.randint(6, 22), minute=random.choice([0, 15, 30, 45]))
            
            flight = Flight(
                flight_number=flight_num,
                airline=random.choice(airlines),
                airport_id=random.choice(airports).id,
                destination=random.choice(destinations),
                flight_type='arrival',
                scheduled_time=arrival_time,
                actual_time=arrival_time + timedelta(minutes=random.randint(-15, 45)),
                status=random.choices(statuses, weights=[5, 50, 10, 15, 10, 10])[0],
                gate=f"{random.choice(['A', 'B', 'C'])}{random.randint(1, 30)}",
                terminal=random.choice(['1', '2', '3']),
                aircraft_type=random.choice(aircrafts)
            )
            db.session.add(flight)
        
        current_date += timedelta(days=1)
    
    # Sauvegarder les changements
    try:
        db.session.commit()
        print("Vols d'exemple ajoutés avec succès!")
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de l'ajout des vols: {e}")

if __name__ == "__main__":
    with app.app_context():
        create_sample_flights()
