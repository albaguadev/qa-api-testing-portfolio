# API Test Plan: JSONPlaceholder (Postman Collection)

This document defines the manual and automated test strategy executed via **Postman** for the JSONPlaceholder API.

---

## 1. Environment & Setup
* **Tool**: Postman Desktop / Web v2.1.1.
* **Base URL**: `https://jsonplaceholder.typicode.com` (Stored as `{{baseUrl}}` in Environment).
* **Variables Management**: 
    * `baseUrl`: Service endpoint.
    * `newId`: Dynamic variable captured from POST responses for E2E chaining.
* **Collection**: `JSONPlaceholder_Validation_Suite`.

---

## 2. Test Strategy
The collection follows a **Structured Validation Lifecycle**:
1. **Pre-request Scripts**: Generating dynamic data (e.g., random strings) using `pm.variables.replaceIn` or custom JS logic.
2. **Tests (Scripts)**: JavaScript-based assertions using the `pm.test` library to validate status codes, response headers, and performance.
3. **Chained Requests (E2E)**: Capturing the `id` from a `POST` response body into an environment variable to parameterize subsequent `GET` requests.

---

## 3. Detailed Test Scenarios

### 🔹 Module 1: Resource Retrieval (GET)
| ID | Name | Method | Endpoint | Validations |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | GetSingle_Success | `GET` | `/posts/1` | Status 200, ID matches 1, Response < 500ms. |
| **TC-02** | GetList_Success | `GET` | `/posts` | Status 200, Body is Array, Schema integrity. |
| **TC-03** | Get_NotFound | `GET` | `/posts/999` | Status 404, Resource does not exist. |

### 🔹 Module 2: Resource Creation (POST)
| ID | Name | Method | Payload | Validations |
| :--- | :--- | :--- | :--- | :--- |
| **TC-04** | Create_Success | `POST` | Valid JSON | Status 201, ID 101 generated, Payload mirrored. |
| **TC-05** | Create_Empty | `POST` | `{}` | Verify API default values vs Error handling. |

### 🔹 Module 3: End-to-End (E2E) Persistence Flow
| ID | Step | Method | Variable Action | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| **TC-06** | 1. Create | `POST` | `pm.environment.set("newId", res.id)` | `201 Created` |
| **TC-07** | 2. Retrieve | `GET` | Fetch `/posts/{{newId}}` | `404 Not Found` (Env. Limit) |

---

## 4. Key Findings & Bug Reporting

### Bug ID: ENV-001
**Title**: Resource Non-Persistence in Mock Environment.
* **Severity**: Low (Environment Constraint).
* **Description**: Resources created via `POST` are not persisted in the server's database.
* **Actual Result**: `GET /posts/101` returns 404 despite a successful 201 response during creation.
* **Impact**: End-to-End flows cannot be fully verified for data persistence.
* **Status**: **Won't Fix** / As Designed for JSONPlaceholder.

---

## 5. Conclusion
The API demonstrates high reliability for standard REST operations. While state persistence is not supported, the status code logic and payload mirroring align with industry standards, making it an ideal environment for showcasing Postman Collection architecture and variable chaining.