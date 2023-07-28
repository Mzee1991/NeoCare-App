
from datetime import datetime, timedelta

def calculate_gestation_age(lmp_date, current_date):
    # Convert the date strings to datetime objects
    lmp_date = datetime.strptime(lmp_date, '%Y-%m-%d')
    current_date = datetime.strptime(current_date, '%Y-%m-%d')

    # Calculate the time difference between the current date and LMP
    time_difference = current_date - lmp_date

    # Calculate the number of weeks and remaining days
    weeks = time_difference.days // 7
    remaining_days = time_difference.days % 7

    return weeks, remaining_days

# Example usage:
lmp_date = '2023-03-10'
current_date = '2023-07-25'
weeks, days = calculate_gestation_age(lmp_date, current_date)

print("Gestation Age: {} weeks and {} days".format(weeks, days))
