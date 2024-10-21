import requests
import json

# Define the API endpoint
url = "https://api.sambanova.ai/v1/chat/completions"

# Your API key
api_key = "82690c99-3085-4848-a67c-77792dc02fff"

# Define the headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# # list of strings
# # Define the payload
# data = {
#     "model": "Meta-Llama-3.1-405B-Instruct",
#     "messages": [
#         # {"role": "system", "content": "give me a positive quote"},
#         {"role": "user", "content": \
#         '''You are an assistant who prioritizes tasks. Here are your tasks:

#         1. Attend the urgent all hands on deck meeting now (Source: Gmail, Sender: Ricky Miura) - This task is marked as "urgent" and requires immediate attention.
#         2. Complete onboarding by tomorrow (Source: Slack, Sender: U07SH6LU9AA) - This task has a deadline of tomorrow, making it a high-priority task.
#         3. Register for classes by the end of this week (Source: Gmail, Sender: Ricky Miura) - This task has a deadline of the end of the week, making it a medium-priority task.
#         4. Send an email titled 'MSDS Practicum Weekly Report- Practicum Name' to Shan, Victor, your faculty mentor, and all company mentors by 2024-10-21 (Source: Canvas) - This task has a specific deadline, but it's further away compared to the other tasks, making it a lower-priority task.
#         5. Renew your subscription (Source: Gmail, Sender: Ricky Miura) - This task does not have a specified deadline, making it the lowest-priority task.
        
#         Rank these tasks in order of priority and give me the list in order of highest to lowest priority. Return only the full list of all tasks.'''}
#     ],
#     "stop": ["<|eot_id|>"],
#     "max_tokens": 1000,
#     "temperature": 0.1,
#     "top_p": 0.1,
#     "top_k": 50
# }

def get_response(agent1_output):
    data = {
    "model": "Meta-Llama-3.1-405B-Instruct",
    "messages": [
        # {"role": "system", "content": "give me a positive quote"},
        {"role": "user", "content": \
        f'''You are an assistant who prioritizes tasks. Here are your tasks:

        {agent1_output}
        
        Rank these tasks in order of priority and give me the list in order of highest to lowest priority. Return only the full list of all tasks in the form of a bulleted HTML list.'''}
    ],
    "stop": ["<|eot_id|>"],
    "max_tokens": 1000,
    "temperature": 0.1,
    "top_p": 0.1,
    "top_k": 50
    }
    response = requests.post(url, headers=headers, data=json.dumps(data)).json()
    content = response['choices'][0]['message']['content']
    return content



# Make the API request
# response = requests.post(url, headers=headers, data=json.dumps(data)).json()
# content = message_content = response['choices'][0]['message']['content']

# print(content)

'''
{"choices":[{"finish_reason":"stop","index":0,"logprobs":null,"message":{"content":"\"Believe you can and you're halfway there.\" - Theodore Roosevelt","role":"assistant"}}],"created":1729462012,"id":"06d8e77f-0304-45af-98b5-5c44aa780d17","model":"Meta-Llama-3.1-405B-Instruct","object":"chat.completion","system_fingerprint":"fastcoe","usage":{"acceptance_rate":9.5,"completion_tokens":15,"completion_tokens_after_first_per_sec":113.49957959722515,"completion_tokens_after_first_per_sec_first_ten":235.60719016083254,"completion_tokens_per_sec":36.79096607473624,"end_time":1729462013.4083827,"is_last_response":true,"prompt_tokens":40,"start_time":1729462012.9409907,"time_to_first_token":0.344043493270874,"total_latency":0.40770878289875234,"total_tokens":55,"total_tokens_per_sec":134.90020894069954}}
'''