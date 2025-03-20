# Reddit API test task

This script demonstrates how to authenticate with Reddit API using OAuth and fetch the 5 latest posts from a given subreddit.

## Requirements and installation

1. Python 3.6 or higher.
2. Install virtual environment & dependencies:
Please consider to use **only one** of the variants
   - For OS Windows, run `Prepare_venv.bat`
   - For OS Windows, run in terminal
         1. Create a virtual environment
        ```bash
        python3 -m venv .venv
        ```
         2. Activate the virtual environment
        ```bash
        .venv\Scripts\activate
      ```
         3. Install dependencies
        ```bash
        pip install -r requirements.txt
      ```
   - For macOS or Linux
   
      1. Create a virtual environment
   ```bash
     python3 -m venv .venv
   ```
      2. Activate the virtual environment
     ```bash
     source .venv/bin/activate
     ```
      3. Install dependencies
     ```bash
     pip install -r requirements.txt
   ```
   
3. Register an app on [Reddit Developer](https://www.reddit.com/prefs/apps).
   - Use **script** as the type.
   - Fill out the `redirect_uri` (use `http://localhost`).
   - Copy `client_id` and `client_secret` credentials into the `.env` file.

  Your `USER_AGENT` shall describe your app. For example:
   ```
   python-app/0.1 by your_username
   ```
4. Fill out the `api_credentials.env` file in the project root with information from the previous step. Required variables:
   ```
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   USER_AGENT=your_user_agent
   ```

## How to Run
Therere are 2 variations of script.
1. To run the script with `PRAW`, execute in terminal:
```bash
python reddit_api_post_PRAW.py
```
Or use `launch.bat`

2. In order to avoid usage PRAW, please consider to use script with `requests`:
```bash
python reddit_api_auth_with_requests.py
```
## Output Example

The script will display the latest posts from the specified subreddit:
```text
Enter subreddit name: python
Auth Success!

Latest 5 posts from r/python:

Title: How to Use Async Agnostic Decorators in Python
Author: patreon-eng
Upvotes: 8

Title: Playa PDF: A strong pdfminer successor
Author: Goldziher
Upvotes: 3

Title: My discord bot crashes Idk why. I've been working on it 15 hours already, please.
Author: Xeinaplays
Upvotes: 0

Title: Interactive Python Learning Series: From Numbers to Exceptions
Author: Haleshot
Upvotes: 20

Title: Thursday Daily Thread: Python Careers, Courses, and Furthering Education!
Author: AutoModerator
Upvotes: 1


Process finished with exit code 0
```
