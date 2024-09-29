import requests
from datetime import datetime
import pytz  # For timezone handling

# Authorization header
headers = {
    "Authorization": "Bearer " + "<INSERT YOUR API KEY HERE>"
}

# List of courses and their assignments API URLs
class_urls = [
    ('<INPUT URL REQUEST FOR GET A SINGLE COURSE FOR CLASS 1 UNDER COURSES CATEGORY HERE!>', '<INPUT URL REQUEST FOR LIST ASSIGNMENTS FOR USER FOR CLASS 1 UNDER ASSIGNMENTS CATEGORY HERE!>'),
    ('<INPUT URL REQUEST FOR GET A SINGLE COURSE FOR CLASS 2 UNDER COURSES CATEGORY HERE!>', '<INPUT URL REQUEST FOR LIST ASSIGNMENTS FOR USER FOR CLASS 2 UNDER ASSIGNMENTS CATEGORY HERE!>')
]

def get_assignments_due_today(user_timezone_str='America/New_York'):
    # Get the current date in the user's timezone
    user_timezone = pytz.timezone(user_timezone_str)
    today_date_obj = datetime.now(user_timezone).date()

    assignments_due_today = []

    for class_info_url, class_assignments_url in class_urls:
        # Fetch class info and assignments
        class_info_response = requests.get(class_info_url, headers=headers)
        class_info = class_info_response.json()

        class_assignments_response = requests.get(class_assignments_url, headers=headers)
        class_assignments = class_assignments_response.json()

        # Extract course code
        course_code = class_info.get('course_code', 'Unknown Course')

        for assignment in class_assignments:
            due_date = assignment.get('due_at')
            if due_date:
                # Convert the due date from UTC to the user's local timezone
                utc_due_date = datetime.strptime(due_date, '%Y-%m-%dT%H:%M:%SZ')
                utc_due_date = utc_due_date.replace(tzinfo=pytz.UTC)
                # Convert to local time
                local_due_date = utc_due_date.astimezone(user_timezone).date()
                # Check if the assignment is due today in the user's local time
                if local_due_date == today_date_obj:
                    assignments_due_today.append({
                        'name': assignment.get('name', 'Unnamed Assignment'),
                        'course_code': course_code
                    })

    # Return the assignments that are due today
    return assignments_due_today
    
    