"""
Script to update database with emergency features tables
"""
from app import app, db

def update_database():
    with app.app_context():
        # Create all tables (including new ones)
        db.create_all()
        print("✓ Database updated successfully!")
        print("✓ EmergencyContact table created")
        print("✓ AmbulanceBooking table created")

if __name__ == '__main__':
    update_database()
