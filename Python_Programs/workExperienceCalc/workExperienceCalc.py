# See tasks.txt to see the purpose of this program
# dates.txt holds the dates that this file calculates

from time import strptime
from datetime import date, datetime, timedelta
from collections import namedtuple
import calendar

def calculateYears(dates):
   
    day_count = 0
    previous_range = None

    for time_period in dates:
        start_date, end_date = time_period.rsplit("-")
        
        start_year, start_month, end_year, end_month = setStartAndEndDates(start_date, end_date)
        #Example results: current_range = (datetime(2010,1,1), datetime(2011,1,1))

        last_month_day = setLastDayInMonth(end_year, end_month)
        current_range = (datetime(start_year,start_month,1), datetime(end_year,end_month,last_month_day))
        current_total_days = (current_range[1]-current_range[0]).days
        #.days is a datetime object that reutrns between 1 and max days of given month of given year
        day_count += current_total_days
        
        if previous_range != None:
            numOfDaysOverlapped = findFalseTime(previous_range, current_range)
            if numOfDaysOverlapped > 0:
                day_count -= numOfDaysOverlapped
            else: 
                next

        #If this date_range is the last of the set, finalize the year calulation.
        if time_period == dates[-1]:
            if day_count >= 364:
                #Using 364 to make sure I catch all "Jan 2000 - Dec 2000" kind of years.
                year_total, leftovers = divmod(day_count, 364)
            else:
                year_total = 0

        previous_range = current_range
    return year_total


#Sets the end_date's day to the last of the month
def setLastDayInMonth(end_year, end_month):
    day_of_week, last_day_in_month = calendar.monthrange(end_year, end_month)
    return last_day_in_month

def findFalseTime(previous_range, current_range):
    #Find overlap and remove it
    Range = namedtuple('Range', ['start', 'end'])
    r1 = Range(start=previous_range[0], end=previous_range[1])
    r2 = Range(start=current_range[0], end=current_range[1])
    latest_start = max(r1.start, r2.start)
    earliest_end = min(r1.end, r2.end)
    overlap = (earliest_end - latest_start).days + 1
    if overlap <= 0:
        return 0
    else:
        return overlap

def setStartAndEndDates(start_date, end_date):
    #Splits into month and year (Ex: Month is "Feb", year is "2004")
    start_month, start_year = start_date.rsplit()
    end_month, end_year = end_date.rsplit()

    #Set months equal to date value
    #Reference: http://www.itmaybeahack.com/book/python-2.6/html/p04/p04c05_time.html
    start_month = strptime(start_month, '%b').tm_mon
    end_month = strptime(end_month, '%b').tm_mon
        
    #Set to decimal value
    start_year = int(start_year)
    end_year = int(end_year)
        
    return [start_year, start_month, end_year, end_month] #Ex: "Feb 2004-Dec 2009" turns into "[2004, 2, 2009, 12]"
        

#To be used in conjuction with month_difference in calculateYears() later.
def totalMonthDifference(end_date, start_date):
    return ((end_date.year - start_date.year)*12 + end_date.month - start_date.month)

def printResults(totals):
    for total in totals:
      print(total) # <---- Final answer / number of full years of work experience

def readFile():
    return [line.rstrip("\n") for line in open("dates.txt")] #Change dates.txt to fit proper file name

def totalYears(persons):
    totals = []
    for person in persons:
        dates = person.split("; ")
        dates = list(set(dates)) # Checks for duplicates
        totals.append(calculateYears(dates))
    return totals

def main():
    #Data file, in this case "dates.txt", is expected to not have any newlines before/after lines of data.
    persons = readFile()
    printResults(totalYears(persons))
main()
