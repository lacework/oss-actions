**DEPRECATED**

Call AWS Credentials Manager yourself.

# initialize-workflow
Calls commonly used actions in a single action.
1. Checkout repository
2. Configures AWS Credentials Manager

<!-- action-docs-description -->
## Description

Gets the workflow environment ready.
<!-- action-docs-description -->

<!-- action-docs-inputs -->

<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

<!-- action-docs-outputs -->

<!-- action-docs-runs -->
## Runs

This action is a `composite` action.
<!-- action-docs-runs -->

## Usage
This action assumes an AWS which requires OIDC to authenticate so specify `id-token: write` for the job.
```yaml
    permissions:
      id-token: write
```
### Example
```yaml
  - id: initialize_workflow
    name: Initialize Workflow
    uses: lacework-dev/oss-actions/initialize-workflow-v1
```