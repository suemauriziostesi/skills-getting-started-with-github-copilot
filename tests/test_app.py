import pytest
from fastapi.testclient import TestClient
import sys
import os

# Ensure src is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all('description' in v and 'participants' in v for v in data.values())

# Add more tests for signup, unregister, and edge cases as needed
