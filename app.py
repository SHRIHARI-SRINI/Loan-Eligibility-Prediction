import tkinter as tk
from tkinter import ttk
import pickle

def predict_loan_eligibility():
    # Get user inputs
    gender = 1 if gender_var.get() == "Male" else 0
    married = 1 if married_var.get() == "Yes" else 0
    dependents = int(dependents_var.get())
    education = 1 if education_var.get() == "Graduate" else 0
    self_employed = 1 if self_employed_var.get() == "Yes" else 0
    applicant_income = float(applicant_income_entry.get())
    coapplicant_income = float(coapplicant_income_entry.get())
    loan_amount = float(loan_amount_entry.get())
    loan_amount_term = float(loan_amount_term_entry.get())
    credit_history = float(credit_history_var.get())
    property_area = 1 if property_area_var.get() == "Urban" else (2 if property_area_var.get() == "Semiurban" else 3)

    features = [
        float(applicant_income_entry.get()),
        float(coapplicant_income_entry.get()),
        float(loan_amount_entry.get())
    ]

    # Make the prediction
    prediction = loaded_model.predict([features])
    # Make the prediction
    

    # Display the result
    result_label.config(text=f'Loan Eligibility: {"Yes" if prediction[0] == 1 else "No"}')

# Create the main application window
app = tk.Tk()
app.title("Loan Eligibility Predictor")

# Gender
gender_var = tk.StringVar()
gender_label = ttk.Label(app, text="Gender:")
gender_combobox = ttk.Combobox(app, textvariable=gender_var, values=["Male", "Female"])
gender_label.grid(row=0, column=0, padx=10, pady=5)
gender_combobox.grid(row=0, column=1, padx=10, pady=5)

# Married
married_var = tk.StringVar()
married_label = ttk.Label(app, text="Married:")
married_combobox = ttk.Combobox(app, textvariable=married_var, values=["Yes", "No"])
married_label.grid(row=1, column=0, padx=10, pady=5)
married_combobox.grid(row=1, column=1, padx=10, pady=5)

# Dependents
dependents_var = tk.StringVar()
dependents_label = ttk.Label(app, text="Dependents:")
dependents_combobox = ttk.Combobox(app, textvariable=dependents_var, values=["0", "1", "2", "3+"])
dependents_label.grid(row=2, column=0, padx=10, pady=5)
dependents_combobox.grid(row=2, column=1, padx=10, pady=5)

# Education
education_var = tk.StringVar()
education_label = ttk.Label(app, text="Education:")
education_combobox = ttk.Combobox(app, textvariable=education_var, values=["Graduate", "Not Graduate"])
education_label.grid(row=3, column=0, padx=10, pady=5)
education_combobox.grid(row=3, column=1, padx=10, pady=5)

# Self Employed
self_employed_var = tk.StringVar()
self_employed_label = ttk.Label(app, text="Self Employed:")
self_employed_combobox = ttk.Combobox(app, textvariable=self_employed_var, values=["Yes", "No"])
self_employed_label.grid(row=4, column=0, padx=10, pady=5)
self_employed_combobox.grid(row=4, column=1, padx=10, pady=5)

# Applicant Income
applicant_income_label = ttk.Label(app, text="Applicant Income:")
applicant_income_entry = ttk.Entry(app)
applicant_income_label.grid(row=5, column=0, padx=10, pady=5)
applicant_income_entry.grid(row=5, column=1, padx=10, pady=5)

# Coapplicant Income
coapplicant_income_label = ttk.Label(app, text="Coapplicant Income:")
coapplicant_income_entry = ttk.Entry(app)
coapplicant_income_label.grid(row=6, column=0, padx=10, pady=5)
coapplicant_income_entry.grid(row=6, column=1, padx=10, pady=5)

# Loan Amount
loan_amount_label = ttk.Label(app, text="Loan Amount:")
loan_amount_entry = ttk.Entry(app)
loan_amount_label.grid(row=7, column=0, padx=10, pady=5)
loan_amount_entry.grid(row=7, column=1, padx=10, pady=5)

# Loan Amount Term
loan_amount_term_label = ttk.Label(app, text="Loan Amount Term:")
loan_amount_term_entry = ttk.Entry(app)
loan_amount_term_label.grid(row=8, column=0, padx=10, pady=5)
loan_amount_term_entry.grid(row=8, column=1, padx=10, pady=5)

# Credit History
credit_history_var = tk.StringVar()
credit_history_label = ttk.Label(app, text="Credit History:")
credit_history_combobox = ttk.Combobox(app, textvariable=credit_history_var, values=["0", "1"])
credit_history_label.grid(row=9, column=0, padx=10, pady=5)
credit_history_combobox.grid(row=9, column=1, padx=10, pady=5)

# Property Area
property_area_var = tk.StringVar()
property_area_label = ttk.Label(app, text="Property Area:")
property_area_combobox = ttk.Combobox(app, textvariable=property_area_var, values=["Urban", "Semiurban", "Rural"])
property_area_label.grid(row=10, column=0, padx=10, pady=5)
property_area_combobox.grid(row=10, column=1, padx=10, pady=5)

# Predict Button
predict_button = ttk.Button(app, text="Predict", command=predict_loan_eligibility)
predict_button.grid(row=11, column=0, columnspan=2, pady=10)

# Result Label
result_label = ttk.Label(app, text="Loan Eligibility: ")
result_label.grid(row=12, column=0, columnspan=2, pady=10)
from joblib import load

# Load the model
loaded_model = load('/home/shrihari/Documents/Loan Eligibility Prediction /loanmodel.joblib')

# Start the main event loop
app.mainloop()
