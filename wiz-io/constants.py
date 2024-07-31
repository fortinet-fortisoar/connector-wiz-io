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
        query IssuesTable(
  $filterBy: IssueFilters
  $first: Int
  $after: String
  $orderBy: IssueOrder
) {
  issues:issuesV2(filterBy: $filterBy
    first: $first
    after: $after
    orderBy: $orderBy) {
    nodes {
      id
      sourceRule{
        __typename
        ... on Control {
          id
          name
          controlDescription: description
          resolutionRecommendation
          securitySubCategories {
            title
            category {
              name
              framework {
                name
              }
            }
          }
        }
        ... on CloudEventRule{
          id
          name
          cloudEventRuleDescription: description
          sourceType
          type
        }
        ... on CloudConfigurationRule{
          id
          name
          cloudConfigurationRuleDescription: description
          remediationInstructions
          serviceType
        }
      }
      createdAt
      updatedAt
      dueAt
      type
      resolvedAt
      statusChangedAt
      projects {
        id
        name
        slug
        businessUnit
        riskProfile {
          businessImpact
        }
      }
      status
      severity
      entitySnapshot {
        id
        type
        nativeType
        name
        status
        cloudPlatform
        cloudProviderURL
        providerId
        region
        resourceGroupExternalId
        subscriptionExternalId
        subscriptionName
        subscriptionTags
        tags
        createdAt
        externalId
      }
      serviceTickets {
        externalId
        name
        url
      }
      notes {
        createdAt
        updatedAt
        text
        user {
          name
          email
        }
        serviceAccount {
          name
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
    """
GET_INVENTORY_ASSETS_QUERY = """
    query CloudResourceSearch(
    $filterBy: CloudResourceFilters
    $first: Int
    $after: String
  ) {
    cloudResources(
      filterBy: $filterBy
      first: $first
      after: $after
    ) {
      nodes {
        ...CloudResourceFragment
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
  fragment CloudResourceFragment on CloudResource {
    id
    name
    type
    subscriptionId
    subscriptionExternalId
    graphEntity{
      id
      providerUniqueId
      name
      type
      projects {
        id
      }
      properties
      firstSeen
      lastSeen
    }
  }
    """
GET_PROJECTS_QUERY = """
    query ProjectsTable(
  $filterBy: ProjectFilters
  $first: Int
  $after: String
  $orderBy: ProjectOrder
) {
  projects(
    filterBy: $filterBy
    first: $first
    after: $after
    orderBy: $orderBy
  ) {
    nodes {
      id
      name
      isFolder
      archived
      businessUnit
      description
    }
  }
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

GET_VULNERABILITIES_FOR_ASSET = """
query VulnerabilityFindingsPage(
  $filterBy: VulnerabilityFindingFilters
  $first: Int
  $after: String
  $orderBy: VulnerabilityFindingOrder
) {
  vulnerabilityFindings(
    filterBy: $filterBy
    first: $first
    after: $after
    orderBy: $orderBy
  ) {
    nodes {
      id
      portalUrl
      name
      CVEDescription
      CVSSSeverity
      score
      exploitabilityScore
      impactScore
      dataSourceName
      hasExploit
      hasCisaKevExploit
      status
      vendorSeverity
      firstDetectedAt
      lastDetectedAt
      resolvedAt
      description
      remediation
      detailedName
      version
      fixedVersion
      detectionMethod
      link
      locationPath
      resolutionReason
      epssSeverity
      epssPercentile
      epssProbability
      validatedInRuntime
      layerMetadata{
        id
        details
        isBaseLayer
      }
      projects {
        id
        name
        slug
        businessUnit
        riskProfile {
          businessImpact
        }
      }
      ignoreRules{
        id
        name
        enabled
        expiredAt
      }
      vulnerableAsset {
        ... on VulnerableAssetBase {
          id
          type
          name
          region
          providerUniqueId
          cloudProviderURL
          cloudPlatform
          status
          subscriptionName
          subscriptionExternalId
          subscriptionId
          tags
          hasLimitedInternetExposure
          hasWideInternetExposure
          isAccessibleFromVPN
          isAccessibleFromOtherVnets
          isAccessibleFromOtherSubscriptions
        }
        ... on VulnerableAssetVirtualMachine {
          operatingSystem
          ipAddresses
        }
        ... on VulnerableAssetServerless {
          runtime
        }
        ... on VulnerableAssetContainerImage {
          imageId
        }
        ... on VulnerableAssetContainer {
          ImageExternalId
          VmExternalId
          ServerlessContainer
          PodNamespace
          PodName
          NodeName
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
"""