# Multi-Agent GitHub Repository Monitor

A sophisticated multi-agent system that monitors GitHub repositories for changes using OpenAI's GPT 4o mini model.

## System Architecture

### Agents Overview

#### 1. **Furious-NYL** (Parent Agent)
- Acts as the central coordinator
- Manages communication between child agents
- Stores and maintains state of repository monitoring
- Receives messages from Ar-Nab-h and forwards information to Spoon-tu

#### 2. **Ar-Nab-h** (Child Agent - Monitor)
- Monitors a public GitHub repository every 10 seconds
- Creates a baseline snapshot of the repository on startup
- Detects new commits and code changes
- Uses GPT 4o mini to analyze the nature of changes
- Reports findings to parent agent

#### 3. **Spoon-tu** (Child Agent - Formatter)
- Checks with parent agent every 11 seconds
- Receives messages about repository changes
- Uses GPT 4o mini to format messages into beautifully structured console output
- Displays detailed, formatted reports to the user

## Features

✨ **Multi-threaded Architecture**: All agents run concurrently with independent timers
🔍 **GitHub Repository Monitoring**: Real-time monitoring of publicly available repositories
🤖 **AI-Powered Analysis**: GPT 4o mini analyzes changes and formats output
🔐 **Secure API Key Input**: API key requested at runtime, never hardcoded
🎨 **Formatted Console Output**: Beautiful, emoji-enhanced formatted reports
⏰ **Independent Intervals**: Each agent operates on its own schedule

## Prerequisites

- Python 3.8+
- OpenAI API key (with access to GPT 4o mini model)
- Internet connection for GitHub API and OpenAI API calls

## Installation

1. **Clone or navigate to the project directory:**
```bash
cd ai-agent-system
```

2. **Create a virtual environment (recommended):**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Configuration

### OpenAI API Key

The system requires an OpenAI API key to function. Follow these steps:

1. **Get your API key:**
   - Visit https://platform.openai.com/api/keys
   - Sign in with your OpenAI account
   - Create a new API key
   - Copy the key

2. **Verify API Credits:**
   - Ensure your account has available API credits
   - GPT 4o mini is cost-effective for text-based operations
   - Check usage at https://platform.openai.com/usage

### Repository Configuration

The default monitored repository is the **Linux Kernel** (torvalds/linux):
- Owner: `torvalds`
- Repository: `linux`

To monitor a different repository, edit `ar_nab_h.py`:

```python
# In ArNabH.__init__()
self.repo_owner = "your-username"
self.repo_name = "your-repository"
```

## Usage

### Starting the System

```bash
python main.py
```

The system will:
1. Display system information and welcome message
2. Prompt you for your OpenAI API key
3. Initialize all agents
4. Start monitoring and reporting

### Example Output

```
================================================================================
🚀 MULTI-AGENT SYSTEM INITIALIZATION
================================================================================

🔐 Multi-Agent System - API Key Configuration
================================================================================

🔥 PARENT AGENT INITIALIZATION
Parent Agent 'Furious-NYL' initialized

🔍 CHILD AGENT INITIALIZATION
Child Agent 'Ar-Nab-h' initialized
   Repository: torvalds/linux
   Check Interval: 10 seconds

📢 Child Agent 'Spoon-tu' initialized
   Check Interval: 11 seconds

✅ API key received (length: 48 characters)

🎯 AGENT SYSTEM READY
================================================================================
```

### Stopping the System

Press `Ctrl+C` to gracefully shut down all agents. The system will:
- Signal all agents to stop
- Complete current operations
- Close connections
- Display shutdown confirmation

## Agent Communication Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      GitHub Repository                       │
│                   (torvalds/linux)                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
                      [GitHub API]
                              ↓
                     [Ar-Nab-h Agent]
                  (Monitors every 10s)
                   ↓GPT Analysis↓
           [Change Detection & Analysis]
                              ↓
                    [Furious-NYL (Parent)]
              (Receives & Stores Messages)
                              ↓
                    [Spoon-tu Agent]
                  (Checks every 11s)
                  ↓GPT Formatting↓
              [Console Output Display]
