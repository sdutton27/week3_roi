# Simon Dutton
# Due April 3, 2023
# Rental Property ROI Calculations - Basic Class
# This program creates the necessary functions to calculate the ROI on a property.

import os # for clearing

class ROICalculator():
    """
        ROICalculator() contains the methods a user can use to calculate the ROI
        for a rental property.
    """
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.investment = 0
        self.cash_on_cash_roi = 0

    def income_calc(self, rental, laundry=0, storage=0, misc=0):
        """ 
            income_calc(rental:float, laundry=0:float, storage=0:float, misc=0:float)
            Calculates the total monthly income for a property.
            Takes in the rental income, laundry income, storage income, and any
            misc. income.
            Returns the sum of these items.
        """
        self.income = rental + laundry + storage + misc
        return self.income

    def expenses_calc(self, taxes, insurance, utilities, hoa, yard, vacancy, repairs, cap_ex, prop_manage, mortgage):
        """ 
            income_calc(taxes:float, insurance:float, utilities:float, hoa:float, 
            yard:float, vacancy:float, repairs:float, cap_ex:float, 
            prop_manage:float, mortgage:float)
            Calculates the total monthly expenses for a property.
            Takes in the taxes, insurance cost, utilities cost, HOA fees, lawn/snow
            care, vacancy cost, repairs cost, capital expenditures (capex), property
            management fees, and mortgage cost.
            Returns the sum of these items.
        """
        self.expenses = taxes + insurance + utilities + hoa + yard + vacancy + repairs + cap_ex + prop_manage + mortgage
        return self.expenses

    def cash_flow_calc(self):
        """
            cash_flow_calc()
            Returns the monthly cash flow on a property
        """
        self.cash_flow = self.income - self.expenses
        return self.cash_flow

    def investment_calc(self, down_payment, closing_costs, rehab_budget, misc=0):
        """
            investment_calc(down_payment:float, closing_costs:float, rehab_budget:float, misc=0:float)
            Calculates the total investment cost for a property.
            Takes in the down payment, the closing costs, the rehab budget, and any
            misc. investment costs.
            Returns the sum of these items.
        """
        self.investment = down_payment + closing_costs + rehab_budget + misc
        return self.investment

    def cash_on_cash_roi_calc(self):
        """
            cash_on_cash_roi_calc()
            Calculates the cash on cash ROI for a property.
            Returns this value.
        """
        annual_cash_flow = self.cash_flow * 12
        self.cash_on_cash_roi = annual_cash_flow / self.investment * 100 #get percentage
        return self.cash_on_cash_roi


roi = ROICalculator()
# uses the values from the example property from the video
print(roi.income_calc(2000))
print(roi.expenses_calc(150, 100, 0, 0, 0, 100, 100, 100, 200, 860))
print(roi.cash_flow_calc())
print(roi.investment_calc(40000, 3000, 7000))
print(f"{roi.cash_on_cash_roi_calc()}%")
