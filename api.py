import requests
import json
from datetime import datetime, timedelta

headers = {"Authorization": "Bearer " + "<INPUT CANVAS API KEY HERE!>"}

class1_info = requests.get('<INPUT URL REQUEST FOR GET A SINGLE COURSE UNDER COURSES CATEGORY HERE!>', headers = headers)
class1_assment = requests.get('<INPUT URL REQUEST FOR LIST ASSIGNMENTS FOR USER UNDER ASSIGNMENTS CATEGORY HERE!>', headers=headers)

# Parse the JSON response
class_info = class1_info.json()
assignments = class1_assment.json()

course_code = class_info.get('course_code')
print(f"{course_code}:")

# Extract, adjust, and print 'due_at' values with 'name'
for assignment in assignments:
        due_at_str = assignment['due_at'][:10]
        due_at_date = datetime.strptime(due_at_str, '%Y-%m-%d')
        adjusted_date = due_at_date - timedelta(days=1) # Date naturally output is wrong by +1 day for some reason, just subtracting one day to get correct due date
        print(f"{assignment['name']}:",adjusted_date.strftime('%Y-%m-%d'),"\n")