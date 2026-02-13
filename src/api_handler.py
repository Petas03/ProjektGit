# API Communication Functions

"""
This module contains functions for communicating with APIs.
"""

import requests


def get_data(url):
    """
    Fetches data from the given URL.
    """
    response = requests.get(url)
    return response.json()


def post_data(url, payload):
    """
    Sends data to the given URL using POST method.
    """
    response = requests.post(url, json=payload)
    return response.json()