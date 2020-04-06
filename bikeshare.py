import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

#created dictionary and lists for month and weeks to simplify verifying if
#user inputted correct values and for while loop in load data function
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6}
month_list = list(months.keys())
week = {'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5,'sun':6}
day_list = list(week.keys())

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no\
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply\
        no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use \
    #a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city?  '\
        'Please enter Chicago, New York or Washington?: ')
        if city.lower() in ["chicago","new york","washington"]:
            break
        else:
            print('Sorry, that\'s not an option. Please check spelling.')

    # get user input for month (all, january, february, ... , june)
    #a while loop to handle invalid inputs
    while True:
        month = input('\nWhich month do you want data for?\n'\
        'Please enter All, Jan, Feb, Mar, Apr, May or Jun: ')
        if (month.lower() in months or month.lower() =='all'):
            break
        else:
            print('    Sorry, please enter a month between Jan-Jun or \"all".')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # while loop to handle invalid inputs
    while True:
        day = input('\nWhich weekday do you want data for?\n'\
        'Please enter All, Mon, Tue, Wed, Thu, Fri, Sat or Sun: ')
        if (day.lower() in day_list or day.lower() =='all'):
            break
        else:
            print('    Sorry, please enter a day of the week or \"all".')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if \
    applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no \
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply no\
        day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #loaded correct csv into panda DataFrame and converted time to_datetime
    #strip month, day and hour from Start Time into separate columns
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.weekday
    df['Hour'] = df['Start Time'].dt.hour

    #all is not in month_list or day_list so if user inputs all, will skip
    #past both if statements and no filters are applied:
    if month in month_list:
        df = df[df['Month']==months[month]]

    if day in day_list:
        df = df[df['Day_of_week']==week[day]]

    #print sample to show output of loading data
    print('SAMPLE OUTPUT OF DATA FRAME')

    #had to use a conditional statement since washington does not have "Gender"
    #and "Birth Year" columns.  I did not show all columns just for visual.
    #This is purely for user experience.  Raw input option comes later that
    #displays everything.
    if city.lower() == 'washington':
        print('\n',df[['Start Time','End Time', 'Trip Duration', 'User Type',
         'Month', 'Day_of_week']].head())
    else:
        print('\n',df[['Start Time','End Time', 'Trip Duration', 'User Type',
        'Gender','Birth Year', 'Month', 'Day_of_week']].head())

    print('\nYou are viewing data from: city: {}, month: {}, day: {}'.format(
    city.title(), month.title(), day.title()))
    print('-'*40)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('-'*40)
    print('POPULAR TRAVEL TIME STATISTICS\n')
    start_time = time.time()

    # display the most common month
    # count unique values of month coln and rtn index instead of count value
    most_month = df['Month'].value_counts().idxmax()
    print('Most frequent travel month: {}'.format(
    month_list[most_month-1].title()))

    # display the most common day of week
    # count unique values of Day_of_week coln and rtn index instead
    most_day = df['Day_of_week'].value_counts().idxmax()
    print('Most frequent travel day: {}'.format(day_list[most_day].title()))

    # display the most common start hour
    # count unique values of hour coln and rtn index instead of count value
    most_hour = df['Hour'].value_counts().idxmax()

    # In order to display AM and PM, I added this conditional to print AM for
    # values less than 12 and for over 13, subtract 12 for PM.
    if most_hour < 13:
        print('Most frequent travel hour: {}pm'.format(most_hour-12))
    else:
        print('Most frequent travel hour: {}am'.format(most_hour))

    print("\nCalculation time: %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('-'*40)
    print('POPULAR STATION AND TRIP STATISTICS\n')
    start_time = time.time()

    # display most commonly used start station
    # comment below was code used to check actual value counts in order to
    # make sure answer made sense.  See this mirrored for next two as well.
    #print(df['Start Station'].value_counts(),'\n')

    # used .idxmax() to return index of max in value count output.
    most_start_stn = df['Start Station'].value_counts().idxmax()
    print('Most common start station: {}'.format(most_start_stn))

    # display most commonly used end station
    #print(df['End Station'].value_counts(),'\n')

    most_end_stn = df['End Station'].value_counts().idxmax()
    print('Most common end station: {}'.format(most_end_stn))

    # display most frequent combination of start station and end station trip
    # created column called "Route" to have all different type of routes
    # since most popular start and end stations may not be the most freq. route
    df['Route'] = df['Start Station'] + ' to ' + df['End Station']
    #print(df['Route'].value_counts(),'\n')

    most_route = df['Route'].value_counts().idxmax()
    print('Most frequent start-end route: {}'.format(most_route))

    print("\nCalculation time: %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('-'*40)
    print('TRIP DURATION STATISTICS\n')
    start_time = time.time()

    # display total travel time
    # sum column "Trip Duration" and convert to hrs/min/sec
    total_time=df['Trip Duration'].sum()
    print('In the month(s) and day(s) you selected, breakdown is:\n'\
    'Total time users traveled on bikes: {} (hrs:min:sec).'.format(str(
    datetime.timedelta(seconds=int(total_time)))))
    print('({} total seconds)\n'.format(total_time))

    # display mean travel time
    #  average column "Trip Duration" and convert to hrs/mins/sec
    avg_time=df['Trip Duration'].mean()
    print('Average time users traveled on bikes: {} (hrs:min:sec).'.format(str(
    datetime.timedelta(seconds=float(avg_time)))))
    print('({} total seconds)'.format(avg_time))

    print("\nCalculation time: %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('-'*40)
    print('USER INFO STATISTICS\n')
    start_time = time.time()

    # Display counts of user types
    print('In the month(s) and day(s) you selected, breakdown is:\n\n'
    'User Types:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    # since Washington does not have gender or birth year data, this
    # conditional statement was used to only run calculations for other two
    # cities
    if city != 'washington':
        print('\nGenders:')
        print(df['Gender'].value_counts())
    else:
        print('\nWashington does not have data on gender or birthdays.')

    # Display earliest, most recent, and most common year of birth
    # same as genders above.  Washington will not run calculations.
    if city.lower() != 'washington':
        earliest_birth=df['Birth Year'].min()
        recent_birth=df['Birth Year'].max()
        most_birth=df['Birth Year'].value_counts().idxmax()

        print('\nBirthday Info:')
        print('Earliest birth year: {}'.format(earliest_birth))
        print('Most recent birth year: {}'.format(recent_birth))
        print('Most common birth year: {}'.format(most_birth))

    print("\nCalculation time: %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays data from DataFrame in increments of 5 lines."""

    print('-'*40)
    print('RAW DATA OUTPUT\n')
    see_more=input('Would you like to see 5 lines of raw data (Y/N)?: \n')

    # declared variables for while loop.
    n = df['Start Time'].count()    # number of rows so max value for 'b'
    a = 0   # lowerbound for df.iloc[] method
    b = 5   # upperbound for df.iloc[] method

    # infinite while loop that is only broken (rtn) if 'yes' is not provided.
    while True:
        if see_more.lower() not in ['y','yes']:
            print('-'*40)
            return
            # loop is broken since 'y' or 'yes' are not selected

        # loop until 'b' is 'n'. Print 5 lines.
        elif b <= n:
            print(df.iloc[a:b])
        # also need to break the while loop if they don't want to see 5 more
        # lines so need "see_more" again.
        see_more=input('\nWould you like to see more (Y/N)?: \n')
        a += 5
        b += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # user option for statistics they want to see.  Options are filters:
        filters = ['time','station','trip duration','user','skip']

        # infinite while loop to make sure value selected by user is in list
        while True:
            filter = input('SELECT STATISTICS TO OUTPUT:\nSelect "time", '\
            '"station", "trip duration", "user" or press "skip": ')

            # match filter value to appropriate function.
            if filter in filters:

                if filter.lower() == 'time':
                    time_stats(df)

                elif filter.lower() == 'station':
                    station_stats(df)

                elif filter.lower() == 'trip duration':
                    trip_duration_stats(df)

                elif filter.lower() == 'user':
                    user_stats(df,city)

                elif filter.lower() == 'skip':
                    break

            else:
                print('\nSorry, that is not a valid option. Check spelling')

        #call raw input function
        display_data(df)

        restart = input('\nWould you like to restart (Y/N)?: ')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
