# Simon Dutton
# Due April 3, 2023
# Rental Property ROI Calculations - User Input Program
# This program calculates the ROI for a property (or many properties) based 
# on the user's input. It is a text-based program.

import os # to clear the terminal

class ROICalculatorInput():
    """
        Calculates the ROI for a property based on the user's input.
    """
    def __init__(self):
        """
            Initiates the necessary variables for the ROICalculatorInput program.
        """
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.investment = 0
        self.cash_on_cash_roi = 0
        self.no_investment = False # switches to True if the user did not actually invest in a property.

        self.unreadable_value = "I'm sorry, I was not able to read the value you put in. Please make sure that you input a number. \nLet's start this section over.\n"

    def calculate_roi(self):
        """
            calculate_roi()
            Calls the necessary functions to calculate the Cash on Cash ROI
            Returns the user's input from the main menu
        """
        self.income_calc()
        self.expenses_calc()
        self.cash_flow_calc()
        self.investment_calc()
        self.cash_on_cash_roi_calc()
        if self.no_investment:
            return "quit" #quit the program completely
        else:
            return input(f"What would you like to do now? {instructions}\n") # back to main menu

    def income_calc(self):
        """
            income_calc()
            Calculates the total monthly income for a property.
            Asks the user for the rental income, laundry income, storage income, and any
            misc. income.
            Sums these items and saves in a global variable, but returns nothing.
        """
        print("\nFirst we will start with some questions about your monthly income on the property.\n")
        while True:
            try: # makes sure inputs are proper floats
                rental = float(input("What is your gross monthly rental income? \n$"))
                laundry = float(input("What is your monthly laundry income? (ie. income from washer/dryer on property) \n$"))
                storage = float(input("What is your monthly storage income? (ie. income from storage shed on property) \n$"))
                misc = float(input("What is your monthly miscellaneous income associated with the property? \n$"))
                break
            except ValueError: # if the user input a string that cannot be converted to float
                print(self.unreadable_value) # try again
        self.income = rental + laundry + storage + misc
        print(f"\n\nYOUR TOTAL MONTHLY INCOME: ${format(self.income, '.2f')}") # format to $xx.xx
        print(f"===========================================")

    def expenses_calc(self):
        """ 
            expenses_calc()
            Calculates the total monthly expenses for a property.
            Asks the user for the taxes, insurance cost, utilities cost, HOA fees, lawn/snow
            care, vacancy cost, repairs cost, capital expenditures (capex), property
            management fees, and mortgage cost.
            Sums these items and saves in a global variable, but returns nothing.
        """
        print("\nNext, we will move on to some questions about the monthly expenses on the property.\n")
        while True:
            try: # makes sure inputs are proper floats
                taxes = float(input("How much will you pay in taxes on the property (monthly)?\nNote: sometimes tax is included in the mortgage. If so, put '0' here. \n$"))
                insurance = float(input("How much will it cost to pay for insurance on the property (monthly)? \nNote: sometimes insurance is included in the mortgage. If so, put '0' here. \n$"))
                utilities = float(input("How much would you like to set aside to pay for utilities (per month)?\nNote: you may make your tenant pay for their own utilities. If so, put '0' here. \n$"))
                hoa = float(input("What is the monthly Homeowners Association Fee (HOA fee) for the property (per month)?\nNote: not all properties require an HOA fee.\nIf your property does not, put '0' here. \n$"))
                yard = float(input("How much would you like to set aside for lawn/yard/snow care (per month)?\nNote: you may have your tenant handle their own lawn/snow care. If so, put '0' here. \n$"))
                vacancy = float(input(f"How much money would you like to set aside per month, knowing that at some point (between renters) the property will be vacant?\nIt is recommended to estimate a 3-5% vacancy, or 3-5% of your rental income.\nAs a refresher, your rental income was ${self.income}.\nFor your convenience, we have calculated the recommended 5% vacancy as ${round(self.income * .05)}. \n$"))
                repairs = float(input("How much money would you like to set aside for potential repair costs (per month)?\nIt is suggested to save around $50-$100 per unit. \n$"))
                cap_ex = float(input("How much money would you like to set aside for capital expenditures (monthly)?\nIt is recommended that you set aside a little money per month so that when big expenses, ie. replacing a roof, come up,\nyou will have set aside money to deal with the cost of these replacements. \n$"))
                prop_manage = float(input(f"How much money would you like to set aside for property management (monthly)? If you have a property manager, you likely will have to pay them 10% of your monthly rental income.\nFor your convenience, your monthly rental income was ${self.income}, so 10% of that is ${round(self.income * .1)}. \n$"))
                mortgage = float(input("How much money needs to go towards your mortgage (per month)? \n$"))
                break
            except ValueError: # if the user input a string that cannot be converted to float
                print(self.unreadable_value) # try everything from this section again

        self.expenses = taxes + insurance + utilities + hoa + yard + vacancy + repairs + cap_ex + prop_manage + mortgage
        print(f"\n\nYOUR TOTAL MONTHLY EXPENSES: ${format(self.expenses, '.2f')}")
        print(f"===========================================")

    def cash_flow_calc(self):
        """
            cash_flow_calc()
            Calculates the monthly cash flow on a property.
            Saves in a global variable, and returns nothing
        """
        self.cash_flow = self.income - self.expenses
        print("\nFor your convenience, we have now calculated your cash flow. \nYour cash flow is the net income you make per month after expenses.")
        print(f"\n\nYOUR TOTAL MONTHLY CASH FLOW: ${format(self.cash_flow, '.2f')}")
        print(f"===========================================")

    def investment_calc(self):
        """
            investment_calc()
            Calculates the total investment cost for a property.
            Asks the user for the down payment, the closing costs, the rehab budget, and any
            misc. investment costs.
            Returns nothing, but saves sum in a global variable.
        """
        print("\nLast set of questions: the only thing left that we need to make your ROI calculation is more information about your investment itself.\n")
        while True:
            try:
                down_payment = float(input("What was the down payment that you paid on the property? \n$"))
                closing_costs = float(input("What were your closing costs? \n$"))
                rehab_budget = float(input("How much did you pay in repair/rehab money?\n(ie. painting, remodeling, etc.)\n$"))
                misc_answer = input("Were there any other miscellaneous costs in your investment? Type 'yes' or 'no'\n")
                if misc_answer == 'yes':
                    misc = float(input("What was their total cost? \n$"))
                elif misc_answer == 'no':
                    misc = 0
                else: #unreadable answer
                    print("Sorry, I didn't catch that. I am imagining you meant that there were no miscellaneous costs, so I will leave that blank.")
                    misc = 0
                break
            except ValueError:
                print(self.unreadable_value)
        
        self.investment = down_payment + closing_costs + rehab_budget + misc
        print(f"\n\nYOUR TOTAL INVESTMENT: ${format(self.investment, '.2f')}")
        print(f"===========================================")

    def cash_on_cash_roi_calc(self):
        """
            cash_on_cash_roi_calc()
            Calculates the Cash On Cash ROI for a property.
            Returns nothing, but saves sum in a global variable
        """
        # TRY/EXCEPT ZeroDivisionError if the investment was $0 (they got the property for free? Why are they even using the calculator?)
        try: 
            annual_cash_flow = self.cash_flow * 12
            self.cash_on_cash_roi = round(annual_cash_flow / self.investment * 100, 2) #get percentage
        
            print("\nThank you for your patience. We have now calculated your Cash on Cash ROI.\nThis can be calculated by dividing your annual cash flow by the total investment on the property.")
            print(f"For your convenience, we have listed those values here:\n\tANNUAL CASH FLOW: ${format(annual_cash_flow, '.2f')}\n\tTOTAL INVESTMENT: ${format(self.investment, '.2f')}")
        
            print(f"\n\nYOUR CASH ON CASH ROI: {self.cash_on_cash_roi}%")
            print(f"===========================================")
        except ZeroDivisionError:
            # if user didn't invest any money, quits the program
            self.no_investment = True
            print("\nHold up, you got this property for free? Um...\n\nWHY ARE YOU EVEN BOTHERING WITH A PROGRAM LIKE THIS. \nIf you didn't invest ANYTHING in this property, how can I calculate your \"return on 'INVESTMENT'\"??? \n\nNo. Just no. I'm done with you. \n\nQutting the program...")
    
    def print_calculations(self):
        """
            print_calculations()
            Formats the printing of the calculated items, and prints them out
            Returns nothing
        """
        print(f"\nYOUR TOTAL MONTHLY INCOME: ${format(self.income, '.2f')}")
        print(f"\nYOUR TOTAL MONTHLY EXPENSES: ${format(self.expenses, '.2f')}")
        print(f"\nYOUR TOTAL MONTHLY CASH FLOW: ${format(self.cash_flow, '.2f')}")
        print(f"\nYOUR TOTAL INVESTMENT: ${format(self.investment, '.2f')}")
        print(f"===========================================")
        print(f"\nYOUR CASH ON CASH ROI: {self.cash_on_cash_roi}%\n\n")
        
    
