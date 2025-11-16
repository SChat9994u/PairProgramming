"""
Ar-Nab-h: Child Agent
Monitors GitHub repository for changes every 10 seconds
Uses GPT 4o mini to analyze code changes and commit details
"""
import threading
import time
import requests
import hashlib
from datetime import datetime
from typing import Dict, List, Optional
from openai import OpenAI


class ArNabH:
    def __init__(self, api_key: str, parent_agent):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        self.parent_agent = parent_agent
        
        # GitHub repository configuration
        self.repo_owner = "torvalds"
        self.repo_name = "linux"
        self.api_base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        
        # Baseline tracking
        self.baseline_hash: Optional[str] = None
        self.baseline_commits: List[Dict] = []
        self.last_check_time = None
        
        # Configuration
        self.check_interval = 10  # seconds
        self.is_running = False
        
        print(f"\n🔍 {datetime.now().strftime('%H:%M:%S')} - Child Agent 'Ar-Nab-h' initialized")
        print(f"   Repository: {self.repo_owner}/{self.repo_name}")
        print(f"   Check Interval: {self.check_interval} seconds")
    
    def get_repo_data(self) -> Dict:
        """Fetch repository data from GitHub API"""
        try:
            response = requests.get(f"{self.api_base_url}", timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching repo data: {e}")
            return {}
    
    def get_recent_commits(self, limit: int = 5) -> List[Dict]:
        """Fetch recent commits from the repository"""
        try:
            response = requests.get(
                f"{self.api_base_url}/commits",
                params={"per_page": limit},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching commits: {e}")
            return []
    
    def create_baseline(self) -> bool:
        """Create initial baseline of repository state"""
        print(f"\n📊 {datetime.now().strftime('%H:%M:%S')} - Creating baseline snapshot...")
        
        repo_data = self.get_repo_data()
        commits = self.get_recent_commits()
        
        if not repo_data or not commits:
            print("❌ Failed to create baseline")
            return False
        
        # Create a hash of current state
        state_string = f"{repo_data.get('updated_at', '')}{len(commits)}{commits[0].get('sha', '') if commits else ''}"
        self.baseline_hash = hashlib.sha256(state_string.encode()).hexdigest()
        self.baseline_commits = commits
        self.last_check_time = datetime.now()
        
        print(f"✅ Baseline created: {self.baseline_hash[:16]}...")
        return True
    
    def detect_changes(self) -> Dict:
        """Check for changes in the repository"""
        current_commits = self.get_recent_commits()
        
        if not current_commits:
            return {
                'repository': f"{self.repo_owner}/{self.repo_name}",
                'changes_detected': False,
                'check_time': datetime.now().isoformat(),
                'reason': 'Failed to fetch commits'
            }
        
        # Create current state hash
        state_string = f"{datetime.now().isoformat()[:10]}{len(current_commits)}{current_commits[0].get('sha', '')}"
        current_hash = hashlib.sha256(state_string.encode()).hexdigest()
        
        # Check if commits have changed
        changes_detected = False
        modified_files = []
        new_commits = []
        
        if self.baseline_commits:
            baseline_shas = [c.get('sha') for c in self.baseline_commits]
            current_shas = [c.get('sha') for c in current_commits]
            
            # Find new commits
            new_commits = [c for c in current_commits if c.get('sha') not in baseline_shas]
            changes_detected = len(new_commits) > 0
        
        # Extract modified files from new commits
        if new_commits:
            for commit in new_commits:
                if 'commit' in commit:
                    modified_files.append({
                        'sha': commit.get('sha', '')[:7],
                        'message': commit.get('commit', {}).get('message', '').split('\n')[0],
                        'author': commit.get('commit', {}).get('author', {}).get('name', 'Unknown'),
                        'date': commit.get('commit', {}).get('author', {}).get('date', '')
                    })
        
        return {
            'repository': f"{self.repo_owner}/{self.repo_name}",
            'changes_detected': changes_detected,
            'check_time': datetime.now().isoformat(),
            'new_commits': len(new_commits),
            'modified_files': modified_files,
            'current_hash': current_hash[:16]
        }
    
    def analyze_changes_with_gpt(self, changes: Dict) -> str:
        """Use GPT 4o mini to analyze the detected changes"""
        if not changes.get('changes_detected'):
            return "No changes detected in the repository."
        
        try:
            prompt = f"""
Analyze the following GitHub repository changes:
- Repository: {changes.get('repository')}
- Changes Detected: Yes
- Number of New Commits: {changes.get('new_commits', 0)}
- Modified Files/Commits:
{chr(10).join([f"  • {f.get('message', 'N/A')} by {f.get('author', 'Unknown')} at {f.get('date', 'N/A')}" for f in changes.get('modified_files', [])])}

Provide a brief analysis of what changed and its potential impact.
"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7,
                timeout=30
            )
            
            return response.choices[0].message.content
        except Exception as e:
            # Fallback: Return a simple analysis
            print(f"   ⚠️  GPT analysis failed: {type(e).__name__}, using fallback")
            return f"Repository has {changes.get('new_commits', 0)} new commit(s). Changes detected in {changes.get('repository', 'repository')}."
    
    def check_and_report(self) -> None:
        """Check for changes and report to parent agent"""
        changes = self.detect_changes()
        
        # Add GPT analysis
        analysis = self.analyze_changes_with_gpt(changes)
        changes['gpt_analysis'] = analysis
        
        # Send to parent agent
        self.parent_agent.process_ar_nab_h_message(changes)
        
        # Update baseline if changes detected
        if changes.get('changes_detected'):
            self.baseline_commits = self.get_recent_commits()
            print(f"   📝 Baseline updated with new commits")
    
    def run(self) -> None:
        """Main loop for Ar-Nab-h agent"""
        self.is_running = True
        
        if not self.create_baseline():
            print("❌ Failed to create baseline. Exiting Ar-Nab-h agent.")
            return
        
        print(f"\n✅ Ar-Nab-h agent started - monitoring every {self.check_interval} seconds")
        print("=" * 80)
        
        try:
            while self.is_running:
                self.check_and_report()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            self.shutdown()
    
    def shutdown(self) -> None:
        """Gracefully shutdown the agent"""
        self.is_running = False
        print(f"\n🛑 {datetime.now().strftime('%H:%M:%S')} - Ar-Nab-h agent shutting down...")
