# Summary: This module contains the user interface and logic for a console-based version of the stock manager program.
# Author: Morgan Hanson
# Date: 7/23/22

from datetime import datetime
from stock_class import Stock, DailyData
from utilities import clear_screen, display_stock_chart
from os import path
import stock_data
from account_class import Traditional, Robo


# Main Menu
def main_menu(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Stock Analyzer ---")
        print("1 - Manage Stocks (Add, Update, Delete, List)")
        print("2 - Add Daily Stock Data (Date, Price, Volume)")
        print("3 - Show Report")
        print("4 - Show Chart")
        print("5 - Manage Data (Save, Load, Retrieve)")
        print("6 - Investor Type")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5", "6", "0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Stock Analyzer ---")
            print("1 - Manage Stocks (Add, Update, Delete, List)")
            print("2 - Add Daily Stock Data (Date, Price, Volume)")
            print("3 - Show Report")
            print("4 - Show Chart")
            print("5 - Manage Data (Save, Load, Retrieve)")
            print("0 - Exit Program")
            option = input("Enter Menu Option: ")
        if option == "1":
            manage_stocks(stock_list)
        elif option == "2":
            add_stock_data(stock_list)
        elif option == "3":
            display_report(stock_list)
        elif option == "4":
            display_chart(stock_list)
        elif option == "5":
            manage_data(stock_list)
        elif option == "6":
            investment_type(stock_list)
        else:
            clear_screen()
            print("Goodbye")

# Manage Stocks
def manage_stocks(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Stocks ---")
        print("1 - Add Stock")
        print("2 - Update Shares")
        print("3 - Delete Stock")
        print("4 - List Stocks")
        print("0 - Exit Manage Stocks")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Add Stock")
            print("2 - Update Shares")
            print("3 - Delete Stock")
            print("4 - List Stocks")
            print("0 - Exit Manage Stocks")
            option = input("Enter Menu Option: ")
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            update_shares(stock_list)
        elif option == "3":
            delete_stock(stock_list)
        elif option == "4":
            list_stocks(stock_list)
        else:
            print("Returning to Main Menu")

# Add new stock to track
def add_stock(stock_list):
    clear_screen()
    option = ""
    while option != "0":
        print("Add Stock")
        _symbol = input("""Enter Stock Symbol:
                        """).upper()
        _name = input("""Enter Stock Name:
                        """).capitalize()
        _shares = float(input("""Enter Number of Shares:
                        """))
        new_stock = Stock(_symbol, _name, _shares)
        stock_list.append(new_stock)
        option = input(""""Press Enter to add another stock, or 0 to exit
                       """)
        
        
        
# Buy or Sell Shares Menu
def update_shares(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Update Shares ---")
        print("1 - Buy Shares")
        print("2 - Sell Shares")
        print("0 - Exit Update Shares")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Update Shares ---")
            print("1 - Buy Shares")
            print("2 - Sell Shares")
            print("0 - Exit Update Shares")
            option = input("Enter Menu Option: ")
        if option == "1":
            buy_stock(stock_list)
        elif option == "2":
            sell_stock(stock_list)
        elif option == "0":
            print("Returning to Main Menu")

# Buy Stocks (add to shares)
def buy_stock(stock_list):
    clear_screen()
    print("----- Buy Stock Menu -----")
    symb_list = []
    print("Stock List:", end= " ")
    for e in stock_list:
        print(e._symbol, end = " ")
    symbol = str(input("Enter Stock to buy: ")).upper()
    shares = float(input("How many shares to buy? "))
    found = False
    for e in stock_list:
        if e._symbol == symbol:
            found =True
            e.buy(shares)
    if found == True:
        print("Bought " + str(shares) + " shares of " + symbol)
    else:
        print("Error: symbol not found!...")
        input("*** Press Enter to Continue ***")
    
        

# Sell Stocks (subtract from shares)
def sell_stock(stock_list):
    clear_screen()
    print("----- Sell Stock Menu -----")
    symb_list = []
    print("Stock List:", end= " ")
    for e in stock_list:
        print(e._symbol, end = " ")
    symbol = str(input("Enter Stock to sell: ")).upper()
    shares = float(input("How many shares to sell? "))
    found = False
    for e in stock_list:
        if e._symbol == symbol:
            found =True
            e.sell(shares)
    if found == True:
        print("Sold " + str(shares) + " shares of " + symbol)
    else:
        print("Error: symbol not found!...")
        input("*** Press Enter to Continue ***")

# Remove stock and all daily data
def delete_stock(stock_list):
    clear_screen()
    print("***Delete A Stock***")
    print("Stock List: ", end="")
    for e in stock_list:
        print(e._symbol + " ", end = "")
    symbol = str(input("""Enter the stock to delete: 
                       """)).upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock._symbol == symbol:
            found = True
            stock_list.pop(i)
        i+=1
    if found == True:
        print ("Deleted " + symbol)
    else:
        print("Error: Symbol not found")
        _ = input("*** Press Enter to Continue ***")
    _ = input("*** Press Enter to Continue ***")

# List stocks being tracked
def list_stocks(stock_list):
    clear_screen()
    print("List of Stocks")
    column = ['Symbol', 'Name', '# of Shares', '----------']
    
    print(f'{column[0]:20} {column[1]:20} {column[2]:20}')
    print(f'{column[3]:20} {column[3]:20} {column[3]:20}')
    for e in stock_list:
        print(f'{e._symbol:20} {e._name:20} {e._shares:20}')
        print(f'{column[3]:20} {column[3]:20} {column[3]:20}')
    _ = input("*** Press Enter to Continue ***")

# Add Daily Stock Data
def add_stock_data(stock_list):
    clear_screen()
    print("***Add Daily Stock Data***")
    print("Stock List: ")
    for e in stock_list:
        print(e._symbol, end = " ")
    
    symbol = str(input("Enter Stock Symbol: ")).upper()
    found = False
    for e in stock_list:
        if e._symbol == symbol:
            found = True
            current_stock = e
    if found == True:
        data = input("""Enter Transaction Date, Price, and Volume separated by commas """)
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(datetime.strptime(date,"%m/%d/%y"),float(price),float(volume))
            current_stock.add_data(daily_data)
            data = input("Press Enter to exit, or add more comma-separated data (date, price, volume)")
        print("Data entry complete")
    else:
        print("Symbol not Found")
        print("*** Press Enter to Continue ***")
# Display Report for All Stocks
def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock._symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock._symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock._shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)

def display_report(stock_data):
    clear_screen()
    print("*** Generating Stock Report ***")
    for stock in stock_data:
        print("Report for: " + stock._symbol + " " + stock._name)
        print("Shares: " + str(stock._shares))
        count = 0
        price_total = 0
        volume_total = 0
        lowPrice = 999999.99
        highPrice= 0
        lowVolume = 999999999999
        highVolume = 0
        startDate = datetime.strptime("12/31/2099","%m/%d/%Y")
        endDate = datetime.strptime("1/1/1900","%m/%d/%Y")
        for daily_data in stock.DataList:
            count += 1
            price_total = price_total + daily_data.close
            volume_total = volume_total + daily_data.volume
            if daily_data.close<lowPrice:
                lowPrice = daily_data.close
            if daily_data.close > highPrice:
                highPrice = daily_data.close
            if daily_data.volume < lowVolume:
                lowVolume = daily_data.volume
            if daily_data.volume > highVolume:
                highVolume = daily_data.volume
            if daily_data.date < startDate:
                startDate = daily_data.date
                startPrice = daily_data.close
            if daily_data.date > endDate:
                endDate = daily_data.date
                endPrice = daily_data.close
            priceChange = endPrice - startPrice
            print(daily_data.date.strftime("%m/%d/%y"), daily_data.close, daily_data.volume)
        if count > 0:
            print("Summary ---" + str(startDate) + " to " + str(endDate))
            print("Low Price: " + str(lowPrice))
            print("High Price: " + str(highPrice))
            print("Average Price: " + str(price_total/count))
            print("Low Volume: " + str(lowVolume))
            print("High Volume: " + str(highVolume))
            print("Average Volume: " + str(volume_total/count))
            print("Starting Price: " + str(startPrice))
            print("Ending Price: " + str(endPrice))
            print("Change in Price: " + str(priceChange))
            print("Profit/Loss: " + str(priceChange * stock.shares))
        else:
            print("No daily history")
            print("""
                  ----------
                  
                  ----------
                  """)
    print("Report Complete")
    _ = input("*** Press Enter to Continue ***")

# Display Chart
def display_chart(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Manage Data Menu
def manage_data(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Data ---")
        print("1 - Save Data to Database")
        print("2 - Load Data from Database")
        print("3 - Retrieve Data from Web")
        print("4 - Import from CSV File")
        print("0 - Exit Manage Data")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Save Data to Database")
            print("2 - Load Data from Database")
            print("3 - Retrieve Data from Web")
            print("4 - Import from CSV File")
            print("0 - Exit Manage Data")
            option = input("Enter Menu Option: ")
        if option == "1":
            stock_data.save_stock_data(stock_list)
            print("--- Data Saved to Database ---")
            _ = input("Press Enter to Continue")
        elif option == "2":
            stock_data.load_stock_data(stock_list)
            print("--- Data Loaded from Database ---")
            _ = input("Press Enter to Continue")
        elif option == "3":
            retrieve_from_web(stock_list)
            print("--- Data Retrieved from Yahoo! Finance ---")
            _ = input("Press Enter to Continue")
        elif option == "4":
            import_csv(stock_list)
        else:
            print("Returning to Main Menu")

# Get stock price and volume history from Yahoo! Finance using Web Scraping
def retrieve_from_web(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Import stock price and volume history from Yahoo! Finance using CSV Import
def import_csv(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Begin program
def main():
    #check for database, create if not exists
    if path.exists("stocks.db") == False:
        stock_data.create_database()
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
