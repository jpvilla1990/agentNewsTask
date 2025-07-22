import requests

class Scrape(object):
    """
    Scrape class to handle Scrape operations.
    """
    def __init__(self, base_url : str, token : str):
        """
        Initialize the Scrape class with the base URL of the Scrape service.
        """
        self.base_url : str = base_url
        self.token : str = token

    def scrape(self, queryUrl : str):
        """
        Perform a Scrape operation with the given query.

        :param url: The Scrape url string.
        :return: The response from the Scrape service.
        """
        url : str = f"{self.base_url}"
        params : dict = {
            'token': self.token,
            'url': queryUrl,
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.content
        else:
            response.raise_for_status()