```

## Monitoring Details

### Ar-Nab-h Monitoring (10-second interval)

Each check performs:
1. **Fetch recent commits** from the monitored repository
2. **Compare with baseline** to detect new commits
3. **Extract change information** including:
   - Commit SHA
   - Commit message
   - Author name
   - Commit timestamp
4. **GPT Analysis**: Analyzes changes and their potential impact
5. **Report to Parent**: Sends comprehensive update to Furious-NYL

### Spoon-tu Formatting (11-second interval)

Each check performs:
1. **Query parent agent** for latest repository status
2. **Check for new messages** since last report
3. **GPT Formatting**: Creates beautifully formatted report including:
   - Repository name and status
   - Timestamp of check
   - List of commits with details
   - Change analysis
   - Visual formatting with sections and emojis
4. **Display**: Prints formatted report to console

## Performance Considerations

- **API Rate Limiting**: GitHub API allows 60 requests/hour unauthenticated
- **OpenAI Rate Limiting**: Check your plan's rate limits
- **Thread Safety**: Uses Python's GIL for thread safety in this context
- **Network Latency**: System includes timeout handling (10 seconds)

## Troubleshooting

### Issue: "Invalid API Key"
**Solution**: Verify your API key is correct and has proper permissions for GPT 4o mini

### Issue: GitHub API Rate Limit Exceeded
**Solution**: Either wait for rate limit reset or use a GitHub token in the API calls

### Issue: Agent Not Detecting Changes
**Solution**: 
- Verify the repository is public
- Check network connectivity
- Ensure sufficient API credits in your OpenAI account

### Issue: Agents Not Starting
**Solution**:
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8 or higher required)
- Review error messages for specific issues

## API Costs

This system uses OpenAI's GPT 4o mini model, which is very cost-effective:

- **Ar-Nab-h**: ~100-200 tokens per 10-second check (analysis)
- **Spoon-tu**: ~200-400 tokens per 11-second check (formatting)
- **Estimated monthly cost**: ~$1-3 for continuous 24-hour monitoring

Check pricing at https://openai.com/pricing

## Advanced Configuration

### Changing Check Intervals

Edit the respective agent files:

```python
# In ar_nab_h.py
self.check_interval = 10  # Change to desired seconds

# In spoon_tu.py
self.check_interval = 11  # Change to desired seconds
```

### Monitoring Multiple Repositories

Create multiple instances of Ar-Nab-h agents with different repositories:

```python
# In main.py
ar_nab_h_1 = ArNabH(api_key=api_key, parent_agent=parent_agent)
ar_nab_h_1.repo_owner = "owner1"
ar_nab_h_1.repo_name = "repo1"

ar_nab_h_2 = ArNabH(api_key=api_key, parent_agent=parent_agent)
ar_nab_h_2.repo_owner = "owner2"
ar_nab_h_2.repo_name = "repo2"
```

### Custom Analysis Prompts

Edit the GPT prompts in the agent files to customize analysis behavior:

```python
# In ar_nab_h.py - analyze_changes_with_gpt()
prompt = f"""
Your custom analysis prompt here...
"""
```

## Security Notes

🔒 **API Key Security**:
- API key is requested at runtime and never stored
- Never commit API keys to version control
- Use environment variables in production (modify the system as needed)

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| openai | 1.3.0+ | OpenAI API client |
| requests | 2.31.0+ | GitHub API HTTP requests |
| python-dotenv | 1.0.0+ | Environment variable management |

## Project Structure

```
ai-agent-system/
├── main.py              # Main orchestrator
├── furious_nyl.py       # Parent agent
├── ar_nab_h.py          # Monitor child agent
├── spoon_tu.py          # Formatter child agent
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Future Enhancements

- 🌐 Support for multiple repository monitoring
- 💾 Persistent state storage (database)
- 📧 Email notifications for important changes
- 🔔 Slack/Discord integration
- 📊 Change statistics and trending
- 🔐 GitHub token support for higher API limits
- 🎯 Configurable repository selection via CLI
- 📝 Detailed change history logging

## Contributing

Feel free to extend this system with additional agents or features!

## License

MIT License - Feel free to use and modify

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review error messages carefully
3. Verify API credentials and permissions
4. Check network connectivity

## References

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Python Threading](https://docs.python.org/3/library/threading.html)

---

**Created**: 2024
**System**: Multi-Agent GitHub Repository Monitor
**Status**: Active Development
