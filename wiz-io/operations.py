"""
    Copyright start
    MIT License
    Copyright (c) 2024 Fortinet Inc
    Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
from .constants import *
from .utils import api_query_call, check_empty_value

logger = get_logger(LOGGER_NAME)


def get_issues(config, params):
    variables = {
    "first":params.get("limit"),
    "filterBy": {
      "relatedEntity": {},
      "createdAt": {},
      "resolvedAt": {},
    },
  }
    if params.get("pagination"):
      pagination = {"after": params.get("pagination")}
      variables.update(pagination)

    if params.get("issueID"):
      issueid = {"id": check_empty_value(params.get("issueID"))}
      variables["filterBy"].update(issueid)

    if params.get("searchQuery"):
      searchQuery = {"search": params.get("searchQuery")}
      variables["filterBy"].update(searchQuery)

    if params.get("projectID"):
      projectID = {"project": [params.get("projectID")]}
      variables["filterBy"].update(projectID)

    if params.get("severity"):
      severity = {"severity": [params.get("severity")]}
      variables["filterBy"].update(severity)

    if params.get("status"):
      status = {"status": [params.get("status")]}
      variables["filterBy"].update(status)

    if params.get("type"):
      type_var = {"type": [params.get("type")]}
      variables["filterBy"].update(type_var)

    if params.get("relatedEntityID"):
      relatedEntityID = {"id": params.get("relatedEntityID")}
      variables["filterBy"]["relatedEntity"].update(relatedEntityID)

    if params.get("realtedEntityType"):
      realtedEntityType = {"type": check_empty_value(params.get("realtedEntityType"))}
      variables["filterBy"]["relatedEntity"].update(realtedEntityType)

    if params.get("relatedCloudPlatform"):
      relatedCloudPlatform = {"cloudPlatform": check_empty_value(params.get("relatedCloudPlatform"))}
      variables["filterBy"]["relatedEntity"].update(relatedCloudPlatform)

    if params.get("createdBefore"):
      createdBefore = {"before": params.get("createdBefore")}
      variables["filterBy"]["createdAt"].update(createdBefore)

    if params.get("createdAfter"):
      createdAfter = {"after": params.get("createdAfter")}
      variables["filterBy"]["createdAt"].update(createdAfter)

    if params.get("resolvedBefore"):
      resolvedBefore = {"before": params.get("resolvedBefore")}
      variables["filterBy"]["resolvedAt"].update(resolvedBefore)

    if params.get("resolvedAfter"):
      resolvedAfter = {"after": params.get("resolvedAfter")}
      variables["filterBy"]["resolvedAt"].update(resolvedAfter)

    try:
        response = api_query_call(config, query=GET_ISSUES_QUERY, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)



def get_inventory_assets(config, params):
    variables = {
    "first":params.get("limit"),
    "filterBy": {
      "projectId": [
        params.get("projectID")
      ],
      "type": [
        params.get("type")
      ],
      "updatedAt": {
        "before":params.get("updatedBefore"),
        "after":params.get("updatedAfter"),
      },
      "deletedAt": {
        "before":params.get("deletedBefore"),
        "after":params.get("deletedAfter"),
      },
      "search":params.get("searchTerm")
    }
  }
    try:
        response = api_query_call(config, query=GET_INVENTORY_ASSETS_QUERY, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)

def get_projects(config, params):
    variables = {
    "first": params.get("limit"),
    "filterBy": {
      "search": params.get("name"),
      "includeArchived": params.get("includeArchivedProjects"),
      "root": True,
      "impact": params.get("businessImpact"),
    },
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

def get_vulnerabilities(config, params):
    variables = {
   "first":params.get("limit"),
   "filterBy":{
      "id":check_empty_value(params.get("vulnerabilityID")),
       "subscriptionExternalId":check_empty_value(params.get("externalSubscriptionID")),
      "assetType":[
         params.get("assetType")
      ],
      "vendorSeverity":[
         params.get("severity")
      ],
      "status":[
         params.get("status")
      ],
      "assetId":check_empty_value(params.get("assetID")),
      "vulnerabilityId":check_empty_value(params.get("vulnerabilityID")),
      "firstSeenAt":{
         "before":params.get("firstSeenBefore"),
         "after":params.get("firstSeenAfter"),
      },
      "resolvedAt":{
         "before":params.get("resolvedBefore"),
         "after":params.get("resolvedAfter"),
      },
      "projectId":[
         params.get("projectID"),
      ],
      "hasFix":params.get("patchAvailable"),
      "hasExploit":params.get("exploitAvailable"),
   }
}
    if len(params.get("pagination")) > 0:
      pagination = {"after": params.get("pagination")}
      variables.update(pagination)

    try:
        response = api_query_call(config, query=GET_VULNERABILITIES_FOR_ASSET, variables=variables)
        return response.json()
    except Exception as err:
        logger.exception(err)
        raise ConnectorError(err)

operations = {
    'get_issues': get_issues,
    'get_inventory_assets': get_inventory_assets,
    'get_projects': get_projects,
    'add_comment_to_issue': add_comment_to_issue,
    'get_vulnerabilities': get_vulnerabilities,
}
