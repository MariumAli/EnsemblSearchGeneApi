import pytest

import requests

# The root url of the flask app
url = 'http://127.0.0.1:5000'


def test_search_api_valid_gene_name_prefix():
    # search for a valid gene name prefix
    r = requests.get(url+'/tbx')
    assert r.status_code == 200


def test_search_api_invalid_gene_name_prefix():
    # search for a gene name prefix with length lesser than 3
    r = requests.get(url+'/tx')
    assert r.status_code == 400


def test_search_api_valid_gene_name_prefix_and_species():
    # search for valid combination of gene name plus species name
    r = requests.get(url+'/tbx/bison_bison_bison')
    assert r.status_code == 200


def test_search_api_invalid_gene_name_prefix_and_species():
    # search for invalid combination of gene name plus species name
    r = requests.get(url+'/tbx/bison')
    assert r.status_code == 200


def test_search_api_invalid_request_type():
    # make an invalid request to server
    r = requests.post(url+'/tbx')
    assert r.status_code == 405