#################################################
instructions = "Please type 'begin' to begin your calculations, 'print' to print what we have calculated for you, or 'quit' to quit."

properties_dict = {} # stores the properties the user has performed calculations on

os.system('cls||clear')
output = input("Welcome to the Cash on Cash ROI Calculator.\nThis program will calculate your Cash on Cash ROI after asking you a series of questions.\nType 'begin' to begin or 'quit' to quit.\n") #does not give them print option but they could print, vals would just be 0

while True:
    if output == 'begin':
        os.system('cls||clear') #clear
        print("Let's get started.")
        # first, ask for name
        name = input("\nBefore we start, let's give a name to this property.\nThis way we can tell it apart from any other properties you may want to calculate the ROI for.\nFor example, 'Seaside 3-bed' or 'Downtown Chicago.'\n").lower() # lowered for consistency
        # whatever it returns, create a new object and store that object in the key "name"
        properties_dict[name] = ROICalculatorInput() # store to the dictionary of properties
        output = properties_dict[name].calculate_roi()
    elif output == 'quit': # quit program
        break
    elif output == 'print':
        # get which property they want to print the values for
        prop_to_print = input("What property would you like to print the ROI for?\nPlease type the name of this property. Otherwise, we will print all the properties we have calculated the ROI for you so far.\n").lower() #lowered since items are stored lower() for consistency 
        if prop_to_print in properties_dict: #if user inputted property properly
            # print info for specific property
            print(f"\nHere are the ROI calculations for the {prop_to_print.title()} property:")
            properties_dict[property].print_calculations()
        else: #if not a specified property/wrong input, print all properties
            print("\nWe could not find that specific property in our calculations.\nHere are all the ROI calculations we have made for you so far.") # could change this if multiple properties
            for property in properties_dict:
                print(f"\nHere are the ROI calculations for the {property.title()} property:")
                properties_dict[property].print_calculations()
        output = input(f"What would you like to do next? {instructions}\n")
    else: #undefined input
        output = input(f"I'm sorry, I didn't quite catch that. {instructions}\n")

print("\nThank you for trying out the Cash on Cash ROI Calculator.\nFor your convenience, here is a reminder of the calculations we just made for you.")
for property in properties_dict:
        if properties_dict[property].no_investment: # if the user did not actually invest in the property, don't print
            print("OH WAIT.\nYou did not actually invest in your property, so there were no calculations to be made.\nGoodbye.")
            break
        # else print the items
        print(f"\nHere are the ROI calculations for the {property.title()} property:")
        properties_dict[property].print_calculations()
print("\nHave a nice day, and good luck investing!")