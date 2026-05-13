# QA Agents - AI News Podcast Generator

An AI-powered automation pipeline that researches the latest AI testing news and converts it into an engaging podcast script with audio output.

## Overview

This project uses [CrewAI](https://crewai.com/) to orchestrate multiple AI agents that work together to:
1. Research latest AI testing news from the web
2. Convert findings into a podcast script format
3. Generate audio from the script

## Features

- **Automated Research**: Uses Tavily search API to find real-time AI testing news
- **Multi-Agent Pipeline**: Researcher → Podcast Writer workflow
- **Audio Generation**: Converts scripts to MP3 using pyttsx3
- **Ollama Integration**: Runs locally using Llama 3.1 model
- **Output Management**: Auto-cleans output folder before each run

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Researcher │ ──> │   Podcast   │ ──> │    Audio    │
│   Agent     │     │   Writer    │     │  Generator  │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │
  Tavily API         Script Text        podcast_audio.mp3
```

## Requirements

- Python 3.11+
- [Ollama](https://ollama.ai/) with Llama 3.1 model
- Tavily API key

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd QA_Agents
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install crewai crewai-tools python-dotenv langchain-community langchain-ollama tavily-python pyttsx3
```

3. **Install and run Ollama**
```bash
# Install Ollama from https://ollama.ai/

# Pull Llama 3.1 model
ollama pull llama3.1
```

4. **Configure environment**
Create a `.env` file in the project root:
```env
TAVILY_API_KEY=your_tavily_api_key_here
```

Get your Tavily API key at: https://tavily.com/

## Usage

### Run the application
```bash
python App.py
```

### Output
- Console: Displays the generated podcast script
- Audio: `output/podcast_audio.mp3`

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TAVILY_API_KEY` | API key for Tavily search | Yes |
| `CROWD_DISABLE_TRACING` | Disable CrewAI telemetry (optional) | No |

### Ollama Configuration

The app uses `llama3.1` model by default. To change:
```python
llm="ollama/llama3"  # or other available model
```

## Project Structure

```
QA_Agents/
├── App.py           # Main application entry point
├── pyproject.toml   # Python package configuration
├── setup.py         # Package setup script
├── .env             # Environment variables (create this)
├── output/          # Generated audio files
│   └── podcast_audio.mp3
├── .venv/           # Virtual environment (if used)
└── README.md        # This file
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| crewai | >=0.30.0 | Multi-agent framework |
| crewai-tools | >=0.1.0 | Tools for agents |
| langchain-ollama | >=0.1.0 | Ollama LLM integration |
| tavily-python | >=0.3.0 | Web search API |
| pyttsx3 | >=2.90.0 | Text-to-speech |

## Troubleshooting

### Issue: Model not found
```bash
ollama pull llama3.1
```

### Issue: Tavily search fails
- Verify your `TAVILY_API_KEY` in `.env`
- Check your Tavily API quota

### Issue: Audio not generating
- Ensure pyttsx3 is installed: `pip install pyttsx3`
- Check Windows audio services are running

### Issue: Encoding errors on Windows
The app includes UTF-8 encoding fixes for Windows terminals.

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request