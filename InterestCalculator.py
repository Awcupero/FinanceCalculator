import math

class InterestCalculator:
    def __init__(self, p :float , a:float, r:float , n:float, t:float ):
        self._p = p  # Principal /payout amount
        self._a = a  # Future value
        self._r = r  # Interest rate
        self._n = n  # Number of compounding periods per year
        self._t = t  # Time in years


    def percentage_convert(self):
        return self._r / 100
    
    def continuous(self):
        final_amount = self._p * math.e ** ( self.percentage_convert() * self._t)
        return round(final_amount , 2)

    def calculate_future_value(self):
        r = self.percentage_convert()
        future_value = round(self._p * (pow((1 + (r) / self._n), self._n * self._t)),2)
        return round(future_value,2 )
 
    def calculate_interest_rate(self):
        interest_rate = self._n * ((self._a / self._p) ** (1 / (self._n * self._t)) - 1)
        return round (interest_rate * 100 ,2)
    
    def calculate_principal(self):
        r = self.percentage_convert()
        principal = self._a / ((1 + r / self._n) ** (self._n * self._t))
        return round(principal,2)
    
    def calculate_time_factor(self):
        r = self.percentage_convert()
        time_factor = math.log(self._a / self._p) / (self._n * math.log(1 + r / self._n))
        return round(time_factor,0)

    def calculate_apy(self):
        r = self.percentage_convert()
        apy = (1 + r  / self._n) ** self._n - 1
        return round(apy * 100, 2)
    
    def compound_amount(self):
        a = self.calculate_future_value()
        compound =  a - self._p
        return round(compound,2)
    
    def annuity_ending_ammount(self):
        r = self.percentage_convert()
        a = self._p * ((1 + (r/self._n)) ** (self._t * self._n) - 1) / (r/self._n)
        return round(a ,2)
    
    def annuity_contirbuted(self):
        c = self._p*self._n*self._t    
        return round (c,2)
    
    def annuity_contirbuted_recurring(self):
        c = self.annuity_recurring()*self._n*self._t    
        return round (c,2)
    
    def annuity_recurring(self):
        r = self.percentage_convert()
        p = self._a*(r/self._n) / ((1 + (r/self._n)) ** (self._t * self._n) - 1) 
        return round(p ,2)


if __name__ == "__main__":


    principal_amount = 1000  # Example principal amount
    future_value = 600000 # Example future value
    interest_rate = 9  # Example interest rate (5%)
    compounding_periods_per_year = 12 # Example number of times interest is compounded per year
    years = 30  # Example time in years



    calculator = InterestCalculator(principal_amount, future_value, interest_rate, compounding_periods_per_year, years)

    #print(calculator.calculate_future_value())
    #print(calculator.compound_amount())
    #print(calculator.calculate_apy())
    #print(calculator.continuous())
    #print(calculator.annuity_payment())
