import allure
import requests
BASE_END_POINT = 'http://34.237.139.81'


class APIRequestor(object):
    """
    get the API respond using requests
    """
    def __init__(self, http_client=None):
        if http_client is None:
            self._http_client = requests
        else:
            self._http_client = http_client

    def request(self, method, url_path, body=None, params=None):
        """
        get the request by the relevant params

        :param method: GET, POST...
        :param url_path: url to be added to our base URL
        :param body: body in the request
        :param params: params in the request if needed
        :return: request respond
        """
        with allure.step(' '.join(['getting API response on endpoint:', str(url_path), ', with method:', str(method),
                                   ', body content:', str(body), ', params:', str(params)])):
            abs_url = "/".join([BASE_END_POINT, url_path])
            return self._http_client.request(method=method, url=abs_url, json=body, params=params)
