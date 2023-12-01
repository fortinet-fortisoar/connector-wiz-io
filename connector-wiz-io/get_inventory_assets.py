import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import api_query_call
import requests, json
logger = get_logger(LOGGER_NAME)


def get_inventory_assets(config, params):
    query = """
    query DataInventoryEntries($query: GraphEntityQueryInput, $projectId: String, $first: Int) {
      graphSearch(
        query: $query,
        projectId: $projectId,
        first: $first
      ) {
        totalCount
        pageInfo {
          endCursor
          hasNextPage
        }
        nodes {
          entities {
            id
            name
            properties
            type
          technologies {
              name
              risk
              usage
              status
            }
          }
        }
      }
    }
    """
    variables = {
      "first": params.get("limit"),
      #"after": "<pagenation hash>",
      "projectId": params.get("projectID"),
      # Example Query: {"type": ["VIRTUAL_MACHINE"], "where": {"cloudPlatform": {"EQUALS": ["AWS"]}}}
      "query": params.get("filterQuery")
    }
    try:
      response = api_query_call(config, query=query, variables=variables)
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)