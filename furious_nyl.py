"""
Furious-NYL: Parent Agent
Coordinates between child agents and manages message flow
"""
import threading
import time
from datetime import datetime
from typing import Dict, Optional, List
from queue import Queue
from openai import OpenAI


class FuriousNYL:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        
        # Message queues for inter-agent communication
        self.ar_nab_h_queue: Queue = Queue()
        self.spoon_tu_queue: Queue = Queue()
        
        # Store latest messages
        self.latest_ar_nab_h_message: Optional[Dict] = None
        self.is_running = True
        
        print(f"\n🔥 {datetime.now().strftime('%H:%M:%S')} - Parent Agent 'Furious-NYL' initialized")
        print("=" * 80)
    
    def process_ar_nab_h_message(self, message: Dict) -> None:
        """Store and process message from Ar-Nab-h agent"""
        self.latest_ar_nab_h_message = message
        print(f"\n📨 {datetime.now().strftime('%H:%M:%S')} - Parent received from Ar-Nab-h:")
        print(f"   Repository: {message.get('repository', 'Unknown')}")
        print(f"   Changes Detected: {message.get('changes_detected', False)}")
        if message.get('changes_detected'):
            print(f"   ⚠️  Modified Files: {len(message.get('modified_files', []))}")
    
    def get_latest_ar_nab_h_message(self) -> Optional[Dict]:
        """Return the latest message from Ar-Nab-h"""
        return self.latest_ar_nab_h_message
    
    def send_to_ar_nab_h(self, message: Dict) -> None:
        """Send message to Ar-Nab-h queue"""
        self.ar_nab_h_queue.put(message)
    
    def send_to_spoon_tu(self, message: Dict) -> None:
        """Send message to Spoon-tu queue"""
        self.spoon_tu_queue.put(message)
    
    def shutdown(self) -> None:
        """Gracefully shutdown the parent agent"""
        self.is_running = False
        print(f"\n🛑 {datetime.now().strftime('%H:%M:%S')} - Parent Agent shutting down...")
    
    def run(self) -> None:
        """Main loop for parent agent - just maintains state"""
        print(f"\n✅ Parent Agent 'Furious-NYL' is active and monitoring child agents...")
        try:
            while self.is_running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.shutdown()
