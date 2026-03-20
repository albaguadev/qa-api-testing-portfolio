Feature: Unified API Functional Testing

  Scenario: Retrieval of resource list via GET
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts"
    When a GET request is executed with ID parameter "1"
    Then the response status code should be 200
    And the response should contain the "title" field

  Scenario: Creation of a new resource via POST
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts"
    When a POST request is executed with title "QA Portfolio" and body "Testing Automation"
    Then the response status code should be 201
    And the response should contain the "id" field

  Scenario: Create and retrieve a new resource
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts"
    When a POST request is executed with title "E2E Test" and body "Persistence Check"
    And a GET request is executed with the generated ID
    Then the response status code should be 200
    And the response should contain the "title" field 