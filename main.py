# Monthly expenses
monthly_expenses = {
    'rent': 1200,
    'utilities': 300,
    'transport': 450,
    'food': 600,
    'entertainment': 110,
    'clothing': 220,
    'health': 30,
    'internet': 60,
    'education': 200,
    'other': 100
}

# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    x = list(monthly_expenses.values())
    return(sum(x)) 

# Find the least expensive expense
def least_expensive(monthly_expenses: dict) -> str:
    """
    Find the least expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        least_expensive: least expensive expense
    """
    mx = list(monthly_expenses.values())[0]
    answer = list(monthly_expenses.keys())[0]
    for k, v in monthly_expenses.items():
        if mx  > v:
            m=v
        answer = k
    return answer

# Find the most expensive expense
def most_expensive(monthly_expenses: dict) -> str:
    """
    Find the most expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        most_expensive: most expensive expense
    """
    mx = 0
    for k, v in monthly_expenses.items():
        if mx  > v:
            m=v
        return k