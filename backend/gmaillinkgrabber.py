import json
import time
import sys
import os
import os.path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from google.oauth2 import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def gmail_authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return creds

def search_messages(service, query):
    query += " newer_than:1d"
    result = service.users().messages().list(userId='me', q=query).execute()
    return result.get('messages', [])

def get_message(service, msg.id):
    message = service.users().messages().get(userId='me', id=msg.id, format='raw').execute()
    return message['raw']

def main():
    service = gmail_authenticate()
    messages = search_messages(service, "subject:Amazon")
    for msg in messages:
        print(get_message(service, msg['id']))

if __name__ == "__main__":
    main()
