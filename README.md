# QA API Testing Portfolio - Reqres

This repository showcases my professional skills in **API Testing**, covering both manual exploration and structured documentation. I use the [Reqres.in](https://reqres.in/) API as a sandbox to demonstrate test planning, bug reporting, and security mindset.

---

## Project Structure

The project is organized into logical modules to ensure scalability and clarity:

* **`manual-testing/`**: 
    * `Reqres_API_Testing.postman_collection.json`: Complete Postman collection with 9+ test cases.
    * `Test_Plan.md`: Detailed strategy, including Happy Paths and Negative Testing.
* **`automation-testing/`**: *(In Progress)* Future automated scripts using Python/Requests.

---

## Testing Scope

I have focused on three main areas of the User Management module:
1.  **Data Retrieval**: Validating query parameters and endpoint integrity.
2.  **Resource Creation**: Testing payload boundaries, empty objects, and data types.
3.  **Authentication**: Identifying security flaws in the Login flow (Token generation and field validation).

---

## How to Run the Tests

1.  **Postman**:
    * Import the `.json` file located in `manual-testing/`.
    * Set up a **Postman Environment** with the variable `{{x-api-key}}`.
    * Run the collection manually or using the Postman Runner.
2.  **Documentation**:
    * Review the `Test_Plan.md` for a full breakdown of expected vs. actual results.

---
