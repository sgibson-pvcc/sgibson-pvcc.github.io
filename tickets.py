# Name: Sherri Gibson
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

########################################    Define global variables ##############################
#define tax rate and prices
Sales_tax_rate = .055
PR_ticket = 10.99

#define gloobal VAriables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

################## define program functions ######################
def main():
    get_user_data()
    perform_calulations()
    display_results()

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calulations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_ticket
    sales_tax = subtotal * Sales_tax_rate
    total = subtotal + sales_tax

def display_results():
    print('*****************************')
    print('*****CINEMA HOUSE MOVIES*****')
    print('Your neighborhood movie house')
    print('-------------------------------')
    print('Tickets         $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax       $ ' + format(Sales_tax_rate,'8,.2f'))
    print('Total           $ ' + format(total,'8,.2f'))
    print('----------------------------------')
    print(str(datetime.datetime.now()))

    ###################################### call on main program to execute
    main()