## Intentionally Vulnerable Application : DevSecOps Pipeline

### Steps Performed

1. **Environment Setup**
   - Configured development environment with necessary tools and dependencies
   - Set up version control and repository structure

2. **Security Scanning Integration**
   - Integrated Static Application Security Testing (SAST) tools - Semgrep
   - Configured dependency vulnerability scanning - Trivy
   - Added container image scanning capabilities - Checkov

3. **Building Intentional Vulnerable App using FastAPI** (`app/main.py`)
   - added Hardcoded DB Credentials
   - added Hardcoded AWS Secret Key
   - added SQL Injection
   - added Command Injection

4. **Semgrep SAST Scan Results** (`semgrep scan --config auto app/ `)
     - Identified AWS access Key : 
     -  CWE-798: Use of Hard-coded Credentials
     - Identified formatted SQL query construction vulnerable to injection attacks
     -  CWE-89: Improper Neutralization of Special Elements used in an SQL Command
     - Detected raw SQLAlchemy query execution without proper parameterization
     -  CWE-89: Improper Neutralization of Special Elements used in an SQL Command