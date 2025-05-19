def add_time(start: str, duration: str, day: str = None) -> str:
    """
    When adding the duration to the start time, the function will return the new time in 12-hour format with the number of days passed.
    If the start day is provided, the function will also return the new day of the week.
    If its past midnight, the function will return "next day" or the number of days later.
    If its past midnight and the start day is provided, the function will return the new day of the week and "next day" or the number of days later.

    Args:
        start (str): Start time
        duration (str): Duration to add
        day (str): Start day (optional)

    Returns:
        str: New time

    """

    start_time, period = start.split()
    start_hour = int(start_time.split(":")[0])
    start_minute = int(start_time.split(":")[1])
    duration_hour = int(duration.split(":")[0])
    duration_minute = int(duration.split(":")[1])

    # Converting start time to 24-hour format
    # If the period is PM and the hour is not 12, add 12 to convert to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    # If the period is AM and the hour is 12, set the hour to 0 (midnight)
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Calculating the new hour and minute by adding the duration
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Handle minute overflow
    # If the new minute is 60 or more, convert the overflow to hours
    if new_minute >= 60:
        new_hour += new_minute // 60  # Adding the quotient to the hour
        new_minute = new_minute % 60  # Setting the minute to the remainder

    # Handle hour overflow
    # Calculate the number of days passed
    days_later = new_hour // 24
    new_hour = new_hour % 24

    # Convert new time back to 12-hour format
    # Determine the period (AM/PM) based on the new hour
    new_period = "AM" if new_hour < 12 else "PM"
    # If the new hour is 0, set it to 12 (midnight in 12-hour format)
    if new_hour == 0:
        new_hour = 12
    # If the new hour is greater than 12, subtract 12 to convert to 12-hour format
    elif new_hour > 12:
        new_hour -= 12

    # Formatting the new time as a string in 12-hour format with leading zero for minutes
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    days_of_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    # Adding the day of the week if the start day is provided
    if day:
        # Converting the day to lowercase and finding the index in the days_of_week list for case-insensitive comparison
        day_index = days_of_week.index(day.lower().capitalize())
        # Calculating the new day index by adding the number of days passed
        new_day_index = (day_index + days_later) % 7
        # Finding the new day based on the new day index
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Adding next day or the number of days later if the new hour is 24 or more
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


# Test Cases Logs
print(add_time("3:00 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
