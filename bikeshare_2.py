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
    while True :
            city = input('Which city would you like to explore chicago, new york city, or washington?').lower()
            if city not in ('new york city', 'chicago', 'washington'):
                print("--------------invaild input try again--------------")
                continue
            else:
                break
    

    # get user input for month (all, january, february, ... , june)
    while True:
            month = input('which month would you like to explore? january, february, march, april, may, june, or all?').lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                print("--------------invaild input try again--------------")
                continue
            else:
                break        

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            day = input('which day of the week do you want to explore? Or, Do you want all days?').lower()
            if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
                print("--------------invaild input try again--------------")
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0] 
    print('\nMost common month: {}'.format(most_common_month))

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day_name()
    most_common_day = df['day'].mode()[0]
    print('\nMost common day: {}'.format(most_common_day))

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\nMost common hour: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df["Start Station"].mode()[0]
    print('\nMost commonly used start station: {}'.format(most_commonly_used_start_station))


    # display most commonly used end station
    most_commonly_used_end_station = df["End Station"].mode()[0]
    print('\nMost commonly used end station: {}'.format(most_commonly_used_end_station))


    # display most frequent combination of start station and end station trip
    most_frequent_combination_of_start_station_and_end_station_trip = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\nMost frequent combination of start station and end station trip: {}'.format(most_frequent_combination_of_start_station_and_end_station_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time: {}'.format(total_travel_time))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('\nCounts of user types:\n {}'.format(counts_of_user_types))

    # Display counts of gender
    if  'Gender' not in df :
        print('Sorry, No gender data is available.')
    else:
        counts_of_gender = df['Gender'].value_counts()
        print('\nCounts of gender: {}'.format(counts_of_gender))
        
       
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Sorry, No birth year data is available.')
    else:
        earliest_year_of_birth = df['Birth Year'].min()
        print('\nEarliest year of birth: {}'.format(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print('\nMost recent year of birth: {}'.format(most_recent_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('\nMost common year of birth: {}'.format(most_common_year_of_birth))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    
    
def view_data(df):
    start = 0
    choice = input('\nDo you want to view the data? Enter yes or no.\n').lower()
    while choice == 'yes':
        try:
            n = int(input('Enter the number of rows to view\n'))
            n = start + n
            print(df[start:n])
            choice = input('More rows? Enter yes or no.\n').lower()
            start = n

        except ValueError:
            print('Enter appropriate integer value')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
