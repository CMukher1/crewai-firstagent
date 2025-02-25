# First Agent - CrewAI Project

A CrewAI-based project that demonstrates the use of multiple LLM providers (OpenAI, OpenRouter, and local Ollama) with configurable agents.

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd first_agent
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys as needed

## Configuration

The project supports multiple LLM providers:

1. OpenAI
2. OpenRouter
3. Local Ollama

To switch between providers, edit `src/first_agent/crew.py` and uncomment the desired configuration.

## Running the Project

```bash
crewai run
```

## Project Structure

```
first_agent/
├── src/
│   └── first_agent/
│       ├── crew.py          # Main crew configuration
│       ├── main.py          # Entry point
│       └── tools/           # Custom tools
├── .env.example            # Example environment variables
├── .gitignore             # Git ignore file
├── pyproject.toml         # Project configuration
└── README.md             # This file
```

## License

MIT
