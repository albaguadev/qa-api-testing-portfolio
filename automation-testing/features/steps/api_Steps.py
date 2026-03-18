from behave import given, when, then
import requests

# --- SHARED CONFIGURATION ---
DEFAULT_HEADERS = {
    "Content-Type": "application/json; charset=UTF-8"
}

@given('the API endpoint is "{url}"')
def step_impl(context, url):
    # The target URL is assigned to the test context
    context.url = url

# --- UNIFIED GET METHOD ---
@when('a GET request is executed with ID parameter "{resource_id}"')
def step_impl(context, resource_id):
    # A GET operation is performed to retrieve a specific resource by ID
    target_url = f"{context.url}/{resource_id}"
    context.response = requests.get(target_url, headers=DEFAULT_HEADERS)

# --- UNIFIED POST METHOD ---
@when('a POST request is executed with title "{title}" and body "{body}"')
def step_impl(context, title, body):
    # A POST operation is executed to create a new resource
    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }
    context.response = requests.post(context.url, json=payload, headers=DEFAULT_HEADERS)

# --- SHARED ASSERTIONS ---
@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    # The received status code is validated against the expected integer
    assert context.response.status_code == status_code

@then('the response should contain the "{key}" field')
def step_impl(context, key):
    # The presence of the specified key is verified within the JSON response body
    response_data = context.response.json()
    assert key in response_data, f"Field '{key}' was not identified in the response"