import requests
import json
from tokens import API_URL, TOKEN

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
                filt_assign = {
                    'source': 'Canvas',
                    'name': assignment['name'],
                    'description': assignment['description'],
                    'due_at': assignment['due_at'],
                    'course_id': assignment['course_id'],
                    'html_url': assignment['html_url']
                }
                
                filtered.append(filt_assign)
    else:
        print(f"Failure :c status is {response.status_code}, message {response.text}")

    return filtered

def main():

    courses = [1621853]

    course_assignments = []
    for c in courses:
         assign_json = get_assignments(c)
         course_assignments.append(assign_json)

    with open('assignments.json', 'w') as f:
        json.dump(course_assignments, f)

if __name__ == "__main__":
    main()