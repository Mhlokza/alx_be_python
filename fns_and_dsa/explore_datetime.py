from datetime import datetime, timedelta
# YYYY-MM-DD HH:MM:SS
def display_current_datetime():
    current_date_and_time = datetime.now()
    current_date = current_date_and_time.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

#YYYY-MM-DD
def calculate_future_date():
    add_days = int(input("enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=add_days)
    return future_date.strftime("%Y-%m-%d")