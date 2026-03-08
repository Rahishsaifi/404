"""
Run the Azure AI Foundry agent locally.

Before running:
    pip install --pre azure-ai-projects>=2.0.0b1
    pip install azure-identity python-dotenv

Set environment variables (or use .env file with your Azure Foundry values).
"""

import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Load .env if present
load_dotenv()

# Endpoint from Azure Foundry (AI Project)
my_endpoint = os.getenv(
    "AZURE_EXISTING_AIPROJECT_ENDPOINT",
    "https://rahishsaifi46-4341-resource.services.ai.azure.com/api/projects/rahishsaifi46-4341",
)

project_client = AIProjectClient(
    endpoint=my_endpoint,
    credential=DefaultAzureCredential(),
)

# Agent name and version (e.g. from AZURE_EXISTING_AGENT_ID "hr-policy:1")
agent_id = os.getenv("AZURE_EXISTING_AGENT_ID", "hr-policy:1")
my_agent, my_version = agent_id.split(":") if ":" in agent_id else (agent_id, "1")

openai_client = project_client.get_openai_client()

# Reference the agent to get a response
response = openai_client.responses.create(
    input=[{"role": "user", "content": "Tell me what you can help with."}],
    extra_body={
        "agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}
    },
)

print(f"Response output: {response.output_text}")
