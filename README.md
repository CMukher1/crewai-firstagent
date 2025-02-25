# Content Creation AI Crew

A sophisticated AI-powered content creation system built with CrewAI that leverages multiple LLM providers to generate and refine high-quality articles.

## Features

- **Content Creator Agent**: Professional writer that generates engaging articles
- **Editor Agent**: Refines and polishes content for clarity and quality
- **Multiple LLM Support**: 
  - Local Ollama (default)
  - OpenAI (configurable)
  - OpenRouter (configurable)
- **Interactive**: Takes user input for article topics
- **Markdown Output**: Generates well-formatted articles in markdown

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd content_agent
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
   - Add your API keys if using OpenAI or OpenRouter

## LLM Configuration

The project supports three LLM providers. Edit `src/content_agent/crew.py` to choose your preferred provider:

1. **Local Ollama** (Default):
```python
self.llm = LLM(
    model="ollama/deepseek-r1:8b",
    base_url="http://localhost:11434"
)
```

2. **OpenAI** (Uncomment and configure):
```python
self.llm = LLM(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

3. **OpenRouter** (Uncomment and configure):
```python
self.llm = LLM(
    model="deepseek/deepseek-r1:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
```

## Usage

1. Run the content creation crew:
```bash
crewai run
```

2. Enter your desired article topic when prompted
3. The crew will:
   - Generate initial content through the Content Creator
   - Refine the content through the Editor
   - Save the final article as 'final_article.md'

## Project Structure

```
content_agent/
├── src/
│   └── content_agent/
│       ├── config/
│       │   ├── agents.yaml    # Agent configurations
│       │   └── tasks.yaml     # Task definitions
│       ├── crew.py           # Main crew setup
│       └── main.py           # Entry point
├── .env.example             # Example environment variables
├── .gitignore              # Git ignore patterns
├── pyproject.toml          # Project configuration
└── README.md              # This file
```

## Agents

### Content Creator
- **Role**: Professional Article Writer
- **Goal**: Create engaging and informative content
- **Capabilities**: 
  - Crafts compelling narratives
  - Adapts to different audiences
  - Breaks down complex topics

### Editor
- **Role**: Senior Content Editor
- **Goal**: Ensure quality and clarity
- **Capabilities**:
  - Enhances readability
  - Ensures consistency
  - Optimizes for SEO
  - Maintains appropriate tone

## Output

The final article is saved as 'final_article.md' and includes:
- Engaging title
- Well-structured introduction
- Detailed main content sections
- Conclusion
- Key takeaways
- SEO optimizations

## License

MIT

## Support

For questions or issues:
- Open an issue in the repository
- Refer to [CrewAI documentation](https://docs.crewai.com)
