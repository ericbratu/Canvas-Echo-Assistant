import requests
import json
from datetime import datetime, timedelta


headers = {"Authorization": "Bearer " + "<INPUT CANVAS API KEY HERE!>"}


# Now can handle multiple classes :D
class_urls = [
    ('<INPUT URL REQUEST FOR GET A SINGLE COURSE UNDER COURSES CATEGORY HERE!>', '<INPUT URL REQUEST FOR LIST ASSIGNMENTS FOR USER UNDER ASSIGNMENTS CATEGORY HERE!>'),
    ('<INPUT URL REQUEST FOR GET A SINGLE COURSE UNDER COURSES CATEGORY HERE!>', '<INPUT URL REQUEST FOR LIST ASSIGNMENTS FOR USER UNDER ASSIGNMENTS CATEGORY HERE!>')
]


for class_info_url, class_assments_url in class_urls:
    # Now broader instead of specific to each class. Retrieves class info and respective assignments
    class_info = requests.get(class_info_url, headers=headers).json()
    class_assments = requests.get(class_assments_url, headers=headers).json()


    # Extract the class code from class info
    course_code = class_info.get('course_code')


    # Print the course code
    print(f"{course_code}:")


# Extract, adjust, and print 'due_at' values with associated assignment title
    for assignment in class_assments:
        if 'due_at' in assignment:
            due_at_str = assignment['due_at'][:10]
            due_at_date = datetime.strptime(due_at_str, '%Y-%m-%d')
            adjusted_date = due_at_date - timedelta(days=1)  # Date naturally output is wrong by +1 day for some reason, just subtracting one day to get correct due date
            print(f"{assignment['name']}:\n{adjusted_date.strftime('%m-%d-%Y')}\n")

