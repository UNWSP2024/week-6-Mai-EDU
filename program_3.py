#Programmer: Mai Lillie
#Date: 10/11/24
# Program #3: Tax Rate


#Function to calculate county sales tax
def county_tax(sales):
    county_total = 0
    county_total = sales * 0.025
    return county_total

#Function to calculate state sales tax
def state_tax(sales):
    state_total = 0
    state_total = sales * 0.05
    return state_total

#Gathers input from the user and gives the output
def main():
    sales = float(input("What was the revenue from total sales?: "))
    state_total = state_tax(sales)
    county_total = county_tax(sales)
    tax_total = state_total + county_total
    print(f'Revenue: {sales:.2f} \nState Tax: {state_total:.2f} \nCounty Tax: {county_total:.2f} \nTotal Tax: {tax_total:.2f}')

#Runs the program
main()
