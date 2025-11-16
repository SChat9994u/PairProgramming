"""
Demo & Testing Script
Validates the multi-agent system setup and API connectivity
"""

import os
import sys
from datetime import datetime


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80)


def test_imports():
    """Test if all required modules can be imported"""
    print_header("TESTING IMPORTS")
    
    required_modules = [
        ('openai', 'OpenAI API Client'),
        ('requests', 'HTTP Library'),
        ('threading', 'Threading Support'),
        ('time', 'Time Utilities'),
        ('getpass', 'Secure Input'),
    ]
    
    all_ok = True
    for module_name, description in required_modules:
        try:
            __import__(module_name)
            print(f"  ✅ {module_name:20} - {description}")
        except ImportError:
            print(f"  ❌ {module_name:20} - MISSING: {description}")
            all_ok = False
    
    return all_ok


def test_local_modules():
    """Test if local agent modules exist and are importable"""
    print_header("TESTING LOCAL MODULES")
    
    modules = [
        'furious_nyl',
        'ar_nab_h',
        'spoon_tu',
        'main',
    ]
    
    all_ok = True
    for module in modules:
        module_path = f"{module}.py"
        if os.path.exists(module_path):
            print(f"  ✅ {module_path:20} - Found")
            try:
                # Try to import it
                if module != 'main':
                    exec(f"from {module} import *")
            except Exception as e:
                print(f"     ⚠️  Import warning: {e}")
        else:
            print(f"  ❌ {module_path:20} - NOT FOUND")
            all_ok = False
    
    return all_ok


def test_api_connectivity(api_key):
    """Test OpenAI API connectivity"""
    print_header("TESTING OPENAI API CONNECTIVITY")
    
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=api_key)
        
        print("  📡 Testing API connection...")
        
        # Make a simple test request
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Say 'API works!'" }],
            max_tokens=10,
            temperature=0.7
        )
        
        print(f"  ✅ OpenAI API is accessible")
        print(f"  ✅ Response: {response.choices[0].message.content.strip()}")
        print(f"  ✅ Model: gpt-4o-mini is available")
        return True
        
    except Exception as e:
        print(f"  ❌ OpenAI API Error: {e}")
        return False


def test_github_connectivity():
    """Test GitHub API connectivity"""
    print_header("TESTING GITHUB API CONNECTIVITY")
    
    try:
        import requests
        
        print("  📡 Testing GitHub API connection...")
        
        # Test with Linux kernel repo
        response = requests.get(
            "https://api.github.com/repos/torvalds/linux",
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"  ✅ GitHub API is accessible")
            print(f"  ✅ Repository: {data.get('full_name')}")
            print(f"  ✅ Stars: {data.get('stargazers_count')}")
            print(f"  ✅ Last Update: {data.get('updated_at')}")
            return True
        else:
            print(f"  ❌ GitHub API Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  ❌ GitHub API Error: {e}")
        return False


def test_threading():
    """Test threading capabilities"""
    print_header("TESTING THREADING")
    
    try:
        import threading
        
        test_results = []
        
        def test_thread():
            test_results.append("Thread executed successfully")
        
        thread = threading.Thread(target=test_thread)
        thread.start()
        thread.join(timeout=2)
        
        if test_results:
            print(f"  ✅ Threading works correctly")
            print(f"  ✅ Can create and manage threads")
            return True
        else:
            print(f"  ❌ Thread execution failed")
            return False
            
    except Exception as e:
        print(f"  ❌ Threading Error: {e}")
        return False


def test_file_permissions():
    """Test if files can be read and written"""
    print_header("TESTING FILE PERMISSIONS")
    
    try:
        test_file = "test_write.tmp"
        
        # Test write
        with open(test_file, 'w') as f:
            f.write("test")
        print(f"  ✅ Can write files")
        
        # Test read
        with open(test_file, 'r') as f:
            content = f.read()
        print(f"  ✅ Can read files")
        
        # Cleanup
        os.remove(test_file)
        print(f"  ✅ Can delete files")
        
        return True
        
    except Exception as e:
        print(f"  ❌ File Permission Error: {e}")
        return False


def run_full_diagnostics(api_key=None):
    """Run all diagnostic tests"""
    print("\n" * 2)
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "MULTI-AGENT SYSTEM DIAGNOSTICS" + " " * 27 + "║")
    print("║" + " " * 25 + f"Started: {datetime.now().strftime('%H:%M:%S')}" + " " * 29 + "║")
    print("╚" + "=" * 78 + "╝")
    
    results = {
        'Imports': test_imports(),
        'Local Modules': test_local_modules(),
        'Threading': test_threading(),
        'File Permissions': test_file_permissions(),
        'GitHub API': test_github_connectivity(),
    }
    
    if api_key:
        results['OpenAI API'] = test_api_connectivity(api_key)
    else:
        print_header("SKIPPING OPENAI API TEST")
        print("  ⏭️  Run with --with-api-test and provide API key to test OpenAI")
    
    # Summary
    print_header("DIAGNOSTIC SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status:10} - {test_name}")
    
    print(f"\n  Total: {passed}/{total} tests passed")
    
    if passed == total:
        print_header("🎉 ALL DIAGNOSTICS PASSED!")
        print("\nYour system is ready to run the multi-agent system!")
        print("\nNext steps:")
        print("  1. Run: python main.py")
        print("  2. Provide your OpenAI API key when prompted")
        print("  3. Watch the agents monitor and report changes!")
    else:
        print_header("⚠️  SOME TESTS FAILED")
        print("\nPlease fix the following issues:")
        for test_name, result in results.items():
            if not result:
                print(f"  • {test_name}")
        print("\nSee errors above for details on how to fix.")
    
    return passed == total


if __name__ == "__main__":
    api_key = None
    
    if "--with-api-test" in sys.argv:
        import getpass
        print("\n🔐 OpenAI API Test Selected")
        api_key = getpass.getpass("Enter your OpenAI API key: ")
    
    success = run_full_diagnostics(api_key)
    sys.exit(0 if success else 1)
