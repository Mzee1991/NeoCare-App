
from datetime import datetime, timedelta

def calculate_delivery_date(lmp_date, current_date):
    # Convert the date strings to datetime objects
    lmp_date = datetime.strptime(lmp_date, '%Y-%m-%d')
    current_date = datetime.strptime(current_date, '%Y-%m-%d')

    # Calculate the time difference between the current date and LMP
    time_difference = current_date - lmp_date

    # Calculate the weeks of amenorrhea
    weeks_of_amenorhea = time_difference.days // 7

    # Calculate the expected date of delivery (40 weeks from LMP)
    expected_delivery_date = lmp_date + timedelta(weeks=40)

    return weeks_of_amenorhea, expected_delivery_date

# Example usage:
lmp_date = '2023-03-10'
current_date = '2023-07-25'
weeks_of_amenorhea, expected_delivery_date = calculate_delivery_date(lmp_date, current_date)

print("Weeks of Amenorrhea:", weeks_of_amenorhea)
print("Expected Date of Delivery:", expected_delivery_date.strftime('%Y-%m-%d'))
