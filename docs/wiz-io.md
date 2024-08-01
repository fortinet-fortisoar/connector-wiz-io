## About the connector
Wiz provides a comprehensive analysis engine that integrates: Cloud Security Posture Management (CSPM) Kubernetes Security Posture Management (KSPM) Cloud Workload Protection (CWPP) + vulnerability management. Infrastructure-as-Code (IaC) scanning.
<p>This document provides information about the Wiz.io Connector, which facilitates automated interactions, with a Wiz.io server using FortiSOAR&trade; playbooks. Add the Wiz.io Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Wiz.io.</p>

### Version information

Connector Version: 2.0.0

FortiSOAR&trade; Version Tested on: 7.4.1-3167

Wiz.io Version Tested on: 

Authored By: Fortinet

Certified: Yes
## Release Notes for version 2.0.0
Following enhancements have been made to the Wiz.io Connector in version 2.0.0:
<ul>
<li>combined asset specific actions into single actions.</li>
<li><p>removed obsolete actions:</p>

<ul>
<li><code>GET VULNERABILITIES FOR ASSET</code></li>
<li><code>GET ISSUES FOR ASSET</code></li>
</ul></li>
<li>Updated actions with more detailed input capabilities</li>

<li><p>Updated Queries for the following actions:</p>

<ul>
<li><code>GET ISSUES</code></li>
<li><code>GET INVENTORY ASSETS</code></li>
<li><code>GET PROJECTS</code></li>
<li><code>ADD COMMENT TO ISSUE</code></li>
<li><code>GET VULNERABILITIES</code></li>
</ul></li>
</ul>

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-wiz-io</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Wiz.io server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Wiz.io server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Wiz.io</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>API Endpoint URL</td><td>Specify the URL of the Wiz.io server to connect and perform automated operations. Provide the API endpoint URL for the GraphQL API. The format is as follow: https://api.your-server-location-here.app.wiz.io
</td>
</tr><tr><td>Client ID</td><td>Specify the API Client ID generated in the service account of the WIZ deployment to access the Wiz.io server.
</td>
</tr><tr><td>Client Secret</td><td>Specify the API Client Secret generated in the service account of the WIZ deployment to access the Wiz.io server.
</td>
</tr><tr><td>Authentication Endpoint URL</td><td>Specify the URL from which to retrieve OAuth token. The URL can be found at the Service Account page of the Wiz.io server.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Issues</td><td>Gets issues  from Wiz.io based on the defined filter and maximum results limit that you have specified.</td><td>get_issues <br/>Investigation</td></tr>
<tr><td>Get Inventory Assets</td><td>Get inventory assets from Wiz.io platform based on the Project ID and other filter criteria that you have specified.</td><td>get_inventory_assets <br/>Investigation</td></tr>
<tr><td>Get Projects</td><td>Get a list of projects and settings based on the filter query and maximum results limit that you have specified.</td><td>get_projects <br/>Investigation</td></tr>
<tr><td>Add Comment to Issue</td><td>Add a comment to an existing issue within Wiz.io based on the issue ID and the comment that you have specified.</td><td>add_comment_to_issue <br/>Investigation</td></tr>
<tr><td>Get Vulnerabilities</td><td>Get vulnerabilities from Wiz.io based on the Asset ID, Project ID, and other filter criteria that you have specified.</td><td> <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Issues
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>Use as a pagination argument to refine your query. Possible values: 1-500.
</td></tr><tr><td>Issue ID</td><td>(Optional) Filter Issues matching these ID.
</td></tr><tr><td>Search Query</td><td>(Optional) Free text search on Issue title or object name. Returns NULL if no match is found.
</td></tr><tr><td>Project ID</td><td>(Optional) Filter Issues from specific projects according to the project ID.
</td></tr><tr><td>Severity</td><td>(Optional) Filter Issues by the Control severity.
</td></tr><tr><td>Status</td><td>(Optional) Filter Issues by their current status.
</td></tr><tr><td>Type</td><td>(Optional) Filter by Issue type.
</td></tr><tr><td>Related Entity ID</td><td>(Optional) Filter Issues by a specific entity ID.
</td></tr><tr><td>Realted Entity Type</td><td>(Optional) Filter Issues by a specific entity type.
</td></tr><tr><td>Created before</td><td>(Optional) This object contains Issues date filters to narrow down your results. Use to return Issues that were created before the specified date period.
</td></tr><tr><td>Created after</td><td>(Optional) This object contains Issues date filters to narrow down your results. Use to return Issues that were created after the specified date period.
</td></tr><tr><td>Resolved before</td><td>(Optional) This object contains Issues date filters to narrow down your results. Use to return Issues that were resolved before the specified date period.
</td></tr><tr><td>Resolved after</td><td>(Optional) This object contains Issues date filters to narrow down your results. Use to return Issues that were resolved after the specified date period.
</td></tr><tr><td>Pagination</td><td>(Optional) Use as a pagination argument to refine your query. Use the Value from the "after" parameter in the previous result.
</td></tr><tr><td>Related Cloud Platform</td><td>(Optional) Filter Issues by cloud platform.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "issues": {
            "nodes": [
                {
                    "id": "",
                    "type": "",
                    "dueAt": "",
                    "notes": [],
                    "status": "",
                    "projects": [
                        {
                            "id": "",
                            "name": "",
                            "slug": "",
                            "riskProfile": {
                                "businessImpact": ""
                            },
                            "businessUnit": ""
                        }
                    ],
                    "severity": "",
                    "createdAt": "",
                    "updatedAt": "",
                    "resolvedAt": "",
                    "sourceRule": {
                        "id": "",
                        "name": "",
                        "controlDescription": "",
                        "securitySubCategories": [
                            {
                                "title": "",
                                "category": {
                                    "name": "",
                                    "framework": {
                                        "name": ""
                                    }
                                }
                            }
                        ],
                        "resolutionRecommendation": ""
                    },
                    "entitySnapshot": {
                        "id": "",
                        "name": "",
                        "tags": {},
                        "type": "",
                        "region": "",
                        "status": "",
                        "createdAt": "",
                        "externalId": "",
                        "nativeType": "",
                        "providerId": "",
                        "cloudPlatform": "",
                        "cloudProviderURL": "",
                        "subscriptionName": "",
                        "subscriptionTags": {},
                        "subscriptionExternalId": "",
                        "resourceGroupExternalId": ""
                    },
                    "serviceTickets": [],
                    "statusChangedAt": ""
                }
            ],
            "pageInfo": {
                "endCursor": "",
                "hasNextPage": ""
            }
        }
    }
}</pre>
### operation: Get Inventory Assets
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>(Optional) Limit the results by the amount provided. Will automatically enable pagination.
</td></tr><tr><td>Project ID</td><td>(Optional) Provide a project id from which the assets should be gathered. Keep the wildcard to allow all projects to be included.
</td></tr><tr><td>Type</td><td>Filter cloud resources by specific entity types. You can specify multiple values in an array. Entity types must be specified in ALL_CAPS format. List of types: https://win.wiz.io/docs/security-graph-object-normalization
</td></tr><tr><td>Search Term</td><td>(Optional) Filter by free text search on cloud resource name.
</td></tr><tr><td>Updated before</td><td>(Optional) This object contains cloud resource date filters to narrow down your report results. Use to return cloud resources that were created or updated in the specified date period. DateTime format: yyyy-MM-dd'T'HH:mm:ss'Z' (ISO 8601 format)
</td></tr><tr><td>Updated after</td><td>(Optional) This object contains cloud resource date filters to narrow down your report results. Use to return cloud resources that were created or updated in the specified date period. DateTime format: yyyy-MM-dd'T'HH:mm:ss'Z' (ISO 8601 format)
</td></tr><tr><td>Deleted before</td><td>(Optional) This object contains cloud resource date filters to narrow down your report results. Use to return cloud resources that were created or updated in the specified date period. DateTime format: yyyy-MM-dd'T'HH:mm:ss'Z' (ISO 8601 format)
</td></tr><tr><td>Deleted after</td><td>(Optional) This object contains cloud resource date filters to narrow down your report results. Use to return cloud resources that were created or updated in the specified date period. DateTime format: yyyy-MM-dd'T'HH:mm:ss'Z' (ISO 8601 format)
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "graphSearch": {
            "totalCount": "",
            "pageInfo": {
                "endCursor": "",
                "hasNextPage": ""
            },
            "nodes": [
                {
                    "entities": [
                        {
                            "id": "",
                            "name": "",
                            "properties": {
                                "_productIDs": [],
                                "_vertexID": "",
                                "accessibleFrom.internet": "",
                                "cloudPlatform": "",
                                "cloudProviderURL": "",
                                "creationDate": "",
                                "externalId": "",
                                "hasAdminPrivileges": "",
                                "hasHighPrivileges": "",
                                "hasSensitiveData": "",
                                "isContainerHost": "",
                                "isEphemeral": "",
                                "isManaged": "",
                                "memoryGB": "",
                                "name": "",
                                "nativeType": "",
                                "numAddressesOpenForHTTP": "",
                                "numAddressesOpenForHTTPS": "",
                                "numAddressesOpenForNonStandardPorts": "",
                                "numAddressesOpenForRDP": "",
                                "numAddressesOpenForSSH": "",
                                "numAddressesOpenForWINRM": "",
                                "openToAllInternet": "",
                                "openToEntireInternet": "",
                                "operatingSystem": "",
                                "passwordAuthDisabled": "",
                                "providerUniqueId": "",
                                "region": "",
                                "regionLocation": "",
                                "resourceGroupExternalId": "",
                                "status": "",
                                "subscriptionExternalId": "",
                                "tags": {
                                    "Name": ""
                                },
                                "totalDisks": "",
                                "updatedAt": "",
                                "vCPUs": "",
                                "zone": ""
                            },
                            "type": "",
                            "technologies": [
                                {
                                    "name": "",
                                    "risk": "",
                                    "usage": "",
                                    "status": ""
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}</pre>
### operation: Get Projects
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>(Optional) Filter by Project name.
</td></tr><tr><td>Business Impact</td><td>(Optional) Filter by business impact
</td></tr><tr><td>Include Archived Projects</td><td>(Optional) Filter Projects that are/are not archived.
</td></tr><tr><td>Limit</td><td>Limit the results by the amount provided. Will automatically enable pagination.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "projects": {
            "pageInfo": {
                "hasNextPage": "",
                "endCursor": ""
            },
            "totalCount": "",
            "nodes": [
                {
                    "id": "",
                    "name": "",
                    "slug": "",
                    "isFolder": "",
                    "childProjectCount": "",
                    "cloudAccountCount": "",
                    "repositoryCount": "",
                    "kubernetesClusterCount": "",
                    "containerRegistryCount": "",
                    "securityScore": "",
                    "archived": "",
                    "businessUnit": "",
                    "description": "",
                    "workloadCount": "",
                    "licensedWorkloadQuota": "",
                    "riskProfile": {
                        "businessImpact": ""
                    },
                    "nestingLevel": "",
                    "ancestorProjects": ""
                }
            ]
        }
    }
}</pre>
### operation: Add Comment to Issue
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Issue ID</td><td>ID of the issue where a comment should be added.
</td></tr><tr><td>Comment</td><td>Comment message to add to a issue.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "createIssueNote": {
            "issueNote": {
                "createdAt": "",
                "id": "",
                "text": "",
                "user": ""
            }
        }
    }
}</pre>
### operation: Get Vulnerabilities
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Status</td><td>(Optional) Filter by finding status. You can specify multiple values in an array.
</td></tr><tr><td>Vulnerability ID</td><td>(Optional) Filter vulnerability findings matching these IDs. You can specify multiple values in an array.
</td></tr><tr><td>External Subscription ID</td><td>(Optional) Filter vulnerability findings from these external subscription IDs (AWS Account, Azure Subscription, GCP Project, and OCI Compartment). You can specify multiple values in an array.
</td></tr><tr><td>Severity</td><td>Filter by vulnerability vendor severity.
</td></tr><tr><td>First Seen before</td><td>(Optional) This object contains vulnerability date filters to narrow down your query's results. Use to return vulnerability findings that were created (first detected) in the specified date period. Format: 2022-12-03T10:15:30Z
</td></tr><tr><td>First Seen after</td><td>(Optional) This object contains vulnerability date filters to narrow down your query's results. Use to return vulnerability findings that were created (first detected) in the specified date period. Format: 2022-12-03T10:15:30Z
</td></tr><tr><td>Resolved before</td><td>(Optional) This object contains vulnerability date filters to narrow down your query's results. Use to return vulnerability findings that were resolved in the specified date period. Format: 2022-12-03T10:15:30Z
</td></tr><tr><td>Resolved after</td><td>(Optional) This object contains vulnerability date filters to narrow down your query's results. Use to return vulnerability findings that were resolved in the specified date period. Format: 2022-12-03T10:15:30Z
</td></tr><tr><td>Project ID</td><td>(Optional) Filter only vulnerability findings for the given projects. You can specify multiple values in an array.
</td></tr><tr><td>Asset ID</td><td>(Optional) Filter only vulnerability findings on these asset IDs.
</td></tr><tr><td>Asset Type</td><td>(Optional) The asset type return in your query. You can specify multiple values as a separated list.
Possible values: "VIRTUAL_MACHINE", "CONTAINER_IMAGE","CONTAINER", "SERVERLESS".
</td></tr><tr><td>Patch available</td><td>(Optional) Filter only vulnerability findings for vulnerabilities with an available fix.
</td></tr><tr><td>Exploit available</td><td>(Optional) Filter only vulnerability findings for vulnerabilities with an available exploit.
</td></tr><tr><td>Limit</td><td>(Optional) Limit the results by the amount provided. Will automatically enable pagination. Values can be from 1 - 5000.
</td></tr><tr><td>Pagination</td><td>(Optional) Use as a pagination argument to refine your query. Use the Value from the "after" parameter in the previous result.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
## Included playbooks
The `Sample - wiz-io - 2.0.0` playbook collection comes bundled with the Wiz.io connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Wiz.io connector.

- Add Comment to Issue
- Get Inventory Assets
- Get Issues
- Get Projects
- Get Vulnerabilities

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
