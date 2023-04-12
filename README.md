# YouTube Comment Deleter

This is a simple Python program that allows you to delete all (owner) comments on a YouTube channel. It uses the YouTube Data API v3 and OAuth2 for authentication. You will need to create a Google Cloud project and enable the YouTube Data API to use this program.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies by running the command `pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client` in your terminal.
3. Download the `client_secret.json` file from your Google Cloud Console and place it in the same directory as `main.py`.
4. Change `CHANNEL_ID` with the desired.
5. Add the desired users to the test user list in the OAuth consent screen.

## Usage

1. Run the program.
2. If it's the first time you do it, it will open a browser and ask you to log in to your Google account and authorize the application to access the YouTube Data API. Once authorized, a `credentials.json` file will be created in the same directory as `main.py`.
3. The program will start deleting all comments on the channel with the ID specified in the `CHANNEL_ID` constant. By default, it will delete 100 comments at a time, wait for 3 seconds, and repeat until all comments are deleted.

## Potential Use Cases

While this program is not particularly useful for most YouTube users, it can be used as a starting point to implement more complex applications, such as a moderating bot that automatically deletes inappropriate comments on a YouTube channel.

To implement a moderating bot, you would need to modify the program to analyze each comment before deciding whether to delete it or not and implement the adequate HTTP request methods.

Please note that the YouTube API doesn't offer the possibility to filter comments by ownership. The best approach to delete all your comments is to use an on-client script that you can run on the browser. I've added a working solution for this to the repository. The server seems to be bottlenecking the process so the timeouts might be incorrect but it does the trick.
