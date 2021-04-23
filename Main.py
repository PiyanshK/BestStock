# Imports

import calendar
import datetime
import json

# Setting up Data

# Json

with open('/content/SPY.json') as SPY:
  spy_data = json.load(SPY)
with open('/content/AMZN.json') as AMZN:
  amzn_data = json.load(AMZN)
with open('/content/AAPL.json') as AAPL:
  aapl_data = json.load(AAPL)
  
# Code

while True:

    try:
        Starting_date = input(
            'What is your starting date for investment, Between 2000-01-03 and 2021-02-02(YYYY-MM-DD)')

        while True:
            try:
                datetime.datetime.strptime(Starting_date, '%Y-%m-%d')
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                Starting_date = input(
                    'What is your starting date for investment, Between 2000-01-03 and 2021-02-02(YYYY-MM-DD)')
            else:
                break

        Ending_date = input(
            'What is your Ending date for investment Between ' + Starting_date + ' and 2021-02-02(YYYY-MM-DD)')

        while True:
            try:
                datetime.datetime.strptime(Ending_date, '%Y-%m-%d')
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                Ending_date = input(
                    'What is your Ending date for investment Between ' + Starting_date + ' and 2021-02-02(YYYY-MM-DD)')
            else:
                break

        money_invested = input('How much money did you invest?')
        money_invested = int(money_invested.replace('$', ''))


        def daily_average_finder(date, data):
            global daily_average
            date = str(date)
            daily_average = float(data[date]['High']) + float(data[date]['Low']) / 2
            return daily_average


        def profit(startingprice, endingprice, money):
            no_of_shares = money // startingprice
            difference = endingprice - startingprice
            profit = no_of_shares * difference
            return profit


        SPY_starting_average = daily_average_finder(Starting_date, spy_data)
        
        SPY_ending_average = daily_average_finder(Ending_date, spy_data)
        
        AMZN_starting_average = daily_average_finder(Starting_date, amzn_data)
        
        AMZN_ending_average = daily_average_finder(Ending_date, amzn_data)
        
        AAPL_starting_avaerage = daily_average_finder(Starting_date, aapl_data)
        
        AAPL_ending_average = daily_average_finder(Ending_date, aapl_data)
        
        SPY_profit = profit(SPY_starting_average, SPY_ending_average, money_invested)
        
        AAPL_profit = profit(AAPL_starting_avaerage, AAPL_ending_average, money_invested)
        
        AMZN_profit = profit(AMZN_starting_average, AMZN_ending_average, money_invested)

        if SPY_profit > AMZN_profit > AAPL_profit:
            print("The best investment between " + Starting_date + ' and ' + Ending_date + ' would be the S and P 500 (between SPY, AMZN, AAPL)' )
        if SPY_profit > AAPL_profit > AMZN_profit:
            print("The best investment between " + Starting_date + ' and ' + Ending_date + ' would be the S and P 500 (between SPY, AMZN, AAPL)' )
        if AMZN_profit > SPY_profit > AAPL_profit:
            print("The best investment between " + Starting_date + ' and ' + Ending_date + ' would be the Amazon (between SPY, AMZN, AAPL)' )
        if AMZN_profit > AAPL_profit > SPY_profit:
            print("The best investment between " + Starting_date + ' and ' + Ending_date + ' would be the Amazon (between SPY, AMZN, AAPL)' )
        if AAPL_profit > SPY_profit > AMZN_profit:
            print("The best investment between " + Starting_date + ' and ' + Ending_date + ' would be the Apple (between SPY, AMZN, AAPL)' )
        if AAPL_profit > AMZN_profit > SPY_profit:
            print("The best investment between " + Starting_date + ' and ' + Ending_date + ' would be the Apple (between SPY, AMZN, AAPL)' )
    
    except KeyError:
        print('Your Dates should not be on a Weekend or National holiday.')
   
   
    else:
        break
