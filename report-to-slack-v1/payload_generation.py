import json
import os

PREFIX = "SLACK_MSG_"
attachment_color = '#E92020'

if os.getenv("ATTACHMENT_COLOR"):
    attachment_color = os.getenv("ATTACHMENT_COLOR")
    print("Use attachment_color from input")

payload = {
    "text": f"{os.environ.get('TITLE_TEXT')}",
    "attachments": [
        {
            "color": f"{attachment_color}",
            "blocks": [
                {
                    "type": "section",
                    "fields": [
                    ]
                }
            ]
        }
    ]
}

# Set up workflow URL
workflow_url = "https://github.com/{}/oss-actions/runs/{}".format(
    os.getenv("GITHUB_REPO"),
    os.getenv("WORKFLOW_RUN_ID"))
os.environ["SLACK_GITHUB_WORKFLOW_URL"] = "<{}|Click Here To View Workflow Run>".format(workflow_url)

# By default, use the trigger branch from the pull request
branch = os.getenv("GITHUB_PULL_REQUEST_BRANCH")
if not branch:
    # For workflow not triggered by pull request, use the trigger branch
    branch_strs = os.getenv("GITHUB_TRIGGER_BRANCH").split("/")
    if branch_strs:
        branch = branch_strs[-1]
os.environ["SLACK_GITHUB_BRANCH"] = branch


data = {}
for key, value in os.environ.items():
    if key.startswith(PREFIX):
        key = key[len(PREFIX):].replace("_"," ")
        data[key] = value

data = {key: value for key, value in reversed(data.items())}

for key, value in data.items():
    section = {

        "type": "mrkdwn",
        "text": f"*{key}*\n{value}"
    }
    payload["attachments"][0]["blocks"][0]["fields"].append(section)

with open("payload.json", 'w') as json_file:
    json.dump(payload, json_file, indent=4)
