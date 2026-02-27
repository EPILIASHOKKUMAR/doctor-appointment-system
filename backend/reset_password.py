"""
Reset password for production users
"""
import requests

PRODUCTION_URL = "https://smartcinicai.onrender.com"
SECRET_KEY = "import-data-2026"

def reset_password():
    print("=" * 60)
    print("PASSWORD RESET FOR PRODUCTION")
    print("=" * 60)
    
    email = input("\nEnter email address: ").strip()
    new_password = input("Enter new password: ").strip()
    
    if not email or not new_password:
        print("❌ Email and password are required!")
        return
    
    confirm = input(f"\nReset password for {email}? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("❌ Cancelled")
        return
    
    print("\n📤 Sending request...")
    
    try:
        response = requests.post(
            f"{PRODUCTION_URL}/reset-user-password",
            json={
                "secret": SECRET_KEY,
                "email": email,
                "new_password": new_password
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("\n✅ SUCCESS!")
            print(f"Password reset for: {email}")
            print(f"\nYou can now login with:")
            print(f"  Email: {email}")
            print(f"  Password: {new_password}")
            
        elif response.status_code == 404:
            print(f"\n❌ ERROR: User with email {email} not found")
            print("Check the email address and try again")
            
        else:
            print(f"\n❌ ERROR: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    reset_password()
