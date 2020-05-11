import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
AVAILABLE_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("\nEnter desired city name to analyse - chicago, new york city or washington?\n")
      if city not in ('chicago', 'new york city', 'washington'):
        print("Sorry, you selected an invalid city.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nEnter month to filter by? all (for all months), january, february, march, april, may, june\n")
      if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        print("Sorry, you selected an invalid month.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nEnter the day of the week you want to filter by: all (for all days), monday, tuesday, wednesday, thursday, friday, saturday, sunday.\n")
      if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print("Sorry, you entered an invalid day of the week.")
        continue
      else:
        break

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


    # Load data file into Pandas DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time column to datetime for easy manipulation
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Get month, day of week and hour from Start Time and create new columns with this data
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # If month selected is not all then filter by the selected month
    if month != 'all':
        month = AVAILABLE_MONTHS.index(month) + 1

    	# create new data with the filtered items
        df = df[df['Month'] == month]

    # If day of the week selected is not all filter by the selected day of the week
    if day != 'all':
        # Create new data from the filtered records
        df = df[df['Day Of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print('The Most Common Month Is:', AVAILABLE_MONTHS[most_common_month - 1])

    # TO DO: display the most common day of week
    most_common_day_of_week = df['Day Of Week'].mode()[0]
    print('The Most Common Day Of The Week Is:', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print('The Most Common Hour Is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].value_counts().idxmax()
    print('The Most Commonly Used Start Station:', most_used_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('\nThe Most Commonly Used End Station Is:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df.groupby(['Start Station', 'End Station']).count()
    print('\nThe Most Commonly Used Combination Of Start Station And End Station Trip Is:', most_used_start_station, " & ", most_common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('The Total Travel Time Is:', total_travel_time/86400, " Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Mean Travel Time Is:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('User Types Counts:\n', user_types_counts)


    # TO DO: Display counts of gender
    try:
        gender_types_counts = df['Gender'].value_counts()
        print('\nGender Types Counts:\n', gender_types_counts)
    except KeyError:
        print("\nGender Types Counts: Data Unavailable.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        print('\nThe Earliest Year Is:', earliest_year_of_birth)
    except KeyError:
        print("\nThe Earliest Year Is: Data Unavailable.")

    try:
        most_recent_year_of_birth = df['Birth Year'].max()
        print('\nThe Most Recent Year Is:', most_recent_year_of_birth)
    except KeyError:
        print("\nThe Most Recent Year Is: Data Unavailable.")

    try:
        most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
        print('\nThe Most Common Year Is:', most_common_year_of_birth)
    except KeyError:
        print("\nThe Most Common Year Is: Data Unavailable.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
