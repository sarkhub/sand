
###########################################
#
# datetimeexamples
#
# date time functions
#
###########################################

from datetime import date, time, datetime, timedelta



def main():

    invoice_date = date.today()

    print("invoice date: ", invoice_date)

    invoice_datetime = datetime.now()

    print()

    print("invoice date time ", invoice_datetime)

    print()


    # timespans (timedelta)
    three_weeks = timedelta(weeks=3)
    three_weeks_from_today = date.today() + three_weeks
    print("three weeks from now ", three_weeks_from_today)

    print()
    three_weeks_ago = date.today() - three_weeks
    print("three weeks ago ", three_weeks_ago)
    print()

    # how long until halloween
    halloween = datetime(2019, 10, 31)
    time_span = halloween - datetime.now()

    days = time_span.days
    seconds = time_span.seconds

    print("Halloween is in", days, "days or", seconds, "seconds")
    print()




if __name__ == "__main__":
    main()
