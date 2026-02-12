# LangGraph Butler "Alfred"

This project implements AI agents using [LangGraph](https://langchain-ai.github.io/langgraph/) and [Ollama](https://ollama.com/) to act as "Alfred", a helpful butler.

There are two main workflows:

1.  **Multimodal Assistant (`main.py`)**:
    *   Uses a vision-capable model (`ministral-3:8b` via Ollama) to extract text from images.
    *   Performs calculations (division) using tools.
    *   Can answer questions based on provided image context (e.g., meal plans/training regimens).

2.  **Email Processor (`main2.py`)**:
    *   Classifies incoming emails as "Spam" or "Legitimate".
    *   Drafts responses for legitimate emails using an LLM (`kimi-k2.5:cloud` via Ollama).
    *   Integrates with [LangFuse](https://langfuse.com/) for observability and trace tracking.

## Prerequisites

*   **Python 3.x**
*   **Ollama**: Running locally with the following models pulled:
    *   `ministral-3:8b` (for vision/main.py)
    *   `qwen3:8b` (for logic/main.py)
    *   `kimi-k2.5:cloud` (for email/main2.py)
    *   *Note: You simplify this by updating the code to use models you have available.*
*   **LangFuse** (Optional, for `main2.py`): Account and API keys if you want to track traces.

## Installation

1.  Clone the repository.
2.  Create and activate a virtual environment (optional but recommended).
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Create a `.env` file in the root directory with the following variables (primarily for `main2.py`):

```env
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_BASE_URL=https://cloud.langfuse.com # or your self-hosted URL
```

## Usage

### Run the Multimodal Assistant
```bash
python main.py
```
This will visualize the graph and then process an example request involving division and reading a training/meal plan from `training_and_meals.png`.

### Run the Email Processor
```bash
python main2.py
```
This will visualize the email processing workflow graph and process example spam and legitimate emails.

## Project Structure

*   `main.py`: Logic for the multimodal assistant agent.
*   `main2.py`: Logic for the email processing agent with LangFuse integration.
*   `reproduce_issue.py`: Minimal script for debugging.
*   `requirements.txt`: Python package dependencies.
