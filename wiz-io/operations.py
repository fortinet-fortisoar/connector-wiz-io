"""
    Copyright start
    MIT License
    Copyright (c) 2023 Fortinet Inc
    Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
from .constants import *
from .utils import api_query_call

logger = get_logger(LOGGER_NAME)


def get_issues(config, params):
    variables = {
        "first": params.get("limit"),
        # "after": "<pagenation hash>",
        "orderBy": {
            "field": "SEVERITY",
            "direction": "DESC"
        },
        # Example Query: {"status": ["RESOLVED"]}
        "filterBy": params.get("filterQuery")
    }
    try:
        response = api_query_call(config, query=GET_ISSUES_QUERY, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)


def get_inventory_assets(config, params):
    variables = {
        "first": params.get("limit"),
        # "after": "<pagenation hash>",
        "projectId": params.get("projectID"),
        # Example Query: {"type": ["VIRTUAL_MACHINE"], "where": {"cloudPlatform": {"EQUALS": ["AWS"]}}}
        "query": params.get("filterQuery")
    }
    try:
        response = api_query_call(config, query=GET_INVENTORY_ASSETS_QUERY, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)


def get_issues_by_asset(config, params):
    variables = {
        "first": params.get("limit"),
        "fetchIssues": True,
        "filterBy": {
            "project": [params.get("projectID")],
            "status": params.get("status"),
            "relatedEntity": {
                "id": params.get("assetID")
            },
            "sourceRule": {}
        },
        "orderBy": {
            "field": "SEVERITY",
            "direction": "DESC"
        },
        "groupBy": "SOURCE_RULE",
        "groupOrderBy": {
            "field": "SEVERITY",
            "direction": "DESC"
        }
    }

    try:
        response = api_query_call(config, query=GET_ISSUES_BY_ASSET_QUERY, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)


def get_projects(config, params):
    variables = {
        "first": params.get("limit"),
        "filterBy": {},
        "orderBy": {
            "field": "IS_FOLDER",
            "direction": "DESC"
        }
    }
    try:
        response = api_query_call(config, query=GET_PROJECTS_QUERY, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)


def add_comment_to_issue(config, params):
    variables = {
        "input": {
            "issueId": params.get("issueID"),
            "text": params.get("comment")
        }
    }
    try:
        response = api_query_call(config, query=ADD_COMMENT_TO_ISSUE_QUERY, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)


operations = {
    'get_issues': get_issues,
    'get_inventory_assets': get_inventory_assets,
    'get_issues_by_asset': get_issues_by_asset,
    'get_projects': get_projects,
    'add_comment_to_issue': add_comment_to_issue
}
