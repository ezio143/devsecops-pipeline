import os
import sqlite3
from fastapi import FastAPI, Form, Query

app = FastAPI()

# Hardcoded credentials - CWE-798
DB_USER = "admin"
DB_PASSWORD = "SuperSecret123!"
DB_HOST = "prod-db.internal.company.com"
# Fake AWS key for Gitleaks to detect
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7DEMO001"

def get_db():
    return sqlite3.connect(":memory:")

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    """SQL Injection - CWE-89"""
    db = get_db()
    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return {"status": "authenticated", "user": result[0]}
    return {"status": "failed"}

@app.get("/ping")
def ping(host: str = Query(...)):
    """Command Injection - CWE-78"""
    result = os.system(f"ping -c 1 {host}")
    return {"status": "ok", "exit_code": result}


@app.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    """User signup endpoint"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    db.commit()
    return {"status": "success", "message": "User registered"}

@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

