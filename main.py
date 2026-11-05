import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


# Constants used throughout the application

FIELDNAMES = ["Type", "Amount", "Category", "Description"]
CSV_FILE="transaction.csv"


# Initialize the transaction CSV file if it doesn't exist

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


# Add a new income or expense transaction

def add_transaction(transaction_type):

    while True:
        try:
            amount_input=input("Amount:")
            if amount_input.strip()=="":
                print("Amount cannot be empty")
                continue
    
            amount=int(amount_input)
            if amount<=0 :
                print("Enter Positive integer")
                continue
            break
                                
        except ValueError:
                print("Enter a Valid input")
    
    while True:    
        category=input("Category: ").strip().title()
        if category.strip()=="":
            print("Category cannot be empty")
            continue
        break
    
    description=input("Description: ")
                    
                
    row = {
            "Type": transaction_type,
            "Amount": amount,
            "Category": category,
           "Description": description
             }
    
    with open(CSV_FILE,"a",newline="")as file:          
                        
        writer=csv.DictWriter(file,fieldnames=FIELDNAMES)    
    
        writer.writerow(row)


# Calculate total income and expenses

def calculate_totals(df):
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()

    return income, expense


# Main application menu and program execution

def main():

    print("====="*10)
    print("             Personal Finance Tracker")
    print("====="*10)
    print("\n")

    initialize_csv()

    while True:
            try:

                print("""
                1. Add Income
                2. Add Expense
                3. View Transaction
                4. Summary
                5. Category Analysis
                6. Expense Search
                7. Data Quality Check
                8. Data Visualization
                9. Income and Expense Comparsion
                10. Exit
                        """)            

                choice=int(input("Enter Your choice: "))
            except ValueError:
                print("Enter Valid input")
                continue

            if choice==1:
                add_transaction("Income")
        
            elif choice==2:
                add_transaction("Expense")
                    
                        

            elif choice==3:
                with open(CSV_FILE,"r",newline="")as file:                                
                    reader=csv.DictReader(file)                            
                    rows=list(reader)

                if not rows:
                    print("no records")   

                else:
                    print("This is Your Transaction history")
                    for row in rows:                            
                        print(row["Type"], row["Amount"], row["Category"], row["Description"])
                                            
        
                                        
            elif choice==4:
                    
                    df = pd.read_csv(CSV_FILE)

                    income,expense=calculate_totals(df)

                
                    print("Your Summary")

                    print(f"Total Income:{income}" )
                    
                    print(f"Total Expense:{expense}")
                            
                    balance = income- expense

                    print("Final Balance:",balance)


            elif choice==5:
                df = pd.read_csv(CSV_FILE)
                print("\n")
                print("Total amount spent by category\n")
                expense=df[df["Type"]=="Expense"]
                if expense.empty:
                    print("No expense data available")
                else: 
                    print(expense.groupby("Category")["Amount"].sum())
                    print("\n")
                    print("Number of expenses by category\n")
                    print(expense["Category"].value_counts())


            elif choice==6:  
               while True:                  
                    try:
                        df = pd.read_csv(CSV_FILE)
                        threshold=int(input("Enter a threshold: "))
                        if threshold < 0:
                            print("Threshold cannot be negative")
                            continue
                        expenses=df[df["Type"]=="Expense"]
                        filtered_expenses=(expenses[expenses["Amount"] >= threshold].sort_values("Amount",ascending=False)[["Amount", "Category", "Description"]])
                        if expenses.empty:
                            print("No expense data available")
                            break
                        else:
                            if filtered_expenses.empty:
                                print("No matching expenses found")
                            else:
                                print(filtered_expenses)
                            break
                    except ValueError:
                        print("Please Enter a Interger")
                        continue
                    
                

            elif choice==7:
                df = pd.read_csv(CSV_FILE)
                print("Number of missing data:\n ",df.isna().sum())
                print("\n")
                        
                print("Potential duplicate transactions: \n",df.duplicated().sum())


            elif choice==8:
                df=pd.read_csv(CSV_FILE)
                expenses=df[df["Type"]=="Expense"]
                result=expenses.groupby("Category")["Amount"].sum()

                if result.empty:
                    print("No expense data available to visualize")

                else:
                    fig ,ax=plt.subplots(1,2, figsize=(12,5))

                    ax[0].bar(result.index,result.values)
                    ax[0].set_title("My Personal Expense")
                    ax[0].set_ylabel("Amount")
                    ax[0].set_xlabel("Category")
                    
            
                    ax[1].pie(result.values, labels=result.index, autopct="%1.1f%%")
                    ax[1].set_title("Expense Distribution")
                    plt.tight_layout()
                    plt.show()


            elif choice==9:
                df = pd.read_csv(CSV_FILE)
                income, expense = calculate_totals(df)
            
                fig, ax=plt.subplots(figsize=(5,6))

                ax.bar(["income","Expense"],[income,expense])
                ax.set_title("Income vs Expense")
                ax.set_ylabel("Amount")
                ax.set_xlabel("Transaction Type")

                plt.tight_layout()
                plt.show()

            elif choice==10:
                print("Thanks For Using")
                break
            else:
                print("Please enter the number inside the give list")


if __name__ == "__main__":
    main()