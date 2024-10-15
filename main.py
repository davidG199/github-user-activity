import pprint

import requests
print("github user CLI")
username = input("Ingresa el nombre del usuario\n")


def fetchUserActivity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        activity = response.json()
        latest_activy = activity
        print("---------------")
        for activity in latest_activy:
            if activity["type"] == "IssueCommentEvent":
                print(f"-- Commented on issue {activity['payload']['issue']['number']}")
            elif activity["type"] == "PushEvent":
                commit_count = len(activity['payload']['commits'])
                print(f"-- Pushed {commit_count} commits to {activity['repo']['name']}")
            elif activity["type"] == "IssuesEvent":
                print(f"-- Opened a new issue in {activity['payload']['issue']['number']}")
            elif activity["type"] == "WatchEvent":
                print(f"-- Starred {activity['repo']['name']}")
            elif activity["type"] == "PullRequestEvent":
                print(f"-- Created pull request {activity['payload']['pull_request']['number']}")
            elif activity["type"] == "PullRequestReviewEvent":
                print(f"-- reviewed pull request {activity['payload']['pull_request']['number']}")
            elif activity["type"] == "PullRequestReviewCommentEvent":
                print(f"-- commented on pull request {activity['payload']['pull_request']['number']}")
            elif activity["type"] == "CreateEvent":
                print(f"-- created {activity['payload']['ref_type']} {activity['payload']['ref']}")
            else:
                print(f"-- {activity['type']}")
    else:
        print(f"Error fetching events for {username}: {response.status_code}")


fetchUserActivity(username)
