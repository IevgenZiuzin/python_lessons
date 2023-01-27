# Користувач вводить дату та час визначеного формату.
# Використати дату та час у повідомленні, змінивши формат дати,
# як це наведено в прикладі. Перевірити правильність вводу даних та формату користувачем,
# Сповістити в разі помилки.
# input -> 24/02/2001 23:12 Description: need....
# output -> Your message on 24 Feb 2001 at 23:12 oc. can b written
# Your Description: need..

import datetime
import re

template = "dd/mm/yyyy hh:mm Description: "
error_message = "\nWrong message format.\nPlease, follow the template and input correct values."

patterns = [re.compile("\d{2}/\d{2}/\d{4}"),
            re.compile("\d{2}:\d{2}"),
            re.compile("(Description: )")]

date_pattern, time_pattern, description_pattern = patterns


def patterns_check(s):
    flag = True
    for i in patterns:
        if not re.search(i, s):
            flag = False
    return flag


def date_validation(d, mth, y, h, m):
    try:
        user_date = datetime.datetime(y, mth, d, h, m)
        return user_date
    except:
        return False


while True:
    print(f"\n({template}<your description>)")
    user_message = input("Type date, time and description as in template above: ")
    # user_message = "22/07/2022 17:06 Description: Hello, world!"

    if len(user_message) >= len(template) and patterns_check(user_message[:len(template)]):

        check_slice = user_message[:len(template)]
        description = user_message[len(template):]

        date = date_pattern.search(check_slice).group().split("/")
        time = time_pattern.search(check_slice).group().split(":")

        day, month, year = [int(i) for i in date]
        hours, minutes = [int(i) for i in time]

        if date_validation(day, month, year, hours, minutes):

            date = date_validation(day, month, year, hours, minutes)

            print(f"\nYour message was written\non:   {date.strftime('%a %d %b %Y')}\nat:   {date.strftime('%H:%M')}")
            print(f"Description: {description}")

            break
        else:
            print(error_message)
    else:
        print(error_message)
