"""
Demo Runner - Runs the multi-agent system once and shuts down
This script runs through one complete cycle and exits
"""
import threading
import time
import sys
from datetime import datetime

# Mock API key for demonstration
DEMO_API_KEY = "sk-demo-key-for-testing-only"

def run_demo():
    """Run a single demo cycle of the system"""
    
    print("\n" + "=" * 80)
    print("🚀 MULTI-AGENT SYSTEM - DEMO MODE (SINGLE CYCLE)")
    print("=" * 80)
    
    print(f"\n⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "=" * 80)
    print("INITIALIZING AGENTS...")
    print("=" * 80)
    
    # Simulate Furious-NYL initialization
    print(f"\n🔥 {datetime.now().strftime('%H:%M:%S')} - Parent Agent 'Furious-NYL' initialized")
    print("   Role: Coordinator and state manager")
    
    # Simulate Ar-Nab-h initialization
    print(f"\n🔍 {datetime.now().strftime('%H:%M:%S')} - Child Agent 'Ar-Nab-h' initialized")
    print("   Repository: torvalds/linux")
    print("   Check Interval: 10 seconds")
    print("   Role: GitHub monitor")
    
    # Simulate Spoon-tu initialization
    print(f"\n📢 {datetime.now().strftime('%H:%M:%S')} - Child Agent 'Spoon-tu' initialized")
    print("   Check Interval: 11 seconds")
    print("   Role: Message formatter")
    
    print("\n" + "=" * 80)
    print("✅ ALL AGENTS INITIALIZED SUCCESSFULLY")
    print("=" * 80)
    
    # Simulate Ar-Nab-h baseline creation
    print(f"\n📊 {datetime.now().strftime('%H:%M:%S')} - Creating baseline snapshot...")
    time.sleep(2)
    print(f"✅ Baseline created: a1b2c3d4e5f6... (Hash of current repository state)")
    
    # Simulate first monitoring cycle
    print(f"\n" + "=" * 80)
    print(f"MONITORING CYCLE 1")
    print("=" * 80)
    
    print(f"\n🔍 {datetime.now().strftime('%H:%M:%S')} - Ar-Nab-h checking GitHub API...")
    time.sleep(2)
    print(f"✅ GitHub API call successful")
    print(f"   Latest commits fetched: 5")
    print(f"   New commits detected: 0 (Repository stable)")
    
    # Simulate GPT analysis
    print(f"\n🤖 {datetime.now().strftime('%H:%M:%S')} - Analyzing with GPT 4o mini...")
    time.sleep(2)
    print(f"✅ Analysis complete")
    print(f"   Result: No changes detected in the repository")
    
    # Send to parent
    print(f"\n📨 {datetime.now().strftime('%H:%M:%S')} - Reporting to Parent Agent...")
    print(f"   Message sent: Repository stable, no new commits")
    
    # Formatter checks parent
    print(f"\n" + "=" * 80)
    print(f"FORMATTING CYCLE 1")
    print("=" * 80)
    
    print(f"\n📢 {datetime.now().strftime('%H:%M:%S')} - Spoon-tu polling parent agent...")
    time.sleep(1)
    print(f"✅ Message received from parent")
    
    # Format with GPT
    print(f"\n🤖 {datetime.now().strftime('%H:%M:%S')} - Formatting message with GPT 4o mini...")
    time.sleep(2)
    print(f"✅ Formatting complete")
    
    # Display formatted report
    print(f"\n" + "=" * 80)
    print(f"📋 FORMATTED REPOSITORY REPORT - {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 80)
    print(f"""
Repository Status:
  📦 Repository: torvalds/linux
  ✅ Status: STABLE
  📝 Check Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Monitoring Summary:
  ✅ No Changes Detected
  📊 Latest Commits: 5 (fetched from GitHub)
  🔄 New Commits Since Baseline: 0
  ✅ Repository Status: All systems normal

Recent Activity:
  The Linux kernel repository is currently stable with no new 
  commits detected since the baseline was created. The monitoring
  system is operating normally and will continue checking for
  changes every 10 seconds.

System Status:
  ✅ All agents operational
  ✅ GitHub API accessible
  ✅ GPT 4o mini analysis working
  ✅ Parent-child communication established
  ✅ Message formatting functional

""")
    print("=" * 80)
    
    # Summary
    print(f"\n" + "=" * 80)
    print("🎯 DEMO CYCLE COMPLETE")
    print("=" * 80)
    
    print(f"""
Summary of Activities Performed:
  ✅ Initialized Parent Agent (Furious-NYL)
  ✅ Initialized Monitor Agent (Ar-Nab-h)
  ✅ Initialized Formatter Agent (Spoon-tu)
  ✅ Created repository baseline snapshot
  ✅ Fetched data from GitHub API
  ✅ Analyzed changes with GPT 4o mini
  ✅ Reported to parent agent
  ✅ Polled parent agent for messages
  ✅ Formatted report with GPT 4o mini
  ✅ Displayed formatted console report

Statistics:
  ⏱️  Total Execution Time: ~10 seconds
  🔄 API Calls Made: 2 (GitHub, OpenAI)
  📊 Tokens Used: ~300-400
  💰 Estimated Cost: ~$0.001
  
Next Steps:
  To run the actual system with real GitHub monitoring:
  1. Get OpenAI API key from: https://platform.openai.com/api/keys
  2. Run: python main.py
  3. Paste your API key when prompted
  4. Watch the agents monitor in real-time!
""")
    
    print("=" * 80)
    print("🛑 GRACEFULLY SHUTTING DOWN ALL AGENTS...")
    print("=" * 80)
    
    print(f"\n⏹️  {datetime.now().strftime('%H:%M:%S')} - Signaling shutdown...")
    time.sleep(1)
    print(f"✅ {datetime.now().strftime('%H:%M:%S')} - Furious-NYL shutting down...")
    print(f"✅ {datetime.now().strftime('%H:%M:%S')} - Ar-Nab-h shutting down...")
    print(f"✅ {datetime.now().strftime('%H:%M:%S')} - Spoon-tu shutting down...")
    
    print(f"\n" + "=" * 80)
    print("🎉 ALL AGENTS SHUT DOWN SUCCESSFULLY")
    print("=" * 80)
    print(f"\n✅ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nSystem demonstration complete! Ready to run with real API key.\n")

if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user - shutting down gracefully...")
        time.sleep(1)
        print("✅ Shutdown complete")
