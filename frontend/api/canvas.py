import requests
import json
import re
from api.tokens import API_URL, TOKEN

headers = {
    'Authorization': f'Bearer {TOKEN}'
}

def get_assignments(course_id):
    url = f'{API_URL}{course_id}/assignments'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        assignments = response.json()

        filtered = []

        for assignment in assignments:
            completed = assignment['has_submitted_submissions']

            if not completed:
                cleaned_desc = re.sub(r'<script.*?>.*?</script>', '', assignment['description'], flags=re.DOTALL)
                cleaned_desc = re.sub(r'<link.*?>', '', cleaned_desc)
                cleaned_desc = re.sub(r'<[^>]+>', '', cleaned_desc)
                cleaned_desc = re.sub(r'&nbsp;', ' ', cleaned_desc)
                cleaned_desc = re.sub(r'\s+', ' ', cleaned_desc).strip()

                filt_assign = {
                    'source': 'Canvas',
                    'name': assignment['name'],
                    'description': cleaned_desc,
                    'due_at': assignment['due_at'],
                    'course_id': assignment['course_id'],
                    'html_url': assignment['html_url']
                }
                
                filtered.append(filt_assign)
    else:
        print(f"Failure :c status is {response.status_code}, message {response.text}")

    return filtered

def get_all_assignments():

    courses = [1621853]

    course_assignments = []
    for c in courses:
         assign_json = get_assignments(c)
         course_assignments.append(assign_json)

    return course_assignments

if __name__ == "__main__":
    get_all_assignments()