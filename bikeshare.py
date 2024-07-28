import time
import pandas as pd
import numpy as np

CITY_DATA = { 'CHICAGO': 'chicago.csv',
              'NEW YORK CITY': 'new_york_city.csv',
              'WASHINGTON': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['CHICAGO', 'NEW YORK CITY', 'WASHINGTON']
    
    while True:
       city = input("Hi, please enter a city name from following list (Chicago, New York City, Washington): ").upper()
       if city in city_list:
           print(f"Excellent! You have selected a right city name: {city.title()}, great job!!!")
           break
       else:
           print(f"Sorry, wrong input, plase enter a city name in the list again, thank you!!!")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['ALL','JANUARY', 'FEBRARY', 'MARCH', 'APRIL', 'MAY', 'JUNE']
    while True:
        month = input("Which month would you prefer? (All, January, Febrary, March, April, May, June): ").upper()
        if month in month_list:
            print(f"Excellent! You have selected month: {month.title()}, great job!!!")
            break
            return month
        else:
            print(f"Sorry, wrong input, plase enter a month name or 'All' in the list again, thank you!!!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekday_list = ['ALL', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    while True:         
        day = input("Please enter a day of the the week (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").upper()
        if day in weekday_list:
            print(f"Excellent! You have selected a right day of the week: {day.title()}, great job!!!")
            break
            return day
        else:
            print(f"Sorry, wrong input, plase enter aright day of the week or 'All' in the list again, thank you!!!")

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'ALL':
   	 	# use the index of the months list to get the corresponding int
        month_list = ['JANUARY', 'FEBRARY', 'MARCH', 'APRIL', 'MAY', 'JUNE']
        month = month_list.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'ALL':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_common_month = df['month'].mode()[0]
    print(f"The Most Common Month is {most_common_month}")

    # TO DO: display the most common day of week

    most_commom_day_of_week = df['day_of_week'].mode()[0]
    print(f"The Most Common Day of Week is {most_commom_day_of_week}")

    # TO DO: display the most common start hour

    df['most common start hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['most common start hour'].mode()[0]
    print(f"The Most Common Start Hour is {most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station= df['Start Station'] 
    most_commonly_used_start_station = start_station.mode()[0]
    print(f"The Most Commonly used start station is {most_commonly_used_start_station}")

    # TO DO: display most commonly used end station
    end_station= df['End Station']
    most_commonly_used_end_station = end_station.mode()[0]
    print(f"The Most Commonly used end station is {most_commonly_used_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    
    df['Combination Start and end']= start_station+ " Between " + end_station
    start_between_end=df['Combination Start and end']
    most_frequent_between_start_end = start_between_end.mode()[0]
    print(f"The Most Frequent Combination of Start Station and End Station trip is {most_frequent_between_start_end}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()/60
    print(f"The Total Travel Time is {total_travel_time} Minutes")

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()/60
    print(f"The Mean Travel Time is {mean_travel_time} Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('\nThe counts of user types are\n', counts_of_user_types)

    # TO DO: Display counts of gender
    counts_of_gender= df['Gender'].value_counts() 
    print('\nThe counts of gender are\n', counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    # Display the earliest year of birth
    earliest_year_of_birth= int(df['Birth Year'].min())
   
    # Display the most recent year of birth
    most_recent_year_of_birth= int(df['Birth Year'].max())
    
    # Display the most common year of birth
    most_common_year_of_birth= int(df['Birth Year'].mode()[0])
    
    print(f"The earliest year of birth is {earliest_year_of_birth}")
    print(f"The most recent year of birth is {most_recent_year_of_birth}")    
    print(f"The most common year of birth is {most_common_year_of_birth}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_position=0
    step_size=10
    while True:
        selection_contious = input("Would you like to see more five rows of data? Type 'Yes' for continous and 'No' for skip:").upper()
        if selection_contious == 'YES':           
            print(df.iloc[start_position:start_position + step_size])
            start_position += step_size
        elif selection_contious == 'NO':
            break
        else:
            print(f"Sorry, wrong input. Please input 'Yes' or 'No' for right selection.")
                                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()