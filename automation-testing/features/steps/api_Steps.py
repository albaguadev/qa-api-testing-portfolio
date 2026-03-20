from behave import given, when, then
import requests

# --- SHARED CONFIGURATION ---
DEFAULT_HEADERS = {
    "Content-Type": "application/json; charset=UTF-8"
}

@given('the API endpoint is "{url}"')
def step_impl(context, url):
    context.url = url

@when('a POST request is executed with title "{title}" and body "{body}"')
def step_impl(context, title, body):
    payload = {"title": title, "body": body, "userId": 1}
    context.response = requests.post(context.url, json=payload, headers=DEFAULT_HEADERS)
    context.generated_id = context.response.json().get('id')

@when('a GET request is executed with ID parameter "{resource_id}"')
def step_impl_static(context, resource_id):
    target_url = f"{context.url}/{resource_id}"
    context.response = requests.get(target_url, headers=DEFAULT_HEADERS)

@when('a GET request is executed with the generated ID')
def step_impl_dynamic(context):
    resource_id = getattr(context, 'generated_id', 1)
        
    target_url = f"{context.url}/{resource_id}"
    context.response = requests.get(target_url, headers=DEFAULT_HEADERS)

# --- SHARED ASSERTIONS ---
@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    actual_code = context.response.status_code
    error_msg = f"Expected status {status_code} but received {actual_code}. Response: {context.response.text}"
    
    assert actual_code == status_code, error_msg

@then('the response should contain the "{key}" field')
def step_impl(context, key):
    response_data = context.response.json()
    assert key in response_data, f"Field '{key}' was not identified in the response"

