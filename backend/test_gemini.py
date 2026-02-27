import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

print(f"API Key found: {'Yes' if GEMINI_API_KEY else 'No'}")
print(f"API Key (first 10 chars): {GEMINI_API_KEY[:10]}..." if GEMINI_API_KEY else "No API key")

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        # List available models
        print("\nAvailable models:")
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                print(f"  - {model.name}")
        
        # Try with gemini-2.5-flash
        model = genai.GenerativeModel('gemini-2.5-flash')
        print("\n✓ Gemini AI configured successfully with gemini-2.5-flash")
        
        # Test a simple query
        response = model.generate_content("Say hello")
        print(f"✓ Test response: {response.text[:50]}...")
        print("\n✓✓✓ Gemini API is working correctly! ✓✓✓")
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
else:
    print("✗ No API key found in .env file")
