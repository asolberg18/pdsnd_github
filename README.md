## Overview
This python script is written as part of a series of projects to complete the Programming for Data Science Nanodegree at Udacity. It is used to explore data provided related to the bikeshare systems for three major cities within the United States: Chicago, New York, and Washington. The program imports data from csv files and uses them to compute descriptive statistics from the data. It provides an interactive user experience by taking in raw user input in order to sort and present the statistics to the user.

## How to Run the Script
This program is written in Python 3 and can be run using any up to date version of a Python integrated development environment (IDE). To read the file, the following software requirements apply:
* Python 3 installed
* NumPy, and pandas imported using Anaconda
* A text editor, like Sublime or Atom
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows)

## The Datasets
The datasets for this script contain bikeshare information in Chicago, New York, and Washington. The data is administered by Motivate, a top bike share provider for large cities within the United States. Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

## The Descriptive statistics
The script aims to provide the following information about the bike share data:

* The most popular times of travel: month, day of the week, hour
* The most popular stations and trip: most common start station, end station, and trip from start to end
* The trip duration: total travel time, average travel time
* User information:
    * Counts of each user type
    * Counts of each gender (only available for New York and Chicago)
    * The earliest, most recent, most common year of birth (only available for New York and Chicago)


## The Interactive Experience
The `bikeshare-project.py` file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. There are four questions that will change the answers:
* Would you like to see data for Chicago, New York, or Washington?
* (If they chose month) Which month - January, February, March, April, May, or June?
* (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
