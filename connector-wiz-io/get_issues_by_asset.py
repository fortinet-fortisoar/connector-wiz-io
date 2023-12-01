import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import api_query_call
import requests, json
logger = get_logger(LOGGER_NAME)


def get_issues_by_asset(config, params):
    query = """
query IssuesGroupedByValueTable($groupBy: IssuesGroupedByValueField!, $filterBy: IssueFilters, $orderBy: IssueOrder, $groupOrderBy: IssuesGroupedByValueOrder, $first: Int, $after: String, $fetchIssues: Boolean!) {
  issuesGroupedByValue(
    groupBy: $groupBy
    filterBy: $filterBy
    first: $first
    after: $after
    orderBy: $groupOrderBy
  ) {
    nodes {
      id
      issues(first: 5, orderBy: $orderBy) {
        nodes @include(if: $fetchIssues) {
          ...IssueDetails
          entityBasicDetails: entity {
            id
            type
            name
          }
          entityExtraDetails: entity {
            id
            properties
            projects {
              id
              name
              slug
              isFolder
              businessUnit
              riskProfile {
                businessImpact
              }
            }
          }
        }
        ...IssueCounts
        pageInfo {
          hasNextPage
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    totalCount
  }
}
    
    fragment IssueDetails on Issue {
  id
  type
  control {
    id
    name
    description
    severity
    type
    query
    enabled
    enabledForLBI
    enabledForMBI
    enabledForHBI
    enabledForUnattributed
    securitySubCategories {
      id
      category {
        id
      }
    }
    sourceCloudConfigurationRule {
      id
      name
    }
    createdBy {
      id
      name
      email
    }
    serviceTickets {
      ...ControlServiceTicket
    }
  }
  sourceRule {
    ...SourceRuleFields
  }
  createdAt
  updatedAt
  projects {
    id
    name
    slug
    isFolder
    businessUnit
    riskProfile {
      businessImpact
    }
  }
  status
  severity
  entity {
    id
    name
    type
  }
  resolutionReason
  entitySnapshot {
    id
    type
    name
    cloudPlatform
    region
    subscriptionName
    subscriptionId
    subscriptionExternalId
    subscriptionTags
    nativeType
    kubernetesClusterId
    kubernetesClusterName
    kubernetesNamespaceName
    containerServiceId
    containerServiceName
    tags
  }
  notes {
    id
    text
  }
  serviceTickets {
    id
    externalId
    name
    url
  }
}
    

    fragment ControlServiceTicket on ServiceTicket {
  id
  externalId
  name
  url
  project {
    id
    name
  }
  integration {
    id
    type
    name
  }
}
    

    fragment SourceRuleFields on IssueSourceRule {
  ... on CloudConfigurationRule {
    id
    name
    description
    subjectEntityType
    securitySubCategories {
      id
      title
      category {
        id
        name
        framework {
          id
          name
          description
          enabled
        }
      }
    }
    control {
      id
      resolutionRecommendation
    }
  }
  ... on CloudEventRule {
    id
    name
    description
    ruleSeverity: severity
    builtin
    generateIssues
    generateFindings
    enabled
    sourceType
    subCategories {
      id
      title
      category {
        id
        name
        framework {
          id
          name
          description
          enabled
        }
      }
    }
  }
  ... on Control {
    id
    name
    query
    type
    enabled
    enabledForHBI
    enabledForLBI
    enabledForMBI
    enabledForUnattributed
    resolutionRecommendation
    controlDescription: description
    securitySubCategories {
      id
      title
      category {
        id
        name
        framework {
          id
          name
          description
          enabled
        }
      }
    }
  }
}
    

    fragment IssueCounts on IssueConnection {
  totalCount
  criticalSeverityCount
  highSeverityCount
  mediumSeverityCount
  lowSeverityCount
  informationalSeverityCount
}
    """
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
      response = api_query_call(config, query=query, variables=variables)
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)