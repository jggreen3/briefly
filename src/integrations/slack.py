
import os
import logging
import dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack():
    
    def __init__(self):
        dotenv.load_dotenv()

        self.client = WebClient(os.getenv('oath_token'))
        self.conversations = self.get_conversations()
        self.start_timestamp = 1129449220

    
    def get_conversations(self):
        try:
            response = self.client.conversations_list(types="public_channel,private_channel,im")
            return response['channels']
        except SlackApiError as e:
            raise f'Error fetching conversations: {e.response["error"]}'
        
    def get_recent_messages(self, channel_id: str):
        try:
            response = self.client.conversations_history(channel=channel_id, limit=100)
            messages = response['messages']
            
            recent_messages = []
            for msg in messages:
                if msg['type'] == 'message' and float(msg['ts']) > self.start_timestamp:
                    recent_messages.append({'source': 'slack',
                                            'sender': msg['user'],  
                                            'body': msg['text'],
                                            'date': msg['ts']})
            return recent_messages if len(recent_messages) > 0 else None
        except SlackApiError as e:
            print(f"Error fetching messages from channel {channel_id}: {e.response['error']}")
        
    def get_all_recent_messages(self):
        all_messages = []
        for conv in self.conversations:
            unread_messages = self.get_recent_messages(conv['id'])     
            if unread_messages:
                all_messages.extend(unread_messages)  
        return all_messages
            

def main():
    slack = Slack()
    messages = slack.get_all_recent_messages()
    print(messages)
    
    # convs = slack.get_conversations()
    # print(convs)



if __name__ == "__main__":
    main()




                
        