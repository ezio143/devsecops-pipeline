# Security Scanner Gap Analysis

## Coverage Matrix

| Vulnerability Class | CWE | Semgrep (SAST) | Trivy (SCA) | Gitleaks (Secrets) | Checkov (IaC) |
|---|---|---|---|---|---|
| SQL Injection | CWE-89 | Detected | - | - | - |
| Hardcoded Credentials (code) | CWE-798 | Detected | - | - | - |
| Command Injection | CWE-78 | Not Detected | - | - | - |
| Leaked AWS Key | CWE-798 | Detected | - | Detected | - |
| Outdated Dependencies | - | - | Detected | - | - |
| Public S3 Bucket | - | - | - | - | Detected |
| Overly Permissive IAM | - | - | - | - | Detected |
| Unencrypted RDS | - | - | - | - | Detected |
| Broken Access Control | CWE-284 | Not Detected | - | - | - |
| Business Logic Flaws | - | Not Detected | - | - | - |


## Identified Gaps

### Gap 1: Broken Access Control (CWE-284)
- Risk: No scanner detects missing authorization checks on endpoints.
- Recommendation: Add authenticated DAST scanning in a staging environment. Supplement with manual threat modeling.

### Gap 2: Business Logic Flaws
- Risk: Scanners cannot detect application-specific logic errors.
- Recommendation: Manual penetration testing, threat modeling workshops, and application-specific test cases.

### Gap 3: Insecure Cryptography Detection
- Risk: Default SAST rules may miss subtle crypto issues.
- Recommendation: Add custom Semgrep rules for crypto patterns. Consider Bandit for Python-specific crypto checks.


## Pipeline Architecture Decisions

### Tool Selection Rationale
- Semgrep: Fast, low false-positive rate for SAST. Supports custom rules.
- Trivy: Single binary handling SCA, container scanning, and IaC.
- Gitleaks: Purpose-built for secret detection. Scans git history.
- Checkov: 1000+ built-in policies for AWS/Azure/GCP.

### Gate Strategy
- All scanners run in parallel for faster feedback and independent failures.
- Gates fail on HIGH/CRITICAL only to avoid blocking on low-severity noise.

### Production Enhancements
1. DAST (OWASP ZAP) against staging
2. SBOM generation (Trivy SBOM output)
3. Diff-aware scanning on PRs
4. Findings sent to triage dashboard (DefectDojo)
5. Runtime monitoring (Falco) for container workloads