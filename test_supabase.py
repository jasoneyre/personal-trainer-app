#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print(f"Testing Supabase connection...")
print(f"URL: {SUPABASE_URL}")
print(f"Key starts with: {SUPABASE_KEY[:20]}...")
print(f"Key length: {len(SUPABASE_KEY)}")

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("✅ Supabase client created successfully")
    
    # Test a simple query
    result = supabase.table('profiles').select('count').execute()
    print("✅ Database query successful")
    print(f"Profiles table accessible: {result}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"Error type: {type(e)}")