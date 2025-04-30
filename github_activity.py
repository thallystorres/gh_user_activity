import argparse
import requests
from datetime import datetime

GITHUB_EVENT_TYPES = {
    "PushEvent": "📦 Pushed commits",
    "PullRequestEvent": "🔀 Pull request opened/closed/merged",
    "IssuesEvent": "🐞 Issue created/closed/reopened",
    "IssueCommentEvent": "💬 Commented on an issue or pull request",
    "ForkEvent": "🍴 Forked the repository",
    "WatchEvent": "⭐ Starred the repository",
    "CreateEvent": "🆕 Created a branch, tag, or repository",
    "DeleteEvent": "🗑️ Deleted a branch or tag",
    "PullRequestReviewEvent": "🧐 Reviewed a pull request",
    "PullRequestReviewCommentEvent": "🗨️ Commented on a pull request review",
    "ReleaseEvent": "🚀 Published a release",
    "MemberEvent": "👥 Added a collaborator",
    "PublicEvent": "🌐 Made the repository public",
    "GollumEvent": "📘 Edited the wiki",
    "CommitCommentEvent": "📝 Commented on a commit",
}


def format_date(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = datetime.strftime(date_obj, "%d/%m/%Y %H:%M:%S")

    return formatted_date


def format_repo_name(repo_name: str, username: str) -> str:
    if '/' not in repo_name:
        return repo_name
    parts = repo_name.split('/')
    owner, repo = parts
    if owner.lower() == username.lower():
        return repo
    return repo_name


def search_activity(username: str):
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise ValueError("Error to access the account")
    events = response.json()
    print(f"Recent activity of {username}: ")
    for event in events[:5]:
        event_type = event["type"]
        description = GITHUB_EVENT_TYPES.get(
            event_type, f"❓ Unknown event: {event_type}")
        event_repo = format_repo_name(event["repo"]["name"], username)
        event_data = format_date(event["created_at"])
        print(f"- {description} → {event_repo} at {event_data}")


def main():
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description=("A simple command line interface (CLI) to fetch the"
                     " recent activity of a GitHub user"))

    parser.add_argument("username", help="Account username to be tracked")
    args = parser.parse_args()

    search_activity(args.username)


if __name__ == '__main__':
    main()
