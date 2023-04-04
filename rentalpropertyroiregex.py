# Simon Dutton
# Due April 3, 2023
# Extra Credit for Rental Property ROI Calculations
# This program uses Regex to get "listings" of properties from a text file,
# and through the information provided in the listing, calculates the ROI for
# that property.

# RegEx option
import re

def print_roi(prop_list):
    """
        print_roi(prop_list:(list:dict))
        Prints out the information that calculates the ROI of a listing.
        Takes in a list of dictionaries which contain the information needed
        to calculate the ROI.
        Returns nothing.
    """
    for listing in properties_list: # for every listing
        print(f"\nHere is the Cash on Cash ROI for {listing['prop_name'].title()}:\n")
        # calculate income
        income = float(listing['rental_income'].replace(",","")) + float(listing['laundry'].replace(",","")) + float(listing['storage'].replace(",","")) + float(listing['misc_income'].replace(",",""))
        print(f"TOTAL MONTHLY INCOME: \t\t$" + format(income, ".2f"))
        # calculate expenses
        expenses = float(listing['taxes'].replace(",","")) + float(listing['insurance'].replace(",","")) + float(listing['utilities'].replace(",","")) + float(listing['hoa'].replace(",","")) + float(listing['lawn'].replace(",","")) + float(listing['vacancy'].replace(",","")) + float(listing['repairs'].replace(",","")) + float(listing['capex'].replace(",","")) + float(listing['prop_management'].replace(",","")) + float(listing['mortgage'].replace(",",""))
        print(f"TOTAL MONTHLY EXPENSES: \t$" + format(expenses, ".2f"))
        # calculate cash flow
        cash_flow = income - expenses
        print(f"TOTAL MONTHLY CASH FLOW: \t$" + format(cash_flow, ".2f"))
        # calculate investment
        investment = float(listing['down'].replace(",","")) + float(listing['closing'].replace(",","")) + float(listing['rehab'].replace(",","")) + float(listing['misc_investments'].replace(",",""))
        print(f"TOTAL INVESTMENT: \t\t$" + format(investment, ".2f"))
        # calculate cash on cash ROI
        annual_cash_flow = cash_flow * 12
        roi = round(annual_cash_flow / investment * 100, 2) #get percentage

        print(f"\n\tCASH ON CASH ROI: {roi}%\n")
        

with open('files/rental_listing.txt') as file:
    """ 
        Creates the regex that finds a listing in the file and gets the proper 
        values to calculate the ROI.
    """
    data = file.read()

    # The regex lets every item have a couple ways it can be formatted/abbreviated
    # in the text file in order to find the information.
    # For example, things like $ in front of money, cents at the end of money, 
    # '/month', := as separators, and more. The items can be on separate lines or all on one line

    # Property Name: " Property Name\s?[:=-]?\s(?P<prop_name>[A-Za-z0-9 ]+)\s? "
    # Rental Income: " (?:Gross Monthly)?\sRental Income\s?[:=-]?\s[$]*(?P<rental_income>[0-9]+(?:,)?[0-9]+[.]?[0-9]{0,2})(?:/month)?\s "
    # Laundry: " Laundry(?: Income)?\s?[:=-]?\s[$]?(?P<laundry>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s "
    # Storage: " Storage(?: Income)?\s?[:=-]?\s[$]?(?P<storage>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s "
    # Misc.: Misc(?:.|ellaneous)?(?: Income)?\s?[:=]\s[$]?(?P<misc_income>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Section Divider: [\s=]+
    # Taxes: Taxes\s?[:=-]?\s[$]?(?P<taxes>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)\s?
    # Insurance: Insurance\s?[:=-]?\s[$]?(?P<insurance>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)\s?
    # Utilities: (Utilities)\s?[:=-]?\s[$]?(?P<utilities>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # HOA: HOA(?: Fees)?\s?[:=-]?\s[$]?(?P<hoa>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Lawn/Snow: Lawn\s?(?:/snow)?(?: care)?[:=-]?\s[$]?(?P<lawn>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Vacancy: Vacancy\s?[:=-]?\s[$]?(?P<vacancy>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Repairs: Repairs\s?[:=-]?\s[$]?(?P<repairs>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Capex: (Capital Expendisures)? ?(?:\(?capex\)?)?\s?[:=-]?\s[$]?(?P<capex>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Property Management: (?:Property|Prop[.]?) Management\s?[:=-]?\s[$]?(?P<prop_management>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Mortgage: Mortgage\s?[:=-]?\s[$]?(?P<mortgage>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Section Divider: [\s=]+
    # Down Payment: Down(?: payment)?\s?[:=-]?\s[$]?(?P<down>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Closing Costs: Closing(?: costs)?\s?[:=-]?\s[$]?(?P<closing>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Repair money/rehab budget: ((?:Repair(?: money)?(?:ments)?)|(?:Rehab(?: budget)?))\s?[:=-]?\s[$]?(?P<rehab>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    # Misc. Investment: Misc(?:.|ellaneous)?(?: other| investments)?\s?[:=-]?\s[$]?(?P<misc_investments>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s
    pattern = re.compile(r'Prop(?:erty)? Name\s?[:=-]?\s(?P<prop_name>[A-Za-z0-9-.,\'\(\) ]+)\s+(?:Gross Monthly)?\s?Rental Income\s?[:=-]?\s[$]*(?P<rental_income>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Laundry(?: Income)?\s?[:=-]?\s[$]?(?P<laundry>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Storage(?: Income)?\s?[:=-]?\s[$]?(?P<storage>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Misc(?:.|ellaneous)?(?: Income)?\s?[:=-]?\s[$]?(?P<misc_income>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?[\s=]+Taxes\s?[:=-]?\s[$]?(?P<taxes>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Insurance\s?[:=-]?\s[$]?(?P<insurance>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Utilities\s?[:=-]?\s[$]?(?P<utilities>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+HOA(?: Fees)?\s?[:=-]?\s[$]?(?P<hoa>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Lawn(?:/snow)?(?: care)?\s?[:=-]?\s[$]?(?P<lawn>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Vacancy\s?[:=-]?\s[$]?(?P<vacancy>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Repairs\s?[:=-]?\s[$]?(?P<repairs>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+(Capital Expendisures)? ?(?:\(?capex\)?)?\s?[:=-]?\s[$]?(?P<capex>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+(?:Property|Prop[.]?) Management\s?[:=-]?\s[$]?(?P<prop_management>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Mortgage\s?[:=-]?\s[$]?(?P<mortgage>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?[\s=]+Down(?: payment)?\s?[:=-]?\s[$]?(?P<down>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Closing(?: costs)?\s?[:=-]?\s[$]?(?P<closing>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+((?:Repair(?: money)?(?:ments)?)|(?:Rehab(?: budget)?))\s?[:=-]?\s[$]?(?P<rehab>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s+Misc(?:.|ellaneous)?(?: other| investments)?\s?[:=-]?\s[$]?(?P<misc_investments>[0-9]+(?:,)?[0-9]*[.]?[0-9]{0,2})(?:/month)?\s*?', re.IGNORECASE)

    # list of properties (dictionary containing the groups for each item)
    properties_list = [m.groupdict() for m in pattern.finditer(data)]

print_roi(properties_list)