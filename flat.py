class Bill:
     """
     object that contains data about bill such as total amount and period of bill
     """

     def __init__(self, total_amount, period):
         self.total_amount = total_amount
         self.period = period


class Flatmate:
    """
    create a flatmate person who live in the flat and pays the share of the bill
    """

    def __init__(self, name, no_of_days):
        self.name = name
        self.no_of_days = no_of_days

    def pays(self, bill, flatmate2):
        weight  = self.no_of_days/(self.no_of_days+ flatmate2.no_of_days)
        total_amount = weight * bill.total_amount
        return total_amount
