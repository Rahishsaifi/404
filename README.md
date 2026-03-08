# Azure AI Foundry Agent – Local Run

Run your Azure AI Foundry agent (`hr-policy`) locally using the AI Projects Python SDK.

## Prerequisites

- **Python 3.9+**
- **Azure CLI** logged in (`az login`) so `DefaultAzureCredential` can authenticate
- An Azure AI Foundry project with your agent deployed

## Setup

### 1. Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install --pre azure-ai-projects>=2.0.0b1
pip install azure-identity python-dotenv
```

### 3. Environment variables

Your `.env` file is already created with the values you provided. To change them later, edit `.env` or set:

| Variable | Description |
|----------|-------------|
| `AZURE_EXISTING_AGENT_ID` | Agent reference, e.g. `hr-policy:1` |
| `AZURE_EXISTING_AIPROJECT_ENDPOINT` | AI Project endpoint URL from Foundry |
| `AZURE_SUBSCRIPTION_ID` | Azure subscription ID |
| (others) | Used by Azure/azd tooling as needed |

## Run the agent

```bash
python run_agent.py
```

This calls your `hr-policy` agent with: *"Tell me what you can help with."* and prints the response.

## Authentication

The script uses `DefaultAzureCredential`, which will try (in order):

1. Environment variables (e.g. `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`)
2. Azure CLI (`az login`)
3. Other configured credentials

Ensure you’re logged in:

```bash
az login
```

**If you see “DefaultAzureCredential failed to retrieve a token”:**

- Install [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) and run `az login`, or
- Use a service principal: set `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, and `AZURE_CLIENT_SECRET` in your environment (or `.env`).

## Project layout

```
dexgpt/
├── .env              # Your env vars (do not commit)
├── .env.example      # Template for env vars
├── .gitignore
├── README.md
├── requirements.txt
└── run_agent.py      # Script to call the agent
```

## Next steps

- Change the prompt in `run_agent.py` (the `content` in `input= [...]`) to try different questions.
- Add a simple CLI or loop to chat with the agent interactively.
# 404
