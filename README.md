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
 
 5. **Terraform Infrastructure Vulnerabilities & Checkov Scan**
    - Integrated infrastructure-as-code scanning using Checkov against Terraform files
    - Summary of notable findings reported by Checkov:
      - Multiple IAM policy issues (resource: aws_iam_policy.admin) indicating an overly-permissive policy that allows Action: "*" and Resource: "*". Related checks failed: CKV_AWS_290, CKV_AWS_287, CKV_AWS_288, CKV_AWS_286, CKV_AWS_62, CKV_AWS_63, CKV_AWS_355, CKV_AWS_289, CKV2_AWS_40 — guidance: avoid wildcard actions/resources and add appropriate constraints.
      - S3 bucket misconfigurations (resource: aws_s3_bucket.data) making sensitive data publicly readable and missing protections: failed checks CKV2_AWS_61, CKV2_AWS_6, CKV2_AWS_62, CKV_AWS_21, CKV_AWS_18, CKV_AWS_20, CKV_AWS_144, CKV_AWS_145 — guidance: remove public ACLs, enable public access block, enable versioning, logging, encryption, lifecycle and replication as appropriate.
      - RDS instance issues (resource: aws_db_instance.database) with plaintext password, publicly accessible, storage not encrypted, lacking enhanced monitoring, Multi-AZ, IAM auth, deletion protection, copy-tags-to-snapshots and automatic minor upgrades: failed checks CKV_AWS_129, CKV_AWS_118, CKV_AWS_157, CKV_AWS_161, CKV_AWS_293, CKV_AWS_16, CKV_AWS_17, CKV_AWS_226, CKV2_AWS_60 — guidance: use secure secrets management, enable encryption, restrict public access, and enable recommended RDS settings.
      - Secrets scan detected a high-entropy string in main.tf (password exposed) failing CKV_SECRET_6 — guidance: remove hardcoded secrets and use a secrets manager or Terraform variables with secure storage.

