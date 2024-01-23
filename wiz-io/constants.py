"""
    Copyright start
    MIT License
    Copyright (c) 2024 Fortinet Inc
    Copyright end
"""

LOGGER_NAME = 'wiz'
REQUEST_TIMEOUT = 600
HEADERS_AUTH = {"Content-Type": "application/x-www-form-urlencoded"}
HEADERS = {"Content-Type": "application/json"}
GET_ISSUES_QUERY = """
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
GET_INVENTORY_ASSETS_QUERY = """
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
GET_ISSUES_BY_ASSET_QUERY = """
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
GET_PROJECTS_QUERY = """
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
ADD_COMMENT_TO_ISSUE_QUERY = """
    mutation CreateIssueComment($input: CreateIssueNoteInput!) {
      createIssueNote(input: $input) {
        issueNote {
          createdAt
          id
          text
          user {
            id
            email
          }
        }
      }
    }
    """
