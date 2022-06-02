# Pipeline IaC

## Deploy pipeline

### Requirements

- AWS CLI
- Configured AWS credentials (`aws configure` or env vars)
- Sufficient permissions in user
- Github personal access token

### Deployment

```shell
$ export GITHUB_TOKEN=<your-token>
$ aws cloudformation deploy --stack-name fastapi-codepipeline \
 --template-file cloudformation/pipeline-template.yaml \
 --capabilities CAPABILITY_IAM \
 --parameter-overrides GitHubOAuthToken=${GITHUB_TOKEN}
```