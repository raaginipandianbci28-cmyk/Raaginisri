from datetime import datetime, timedelta
def date_operations_demo():
    date_str  = "2023-10-25 14:30:00"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print(f"1. String to Date Object: {date_obj}")
    ts1 = datetime(2023, 10, 25, 10, 0, 0)
    ts2 = datetime(2023, 10, 25, 12, 30, 45)
    diff_seconds = (ts2 - ts1).total_seconds()
    print(f"2. Difference in Seconds: {diff_seconds} seconds")
    now = datetime.now()
    weekday_name = now.strftime("%A")
    print(f"3. Current Date/Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   Weekday: {weekday_name}")
    days_to_change = 10
    future_date = date_obj + timedelta(days=days_to_change)
    past_date = date_obj - timedelta(days=days_to_change)
    print(f"4. Original: {date_obj.date()}")
    print(f"   Added {days_to_change} days: {future_date.date()}")
    print(f"   Subtracted {days_to_change} days: {past_date.date()}")
    start_date = datetime(2023, 10, 1).date()
    end_date = datetime(2023, 10, 31).date()
    weekends_count = 0
    current_day = start_date
    while current_day <= end_date:
        if current_day.weekday() >= 5:
            weekends_count += 1
        current_day += timedelta(days=1)
        print(f"5. Weekends between {start_date} and {end_date}: {weekends_count}")
        if __name__ == "__main__":
            date_operations_demo()
