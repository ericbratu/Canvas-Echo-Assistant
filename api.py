import requests
import json
from datetime import datetime, timedelta

headers = {"Authorization": "Bearer " + "<INPUT CANVAS API KEY HERE!>"}

response = requests.get('<INPUT URL REQUEST HERE!>', headers=headers)

# Parse the JSON response
assignments = response.json()

# Extract, adjust, and print the 'due_at' values
for assignment in assignments:
    if 'due_at' in assignment:
        due_at_str = assignment['due_at'][:10]
        due_at_date = datetime.strptime(due_at_str, '%Y-%m-%d')
        adjusted_date = due_at_date - timedelta(days=1)
        print(adjusted_date.strftime('%Y-%m-%d'))
