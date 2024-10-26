import pytest
from fastapi.testclient import TestClient
from app import app  # Assuming the main app code is saved as app.py

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Calculator API. Use the /calculate endpoint to perform operations."}

def test_addition():
    response = client.post("/calculate", json={"operation": "add", "num1": 10, "num2": 5})
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "num1": 10, "num2": 5, "result": 15}

def test_subtraction():
    response = client.post("/calculate", json={"operation": "subtract", "num1": 10, "num2": 5})
    assert response.status_code == 200
    assert response.json() == {"operation": "subtract", "num1": 10, "num2": 5, "result": 5}

def test_multiplication():
    response = client.post("/calculate", json={"operation": "multiply", "num1": 10, "num2": 5})
    assert response.status_code == 200
    assert response.json() == {"operation": "multiply", "num1": 10, "num2": 5, "result": 50}

def test_division():
    response = client.post("/calculate", json={"operation": "divide", "num1": 10, "num2": 5})
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "num1": 10, "num2": 5, "result": 2}

def test_division_by_zero():
    response = client.post("/calculate", json={"operation": "divide", "num1": 10, "num2": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}

def test_unsupported_operation():
    response = client.post("/calculate", json={"operation": "modulus", "num1": 10, "num2": 5})
    assert response.status_code == 400
    assert response.json() == {"detail": "Unsupported operation. Use add, subtract, multiply, or divide."}
