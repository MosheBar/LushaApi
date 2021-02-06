import json
import os
import allure
import pytest
from infra.api_infra.api_requestor import APIRequestor
from infra.infra_utils.assertion import Compare

"""
getting the tests to run from test_suites.json in current directory
"""
params_path = os.path.dirname(__file__)
with open("/".join([params_path, 'test_suites.json']), 'r') as f:
    test_suite = []
    my_pre_file = json.load(f)
    for line in my_pre_file:
        test_suite.insert(0, [line.get('test_name'),
                              line.get('endpoint', None),
                              line.get('method', None),
                              line.get('body', None),
                              line.get('expected_response', None),
                              line.get('expected_status_code', None),
                              line.get('validation', None),
                              line.get('params', None)])


@pytest.mark.parametrize('test_name, endpoint, method, body, expected_response, expected_status_code, validation, params',
                         test_suite, ids=['-'.join([i[1], i[0]]) for i in test_suite])
def test_api(test_name, endpoint, method, body, expected_response, expected_status_code, validation, params):
    """
    test API endpoint with the relevant variable

    :param endpoint: the relevant endpoint to be request from
    :param method: the relevant method to request with
    :param body: request body
    :param expected_response: the expected response to compare with
    :param expected_status_code: the expected status code to compare with
    :param validation: validation method to compare with
    :param params: additional params to the request if needed
    :return: test result
    """
    response = None
    with allure.step(' '.join(['getting API response on endpoint:', str(endpoint)])):
        response = APIRequestor().request(method=method, url_path=endpoint, body=body, params=params)
    with allure.step(' '.join(['Asserting API status code expected:', str(expected_status_code), ', with response:', str(response.status_code)])):
        Compare.equal.__call__(a=expected_status_code, b=response.status_code, free_text=f"Status code is not as expected: {response.status_code} instead of expected: {expected_status_code}")
    with allure.step('starting API validation'):
        validation = 'equal' if not validation else validation
        with allure.step(' '.join(['Validation with method:', str(validation)])):
            Compare.__dict__[validation](a=str(response), b=str(expected_response),
                                         free_text=f"Failed to compare, Response is not as expected: {response} instead of {expected_response}")
