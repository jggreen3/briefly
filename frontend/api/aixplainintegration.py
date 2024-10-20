import os
import dotenv

from aixplain.factories import AgentFactory
from aixplain.modules.agent import ModelTool

# Create the summarizer agent


dotenv.load_dotenv()

agent = AgentFactory.get("67156bd357c705a318033bbd")

# Define the dataset with emails
# query_2 = [
#     # Slack messages
#     {'source': 'slack', 'sender': 'U07SNHXJYAF', 'body': '<@U07SNHXJYAF> has joined the channel', 'date': '1729449213.850119'},
#     {'source': 'slack', 'sender': 'U07SH6LU9AA', 'body': 'Hey <@U07SNHNAG3D>,\nPlease complete your onboarding by tomorrow!', 'date': '1729446667.200089'},
#     {'source': 'slack', 'sender': 'U07SH6LU9AA', 'body': '<@U07SH6LU9AA> has joined the channel', 'date': '1729446606.451809'},
#     {'source': 'slack', 'sender': 'U07SNHXJYAF', 'body': '<@U07SNHXJYAF> has joined the channel', 'date': '1729449220.338859'},
#     {'source': 'slack', 'sender': 'U07SH6LU9AA', 'body': '<@U07SH6LU9AA> has joined the channel', 'date': '1729446606.383059'},
#     {'source': 'slack', 'sender': 'U07SNHNAG3D', 'body': '<@U07SNHNAG3D> has joined the channel', 'date': '1729387376.300799'},
#     {'source': 'slack', 'sender': 'U07SNHXJYAF', 'body': '<@U07SNHXJYAF> has joined the channel', 'date': '1729449203.434749'},
#     {'source': 'slack', 'sender': 'U07SH6LU9AA', 'body': '<@U07SH6LU9AA> has joined the channel', 'date': '1729446606.291449'},
#     {'source': 'slack', 'sender': 'U07SNHNAG3D', 'body': '<@U07SNHNAG3D> has joined the channel', 'date': '1729387376.067899'},
    
#     # Canvas task
#     {
#         "source": "Canvas",
#         "name": "Weekly Email 1",
#         "description": (
#             "Send an email with the title “MSDS Practicum Weekly Report- Practicum Name” (The Practicum Name is "
#             "the same as this slack channel name) and with the same content of the weekly report to Shan, Victor, "
#             "your faculty mentor, and all your company mentors. If you are not sure which company personnel you should "
#             "include on the email, confirm with the company mentor you work directly with. This is a group assignment. "
#             "Only one person needs to send this email. Nothing needs to be done on Canvas. I will give you points when "
#             "receiving your email."
#         ),
#         "due_at": "2024-10-21T06:59:59Z",
#         "course_id": 1621853,
#         "html_url": "https://usfca.instructure.com/courses/1621853/assignments/7479341"
#     },
    
#     # Emails from Ricky Miura
#     {'source': 'ts.test.personal@gmail.com', 'date': '1729457711000', 'sender': 'Ricky Miura <rickymiura525@gmail.com>', 'body': 'This is a reminder to renew your subscription!'},
#     {'source': 'ts.test.work@gmail.com', 'date': '1729457755000', 'sender': 'Ricky Miura <rickymiura525@gmail.com>', 'body': 'VERY URGENT!!!!\r\nALL HANDS ON DECK MEETING TOMORROW!\r\n'},
#     {'source': 'ts.test.school@gmail.com', 'date': '1729457801000', 'sender': 'Ricky Miura <rickymiura525@gmail.com>', 'body': 'Hey User,\r\nPlease register for classes by the end of this week!\r\n'}
# ]


# Run the agent with the dataset
# agent_response = agent.run(
#     query=f"Given the following data, summarize them into a numbered list of tasks to complete that are brief and concise but still capture all of the original context, only create tasks if there is an actionable item, also state which source and sender it comes from: {query_2}"
# )
# # Output the response from the agent
# print(agent_response)


def get_agent1_response(messages_and_assignments:str):
    input_query = f"Given the following data, summarize them into a numbered list of tasks to complete that are brief and concise but still capture all of the original context, only create tasks if there is an actionable item, also state which source and sender it comes from: {messages_and_assignments}"
    agent_response = agent.run(query=input_query)
    return agent_response['data']['output']