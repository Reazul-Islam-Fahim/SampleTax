from datetime import datetime

def calculate_age(dob: str) -> int:
    # Convert the dob string to a datetime object (assuming the format is 'YYYY-MM-DD')
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    
    # Get today's date
    today = datetime.today()
    
    # Calculate age
    age = today.year - dob_date.year
    
    # Adjust if the birthday hasn't occurred yet this year
    if today.month < dob_date.month or (today.month == dob_date.month and today.day < dob_date.day):
        age -= 1
    
    return age

