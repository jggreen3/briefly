import os
import json
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Define the scopes (access permissions) that you request from the user
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_user(token_file, client_secret_file):
    creds = None
    
    # Step 1: Check if the token JSON file already exists for this account
    if os.path.exists(token_file):
        with open(token_file, 'r') as token:
            creds_data = json.load(token)
            creds = Credentials.from_authorized_user_info(creds_data, SCOPES)
    
    # Step 2: If credentials are not valid or the JSON file doesn't exist, start the OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh the token if it's expired
            creds.refresh(Request())
        else:
            # If the JSON file doesn't exist, start the OAuth flow
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Step 3: Save the new credentials to a JSON file for future use
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    # Return the credentials object, which contains access to the Gmail API
    return creds

def get_message(service, user_id, msg_id):
    """Get the message details."""
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        return message
    except Exception as error:
        print(f'An error occurred: {error}')
        return None
    
def get_message_body(payload):
    # If the message is multipart
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                # Extract plain text body
                return part['body']['data']
            elif part['mimeType'] == 'text/html' and 'data' in part['body']:
                # Extract HTML body (you can prefer plain text if needed)
                return part['body']['data']
    else:
        # Non-multipart message, try to get the plain text or HTML body directly
        if payload['mimeType'] == 'text/plain' and 'data' in payload['body']:
            return payload['body']['data']
        elif payload['mimeType'] == 'text/html' and 'data' in payload['body']:
            return payload['body']['data']
    
    # Return empty string if no body found
    return ""

def decode_base64url(encoded_body):
    """Decodes a base64url encoded email body."""
    import base64
    decoded_bytes = base64.urlsafe_b64decode(encoded_body.encode('UTF-8'))
    return decoded_bytes.decode('UTF-8')

def fetch_messages(payload):
    email_body_encoded = get_message_body(payload)
    
    if email_body_encoded:
        email_body = decode_base64url(email_body_encoded)
        return email_body
    else:
        print("No body found for this email.")

def get_all_messages():
    # Path to the client secret file downloaded from Google Cloud Console
    client_secret_file = 'client_secret.json'
    
    # Define a list of users and their respective token files
    users = [
        {"email": "ts.test.personal@gmail.com", "token_file": "token_personal.json"},
        {"email": "ts.test.work@gmail.com", "token_file": "token_work.json"},
        {"email": "ts.test.school@gmail.com", "token_file": "token_school.json"}
        # Add more users as needed
    ]
    
    all_creds = {}
    
    # Authenticate each user
    for user in users:
        email = user['email']
        token_file = user['token_file']
        
        print(f'Authenticating {email}...')
        creds = authenticate_user(token_file, client_secret_file)
        
        # Store the credentials for this user
        all_creds[email] = creds
    
    # Now, you can use the credentials to access Gmail API for each user
    all_messages = {}

    for email, creds in all_creds.items():
        print(f'Fetching messages for {email}...')
        service = build('gmail', 'v1', credentials=creds)
        
        # Do something with the Gmail API, like listing the messages
        query = 'is:unread'
        results = service.users().messages().list(userId='me', q=query, labelIds=['INBOX']).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print(f'No new messages for {email}.')
        else:
            print(f'Found {len(messages)} new messages for {email}.')
            all_messages[email] = [service, messages]
    
    if len(all_messages) == 0:
        print("You're all up to date!")
    
    else:
        messsage_content = []
        for email, content in all_messages.items():
            service = content[0]
            messages = content[1]
            for msg in messages:
                data = {}
                data['source'] = email
                message_data = get_message(service, 'me', msg['id'])
                data['date'] = message_data['internalDate']
                payload = message_data['payload']
                header = payload['headers']
                from_email = next((item for item in header if item['name'] == 'From'), None)['value']
                data['sender'] = from_email
                body = fetch_messages(payload)
                data['body'] = body
                messsage_content.append(data)
        return messsage_content

if __name__ == '__main__':
    get_all_messages()
