# Security in DevOps Tutorials: SAST, SCA, and DAST

This repository contains the code examples and workflows accompanying my series of blog posts introducing key application security testing methodologies: Static Application Security Testing (SAST), Software Composition Analysis (SCA), and Dynamic Application Security Testing (DAST) within a DevOps context.

The tutorial series guides you through building a simple, intentionally vulnerable Flask application and using various security tools to identify its weaknesses, integrating these scans into a GitHub Actions CI/CD pipeline.

## Tutorial Series

- [Step 1: Fortifying the Foundation with SAST and SCA](https://pandelig.com/blog/security-in-devops-step-1-fortifying-the-foundation-with-sast-and-sca): This article introduces SAST and SCA, explaining how they help find vulnerabilities in code and dependencies early in the SDLC. It walks you through setting up a vulnerable Flask app, using SonarQube (locally and via GitHub Actions) for SAST, and `pip-audit` (locally and via GitHub Actions) for SCA.
- [Step 2: Uncovering Runtime Vulnerabilities with DAST](https://pandelig.com/blog/security-in-devops-step-2-uncovering-runtime-vulnerabilities-with-dast): Building on Step 1, this article dives into DAST. It shows how to test the running application using OWASP ZAP's graphical interface via Docker and how to automate ZAP scans within a GitHub Actions workflow to find runtime vulnerabilities.

## Clone the repository

```bash
git clone https://github.com/pandelig/sast-sca-dast-demo.git
cd sast-sca-dast-demo
````

## License

[MIT](https://github.com/pandelig/sast-sca-dast-demo/blob/main/LICENSE)
