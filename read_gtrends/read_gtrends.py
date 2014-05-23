import pandas as pand
from dateutil import parser, rrule

def read_gtrends(report_file):
    """Read google trends CSV file and return TimeSeries object"""
    f = open(report_file, 'r')
    thisLine = f.readline()
    startData = False

    dates_array = []
    interest_array = []

    while (thisLine != ''):
        # scan until beginning of data
        if (not startData and thisLine.startswith('Interest over time')):
            startData = True
            f.readline()
            thisLine = f.readline()
            continue

        # begin reading data
        if (startData):
            try:
                date_str, interest_str = thisLine.split(',')
                date1_str, date2_str = date_str.split(' - ')
                date_range = list(rrule.rrule(rrule.DAILY, dtstart=parser.parse(date1_str), until=parser.parse(date2_str)))
                interest_val = int(interest_str)
            except ValueError:
                break
            dates_array.extend(date_range)
            interest_array.extend([interest_val] * len(date_range))

        thisLine = f.readline()

    f.close()

    return pand.Series(interest_array, index=dates_array)