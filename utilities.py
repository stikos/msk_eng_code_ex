"""
File:       utils.py
Desc:       Simple utility functions, mainly to reduce redundancies.
"""
__author__ = "Konstantinos Liosis"
__copyright__ = "Copyright 2021"
__credits__ = "Konstantinos Liosis"
__license__ = None
__version__ = "1.0.0"
__maintainer__ = "Konstantinos Liosis"
__email__ = "konstantinos.liosis@ucalgary.ca"
__status__ = "Development"

import requests


def exec_req(endpoint):
    """Execute requests and catch exceptions

    :param endpoint: The endpoint for the API call

    :return: The response object in JSON format. If None, either an exception
    was raised or an
    error occurred.
    """
    try:
        req = requests.get(endpoint)
    except requests.exceptions.RequestException as e:
        # In case of a Timeout, BadRequest, HTTPError, ConnectionError
        print("Oops! That did not go as planned... Let's try again\n")
        return None

    # Check if the request completed successfully
    # This should never fail for the ENSEMBL API call, since the ENSEMBL ID is
    # retrieved only in the case of a successful API call to GeneNetwork
    if req.status_code != 200:
        # If it did not, print the respective error message and restart
        print(req.json()["message"] + '\n')
        return None
    else:
        return req.json()


def get_transcripts(trans_object):
    """Get the transcripts object and create the sorted list.

    :param trans_object: The Transcripts object, as returned from ENSEMBL
    :return: The transcripts list, in descending order of exons.
    """

    # The transcripts list to be returned
    t_list = []

    for trans in trans_object:
        n_exons = len(trans["Exon"])
        _id = trans["id"]
        canonical = trans["is_canonical"]
        t_list.append([_id, n_exons, canonical])

    return sorted(t_list, key=lambda x: x[1], reverse=True)
