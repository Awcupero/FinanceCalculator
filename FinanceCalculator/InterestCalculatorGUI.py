import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from InterestCalculator import InterestCalculator
import os

# Change for you adjusting the UI
principalamountrow =1
futurealuerow =2
interestraterow =5
compoundingperiodrow =3
timerow =4
selectcalculationrow =0
textrow =7
bottonrow =8
 
class InterestCalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Finance Calculator v 0.8")
        self.geometry("338x375")
        self.iconbitmap("FinanceCalculator\\favicon.ico")
        self.resizable(width=False, height=False)

        # Get the directory of the current Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the relative path to the file
        file_path = os.path.join(script_dir, "Textbox.txt")

        # Load description text from file
        with open(file_path, 'r') as file:
            description = file.read()

        self.description_text = tk.Text(self, height=10, width= 40, wrap="word")
        self.description_text.insert(tk.END, description)
        self.description_text.config(state=tk.DISABLED)
        self.description_text.grid(row=textrow, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        self.principal_label = ttk.Label(self, text="Principal Amount:")
        self.principal_label.grid(row=principalamountrow, column=0, padx=5, pady=5, sticky="w")
        self.payout_label = ttk.Label(self, text="Payout Amount:")
        self.payout_label.grid(row=principalamountrow, column=0, padx=5, pady=5, sticky="w")
        self.principal_entry = ttk.Entry(self)
        self.principal_entry.insert(0, "0")  # Set default value to 0
        self.principal_entry.grid(row=principalamountrow, column=1, padx=5, pady=5 ,sticky="ew")

        
        self.future_label = ttk.Label(self, text="Future Value:")
        self.future_label.grid(row=futurealuerow, column=0, padx=5, pady=5, sticky="w")
        self.amount_label = ttk.Label(self, text="Amount:")
        self.amount_label.grid(row=futurealuerow, column=0, padx=5, pady=5, sticky="w")
        self.future_entry = ttk.Entry(self)
        self.future_entry.insert(0, "0")  # Set default value to 0
        self.future_entry.grid(row=futurealuerow, column=1, padx=5, pady=5, sticky="ew")

        
        self.rate_label = ttk.Label(self, text="Interest Rate (%):")
        self.rate_label.grid(row=interestraterow, column=0, padx=5, pady=5, sticky="w")
        self.rate_entry = ttk.Entry(self)
        self.rate_entry.insert(0, "0")  # Set default value to 0
        self.rate_entry.grid(row=interestraterow, column=1, padx=5, pady=5, sticky="ew")

        
        self.period_label = ttk.Label(self, text="Compounding Period:")
        self.period_label.grid(row=compoundingperiodrow, column=0, padx=5, pady=5, sticky="w")
        self.payrate_label = ttk.Label(self, text="Payment Frequency :")
        self.payrate_label.grid(row=compoundingperiodrow, column=0, padx=5, pady=5, sticky="w")
        self.period_combobox = ttk.Combobox(self, values=["annually", "semiannually", "quarterly", "monthly", "weekly", "daily"])
        self.period_combobox.current(0)
        self.period_combobox.grid(row=compoundingperiodrow, column=1, padx=5, pady=5,sticky="ew")
        
        self.time_label = ttk.Label(self, text="Time (years):")
        self.time_label.grid(row=timerow, column=0, padx=5, pady=5, sticky="w")
        self.time_entry = ttk.Entry(self)
        self.time_entry.insert(0, "0")  # Set default value to 0
        self.time_entry.grid(row=timerow, column=1, padx=5, pady=5, sticky="ew")
        
        self.calculation_label = ttk.Label(self, text="Select Calculation:")
        self.calculation_label.grid(row=selectcalculationrow, column=0, padx=5, pady=5, sticky="w")
        self.calculation_combobox = ttk.Combobox(self, values=["Time Factor", "Interest Rate", "Future Value","Principal","Continuous","Annuity Ending Ammount" ,"Annuity Recurring Payment"])
        self.calculation_combobox.current(0)
        self.calculation_combobox.grid(row=selectcalculationrow, column=1, padx=5, pady=5, sticky="ew")

        self.calculate_button = ttk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=bottonrow, column=0, columnspan=1, padx=5, pady=10,sticky="ew")

        self.update_button = ttk.Button(self, text="Update", command=self.update)
        self.update_button.grid(row=bottonrow, column=1, columnspan=1, padx=5, pady=10,sticky="ew")
        
        self.hide_entries()

    def calculate(self):
        try:
            principal = float(self.principal_entry.get())
            future_value = float(self.future_entry.get())
            interest_rate = float(self.rate_entry.get())
            period = self.period_combobox.get()
            time = float(self.time_entry.get())
            
            n = periods[period]
            
            calculator = InterestCalculator(principal, future_value, interest_rate, n, time)
            
            selected_calculation = self.calculation_combobox.get()

            if selected_calculation == "Time Factor":
                result_message = f"Time: {calculator.calculate_time_factor():.0f} Years \n"
            elif selected_calculation == "Continuous":
                result_message = f"Continuous: ${calculator.continuous()}\n"
            elif selected_calculation == "Interest Rate":
                result_message = f"Interest Rate: {calculator.calculate_interest_rate()}%\n"
            elif selected_calculation == "Future Value":
                result_message = f"Initial balance: ${calculator._p}\n"
                result_message += f"Future Value: ${calculator.calculate_future_value()}\n"
                result_message += f"Interest Earned:  ${calculator.compound_amount()}\n"
                result_message += f"APY:{calculator.calculate_apy()}%\n"
            elif selected_calculation == "Principal":
                result_message = f"Principal amount {calculator.calculate_principal()}"
            elif selected_calculation == "Annuity Ending Ammount":
                result_message = f"Final Amount: ${calculator.annuity_ending_ammount()}\n"
                result_message += f"Contirbuted: ${calculator.annuity_contirbuted()}\n"
                result_message += f"Insterest Earned: ${round(calculator.annuity_ending_ammount() - calculator.annuity_contirbuted(),2)}\n"
            elif selected_calculation == "Annuity Recurring Payment":
                result_message =f"Payment: ${calculator.annuity_recurring()}\n"
                result_message += f"Contirbuted: ${calculator.annuity_contirbuted_recurring()}\n"
                result_message += f"Insterest Earned: ${round(future_value- calculator.annuity_contirbuted_recurring(),2)}\n"

            messagebox.showinfo("Calculation Result", result_message)
            
        except ValueError :
            messagebox.showerror("Error", "Please enter valid numeric values.")

        except ZeroDivisionError :
            messagebox.showerror("Error", "You can not divide by zero.")


    def update(self):
        
        self.hide_entries()

        update = self.calculation_combobox.get() 
    
        if update == "Time Factor":
            self.future_entry.grid()
            self.future_label.grid()
            self.period_label.grid()
            self.period_combobox.grid()
            self.principal_entry.grid()
            self.principal_label.grid()
            self.rate_entry.grid()
            self.rate_label.grid()
            self.calculate_button.grid()

        elif update == "Interest Rate":
            self.future_label.grid()
            self.future_entry.grid()
            self.period_label.grid()
            self.period_combobox.grid()
            self.time_label.grid()
            self.time_entry.grid()
            self.principal_entry.grid()
            self.principal_label.grid()
            self.calculate_button.grid()

        elif update == "Future Value":
            self.period_label.grid()
            self.period_combobox.grid()
            self.principal_entry.grid()
            self.principal_label.grid()
            self.time_label.grid()
            self.time_entry.grid()
            self.rate_entry.grid()
            self.rate_label.grid()
            self.calculate_button.grid()
        
        elif update == "Principal":
            self.future_label.grid()
            self.future_entry.grid()
            self.period_label.grid()
            self.period_combobox.grid()
            self.time_label.grid()
            self.time_entry.grid()
            self.rate_entry.grid()
            self.rate_label.grid()
            self.calculate_button.grid()

        elif update == "Continuous":
            self.principal_entry.grid()
            self.principal_label.grid()
            self.rate_entry.grid()
            self.rate_label.grid()       
            self.time_label.grid()
            self.time_entry.grid()
            self.calculate_button.grid()

        elif update == "Annuity Ending Ammount":
            self.payout_label.grid()
            self.principal_entry.grid()
            self.time_label.grid()
            self.time_entry.grid()
            self.payrate_label.grid()
            self.period_combobox.grid()
            self.rate_entry.grid()
            self.rate_label.grid()    
            self.calculate_button.grid()

        elif update == "Annuity Recurring Payment":
            self.future_entry.grid()
            self.amount_label.grid()
            self.time_label.grid()
            self.time_entry.grid()
            self.payrate_label.grid()
            self.period_combobox.grid()
            self.rate_entry.grid()
            self.rate_label.grid()    
            self.calculate_button.grid()


            



    def hide_entries(self):
        self.future_label.grid_remove()
        self.future_entry.grid_remove()
        self.rate_label.grid_remove()
        self.rate_entry.grid_remove()
        self.period_label.grid_remove()
        self.period_combobox.grid_remove()
        self.time_label.grid_remove()
        self.time_entry.grid_remove()
        self.principal_entry.grid_remove()
        self.principal_label.grid_remove()
        self.calculate_button.grid_remove()
        self.payout_label.grid_remove()
        self.amount_label.grid_remove()
        self.payrate_label.grid_remove()
    


# Dictionary for compounding periods
periods = {
    "annually": 1, 
    "semiannually": 2,
    "quarterly": 4,
    "monthly": 12,
    "weekly": 52,
    "daily": 365
}

if __name__ == "__main__":

    file_path = "Textbox.txt"
    app = InterestCalculatorGUI()
    app.mainloop()

