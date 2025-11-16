@echo off
REM To use this script, set your OpenAI API key as an environment variable before running:
REM set OPENAI_API_KEY=your-api-key-here
REM Then run: run.bat

REM Check if OPENAI_API_KEY is set
if not defined OPENAI_API_KEY (
    echo.
    echo ERROR: OPENAI_API_KEY environment variable is not set.
    echo.
    echo To run this script:
    echo 1. Set your API key: set OPENAI_API_KEY=your-api-key-here
    echo 2. Run this batch file: run.bat
    echo.
    pause
    exit /b 1
)

REM Run the Python script
cd /d c:\Users\GuestUser\OneDrive\Desktop\PairProg\ai-agent-system
python run_single_cycle.py

pause
