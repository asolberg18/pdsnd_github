"""
This program analyzes rideshare data for several cities and
interactively displays important summary statistics.

Developed by Amber Solberg
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n").lower()
        if city not in CITY_DATA:
            print("Sorry, please enter one of the three available city options (case sensitive): New York City, Chicago, or Washington. Please try again.")
            continue
        else:
            break

    print("Your city of choice was: {}".format(city))

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWould you like to filter by month? The available options are months: January, February, March, April, May, and June.\nOtherwise, type 'all' if you do not want to filter by month.\n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Sorry, please enter one of the following selections: January, February, March, April, May, June, or all")
            continue
        else:
            break

    print("Your month of choice was: {}".format(month))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWould you like to filter by day? If so, please enter either: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday.\nOtherwise, type 'all' if you do not want to filter by day.\n").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Sorry, please enter one of the following options: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all")
            continue
        else:
            break

    print("Your day of choice was: {}".format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        # Load in data file
        df = pd.read_csv(CITY_DATA[city])

        # convert the Start Time column and End Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])

        # Extract month and day of week from Start Time columns to create new columns to filter by
        df['month'] = df['Start Time'].dt.month
        df['weekday'] = df['Start Time'].dt.weekday_name

        # Extract hour from Start Time column to create new hour column to filter by later in time_stats function
        df['hour'] = df['Start Time'].dt.hour

        # Filter by month based on user input selections
        if month != 'all':
            # Use index of month list to grab corresponding integer
            month_list = ['january', 'february', 'march', 'april', 'may', 'june']
            month = month_list.index(month) + 1

            # Filter by month
            df = df[df['month'] == month]

        # Filter by day of week based on user input selections
        if day != 'all':
            df = df[df['weekday'] == day.title()]

        return df

    except Exception as e:
        print("Couldn't load in the file. The following error occured: {}".format(e))


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most frequently traveled month: {}".format(popular_month))

    # display the most common day of week
    popular_day = df['weekday'].mode()[0]
    print("Most frequently traveled day of the week: {}".format(popular_day))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour: {}".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(end_station))

    # display most frequent combination of start station and end station trip
    df['trip_combo'] = df['Start Station']+ " " + df['End Station']
    popular_trip = df['trip_combo'].mode()[0]
    print("The most popular combined trip is: {}".format(popular_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    total_days = total_travel_time/86400
    print("Total travel time: {} Days".format(total_days))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_minutes = mean_travel_time/60
    print("Mean travel time: {} minutes".format(mean_minutes))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("Here are the counts of various user types: {}".format(user_type))


    if city != 'washington':
        # Display counts of gender
        gender_types = df['Gender'].value_counts()
        print("Here are the counts of users by gender: {}".format(gender_types))

        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("The earliest birth year is: {}".format(earliest_year))

        recent_year = df['Birth Year'].max()
        print("The most recent birth year is: {}".format(recent_year))

        common_year = df['Birth Year'].mode()[0]
        print("The most common birth year is: {}".format(common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, start):
    """Displays five lines of data if the user specifies they want to."""
    display = input("\nWould you like to view individual trip data? Type 'yes' or 'no'.\n").lower()
    if display == 'yes':
        print(df.iloc[start:start+5])
        start += 5
        return display_data(df, start)
    if display == 'no':
        return
    else:
        print("I'm sorry I didn't catch that. Please enter 'yes' or 'no'.")
        return display_data(df, start)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
