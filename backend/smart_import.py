"""
Smart import that handles foreign key constraints properly
"""
import requests
import json

PRODUCTION_URL = "https://smartcinicai.onrender.com"
SECRET_KEY = "import-data-2026"

# Data in correct order (users first, then hospitals, then doctors)
data_to_import = {
    "users": [
        {"email": "2@gmail.com", "password": "1", "name": "ADITHYA", "user_type": "hospital_admin", "phone": "+917893031396"},
        {"email": "eppiliashokkumara@gmail.com", "password": "1", "name": "ASHOK HOSPITALS", "user_type": "hospital_admin", "phone": "+917893031396"},
        {"email": "Aditya@gmail.com", "password": "1", "name": "ADITHYA", "user_type": "hospital_admin", "phone": "8989723145"},
        {"email": "123@gmail.com", "password": "1", "name": "ASHISH", "user_type": "hospital_admin", "phone": "6567898769"},
    ],
    "hospitals": [
        {"name": "ADITHYA HOSPITALS", "address": "SRI SAI NAGAR , PRAGATHI NAGAR,BACHUPALLY", "contact": "+917893031396", "admin_email": "2@gmail.com", "description": "ONE OF THE MOST FAMOUS HOSPITALS IN THE PRESENT CITY"},
        {"name": "ASHOK HOSPITAL", "address": "4-3/10, SRI SAI NAGAR, BACHUPALLY, HYDERABAD", "contact": "+917893031396", "admin_email": "eppiliashokkumara@gmail.com", "description": "best hospital in the hyderabad"},
        {"name": "Aditya Hospitals", "address": "hyderabad", "contact": "8989723145", "admin_email": "Aditya@gmail.com", "description": "famous hospital in the hyderabad and good in cardiac"},
        {"name": "ESI HOSPITAL", "address": "SANATH NAGAR, ERRAGADA, HYDERABAD", "contact": "6567898769", "admin_email": "123@gmail.com", "description": "Govt hospital and free for ESI card holders"},
    ],
    "doctors": [
        {"email": "3@gmail.com", "password": "1", "name": "DEESHA", "hospital_name": "ADITHYA HOSPITALS", "specialization": "Orthopedic", "experience": 3, "fee": 1000, "about": "MBBS IN THE MADURAI UNIVERSITY"},
        {"email": "naveenraj131521@gmail.com", "password": "1", "name": "Naveen", "hospital_name": "ADITHYA HOSPITALS", "specialization": "Cardiologist", "experience": 10, "fee": 2300, "about": ""},
        {"email": "Ashok@gmail.com", "password": "1", "name": "ASHOK", "hospital_name": "ESI HOSPITAL", "specialization": "Dermatologist", "experience": 5, "fee": 1000, "about": "Board-certified Dermatologist"},
        {"email": "Ashish@gmail.com", "password": "1", "name": "ASHISH", "hospital_name": "ESI HOSPITAL", "specialization": "General Physician", "experience": 10, "fee": 1500, "about": "Passionate General Practitioner"},
        {"email": "adi@gmail.com", "password": "1", "name": "Aditya", "hospital_name": "Aditya Hospitals", "specialization": "Cardiologist", "experience": 12, "fee": 2000, "about": "Senior Cardiologist"},
        {"email": "jagan@gmail.com", "password": "1", "name": "Jagan", "hospital_name": "Aditya Hospitals", "specialization": "Orthopedic", "experience": 15, "fee": 2000, "about": "Expert in joint conditions"},
        {"email": "SUBARAO@gmail.com", "password": "1", "name": "SUBARAO", "hospital_name": "ASHOK HOSPITAL", "specialization": "Neurologist", "experience": 15, "fee": 2000, "about": "Expert Neurologist"},
        {"email": "Akshith@gmail.com", "password": "1", "name": "AKSHITH", "hospital_name": "ASHOK HOSPITAL", "specialization": "General Physician", "experience": 20, "fee": 2000, "about": "Seasoned General Physician"},
    ]
}

def import_data():
    print("=" * 60)
    print("SMART DATA IMPORT TO PRODUCTION")
    print("=" * 60)
    print(f"\nProduction URL: {PRODUCTION_URL}")
    print(f"\nData to import:")
    print(f"  - {len(data_to_import['users'])} Hospital Admins")
    print(f"  - {len(data_to_import['hospitals'])} Hospitals")
    print(f"  - {len(data_to_import['doctors'])} Doctors")
    
    confirm = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("❌ Import cancelled")
        return
    
    print("\n📤 Sending data to production...")
    
    try:
        response = requests.post(
            f"{PRODUCTION_URL}/smart-import-data",
            json={
                "secret": SECRET_KEY,
                "data": data_to_import
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("\n✅ SUCCESS!")
            print("=" * 60)
            print(f"Status: {result.get('status')}")
            print(f"Message: {result.get('message')}")
            
            imported = result.get('imported', {})
            print(f"\n📊 Imported:")
            print(f"   - Users: {imported.get('users', 0)}")
            print(f"   - Hospitals: {imported.get('hospitals', 0)}")
            print(f"   - Doctors: {imported.get('doctors', 0)}")
            
            current = result.get('current_data', {})
            print(f"\n📊 Total in Production:")
            print(f"   - Users: {current.get('users', 0)}")
            print(f"   - Hospitals: {current.get('hospitals', 0)}")
            print(f"   - Doctors: {current.get('doctors', 0)}")
            
            print("\n✅ Visit: " + PRODUCTION_URL)
            
        else:
            print(f"\n❌ ERROR: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    import_data()
