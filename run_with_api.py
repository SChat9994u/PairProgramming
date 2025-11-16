"""
API Key Runner - Securely runs the main program with API key
"""
import subprocess
import sys
import os
import getpass

if __name__ == "__main__":
    # Get API key from environment or prompt user
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        api_key = getpass.getpass("Enter your OpenAI API key: ")
    
    # Set the API key in environment
    env = os.environ.copy()
    env['OPENAI_API_KEY'] = api_key
    
    # Run main.py and pass the API key via stdin
    process = subprocess.Popen(
        [sys.executable, "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env,
        text=True
    )
    
    # Send API key to stdin
    stdout, _ = process.communicate(input=api_key + "\n", timeout=60)
    print(stdout)
