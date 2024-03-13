## About the connector
Wiz provides a comprehensive analysis engine that integrates: Cloud Security Posture Management (CSPM) Kubernetes Security Posture Management (KSPM) Cloud Workload Protection (CWPP) + vulnerability management. Infrastructure-as-Code (IaC) scanning.
<p>This document provides information about the Wiz.io Connector, which facilitates automated interactions, with a Wiz.io server using FortiSOAR&trade; playbooks. Add the Wiz.io Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Wiz.io.</p>

### Version information

Connector Version: 1.1.0

FortiSOAR&trade; Version Tested on: 7.4.1-3167

Wiz.io Version Tested on: 

Authored By: Fortinet

Certified: Yes
## Release Notes for version 1.1.0
Following enhancements have been made to the Wiz.io Connector in version 1.1.0:
<ul>
<li>Added new action "Get Vulnerabilities for Asset" and its playbook.</li>



<li>Updated the Query for "Get Issues" action.</li>
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
</tr><tr><td>Client ID</td><td>Specify the API Client ID generated in the service account of the WIZ deployment to access the Wiz.io server to connect and perform the automated operations.
</td>
</tr><tr><td>Client Secret</td><td>Specify the API Client Secret generated in the service account of the WIZ deployment to access the Wiz.io server to connect and perform the automated operations.
</td>
</tr><tr><td>Authentication Endpoint URL</td><td>Specify the URL from which to retrieve OAuth token. The URL can be found at the Service Account page of the Wiz.io server.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Issues</td><td>Get issues for all assets from Wiz.io based on the filter query and maximum results limit that you have specified.</td><td>get_issues <br/>Investigation</td></tr>
<tr><td>Get Inventory Assets</td><td>Get inventory assets from Wiz.io platform based on the Project ID and other filter criteria that you have specified.</td><td>get_inventory_assets <br/>Investigation</td></tr>
<tr><td>Get Issues for Asset</td><td>Get issues for all assets from Wiz.io based on the Asset ID, Project ID, Status, and other filter criteria that you have specified.</td><td>get_issues_by_asset <br/>Investigation</td></tr>
<tr><td>Get Projects</td><td>Get a list of projects based on the filter query and maximum results limit that you have specified.</td><td>get_projects <br/>Investigation</td></tr>
<tr><td>Add Comment to Issue</td><td>Add a comment to an existing issue within Wiz.io based on the issue ID and the comment that you have specified.</td><td>add_comment_to_issue <br/>Investigation</td></tr>
<tr><td>Get Vulnerabilities for Asset</td><td>Get vulnerabilities for all assets from Wiz.io based on the Asset ID, Project ID, and other filter criteria that you have specified.</td><td>get_vulnerabilities_for_asset <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Issues
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter Query</td><td>Specify the filter query to fetch the issues from Wiz. For example: { "severity": ["CRITICAL"]}
</td></tr><tr><td>Limit</td><td>Specify the maximum number of results to be returned in response.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "issues": {
            "totalCount": "",
            "pageInfo": {
                "hasNextPage": "",
                "endCursor": ""
            },
            "nodes": [
                {
                    "id": "",
                    "severity": "",
                    "status": "",
                    "entity": {
                        "id": "",
                        "name": "",
                        "type": ""
                    },
                    "control": {
                        "name": ""
                    }
                }
            ]
        }
    }
}</pre>
### operation: Get Inventory Assets
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter Query</td><td>Specify the filter query to fetch the inventory assets from Wiz. For example: { "type": ["VIRTUAL_MACHINE"]}
</td></tr><tr><td>Project ID</td><td>(Optional) Specify the project ID whose associated inventory assets are to be retrieved.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the maximum number of results to be returned in response.
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
### operation: Get Issues for Asset
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Asset ID</td><td>Specify the asset ID whose associated issues are to be retrieved.
</td></tr><tr><td>Project ID</td><td>Specify the project ID whose associated issues are to be retrieved.
</td></tr><tr><td>Status</td><td>Select the issue status associated with the specified asset and project ID. You can choose from the following options: Open , Resolved , In Progress  & Rejected.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the maximum number of results to be returned in response.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "issuesGroupedByValue": {
            "nodes": [
                {
                    "id": "",
                    "issues": {
                        "nodes": [
                            {
                                "id": "",
                                "type": "",
                                "control": {
                                    "id": "",
                                    "name": "",
                                    "description": "",
                                    "severity": "",
                                    "type": "",
                                    "query": {
                                        "as": "",
                                        "relationships": [
                                            {
                                                "negate": "",
                                                "type": [
                                                    {
                                                        "type": ""
                                                    }
                                                ],
                                                "with": {
                                                    "relationships": [
                                                        {
                                                            "type": [
                                                                {
                                                                    "type": ""
                                                                }
                                                            ],
                                                            "with": {
                                                                "type": [
                                                                    ""
                                                                ],
                                                                "where": {
                                                                    "categories": {
                                                                        "EQUALS": []
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    ],
                                                    "type": []
                                                }
                                            }
                                        ],
                                        "select": "",
                                        "type": [],
                                        "where": {
                                            "cloudPlatform": {
                                                "EQUALS": []
                                            }
                                        }
                                    },
                                    "enabled": "",
                                    "enabledForLBI": "",
                                    "enabledForMBI": "",
                                    "enabledForHBI": "",
                                    "enabledForUnattributed": "",
                                    "securitySubCategories": [
                                        {
                                            "id": "",
                                            "category": {
                                                "id": ""
                                            }
                                        }
                                    ],
                                    "sourceCloudConfigurationRule": "",
                                    "createdBy": "",
                                    "serviceTickets": ""
                                },
                                "sourceRule": {
                                    "id": "",
                                    "name": "",
                                    "query": {
                                        "as": "",
                                        "relationships": [
                                            {
                                                "negate": "",
                                                "type": [
                                                    {
                                                        "type": ""
                                                    }
                                                ],
                                                "with": {
                                                    "relationships": [
                                                        {
                                                            "type": [
                                                                {
                                                                    "type": ""
                                                                }
                                                            ],
                                                            "with": {
                                                                "type": [
                                                                    ""
                                                                ],
                                                                "where": {
                                                                    "categories": {
                                                                        "EQUALS": []
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    ],
                                                    "type": []
                                                }
                                            }
                                        ],
                                        "select": "",
                                        "type": [],
                                        "where": {
                                            "cloudPlatform": {
                                                "EQUALS": []
                                            }
                                        }
                                    },
                                    "type": "",
                                    "enabled": "",
                                    "enabledForHBI": "",
                                    "enabledForLBI": "",
                                    "enabledForMBI": "",
                                    "enabledForUnattributed": "",
                                    "resolutionRecommendation": "",
                                    "controlDescription": "",
                                    "securitySubCategories": [
                                        {
                                            "id": "",
                                            "title": "",
                                            "category": {
                                                "id": "",
                                                "name": "",
                                                "framework": {
                                                    "id": "",
                                                    "name": "",
                                                    "description": "",
                                                    "enabled": ""
                                                }
                                            }
                                        }
                                    ]
                                },
                                "createdAt": "",
                                "updatedAt": "",
                                "projects": [
                                    {
                                        "id": "",
                                        "name": "",
                                        "slug": "",
                                        "isFolder": "",
                                        "businessUnit": "",
                                        "riskProfile": {
                                            "businessImpact": ""
                                        }
                                    }
                                ],
                                "status": "",
                                "severity": "",
                                "entity": {
                                    "id": "",
                                    "name": "",
                                    "type": ""
                                },
                                "resolutionReason": "",
                                "entitySnapshot": {
                                    "id": "",
                                    "type": "",
                                    "name": "",
                                    "cloudPlatform": "",
                                    "region": "",
                                    "subscriptionName": "",
                                    "subscriptionId": "",
                                    "subscriptionExternalId": "",
                                    "subscriptionTags": {},
                                    "nativeType": "",
                                    "kubernetesClusterId": "",
                                    "kubernetesClusterName": "",
                                    "kubernetesNamespaceName": "",
                                    "containerServiceId": "",
                                    "containerServiceName": "",
                                    "tags": {
                                        "Name": ""
                                    }
                                },
                                "notes": [],
                                "serviceTickets": [],
                                "entityBasicDetails": {
                                    "id": "",
                                    "type": "",
                                    "name": ""
                                },
                                "entityExtraDetails": {
                                    "id": "",
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
                                    "projects": [
                                        {
                                            "id": "",
                                            "name": "",
                                            "slug": "",
                                            "isFolder": "",
                                            "businessUnit": "",
                                            "riskProfile": {
                                                "businessImpact": ""
                                            }
                                        }
                                    ]
                                }
                            }
                        ],
                        "totalCount": "",
                        "criticalSeverityCount": "",
                        "highSeverityCount": "",
                        "mediumSeverityCount": "",
                        "lowSeverityCount": "",
                        "informationalSeverityCount": "",
                        "pageInfo": {
                            "hasNextPage": ""
                        }
                    }
                }
            ],
            "pageInfo": {
                "hasNextPage": "",
                "endCursor": ""
            },
            "totalCount": ""
        }
    }
}</pre>
### operation: Get Projects
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter Query</td><td>Specify the filter query to fetch projects from Wiz. For example: { "id": {"equals": "d6ac50bb-aec0-52fc-80ab-bacd7b02f178"}}
</td></tr><tr><td>Limit</td><td>Specify the maximum number of results to be returned in response.
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
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Issue ID</td><td>Specify the issue ID for which the comment is to be added.
</td></tr><tr><td>Comment</td><td>Specify the comment to add to the issue.
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
### operation: Get Vulnerabilities for Asset
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Asset ID</td><td>Specify the asset ID whose associated vulnerabilities are to be retrieved.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the maximum number of results to be returned in response.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - wiz-io - 1.1.0` playbook collection comes bundled with the Wiz.io connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Wiz.io connector.

- Add Comment to Issue
- Get Inventory Assets
- Get Issues
- Get Issues for Asset
- Get Projects
- Get Vulnerabilities for Asset

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
