"""
This file includes the helper functions for the connector
"""
import requests
from .constants import REQUEST_TIMEOUT, LOGGER_NAME, HEADERS_AUTH, HEADERS
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger(LOGGER_NAME)

def get_auth_token(config, **kwargs):
    try:
        url = config.get("authenticationEndpointURL")
        auth_payload = {
        "grant_type": "client_credentials",
        "audience": "wiz-api",
        "client_id": config.get("clientID"),
        "client_secret": config.get("clientSecret"),
        }
        response = requests.post(url=url, headers=HEADERS_AUTH, data=auth_payload, timeout=REQUEST_TIMEOUT)
        if response.status_code != requests.codes.ok:
            logger.error("Error: {0}".format(response.json()))
            raise ConnectorError('Error: {0}'.format(response.json()))
        response_json = response.json()
        TOKEN = response_json.get('access_token')
        if not TOKEN:
            logger.error("Error: {0}".format(response_json.get("message")))
            raise Exception('Error: {0}'.format(response_json.get("message")))
        return TOKEN
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))

def api_query_call(config, query=None, variables=None, **kwargs):
    try:
        url = config.get("aPIEndpointURL") + "/graphql"
        TOKEN = get_auth_token(config)
        HEADERS["Authorization"] = "Bearer " + TOKEN
        if variables != None:
        	data = {"variables": variables, "query": query}
        else:
        	data = {"query": query}    
        result = requests.post(url=url, headers=HEADERS, json=data, timeout=REQUEST_TIMEOUT)
        return result
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))