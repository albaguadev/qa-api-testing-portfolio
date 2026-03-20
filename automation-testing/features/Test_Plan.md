# Test Plan: RESTful API Automation Suite

## 1. Introduction
This document defines the strategy, environment, and technical scope for the automated functional testing of the **JSONPlaceholder API**. The primary objective is to validate the integrity of RESTful endpoints using a **Behavior-Driven Development (BDD)** approach.

---

## 2. Test Strategy
A modular automation strategy was implemented to ensure scalability and maintainability:

* **Framework**: Python with the **Behave** library for Gherkin scenario execution.
* **HTTP Client**: **Requests** library for synchronous API interaction.
* **Architecture**: Separation of concerns between Feature files (Business Logic) and Step Definitions (Technical Implementation).
* **Defensive Programming**: Use of `getattr()` for safe context attribute retrieval to prevent runtime exceptions.

---

## 3. Scope of Testing
The following HTTP methods and scenarios are covered:

| Method | Resource | Objective | Expected Result |
| :--- | :--- | :--- | :--- |
| **GET** | `/posts/{id}` | Validate retrieval of existing resources. | `200 OK` + Data Integrity. |
| **POST** | `/posts` | Validate resource creation and ID generation. | `201 Created` + Response Body. |
| **E2E** | `/posts` -> `/posts/{id}` | Validate persistence flow (Create & Read). | `404 Not Found` (Environment Limit). |

---

## Environment & Tools
* **Target API**: `https://jsonplaceholder.typicode.com`
* **Test Runner**: Behave (Python-based)
* **Dependencies**: Defined in `requirements.txt`
* **Logging**: Automated failure diagnostics via `environment.py` hooks.

---

## Technical Implementation Details

### Enhanced Assertions
All assertions are designed with **High Verbosity**. In the event of a failure, the framework captures and displays:
* Expected vs. Actual Status Codes.
* Prettified JSON Response Body for immediate root-cause analysis.

### State Management
The `context` object is utilized to pass the `generated_id` from a `POST` operation to a subsequent `GET` request, simulating a real-world End-to-End lifecycle.

---

## 6. Documented Environmental Constraints
### Scenario: End-to-End Persistence
**Status: Expected Failure (404)**

As a design choice, the framework does not utilize artificial "fallbacks" to mask environment limitations. Since **JSONPlaceholder** is a stateless mock API, resources created via `POST` are not physically persisted. 

* **Test Result**: The test correctly identifies the absence of the resource (404).
* **Justification**: This failure serves as a validation of the framework's diagnostic accuracy and its ability to report data discrepancies in a transparent manner.

---

## 7. Execution Instructions
To execute the test suite with full log visibility, the following command must be used:
```bash
python -m behave --no-capture