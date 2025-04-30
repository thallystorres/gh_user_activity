# GitHub User Activity Tracker

A simple command-line interface (CLI) tool to fetch and display the recent public activity of a GitHub user.

## Features

- Fetches the latest public events of a GitHub user.
- Displays event types with descriptive icons (e.g., ⭐ for starring a repository).
- Formats repository names and timestamps for better readability.
- Handles unknown event types gracefully.

## Requirements

- Python 3.7 or higher
- Dependencies:
  - `requests`
  - (Optional) `colorama` for colored output

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gh_user_activity.git
   cd gh_user_activity

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Usage

Run the script with the GitHub username as an argument:

```bash
   python github_activity.py <username>
```

For example:

```bash
    python github_activity.py thallystorres
```

This will display the recent public activity of the specified GitHub user.

## Example Output

```bash:
Recent activity of thallystorres: 
- 🆕 Created a branch, tag, or repository → psql-studies at 29/04/2025 21:15:41
- 🆕 Created a branch, tag, or repository → psql-studies at 29/04/2025 21:14:50
- 📦 Pushed commits → django-blog at 27/04/2025 18:39:09
- 📦 Pushed commits → django-blog at 27/04/2025 18:03:54
- 📦 Pushed commits → django-blog at 23/04/2025 20:51:37
```

## Error Handling

- If the GitHub API Is unreachable or the username is invalid, the program will display an error message.
- If the rat limit is exceeded, the program wwill notify the user and suggest trying again later.
