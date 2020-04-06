### 05 Apr 2020

### US Bikeshare Data Analysis Project - Sugumar Prabhakaran

### Description
This python script calculates various statistics and produces raw output from a US Bikeshare company based in three cities: Chicago, New York city and Washington.

The program is split into different areas:

1. **Receive Input.**  User input is received to identify which city (Chicago, NY or Washington) to look at as well as which months and days of the week to filter.

2. **Load Data.**  Once this info is received the appropriate city data .csv file is loaded into a pandas DataFrame and filtered according to the month and day of week from user.

3. **Calculate Statistics.**  Next, the program asks if the user wants one of four types of statistics calculated and based on this, selects the appropriate function to run.  The four statistics outputted are:

    * **Time statistics.**  to determine most common periods operated;
    * **Station statistics.**  to determine most popular stations and routes;
    * **Duration statistics.**  to determine total and average time on bikes; and
    * **User statistics.**  to determine breakdown by customer, gender, birth year.

4. **Display Raw Output.**  The last section asks if you want to see raw data based on user selected filters and displays this 5 lines at a time until the user wishes to stop.

### Files used

* bikeshare.py
* chicago.csv
* new_york_city.csv
* washington.csv

### Credits
Udacity knowledge section: https://knowledge.udacity.com/.
