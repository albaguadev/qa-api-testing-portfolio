import logging

def before_all(context):
    # Logging is initialized to capture test execution details
    logging.basicConfig(level=logging.INFO)
    context.logger = logging.getLogger("API_Testing")

def before_scenario(context, scenario):
    # The session is prepared before each individual test case
    context.logger.info(f"Execution started for Scenario: {scenario.name}")

def after_all(context):
    # Final cleanup and summary logging are performed
    context.logger.info("Test suite execution completed.")