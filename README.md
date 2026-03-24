# Hybrid API Automation Portfolio: Python (BDD) & Postman

This repository demonstrates a dual-strategy approach to **API Quality Assurance**. A professional automation framework constructed with **Python and Behave** is presented, complemented by an advanced **Postman Collection**, both targeting the **JSONPlaceholder API**.

## Project Architecture
The repository is structured to showcase proficiency in two distinct automation stacks:

* **`automation-python/`**: A BDD framework utilizing **Python**, **Behave (Gherkin)**, and the **Requests** library.
* **`manual-testing/`**: Strategic documentation including the **Test Plan** and environmental constraint analysis.

---

## Stack 1: Python & Behave (BDD)
Focus is placed on scalability and "Clean Code" principles:
* **BDD Implementation**: Scenarios are defined in Gherkin to ensure high readability between technical and non-technical stakeholders.
* **Defensive Programming**: The `getattr()` function is utilized for safe attribute retrieval, ensuring suite stability across execution cycles.
* **Hooks & Environment**: Automated failure diagnostics are integrated via `environment.py`, allowing for the capture of prettified JSON response bodies upon assertion failure.

---

## Stack 2: Postman & Newman
Focus is placed on execution speed and integrated environment management:
* **Dynamic Chaining**: The `id` from `POST` responses is captured to parameterize subsequent `GET` requests via `pm.environment.set()`.
* **JavaScript Assertions**: Custom scripts are implemented for status code validation, schema integrity, and performance benchmarking (Response Time < 500ms).
* **CLI Execution**: The collection is fully compatible with **Newman** for integration into CI/CD pipelines.

---

## Strategic Findings: Statelessness Analysis
The **stateless nature** of the JSONPlaceholder mock API was identified and documented:
* **Observation**: Resources created via `POST` are simulated and are not physically persisted in the database.
* **Test Design**: Both the Python framework and the Postman collection are engineered to detect the resulting **404 Not Found** status upon retrieval.
* **Conclusion**: This demonstrates a robust diagnostic system that accurately reports system behavior rather than masking environmental limitations.

---

## Execution Instructions

### Option A: Python (BDD)
1. Dependencies are installed via: `pip install -r requirements.txt`
2. The suite is executed using: `python -m behave --no-capture`

### Option B: Postman
1. The `.json` files are imported from the `/postman-collections` directory.
2. The **`JSONPlaceholder-Env`** environment is selected.
3. Execution is performed via **Collection Runner** or **Newman**:
   ```bash
   newman run postman-collections/collection.json -e postman-collections/environment.json