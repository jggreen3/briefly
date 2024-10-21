import os

from aixplain.factories import AgentFactory
from aixplain.modules.agent import ModelTool
from api.canvas import get_all_assignments
from api.slack import Slack
from api.gmail import get_all_messages

# Create the summarizer agent

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
#     {'source': 'ts.test.work@gmail.com', 'date': '1729457755000', 'sender': 'Ricky Miura <rickymiura525@gmail.com>', 'body': 'VERY URGENT!!!!\r\nALL HANDS ON DECK MEETING NOW!\r\n'},
#     {'source': 'ts.test.school@gmail.com', 'date': '1729457801000', 'sender': 'Ricky Miura <rickymiura525@gmail.com>', 'body': 'Hey User,\r\nPlease register for classes by the end of this week!\r\n'}
# ]


# Initialize lists to hold tasks by source
canvas_tasks = []
slack_tasks = []
email_tasks = []

# Function to run the agent
def run_agent(data, model_name):
    return agent.run(
        query=f"Given the following data, summarize them into a numbered list of tasks to complete that are brief and concise but still capture all of the original context, only create tasks if there is an actionable item, also state which source and sender it comes from: {data}"
    )

def get_llm_response():
    canvas_messages = get_all_assignments()
    print(canvas_messages)

    canvas_response = run_agent(canvas_messages, "Canvas_Model")
    canvas_todo_list = canvas_response["data"]["output"]

    s = Slack()
    slack_messages = s.get_all_recent_messages()

    slack_response = run_agent(slack_messages, "Slack_Model")
    slack_todo_list = slack_response["data"]["output"]

    gmail_messages = get_all_messages()

    email_response = run_agent(gmail_messages, "Gmail_Model")
    email_todo_list = email_response["data"]["output"]

    return canvas_todo_list, slack_todo_list, email_todo_list

# Run the respective LLMs for each source
# if canvas_tasks:
#     canvas_response = run_agent(canvas_tasks, "Canvas_Model")
#     canvas_todo_list = canvas_response["data"]["output"]
# else:
#     canvas_todo_list = []

# if slack_tasks:
#     slack_response = run_agent(slack_tasks, "Slack_Model")
#     slack_todo_list = slack_response["data"]["output"]
# else:
#     slack_todo_list = []

# if email_tasks:
#     email_response = run_agent(email_tasks, "Email_Model")
#     email_todo_list = email_response["data"]["output"]
# else:
#     email_todo_list = []

# # Output the lists
# print("Canvas Tasks:")
# print(canvas_todo_list)

# print("\nSlack Tasks:")
# print(slack_todo_list)

# print("\nEmail Tasks:")
# print(email_todo_list)