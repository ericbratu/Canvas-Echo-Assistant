#CODE WORKS WHEN PLUGGED INTO AMAZON DEVELOPER CONSOLE

import requests
from datetime import datetime, timedelta

headers = {
    "Authorization": "Bearer " + "<INSERT YOUR API KEY HERE>"
}

# Now can handle multiple classes :D
class_urls = [
    ('<INPUT URL REQUEST FOR GET A SINGLE COURSE FOR CLASS 1 UNDER COURSES CATEGORY HERE!>', '<INPUT URL REQUEST FOR LIST ASSIGNMENTS FOR USER FOR CLASS 1 UNDER ASSIGNMENTS CATEGORY HERE!>'),
    ('<INPUT URL REQUEST FOR GET A SINGLE COURSE FOR CLASS 2 UNDER COURSES CATEGORY HERE!>', '<INPUT URL REQUEST FOR LIST ASSIGNMENTS FOR USER FOR CLASS 2 UNDER ASSIGNMENTS CATEGORY HERE!>')
    #REPEAT FOR ALL CLASSES
]

def get_assignments_due_today():
    today_date_str = datetime.now().strftime('%m-%d-%Y')
    today_date_obj = datetime.now().date()
    assignments_due_today = []

    for class_info_url, class_assignments_url in class_urls:
        # Now broader instead of specific to each class.
        class_info_response = requests.get(class_info_url, headers=headers)
        class_info = class_info_response.json()

        # Retrieves class info and respective assignments
        class_assignments_response = requests.get(class_assignments_url, headers=headers)
        class_assignments = class_assignments_response.json()

        # Extract the class code from class info
        course_code = class_info.get('course_code')

        for assignment in class_assignments:
            due_date = assignment.get('due_at')
            if due_date:
                due_date_obj = datetime.strptime(due_date.split('T')[0], '%Y-%m-%d').date()
                adjusted_due_date = due_date_obj - timedelta(days=1)
                #print(f"Found assignment: {assignment.get('name')} due on {adjusted_due_date}") AKA TESTING STATEMEMNT
                if adjusted_due_date == today_date_obj:
                    assignments_due_today.append({
                        'name': assignment.get('name', 'Unnamed Assignment'),
                        'course_code': course_code
                    })

    return assignments_due_today