# Quick Start Guide - Multi-Agent GitHub Monitor

## 5-Minute Setup

### Step 1: Get OpenAI API Key
1. Go to https://platform.openai.com/api/keys
2. Click "Create new secret key"
3. Copy the key (you'll need it in Step 3)

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the System
```bash
python main.py
```

When prompted, paste your OpenAI API key and press Enter.

## What Happens Next

The system will:

1. **Initialize 3 Agents**
   - Furious-NYL (Parent/Coordinator)
   - Ar-Nab-h (GitHub Monitor)
   - Spoon-tu (Report Formatter)

2. **Start Monitoring** (Default: Linux Kernel Repository)
   - Every 10 seconds: Ar-Nab-h checks for changes
   - Every 11 seconds: Spoon-tu displays formatted reports
   - Parent agent coordinates communication

3. **Display Reports** to your console with:
   - New commits detected
   - Files changed
   - AI analysis of changes

## Stop the System

Press `Ctrl+C` at any time to gracefully shutdown all agents.

## Change the Repository

To monitor a different repository, edit `ar_nab_h.py`:

Find this section in `ArNabH.__init__()`:
```python
# GitHub repository configuration
self.repo_owner = "torvalds"
self.repo_name = "linux"
```

Replace with:
```python
self.repo_owner = "your-username"
self.repo_name = "your-repository"
```

Then run `python main.py` again.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "No module named 'openai'" | Run: `pip install -r requirements.txt` |
| "Invalid API key" | Verify your API key is correct and active |
| No output appears | Check network connection and API credits |

## System Requirements

- Python 3.8 or higher
- OpenAI API key with GPT 4o mini access
- Internet connection

## Estimated Costs

- Continuous 24-hour monitoring: ~$1-3/month
- One-time setup: Free
- API overages: Pay-as-you-go (very affordable)

## Next Steps

- Review the full README.md for advanced configuration
- Customize the repository being monitored
- Modify check intervals in agent files
- Add more agents to monitor multiple repositories

## Example Run

```
================================================================================
🚀 MULTI-AGENT SYSTEM INITIALIZATION
================================================================================

🔐 Multi-Agent System - API Key Configuration
================================================================================

Enter your OpenAI API key: ••••••••••••••••••••••••••••••••

✅ API key received (length: 48 characters)
================================================================================

🎯 AGENT SYSTEM READY
================================================================================

Agent Configuration:
  • Parent Agent: Furious-NYL (Coordinator)
  • Child Agent 1: Ar-Nab-h (GitHub Monitor - 10s interval)
  • Child Agent 2: Spoon-tu (Message Formatter - 11s interval)

Starting at: 2024-11-16 14:25:30

Press Ctrl+C to stop the system gracefully
================================================================================

✅ Parent Agent 'Furious-NYL' is active and monitoring child agents...

✅ Ar-Nab-h agent started - monitoring every 10 seconds

✅ Spoon-tu agent started - checking every 11 seconds

📊 Creating baseline snapshot...
✅ Baseline created: 7f8e9d0c1b2a3f4e...

================================================================================

[Reports will appear here as changes are detected and formatted]

```

## Help & Support

- Check README.md for detailed documentation
- Review code comments for understanding agent logic
- Modify timeout values if experiencing API issues
- Ensure adequate API rate limits for your plan

Enjoy monitoring! 🚀
