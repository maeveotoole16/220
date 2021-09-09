"""
Maeve O'Toole

interest.py

This program aims to compute the monthly
interest charge on a credit card account.

This assignment is entirely my own work.

"""
# Step 1
    # net balance * number of days in the billings cycle
    # net payment receieved before the end of the billing cycle
# Step 2
    # days before the end of the cycle = days in billing cycle - day of payment
# Step 3
    # Step 1 - Step 2
# Step 4
    # Step 3 / days in the billing cycle = average daily balance
# Step 5
    # Convert the average daily balance to monthly (divide daily balance by 12)
# Step 6
    # Taje the average daily balance and multiply it by the monthly and convert to a percentage

def main():

    annual = eval(input("Enter the annual interest rate here: "))
    cycle = eval(input("Enter the number of days in the billing cycle here: "))
    net = eval(input("Enter the previous net balance here: "))
    payment = eval(input("Enter the payment amount here: "))
    day = eval(input("Enter the day of the billing cycle the in which the payment was made here: "))
    first = net * cycle
    days_left = payment * ( cycle - day )
    daily = first - days_left
    average_daily_balance = ( daily / cycle )
    monthly = ( annual / 12 )
    monthly_interest_charge = ((average_daily_balance * monthly)/100)
    print(round(monthly_interest_charge,2))

if __name__== "__main__":
    main()
