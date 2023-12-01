## About the connector
Wiz provides a comprehensive analysis engine that integrates: Cloud Security Posture Management (CSPM) Kubernetes Security Posture Management (KSPM) Cloud Workload Protection (CWPP) + vulnerability management. Infrastructure-as-Code (IaC) scanning.
<p>This document provides information about the Wiz.io Connector, which facilitates automated interactions, with a Wiz.io server using FortiSOAR&trade; playbooks. Add the Wiz.io Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Wiz.io.</p>

### Version information

Connector Version: 1.0.0


Authored By: Julian Petersohn

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-wiz</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Wiz.io server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Wiz.io server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Wiz.io</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>API Endpoint URL</td><td>
</td>
</tr><tr><td>Client ID</td><td>
</td>
</tr><tr><td>Client Secret</td><td>
</td>
</tr><tr><td>Authentication Endpoint URL</td><td>
</td>
</tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Issues</td><td>Get Issues for all Assets from Wiz.io</td><td> <br/></td></tr>
<tr><td>Get Inventory Assets</td><td>Get Inventory Assets from Wiz.io platform</td><td> <br/></td></tr>
<tr><td>Get Issues by Asset</td><td>Get Issues for all Assets from Wiz.io and allows to filter for a specific Asset, Project and Status</td><td> <br/></td></tr>
<tr><td>Get Projects</td><td>Get a list of projects and settings of the projects.</td><td> <br/></td></tr>
</tbody></table>

### operation: Get Issues
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>Limit the results by the amount provided. Will automatically enable pagination.
</td></tr><tr><td>Filter Query</td><td>Using json syntax to define a query for the results.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: Get Inventory Assets
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>Limit the results by the amount provided. Will automatically enable pagination.
</td></tr><tr><td>Project ID</td><td>Provide a project id from which the assets should be gathered.  Keep the wildcard to allow all projects to be included.
</td></tr><tr><td>Filter Query</td><td>Provide a Query which filters for the necessary asset like a VM on AWS, etc.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: Get Issues by Asset
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>Limit the results by the amount provided. Will automatically enable pagination.
</td></tr><tr><td>Project ID</td><td>Filter for specific Assets and Issues within a Project.
</td></tr><tr><td>Status</td><td>Provide a list of issue status. Possible values are allowed: OPEN, RESOLVED, IN_PROGRESS & REJECTED. The input needs to be a
</td></tr><tr><td>Asset ID</td><td>Provide the ID of an Asset Issues should retrieved for.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: Get Projects
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>Limit the results by the amount provided. Will automatically enable pagination.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
## Included playbooks
The `Sample - wiz - 1.0.0` playbook collection comes bundled with the Wiz.io connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Wiz.io connector.

