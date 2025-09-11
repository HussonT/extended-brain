#!/usr/bin/env python3
"""Test API connection"""

import os
from pathlib import Path
from dotenv import load_dotenv
import anthropic

# Load .env
env_path = Path('/Users/tomhusson/second-brain/.env')
load_dotenv(env_path)

api_key = os.environ.get('ANTHROPIC_API_KEY')
print(f"API Key found: {api_key[:10]}...")

try:
    client = anthropic.Client(api_key=api_key)
    print("Client created successfully")
    
    response = client.messages.create(
        model="claude-3-5-sonnet-latest",
        messages=[{"role": "user", "content": "Say hello"}],
        max_tokens=100,
        timeout=10.0
    )
    
    print(f"Response: {response.content[0].text}")
    
except Exception as e:
    print(f"Error: {e}")