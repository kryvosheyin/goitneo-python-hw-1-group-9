from datetime import datetime, timedelta
from collections import defaultdict

def get_upcoming_birthdays(users):

    today = datetime.now().date()
    next_week_date = today + timedelta(days=7)

    upcoming_birthdays = defaultdict(list)
    
    for user in users:
        birthday_this_year = user['birthday'].replace(year=today.year).date()
        upcoming_date = birthday_this_year if birthday_this_year >= today else user['birthday'].replace(year=today.year+1).date()

        if upcoming_date.weekday() >= 5: 
            upcoming_date += timedelta(days=(7 - upcoming_date.weekday()))

        if today < upcoming_date <= next_week_date:
            upcoming_birthdays[upcoming_date].append(user['name'])

    sorted_days = sorted(upcoming_birthdays)

    if len(upcoming_birthdays)==0:
        print("There are no upcoming birthdays within next week time period")

    for day in sorted_days:
        if day in upcoming_birthdays:
            print(f"{day.strftime('%A')}: {', '.join(upcoming_birthdays[day])}")


users = [{'name': 'Michael Sims', 'birthday': datetime(1922, 10, 13)},
          {'name': 'John Bautista', 'birthday': datetime(1994, 10, 14)}, 
          {'name': 'Aaron Blake', 'birthday': datetime(1959, 4, 3)}, 
          {'name': 'Louis Flores', 'birthday': datetime(1931, 10, 19)}, 
          {'name': 'Patricia Perez', 'birthday': datetime(1971, 11, 13)}, 
          {'name': 'Cynthia Lang', 'birthday': datetime(1997, 10, 20)}, 
          {'name': 'Alicia Ramirez', 'birthday': datetime(1974, 11, 20)}, 
          {'name': 'Sandra Myers', 'birthday': datetime(1910, 2, 11)}, 
          {'name': 'Mary Morris', 'birthday': datetime(2020, 10, 20)}, 
          {'name': 'Brendan Mathews', 'birthday': datetime(1939, 11, 24)}]

get_upcoming_birthdays(users)