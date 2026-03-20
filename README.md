# API Automation Framework: RESTful Testing Portfolio

This repository showcases a professional **Behavior-Driven Development (BDD)** framework designed for API testing. The project utilizes **Python**, **Behave**, and the **Requests** library to validate RESTful services.

## Project Architecture
The framework is built with a modular and scalable structure:
* **`features/`**: Contains Gherkin scenarios defined in plain English.
* **`features/steps/`**: Business logic implementation using Python.
* **`features/environment.py`**: Automated hooks for logging and failure diagnostics.
* **`manual-testing/`**: Documentation of manual test cases and identified vulnerabilities.

---

## Automation Strategy
A **Unified Criterion** was established to handle multiple HTTP methods within a single execution suite:

* **Resource Retrieval (GET)**: Validation of data integrity and status codes for existing resources.
* **Resource Creation (POST)**: Verification of payload processing and the issuance of unique resource identifiers.
* **Global Assertions**: Reusable validation steps were implemented to ensure the presence of required JSON fields and correct HTTP status codes.

---

## Technical Decisions & Challenges
During the development phase, the following engineering choices were made:

1. **Environment Migration**: The test environment was migrated to **JSONPlaceholder** to ensure framework stability and mitigate 403 Forbidden errors caused by third-party WAF (Web Application Firewall) restrictions.
2. **Impersonal Logging**: An automated logging system was integrated via `environment.py` to capture response bodies during failed steps, facilitating rapid root-cause analysis.
3. **DRY Principle**: Step definitions were centralized in `api_steps.py` to prevent code duplication and enhance maintainability.

---

## Installation & Execution

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd <project-folder>

