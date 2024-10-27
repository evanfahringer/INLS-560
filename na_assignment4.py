# Constants for Lifeguard Position
MIN_AGE = 18
MIN_YEARS_LIFEGUARDING = 3

# User's provided data:
age = int(input('Enter your age: '))
lg_experience = int(input('Enter how many years you have been a lifeguard: ')) # any error would be user error in this case.

if age > MIN_AGE and lg_experience > MIN_YEARS_LIFEGUARDING:
    print('You are eligible the Lifeguard Position.')
else:
# Multi-line with f-string
    print(f"""
Sorry, you do not meet the requirements for the Lifeguard Position. 
          
You need at least:
- {MIN_AGE} minimum required age
- {MIN_YEARS_LIFEGUARDING} years as a lifeguard
""")