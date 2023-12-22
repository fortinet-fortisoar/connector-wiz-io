import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import api_query_call
import requests, json
logger = get_logger(LOGGER_NAME)


def get_issues(config, params):
    query = """
    query IssuesQuery($first: Int, $orderBy: IssueOrder, $filterBy: IssueFilters, $after: String) {
      issues(first: $first, filterBy: $filterBy, orderBy: $orderBy, after: $after) {
        totalCount
        pageInfo {
          hasNextPage
          endCursor
        }
        nodes {
          id
          severity
          status
          entity {
            id
            name
            type
          }
          control {
            name
          }
        }
      }
    }
    """
    variables = {
      "first": params.get("limit"),
      #"after": "<pagenation hash>",
      "orderBy": {
        "field": "SEVERITY",
        "direction": "DESC"
      },
      # Example Query: {"status": ["RESOLVED"]}
      "filterBy": params.get("filterQuery")
    }
    
    
    try:
      response = api_query_call(config, query=query, variables=variables)
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)