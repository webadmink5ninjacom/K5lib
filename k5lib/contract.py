import requests
import json
import logging
import k5.authenticate

# List regions
def rest_list_regions(globalToken):
    headers = {'Content-Type': 'application/json',
               'Accept' : 'application/json',
               'X-Auth-Token': globalToken}

    url = 'https://identity.gls.cloud.global.fujitsu.com/v3/regions'

    try:
        r = requests.get(url, headers=headers)

        logging.info(r)

        return r
    except:
        logging.debug(r)
        logging.debug(r.json)
        return


def list_regions(domainToken):

    request = rest_list_regions(domainToken)
    r = request.json()

    return r
# Todo: Find a method to return region list instead of full json
#    return r['token']['user']['domain']['id']


# Show region
def rest_show_region(domainToken, regionId):
    headers = {'Content-Type': 'application/json',
               'Accept' : 'application/json',
               'X-Auth-Token': domainToken}

    url = 'https://identity.gls.cloud.global.fujitsu.com/v3/regions/' + regionId

    try:
        r = requests.get(url, headers=headers)

        logging.info(r)

        return r
    except:
        logging.debug(r)
        logging.debug(r.json)
        return

def show_region(domainToken, regionId):

    request = rest_show_region(domainToken, regionId)
    r = request.json()

    return r


