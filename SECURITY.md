# Security Policy

## 🛡️ Security Overview

The AiLab-workbench project takes security seriously. Although this is primarily an educational repository containing lab assignments and algorithm implementations, we want to ensure that any code shared is safe and secure for all users.

## 🔍 Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| Older   | :x:                |

As this is a continuously updated educational repository, we recommend always using the latest version from the main branch.

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability in this project, please help us maintain the security of our users by reporting it responsibly.

### Where to Report

**Please DO NOT report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by:

1. **Creating a Security Advisory**
   - Navigate to the [Security tab](https://github.com/H0NEYP0T-466/AiLab-workbench/security) of this repository
   - Click on "Report a vulnerability"
   - Fill out the form with details about the vulnerability

2. **Email** (Alternative)
   - If you prefer email or the Security Advisory feature is unavailable
   - Open a regular issue titled "Security Concern - Please Contact"
   - We will respond with a private communication channel

### What to Include

When reporting a vulnerability, please include:

- **Type of vulnerability** (e.g., code injection, path traversal, etc.)
- **Full paths** of source file(s) related to the vulnerability
- **Location** of the affected source code (tag/branch/commit or direct URL)
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact** of the vulnerability and potential attack scenarios
- **Any potential fixes** you've identified (optional)

### What to Expect

After submitting a vulnerability report:

1. **Acknowledgment**: We will acknowledge receipt within **48 hours**
2. **Assessment**: We will assess the vulnerability and determine its severity within **5 business days**
3. **Updates**: We will keep you informed of our progress
4. **Resolution**: We aim to resolve critical vulnerabilities within **30 days**
5. **Disclosure**: After a fix is released, we may publicly acknowledge your responsible disclosure (with your permission)

## 🔒 Security Best Practices

When using this repository:

### For Contributors

- **Never commit sensitive data**: No API keys, passwords, or personal information
- **Validate inputs**: Always validate and sanitize user inputs in your code
- **Use safe libraries**: Keep dependencies updated and use well-maintained packages
- **Review PRs carefully**: Check for potential security issues in pull requests
- **Follow secure coding practices**: Adhere to OWASP guidelines where applicable

### For Users

- **Keep Python updated**: Use Python 3.7 or higher
- **Update dependencies**: Regularly update numpy, pandas, and matplotlib
- **Isolate execution**: Consider using virtual environments
- **Review code**: Understand code before executing it
- **Report issues**: If you find suspicious code, report it

## 🔐 Known Security Considerations

### Data Files
- CSV files (`processed_sensor_data.csv`, `student_practice_data.csv`) contain only sample data
- No personal or sensitive information is stored in the repository

### Code Execution
- Lab files are meant to be run in educational contexts
- Always review code before execution
- Use virtual environments to isolate dependencies

### Dependencies
Current runtime dependencies:
- NumPy: Scientific computing library (regularly updated by maintainers)
- Pandas: Data manipulation library (regularly updated by maintainers)
- Matplotlib: Plotting library (regularly updated by maintainers)

We monitor these dependencies for known vulnerabilities and will update as needed.

## 📋 Security Update Policy

When a security issue is identified:

1. **Assessment**: Evaluate the severity and impact
2. **Fix**: Develop and test a fix
3. **Notification**: Inform users through:
   - GitHub Security Advisory
   - Repository README update
   - Commit messages clearly marked with [SECURITY]
4. **Documentation**: Update this SECURITY.md file with lessons learned

## 🎓 Educational Context

Please note:

- This repository contains **educational code** for learning purposes
- Code is designed to demonstrate algorithms and concepts
- Production use may require additional security hardening
- Always perform security reviews before using code in production environments

## 📚 Resources

For more information about security best practices:

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [Secure Coding Guidelines](https://www.securecoding.cert.org/)

## 🤝 Security Hall of Fame

We appreciate security researchers who help keep our project safe. With their permission, we recognize contributors who have responsibly disclosed security issues:

*No vulnerabilities reported yet.*

## 📞 Contact

For non-security issues, please use:
- [Issue Tracker](https://github.com/H0NEYP0T-466/AiLab-workbench/issues)
- [Discussions](https://github.com/H0NEYP0T-466/AiLab-workbench/discussions)

---

**Last Updated**: January 2026

Thank you for helping keep AiLab-workbench and its users safe! 🛡️
