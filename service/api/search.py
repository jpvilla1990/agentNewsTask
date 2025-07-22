import requests

class Search(object):
    """
    Search class to handle search operations.
    """
    def __init__(self, base_url : str, token : str):
        """
        Initialize the Search class with the base URL of the search service.
        """
        self.base_url : str = base_url
        self.token : str = token

        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def search(self, query : str):
        """
        Perform a search operation with the given query.

        :param query: The search query string.
        :return: The response from the search service.
        """
        url : str = f"{self.base_url}/search"
        payload : dict = {'query': query}
        response = requests.post(url, json=payload, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()