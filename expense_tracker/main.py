# import natives packages
import os
import json
from datetime import datetime

#############################
# VARIABLES
#############################

file_path = os.path.join(os.getcwd(), "expenses.json") # "$PWD/expenses.json"
budget_path = os.path.join(os.getcwd(), "budget.json") # "$PWD/budget.json"

#############################
# Budget Functions
#############################

# get budget from json file
def get_budgets() -> dict:
    if os.path.exists(budget_path):
        with open(budget_path, "r") as json_file:
            return json.load(json_file)
    else:
        return {}
    
budget_dict = get_budgets()
    
# Save budget to json file
def save_budget(budget: dict) -> None:
    with open(budget_path, "w") as json_file:
        json.dump(budget, json_file, indent=2)

# Add a budget for a specific month and year
def add_budget_for_month(budget: float, month: int, year: int) -> dict:
    # verify the budget is a number
    if not isinstance(budget, (int, float)):
        return {"error": "budget must be a number"}
    
    # verify if the budget is positive
    if budget <= 0:
        return {"error": "budget must be a positive number"}
    
    id = f"{year}-{month:02d}"

    # check if the budget for the month and year already exist, if exist we will update it, if not we will add it
    if id in budget_dict:
        budget_dict[id] = budget
        save_budget(budget_dict)
        return {f"updated_budget_for_{year}_{month:02d}": budget}

    budget_dict[id] = budget
    save_budget(budget_dict)
    return budget_dict

# Update the budget for a specific month and year
def update_budget_for_month(budget: float, month: int, year: int) -> dict:
    # verify the budget is a number
    if not isinstance(budget, (int, float)):
        return {"error": "budget must be a number"}
    
    # verify if the budget is positive
    if budget <= 0:
        return {"error": "budget must be a positive number"}
    
    id = f"{year}-{month:02d}"
    amount = budget
    save_budget({id: amount})
    return {f"updated_budget_for_{year}_{month:02d}": amount}

#############################
# Expense Functions
#############################

# get json file content
def get_json_content() -> dict:
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    else:
        return {}

espense_dict = get_json_content()

# Save to json file
def save_to_json(data: dict) -> None:
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

# List all espense
def list_all_espenses() -> dict:
    return get_json_content()

# Print list all espenses
def print_espenses_list() -> dict:
    all_local_espenses = get_json_content()
    expenses_text = """ID | Date       | Category         | Description           | Amount \n-----------------------------------------------"""
    for espense_id, espense in all_local_espenses.items():
        expenses_text += f"\n{espense_id} | {espense['date']} | {espense['category']:<15} | {espense['description']:<20} | {espense['amount']}"
    return expenses_text

# Summary of espenses amount
def summary_espenses_amount() -> dict:
    all_local_espenses = get_json_content()
    total_amount = sum(espense["amount"] for espense in all_local_espenses.values())
    return total_amount

# Summary of espenses amount by month
def summary_espenses_amount_by_month() -> dict:
    all_local_espenses = get_json_content()
    summary = {}
    for espense in all_local_espenses.values():
        month = espense["date"][:7] # get the month in format YYYY-MM
        if month not in summary:
            summary[month] = 0
        summary[month] += espense["amount"]
    return summary

""" 
    Summary of espenses amount for a specific month. 
    example: summary_espenses_amount_for_month(1, 2024) 
    will return the total amount of espenses for the month of January of 2024
"""
def summary_espenses_amount_for_month(month: int, year: int) -> dict:
    all_local_espenses = get_json_content()
    month_str = f"{year}-{month:02d}"
    total_amount = sum(espense["amount"] for espense in all_local_espenses.values() if espense["date"][:7] == month_str)
    return total_amount

# Adding new espense 
def add_espense(category: str, description: str, amount: float) -> dict:

    # verify the amount is a number
    if not isinstance(amount, (int, float)):
        return {"error": "amount must be a number"}
    
    # verify if the amount is positive
    if amount <= 0:
        return {"error": "amount must be a positive number"}
    
    month_sumary_amount = summary_espenses_amount_for_month(datetime.now().month, datetime.now().year)
    budget_for_month = budget_dict.get(f"{datetime.now().year}-{datetime.now().month:02d}", 0)
    
    if month_sumary_amount + amount > budget_for_month:
        return {"error": "adding this espense will exceed the budget for this month"}
    
    id = len(espense_dict) + 1
    """
        some times the id can be repeated if we delete an espense and add a new one, 
        so we need to check if the id is already exist in the espense_dict
    """
    while str(id) in espense_dict:
        id += 1

    category = category
    description = description
    now_date = datetime.now().strftime("%Y-%m-%d")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    espense_dict[id] = {
        'date': now_date,
        "category": category,
        "description": description,
        "amount": amount,
        "created_at": created_at,
        "updated_at": updated_at
    }

    save_to_json(espense_dict)

    return espense_dict
     
# Update existing espense description
def update_espense_description(espense_id : int, new_description : str) -> dict:
    local_espense_dict = get_json_content()
    if str(espense_id) in local_espense_dict:
        local_espense_dict[str(espense_id)]["description"] = new_description
        local_espense_dict[str(espense_id)]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_json(local_espense_dict)
        return local_espense_dict
    else:
        return {"error": "espense not found"}

def update_espense_amount(espense_id : int, new_amount : float) -> dict:
    # verify the new ammount is a number
    if not isinstance(new_amount, (int, float)):
        return {"error": "amount must be a number"}
    
    # verify if the new amount is positive
    if new_amount <= 0:
        return {"error": "amount must be a positive number"}

    local_espense_dict = get_json_content()
    if str(espense_id) in local_espense_dict:
        local_espense_dict[str(espense_id)]["amount"] = new_amount
        local_espense_dict[str(espense_id)]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_json(local_espense_dict)
        return local_espense_dict
    else:
        return {"error": "espense not found"}

# Delete espense
def delete_espense(espense_id : int) -> dict:
    local_espense_dict = get_json_content()
    if str(espense_id) in local_espense_dict:
        del local_espense_dict[str(espense_id)]
        save_to_json(local_espense_dict)
        return local_espense_dict
    else:
        return {"error": "espense not found"}

# Export data to a csv file
def export_to_csv(file_name: str) -> None:
    all_local_espenses = get_json_content()
    with open(file_name, "w") as csv_file:
        csv_file.write("ID,Date,Category,Description,Amount\n")
        for espense_id, espense in all_local_espenses.items():
            csv_file.write(f"{espense_id},{espense['date']},{espense['category']},{espense['description']},{espense['amount']}\n")


print(add_espense("Dansing club bill", "monthly subscription", 500))