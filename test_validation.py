"""
Basic validation tests for the Personal Trainer App
Tests the structure and presence of key functions
"""

import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_imports():
    """Test that all required modules can be imported"""
    try:
        import streamlit
        import supabase
        from dotenv import load_dotenv
        print("✓ All required modules can be imported")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_app_structure():
    """Test that app.py has the expected structure"""
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Check for key functions
    required_functions = [
        'sign_up',
        'sign_in',
        'sign_out',
        'create_workout',
        'get_workouts',
        'create_meal_plan',
        'get_meal_plans',
        'assign_workout',
        'assign_meal_plan',
        'get_today_assignments',
        'mark_workout_complete',
        'mark_meal_complete',
        'trainer_dashboard',
        'client_dashboard',
        'main'
    ]
    
    missing = []
    for func in required_functions:
        if f"def {func}(" not in content:
            missing.append(func)
    
    if missing:
        print(f"✗ Missing functions: {', '.join(missing)}")
        return False
    else:
        print(f"✓ All {len(required_functions)} required functions present")
        return True


def test_schema_structure():
    """Test that schema.sql has the expected tables"""
    with open('schema.sql', 'r') as f:
        content = f.read()
    
    required_tables = [
        'profiles',
        'workouts',
        'meal_plans',
        'workout_assignments',
        'meal_assignments'
    ]
    
    missing = []
    for table in required_tables:
        if f"CREATE TABLE IF NOT EXISTS {table}" not in content:
            missing.append(table)
    
    if missing:
        print(f"✗ Missing tables in schema: {', '.join(missing)}")
        return False
    else:
        print(f"✓ All {len(required_tables)} required tables present in schema")
        return True


def test_rls_policies():
    """Test that RLS policies are defined"""
    with open('schema.sql', 'r') as f:
        content = f.read()
    
    if 'ENABLE ROW LEVEL SECURITY' in content and 'CREATE POLICY' in content:
        print("✓ Row Level Security policies are defined")
        return True
    else:
        print("✗ RLS policies missing or incomplete")
        return False


def test_requirements():
    """Test that requirements.txt has necessary packages"""
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    required_packages = ['streamlit', 'supabase', 'python-dotenv']
    missing = []
    
    for package in required_packages:
        if package not in content:
            missing.append(package)
    
    if missing:
        print(f"✗ Missing packages in requirements.txt: {', '.join(missing)}")
        return False
    else:
        print(f"✓ All required packages present in requirements.txt")
        return True


def test_env_example():
    """Test that .env.example exists and has required variables"""
    if not os.path.exists('.env.example'):
        print("✗ .env.example file missing")
        return False
    
    with open('.env.example', 'r') as f:
        content = f.read()
    
    required_vars = ['SUPABASE_URL', 'SUPABASE_KEY']
    missing = []
    
    for var in required_vars:
        if var not in content:
            missing.append(var)
    
    if missing:
        print(f"✗ Missing variables in .env.example: {', '.join(missing)}")
        return False
    else:
        print("✓ .env.example has all required variables")
        return True


def run_all_tests():
    """Run all validation tests"""
    print("\n" + "="*60)
    print("Personal Trainer App - Validation Tests")
    print("="*60 + "\n")
    
    tests = [
        ("Import Tests", test_imports),
        ("App Structure", test_app_structure),
        ("Schema Structure", test_schema_structure),
        ("RLS Policies", test_rls_policies),
        ("Requirements", test_requirements),
        ("Environment Config", test_env_example),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\n{name}:")
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "="*60)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    print("="*60 + "\n")
    
    return all(results)


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
