"""
Main Orchestrator for Multi-Agent System
Coordinates parent agent and child agents
"""
import threading
import time
import getpass
from datetime import datetime
from furious_nyl import FuriousNYL
from ar_nab_h import ArNabH
from spoon_tu import SpoonTu


def get_api_key() -> str:
    """Get OpenAI API key from user at runtime"""
    print("\n" + "=" * 80)
    print("🔐 Multi-Agent System - API Key Configuration")
    print("=" * 80)
    print("\nThis system requires an OpenAI API key for GPT 4o mini models.")
    print("Your API key will be used only for this session and not stored.")
    print("\nTo get your API key:")
    print("  1. Visit: https://platform.openai.com/api/keys")
    print("  2. Create a new API key")
    print("  3. Copy and paste it here\n")
    
    api_key = getpass.getpass("Enter your OpenAI API key: ")
    
    if not api_key or len(api_key.strip()) == 0:
        raise ValueError("API key cannot be empty")
    
    return api_key.strip()


def main():
    """Main entry point for the multi-agent system"""
    print("\n" + "=" * 80)
    print("🚀 MULTI-AGENT SYSTEM INITIALIZATION")
    print("=" * 80)
    
    try:
        # Get API key from user
        api_key = get_api_key()
        
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
        print("🎯 AGENT SYSTEM READY")
        print("=" * 80)
        print("\nAgent Configuration:")
        print("  • Parent Agent: Furious-NYL (Coordinator)")
        print("  • Child Agent 1: Ar-Nab-h (GitHub Monitor - 10s interval)")
        print("  • Child Agent 2: Spoon-tu (Message Formatter - 11s interval)")
        print(f"\nStarting at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nPress Ctrl+C to stop the system gracefully")
        print("=" * 80)
        
        # Create and start threads for each agent
        threads = []
        
        # Parent agent thread
        parent_thread = threading.Thread(
            target=parent_agent.run,
            name="Furious-NYL",
            daemon=False
        )
        threads.append(parent_thread)
        
        # Ar-Nab-h agent thread
        ar_nab_h_thread = threading.Thread(
            target=ar_nab_h.run,
            name="Ar-Nab-h",
            daemon=False
        )
        threads.append(ar_nab_h_thread)
        
        # Spoon-tu agent thread
        spoon_tu_thread = threading.Thread(
            target=spoon_tu.run,
            name="Spoon-tu",
            daemon=False
        )
        threads.append(spoon_tu_thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        print("\n" + "=" * 80)
        print("🏁 SYSTEM SHUTDOWN COMPLETE")
        print("=" * 80)
        
    except KeyboardInterrupt:
        print("\n\n" + "=" * 80)
        print("⚠️  SHUTDOWN SIGNAL RECEIVED")
        print("=" * 80)
        print("Gracefully shutting down all agents...")
        
        # Signal all agents to stop
        try:
            parent_agent.shutdown()
            ar_nab_h.shutdown()
            spoon_tu.shutdown()
        except:
            pass
        
        # Wait a moment for clean shutdown
        time.sleep(2)
        print("\n✅ All agents have been shut down")
        
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("Please provide a valid API key.")
    except Exception as e:
        print(f"\n❌ Fatal Error: {e}")
        print("Please check your configuration and try again.")


if __name__ == "__main__":
    main()
