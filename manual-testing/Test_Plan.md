# API Test Plan: Reqres Project

This document details the test strategy and scenarios executed for the **Reqres API**, based on the exported Postman collection: `Reqres_API_Testing`.

## Environment & Tools
* **Base URL:** `https://reqres.in/api`
* **Auth Method:** API Key (Header: `x-api-key`) managed via collection variables.
* **Testing Tool:** Postman v2.1.0.

---

## Test Scenarios

### 1. User Management: Get List Users
Tests focused on data retrieval and query parameter handling.

| ID | Name | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | GetUser_Success | `GET` | `/users?page=1` | Verify successful retrieval of user list for page 1. |
| **TC-02** | GetUser_InvalidEndpoint | `GET` | `/apis/users` | Negative test checking behavior for misspelled endpoints (`/apis/`). |
| **TC-03** | GetUser_InvalidPayload | `GET` | `/users?page=abc` | Verify how the system handles non-numeric query parameters. |

### 2. User Management: Add Request (POST)
Tests focused on resource creation and payload validation.

| ID | Name | Method | Payload | Expected Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | CreateUser_Success | `POST` | `{"name": "morpheus", "job": "leader"}` | Return `201 Created` with new ID and timestamp. |
| **TC-02** | CreateUser_EmptyPayload | `POST` | `{}` | Verify if the API rejects or handles empty JSON objects. |
| **TC-03** | CreateUser_InvalidData | `POST` | `{"name": 12345, "job": null}` | Verify validation for incorrect data types (e.g., number as name). |

### 3. User Management: Login
Tests focused on authentication security and error messaging.

| ID | Name | Method | Payload | Expected Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Login_Success | `POST` | Valid credentials | Return `200 OK` + Authorization Token. |
| **TC-02** | Login_MissingPassword | `POST` | Email only | Return `400 Bad Request` with "Missing password" error. |
| **TC-03** | Login_UserNotFound | `POST` | Unregistered email | Return `400 Bad Request` with "user not found" error. |

---

## Security & Variables
* **API Key:** The collection uses a variable `{{x-api-key}}` for authentication.
* **Note:** For security reasons, the `current value` of the API Key is not included in the repository. Users must set their own environment variable to run the tests.

---

## Key Findings
* **Query Params:** The API defaults to page 1 when receiving invalid strings in `?page=abc`.
* **Payload Validation:** The system currently accepts empty JSON objects in POST requests, returning a `201 Created` status (Potential Bug).