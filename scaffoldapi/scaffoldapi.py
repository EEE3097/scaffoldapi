import requests
import json

def who_am_i_online():
    """ Returns in prettyprint json basic info that can be gathered about your IP by the webservice ipinfo.io

    Returns
    -------
    requests Response object
    """
    try:
        r = requests.get('https://ipinfo.io/')
        r.raise_for_status()
        print(json.dumps(r.json(), indent=4, sort_keys=True))

    except requests.exceptions.HTTPError as ehttp:
        print("Http Error:", ehttp)
    except requests.exceptions.ConnectionError as ece:
        print("Error Connecting:", ece)
    except requests.exceptions.Timeout as eto:
        print("Timeout Error:", eto)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return r


def returns_sum_as_float(a, b):
    """
    Returns the sum of a and b as a float

    Parameters
    ----------
    a: a number
    b: a number

    Returns
    -------
    float
    """
    return float(a + b)
