# briefly

## Inspiration
As college students, we often found it overwhelming to keep track of communications and assignments across all the different platforms our professors use. With constant deadlines and notifications, it's hard to stay organized, prioritize, and avoid falling behind. We wanted to build a tool that could help students manage everything effortlessly.

## What it does
Briefly automatically summarizes and prioritizes emails, Slack messages, and Canvas assignments for students. It pulls in data from all three platforms, and wraps this all inside a chatbot. Users can ask about their upcoming tasks and deadlines, getting a clear overview of where to focus their attention. 

## How we built it
We pulled information from the Gmail API, Slack API, and Canvas API to pull in real-time data. We used the aiXplain SDK to summarize communications from Gmail and Slack to highlight key information, and SambaNova to prioritize each of the tasks. We built a chatbot that has knowledge of the user's emails, Slack messages, and Canvas assignments.

## Challenges we ran into
One of the biggest challenges we ran into was the size of our inputs to the LLMs. We fixed this by splitting the input into three separate queries for Gmail, Slack, and Canvas, and passed our inputs individually. Another challenge we had was that we were using many new tools we were unfamiliar with, which came with some unexpected challenges of its own.

## Accomplishments that we're proud of
We're proud of deploying a functional student assistant that we hope to use in our everyday lives. We're also proud of the new tools we learned to use in a relatively short amount of time, such as aiexplain and SambaNova. 

## What we learned
During this hackathon, many of us gained further familiarity with tools, such as Git and React. We also learn how to adapt to using new tools for the first time, such as aiXplain and SambaNova.

## What's next for Briefly
In the future, we hope to integrate more student tools, such as Google Calender. We would also like to include options to take actions from the chatbot itself, such as the option to schedule an event on Google Calendar. Lastly, we would like to track completion status of tasks and keep track of tasks over multiple sessions.
