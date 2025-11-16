"""
Single Cycle Runner - Runs the system once with API and shuts down
"""
import sys
import os
import time
from datetime import datetime

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_single_cycle():
    """Run one complete cycle with actual API"""
    
    # Get API key from environment or prompt user
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        import getpass
        api_key = getpass.getpass("Enter your OpenAI API key: ")
    
    print("\n" + "=" * 80)
    print("🚀 MULTI-AGENT SYSTEM - SINGLE CYCLE WITH REAL API")
    print("=" * 80)
    
    # Import agents
    from furious_nyl import FuriousNYL
    from ar_nab_h import ArNabH
    from spoon_tu import SpoonTu
    
    try:
        print(f"\n✅ API key received (length: {len(api_key)} characters)")
        print("=" * 80)
        
        # Initialize parent agent
        print("\n1️⃣  Initializing Parent Agent...")
        parent_agent = FuriousNYL(api_key=api_key)
        
        # Initialize child agents
        print("\n2️⃣  Initializing Child Agents...")
        ar_nab_h = ArNabH(api_key=api_key, parent_agent=parent_agent)
        spoon_tu = SpoonTu(api_key=api_key, parent_agent=parent_agent)
        
        print("\n" + "=" * 80)
        print("🎯 AGENT SYSTEM READY - STARTING SINGLE CYCLE")
        print("=" * 80)
        
        # Create baseline
        print("\n📊 Creating baseline snapshot...")
        ar_nab_h.create_baseline()
        
        # First monitoring check
        print(f"\n🔍 Performing GitHub API check...")
        ar_nab_h.check_and_report()
        
        # Wait a moment
        time.sleep(2)
        
        # Format and display
        print(f"\n📢 Formatting and displaying report...")
        spoon_tu.check_for_messages()
        
        # Shutdown
        print(f"\n" + "=" * 80)
        print("🛑 SHUTTING DOWN AFTER SINGLE CYCLE")
        print("=" * 80)
        
        parent_agent.shutdown()
        ar_nab_h.shutdown()
        spoon_tu.shutdown()
        
        time.sleep(1)
        
        print(f"\n✅ Single cycle completed successfully!")
        print(f"   Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n" + "=" * 80)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        try:
            parent_agent.shutdown()
            ar_nab_h.shutdown()
            spoon_tu.shutdown()
        except:
            pass
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_single_cycle()
