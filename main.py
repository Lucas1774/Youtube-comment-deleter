import os
import time
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CLIENT_SECRETS_FILE = os.path.join(os.path.dirname(__file__), 'service_account.json')
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
load_dotenv()
CHANNEL_ID = os.environ.get("CHANNEL_ID")

def main():
    if os.path.exists('credentials.json'):
        credentials = Credentials.from_authorized_user_file('credentials.json', scopes = SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes = SCOPES)
        credentials = flow.run_local_server(port=0)
        with open('credentials.json', 'w') as token:
            token.write(credentials.to_json())

    youtube = build('youtube', 'v3', credentials=credentials)
    nextPageToken = None

    while True:
        try:
            response = youtube.commentThreads().list(
                part = "id,snippet",
                allThreadsRelatedToChannelId = CHANNEL_ID,
                maxResults = 100,
                textFormat ='plainText',
                pageToken = nextPageToken
            ).execute()
            time.sleep(3)
        except HttpError as error:
            print(f'An error occurred: {error}')
            nextPageToken = None
            time.sleep(3)

        for item in response['items']:
            try:
                comment_id = item['snippet']['topLevelComment']['id']
                print ("comment ID: " + comment_id)
                youtube.comments().delete(id = comment_id).execute()
                time.sleep(3)
            except HttpError as error:
                print(f'An error occurred: {error}')
                time.sleep(3)
                
        nextPageToken = response.get('nextPageToken')
        if not nextPageToken:
            break

if __name__ == '__main__':
    main()
