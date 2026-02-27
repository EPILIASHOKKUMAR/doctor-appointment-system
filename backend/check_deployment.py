"""
Check if the production deployment is ready for data import
"""
import requests
import time

PRODUCTION_URL = "https://smartcinicai.onrender.com"

print("=" * 60)
print("CHECKING PRODUCTION DEPLOYMENT STATUS")
print("=" * 60)
print(f"\nProduction URL: {PRODUCTION_URL}")
print("\nChecking if the import endpoint is available...")

try:
    # Try to access the import endpoint (should return 403 without secret)
    response = requests.post(
        f"{PRODUCTION_URL}/import-production-data",
        json={"secret": "wrong-secret"},
        timeout=30
    )
    
    if response.status_code == 403:
        print("\n✅ SUCCESS! Import endpoint is available!")
        print("The deployment is ready for data import.")
        print("\nYou can now run:")
        print("  python import_to_production.py")
        
    elif response.status_code == 404:
        print("\n⏳ WAITING... Import endpoint not found yet.")
        print("Render is still deploying the new code.")
        print("\nPlease wait 2-3 more minutes and try again.")
        print("\nTo check deployment status:")
        print("1. Go to https://dashboard.render.com/")
        print("2. Click on your service")
        print("3. Check the 'Events' or 'Logs' tab")
        
    else:
        print(f"\n⚠️  Unexpected response: {response.status_code}")
        print(response.text[:200])
        
except requests.exceptions.ConnectionError:
    print("\n❌ ERROR: Cannot connect to production server")
    print("\nPossible reasons:")
    print("1. Render is still starting up (wait 2-3 minutes)")
    print("2. The service is down")
    print("3. Internet connection issue")
    print("\nCheck status at: https://dashboard.render.com/")
    
except requests.exceptions.Timeout:
    print("\n⏳ Server is slow to respond...")
    print("This might mean Render is still deploying.")
    print("Wait a few minutes and try again.")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")

print("\n" + "=" * 60)
