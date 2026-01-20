# 🛡 Security Policy

## Supported Versions

We release patches for security vulnerabilities. The following table shows which versions are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < 1.0   | :x:                |

---

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

We take the security of AiLab-workbench seriously. If you have discovered a security vulnerability, we appreciate your help in disclosing it to us in a responsible manner.

### How to Report

Please report security vulnerabilities by using one of the following methods:

#### 1. GitHub Private Vulnerability Reporting (Recommended)

Use GitHub's private vulnerability reporting feature:

1. Go to the [Security tab](https://github.com/H0NEYP0T-466/AiLab-workbench/security)
2. Click "Report a vulnerability"
3. Fill out the vulnerability report form

#### 2. Email

Send an email to the repository maintainers with the following information:

- **Subject**: Security Vulnerability in AiLab-workbench
- **Description**: Detailed description of the vulnerability
- **Steps to Reproduce**: Clear steps to reproduce the issue
- **Impact**: Potential impact and severity assessment
- **Suggested Fix**: If you have suggestions for fixing the issue

---

## What to Include in Your Report

To help us understand and resolve the issue quickly, please include:

- **Type of vulnerability** (e.g., code injection, data exposure, etc.)
- **Full paths** of source files related to the vulnerability
- **Location** of the affected source code (tag/branch/commit or direct URL)
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact assessment** - what an attacker could achieve
- **Any potential mitigations** you've identified

---

## Response Timeline

We aim to respond to security vulnerability reports according to the following timeline:

| Stage | Timeline |
|-------|----------|
| **Initial Response** | Within 48 hours |
| **Vulnerability Confirmation** | Within 7 days |
| **Fix Development** | Varies by severity and complexity |
| **Security Advisory** | Published with fix release |

### Response Process

1. **Acknowledgment**: We'll confirm receipt of your vulnerability report within 48 hours
2. **Investigation**: We'll investigate and validate the reported vulnerability
3. **Communication**: We'll keep you informed about our progress
4. **Resolution**: We'll develop and test a fix
5. **Disclosure**: We'll coordinate public disclosure with you

---

## Security Update Policy

### Severity Levels

We classify security vulnerabilities using the following severity levels:

- **Critical**: Remote code execution, data loss, or complete system compromise
- **High**: Significant data exposure or privilege escalation
- **Medium**: Limited data exposure or functionality bypass
- **Low**: Minor security improvements or best practice violations

### Patch Release Schedule

- **Critical vulnerabilities**: Emergency patch within 24-48 hours
- **High severity**: Patch within 7 days
- **Medium severity**: Patch in next regular release
- **Low severity**: Patch in next minor version

---

## Security Best Practices

While using AiLab-workbench, we recommend:

### For Users

- Always use the latest version of the software
- Keep dependencies (NumPy, Pandas, Matplotlib) up to date
- Review code before running from untrusted sources
- Use virtual environments to isolate dependencies
- Be cautious with data files from unknown sources

### For Contributors

- Follow secure coding practices outlined in [CONTRIBUTING.md](CONTRIBUTING.md)
- Sanitize all user inputs
- Avoid hardcoding sensitive information (credentials, API keys)
- Use parameterized queries when working with data
- Review dependencies for known vulnerabilities
- Add appropriate error handling and validation

---

## Known Security Considerations

### Current Scope

This project is primarily educational and designed for:
- Learning AI/ML algorithms
- Practicing Python programming
- Understanding data structures and algorithms

### Data Handling

- Input validation is limited in educational examples
- CSV files should be from trusted sources
- User-provided graph data is not extensively validated

---

## Security-Related Configuration

### Python Dependencies

We recommend keeping all dependencies updated:

```bash
pip install --upgrade numpy pandas matplotlib
```

Check for known vulnerabilities in dependencies:

```bash
pip install safety
safety check
```

---

## Disclosure Policy

### Our Commitment

- We will work with you to understand and resolve the issue
- We will keep you informed throughout the process
- We will credit you in the security advisory (unless you prefer to remain anonymous)
- We will not take legal action against researchers who report vulnerabilities in good faith

### Coordinated Disclosure

We follow a coordinated disclosure process:

1. Vulnerability is reported privately
2. Fix is developed and tested
3. Security advisory is prepared
4. Fix is released
5. Advisory is published 24-48 hours after release

---

## Security Hall of Fame

We recognize and thank security researchers who help make AiLab-workbench more secure:

<!-- This section will be updated as vulnerabilities are reported and fixed -->

*No security issues have been reported yet.*

---

## Questions?

If you have questions about this security policy or the project's security posture:

- Open a [discussion thread](https://github.com/H0NEYP0T-466/AiLab-workbench/discussions)
- Contact the maintainers through GitHub

**Note**: For security vulnerabilities, please follow the reporting process above instead of using public channels.

---

## Updates to This Policy

This security policy may be updated from time to time. Significant changes will be announced through:

- GitHub release notes
- Repository announcements
- Security advisories

Last updated: January 2026

---

<p align="center">
  <strong>Thank you for helping keep AiLab-workbench secure! 🔒</strong>
</p>
