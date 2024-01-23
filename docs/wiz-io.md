
<h2>About the connector</h2>

<p>Wiz provides a comprehensive analysis engine that integrates: Cloud Security Posture Management (CSPM) Kubernetes Security Posture Management (KSPM) Cloud Workload Protection (CWPP) + vulnerability management. Infrastructure-as-Code (IaC) scanning.</p>

<p>This document provides information about the Wiz.io Connector, which facilitates automated interactions, with a Wiz.io server using FortiSOAR&trade; playbooks. Add the Wiz.io Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Wiz.io.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Contributors: Julian Petersohn</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-wiz-io</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Wiz.io server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Wiz.io server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Wiz.io</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>API Endpoint URL</td><td>Specify the URL of the Wiz.io server to connect and perform automated operations. Provide the API endpoint URL for the GraphQL API. The format is as follow: https://api.<location>.app.wiz.io</td>
</tr><tr><td>Client ID</td><td>Specify the API Client ID generated in the service account of the WIZ deployment to access the Wiz.io server to connect and perform the automated operations.</td>
</tr><tr><td>Client Secret</td><td>Specify the API Client Secret generated in the service account of the WIZ deployment to access the Wiz.io server to connect and perform the automated operations.</td>
</tr><tr><td>Authentication Endpoint URL</td><td>Specify the URL which is used to retrieve OAuth Token from. The URL can be found at the Service Account page to access the Wiz.io server to connect and perform the automated operations.</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Issues</td><td>Get Issues for all Assets from Wiz.io</td><td> <br/></td></tr>
<tr><td>Get Inventory Assets</td><td>Get Inventory Assets from Wiz.io platform.</td><td> <br/></td></tr>
<tr><td>Get Issues by Asset</td><td>Get Issues for all Assets from Wiz.io and allows to filter for a specific Asset, Project and Status.</td><td> <br/></td></tr>
<tr><td>Get Projects</td><td>Get a list of projects and settings of the projects.</td><td> <br/></td></tr>
<tr><td>Add Comment to Issue</td><td>Add a comment to an existing issue within Wiz.io</td><td> <br/></td></tr>
</tbody></table>

<h3>operation: Get Issues</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter Query</td><td>Specify the filter query to fetch the issues from Wiz.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of issues to be returned in response.
</td></tr></tbody></table>

<h4>Output</h4>

<p>No output schema is available at this time.</p>

<h3>operation: Get Inventory Assets</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Project ID</td><td>Specify the project ID for which the inventory assets will be returned.
</td></tr><tr><td>Filter Query</td><td>Specify the filter query to fetch the inventory assets from Wiz.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of inventory assets to be returned in response.
</td></tr></tbody></table>

<h4>Output</h4>

<p>No output schema is available at this time.</p>

<h3>operation: Get Issues by Asset</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Asset ID</td><td>Specify the asset ID for which the issues will be returned.
</td></tr><tr><td>Project ID</td><td>Specify the project ID for which the issues will be returned.
</td></tr><tr><td>Status</td><td>Specify the issue status, values are OPEN, RESOLVED, IN_PROGRESS & REJECTED.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of issues to be returned in response.
</td></tr></tbody></table>

<h4>Output</h4>

<p>No output schema is available at this time.</p>

<h3>operation: Get Projects</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>Specify the maximum number of projects to be returned in response.
</td></tr></tbody></table>

<h4>Output</h4>

<p>No output schema is available at this time.</p>

<h3>operation: Add Comment to Issue</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Issue ID</td><td>Specify the ID of the issue for which the comment should be added.
</td></tr><tr><td>Comment</td><td>Specify the comment message to add to issue.
</td></tr></tbody></table>

<h4>Output</h4>

<p>No output schema is available at this time.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - wiz-io - 1.0.0</code> playbook collection comes bundled with the Wiz.io connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Wiz.io connector.</p>

<ul>
<li>Add Comment to Issue</li>
<li>Get Inventory Assets</li>
<li>Get Issues</li>
<li>Get Issues by Asset</li>
<li>Get Projects</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
