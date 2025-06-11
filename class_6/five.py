employees = [
    {'id': 1, 'name': 'Stephanie Black', 'email': 'stephanieblack@example.com', 'job_title': 'Marketing Specialist', 'department': 'Marketing', 'salary': 61702.34},
    {'id': 2, 'name': 'Travis Watson', 'email': 'traviswatson@example.com', 'job_title': 'Legal Advisor', 'department': 'Legal', 'salary': 87534.28},
    {'id': 3, 'name': 'Rebecca Hunter', 'email': 'rebeccahunter@example.com', 'job_title': 'HR Manager', 'department': 'Human Resources', 'salary': 72214.19},
    {'id': 4, 'name': 'Gregory Mitchell', 'email': 'gregorymitchell@example.com', 'job_title': 'Software Engineer', 'department': 'Engineering', 'salary': 102893.45},
    {'id': 5, 'name': 'Catherine Allen', 'email': 'catherineallen@example.com', 'job_title': 'Account Executive', 'department': 'Sales', 'salary': 68102.56},
    {'id': 6, 'name': 'Dustin Stevens', 'email': 'dustinstevens@example.com', 'job_title': 'Financial Analyst', 'department': 'Finance', 'salary': 84759.23},
    {'id': 7, 'name': 'Andrea Ross', 'email': 'andreaross@example.com', 'job_title': 'Customer Support Rep', 'department': 'Support', 'salary': 49431.77},
    {'id': 8, 'name': 'Samuel Bennett', 'email': 'samuelbennett@example.com', 'job_title': 'Data Analyst', 'department': 'Engineering', 'salary': 76004.19},
    {'id': 9, 'name': 'Laura Rivera', 'email': 'laurarivera@example.com', 'job_title': 'Marketing Specialist', 'department': 'Marketing', 'salary': 62107.52},
    {'id': 10, 'name': 'Kenneth Gray', 'email': 'kennethgray@example.com', 'job_title': 'Operations Manager', 'department': 'Operations', 'salary': 93402.76},
    {'id': 11, 'name': 'Denise Barnes', 'email': 'denisebarnes@example.com', 'job_title': 'Customer Support Rep', 'department': 'Support', 'salary': 51320.12},
    {'id': 12, 'name': 'George Snyder', 'email': 'georgesnyder@example.com', 'job_title': 'Legal Advisor', 'department': 'Legal', 'salary': 89124.67},
    {'id': 13, 'name': 'Janet Cunningham', 'email': 'janetcunningham@example.com', 'job_title': 'Software Engineer', 'department': 'Engineering', 'salary': 99751.13},
    {'id': 14, 'name': 'Brian Daniels', 'email': 'briandaniels@example.com', 'job_title': 'Account Executive', 'department': 'Sales', 'salary': 70123.55},
    {'id': 15, 'name': 'Christina Spencer', 'email': 'christinaspencer@example.com', 'job_title': 'HR Manager', 'department': 'Human Resources', 'salary': 74780.98},
    {'id': 16, 'name': 'Sean Patterson', 'email': 'seanpatterson@example.com', 'job_title': 'Marketing Specialist', 'department': 'Marketing', 'salary': 60982.41},
    {'id': 17, 'name': 'Nicole Hawkins', 'email': 'nicolehawkins@example.com', 'job_title': 'Data Analyst', 'department': 'Engineering', 'salary': 78320.87},
    {'id': 18, 'name': 'Brandon Payne', 'email': 'brandonpayne@example.com', 'job_title': 'Operations Manager', 'department': 'Operations', 'salary': 95001.22},
    {'id': 19, 'name': 'Amy Wallace', 'email': 'amywallace@example.com', 'job_title': 'Customer Support Rep', 'department': 'Support', 'salary': 48765.39},
    {'id': 20, 'name': 'Justin Riley', 'email': 'justinriley@example.com', 'job_title': 'Financial Analyst', 'department': 'Finance', 'salary': 83217.95},
    # ... continued up to 100 entries
]

for emp in employees:
    print(emp['name'], '-',emp['salary'])

users = {1,5,'sd', 3.14, 'hello', 2, 4, 6, 7, 8, 9, 10}
print(type(users))
print(users)