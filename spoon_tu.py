"""
Spoon-tu: Child Agent
Formats and displays messages from parent agent every 11 seconds
Uses GPT 4o mini to create nicely formatted console output
"""
import threading
import time
from datetime import datetime
from typing import Optional, Dict
from openai import OpenAI


class SpoonTu:
    def __init__(self, api_key: str, parent_agent):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        self.parent_agent = parent_agent
        
        # Configuration
        self.check_interval = 11  # seconds
        self.is_running = False
        self.last_displayed_message: Optional[Dict] = None
        
        print(f"\n📢 {datetime.now().strftime('%H:%M:%S')} - Child Agent 'Spoon-tu' initialized")
        print(f"   Check Interval: {self.check_interval} seconds")
    
    def format_message_with_gpt(self, message: Dict) -> str:
        """Use GPT 4o mini to create a nicely formatted message"""
        try:
            prompt = f"""
Create a beautifully formatted console report based on the following repository monitoring data:

Repository: {message.get('repository', 'Unknown')}
Check Time: {message.get('check_time', 'Unknown')}
Changes Detected: {'✅ YES' if message.get('changes_detected') else '❌ NO'}
Number of New Commits: {message.get('new_commits', 0)}

{'Modified Files/Commits:' if message.get('modified_files') else ''}
{chr(10).join([f"  • [{f.get('sha', 'N/A')}] {f.get('message', 'N/A')} by {f.get('author', 'Unknown')}" for f in message.get('modified_files', [])])}

GPT Analysis:
{message.get('gpt_analysis', 'No analysis available')}

Please format this as a clear, visually appealing console report with appropriate sections, emojis, and formatting.
"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400,
                temperature=0.9
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error formatting message: {e}"
    
    def display_formatted_message(self, message: Dict) -> None:
        """Display the formatted message"""
        if message == self.last_displayed_message:
            print(f"\n⏳ {datetime.now().strftime('%H:%M:%S')} - No new messages from parent agent")
            return
        
        self.last_displayed_message = message
        
        # Format message using GPT
        formatted_output = self.format_message_with_gpt(message)
        
        print("\n" + "=" * 80)
        print(f"📋 FORMATTED REPOSITORY REPORT - {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 80)
        print(formatted_output)
        print("=" * 80)
    
    def check_for_messages(self) -> None:
        """Check if parent agent has new messages"""
        latest_message = self.parent_agent.get_latest_ar_nab_h_message()
        
        if latest_message:
            self.display_formatted_message(latest_message)
        else:
            print(f"\n⏳ {datetime.now().strftime('%H:%M:%S')} - Waiting for first message from Ar-Nab-h agent...")
    
    def run(self) -> None:
        """Main loop for Spoon-tu agent"""
        self.is_running = True
        
        print(f"\n✅ Spoon-tu agent started - checking every {self.check_interval} seconds")
        print("=" * 80)
        
        try:
            # Initial check
            time.sleep(2)
            self.check_for_messages()
            
            while self.is_running:
                time.sleep(self.check_interval)
                self.check_for_messages()
        except KeyboardInterrupt:
            self.shutdown()
    
    def shutdown(self) -> None:
        """Gracefully shutdown the agent"""
        self.is_running = False
        print(f"\n🛑 {datetime.now().strftime('%H:%M:%S')} - Spoon-tu agent shutting down...")
