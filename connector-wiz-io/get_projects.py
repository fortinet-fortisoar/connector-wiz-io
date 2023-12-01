import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import api_query_call
import requests, json
logger = get_logger(LOGGER_NAME)


def get_projects(config, params):
    query = """
    query ProjectsTable($filterBy: ProjectFilters, $first: Int, $after: String, $orderBy: ProjectOrder) {
      projects(filterBy: $filterBy, first: $first, after: $after, orderBy: $orderBy) {
        pageInfo {
            hasNextPage
            endCursor
        }
        totalCount
        nodes {
          id
          name
          slug
          isFolder
          childProjectCount
          cloudAccountCount
          repositoryCount
          kubernetesClusterCount
          containerRegistryCount
          securityScore
          archived
          businessUnit
          description
          workloadCount
          licensedWorkloadQuota
          riskProfile {
            businessImpact
          }
          nestingLevel
          ancestorProjects {
            ...ProjectsBreadcrumbsItemDetails
          }
        }
      }
    }

        fragment ProjectsBreadcrumbsItemDetails on Project {
      id
      name
      isFolder
    }
    """
    variables = {
      "first": params.get("limit"),
      "filterBy": {},
      "orderBy": {
        "field": "IS_FOLDER",
        "direction": "DESC"
      }
    }
    try:
      response = api_query_call(config, query=query, variables=variables)
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)