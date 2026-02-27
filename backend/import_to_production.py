"""
Import local data to production (Render deployment)
This script sends your exported data to the production server
"""
import requests
import json

# Your production URL
PRODUCTION_URL = "https://smartcinicai.onrender.com"

# Secret key for security (matches the one in app.py)
SECRET_KEY = "import-data-2026"

def import_data():
    print("=" * 60)
    print("IMPORTING DATA TO PRODUCTION")
    print("=" * 60)
    print(f"\nProduction URL: {PRODUCTION_URL}")
    print("This will import all your local hospitals, doctors, and users")
    print("\n⚠️  WARNING: This may create duplicate entries if data already exists!")
    
    # Confirm
    confirm = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("❌ Import cancelled")
        return
    
    print("\n📤 Sending data to production...")
    
    try:
        # Send POST request to import endpoint
        response = requests.post(
            f"{PRODUCTION_URL}/import-production-data",
            json={"secret": SECRET_KEY},
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("\n✅ SUCCESS!")
            print("=" * 60)
            print(f"Status: {result.get('status')}")
            print(f"Message: {result.get('message')}")
            print(f"Executed Statements: {result.get('executed_statements')}")
            
            current_data = result.get('current_data', {})
            print(f"\n📊 Current Production Data:")
            print(f"   - Users: {current_data.get('users')}")
            print(f"   - Hospitals: {current_data.get('hospitals')}")
            print(f"   - Doctors: {current_data.get('doctors')}")
            
            errors = result.get('errors')
            if errors and errors != 'None':
                print(f"\n⚠️  Errors encountered: {len(errors)}")
                for error in errors[:5]:  # Show first 5 errors
                    print(f"   - {error}")
            
            print("\n✅ You can now visit: " + PRODUCTION_URL)
            
        elif response.status_code == 403:
            print("\n❌ ERROR: Unauthorized - Invalid secret key")
            print("The secret key in this script doesn't match the server")
            
        elif response.status_code == 404:
            print("\n❌ ERROR: production_data.sql file not found on server")
            print("You need to upload the file to the server first")
            
        else:
            print(f"\n❌ ERROR: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to production server")
        print("Please check:")
        print("1. The server is running")
        print("2. The URL is correct")
        print("3. Your internet connection")
        
    except requests.exceptions.Timeout:
        print("\n❌ ERROR: Request timed out")
        print("The server took too long to respond")
        print("Try again in a few minutes")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    import_data()
