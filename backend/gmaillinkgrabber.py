import json
import time

from google.oauth2 import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def gmail_authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token', SCOPES)
    return creds

def search_messages(service, query):
    result = service.users().messages().list(userId='me').execute()
    return result.get('messages', [])

def get_message(service):
    message = service.users().messages().get(userId='me', format='raw').execute()
    return message['raw']

def main():
    service = gmail_authenticate()
    messages = search_messages(service, "subject:Amazon")
    for msg in messages:
        print(get_message(service))

if __name__ == "__main__":
    main()
