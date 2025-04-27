import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the 'bld' directory if it doesn't exist
if not os.path.exists('bld'):
    os.makedirs('bld')

# Function to generate the pie chart for expense share
def generate_pie_chart(data):
    # Calculate the total expenses and ratios
    total_expense = data[['Cost', 'Marketing_Spend', 'Employee_Salary', 'Operational_Expense']].sum(axis=1)
    data['Cost_Expense_Ratio'] = data['Cost'] / total_expense * 100
    data['Marketing_Spend_Ratio'] = data['Marketing_Spend'] / total_expense * 100
    data['Employee_Salary_Ratio'] = data['Employee_Salary'] / total_expense * 100
    data['Operational_Expense_Ratio'] = data['Operational_Expense'] / total_expense * 100

    # Calculate mean ratios for the pie chart
    labels = ['Cost', 'Marketing Spend', 'Employee Salary', 'Operational Expense']
    ratios = data[['Cost_Expense_Ratio', 'Marketing_Spend_Ratio', 'Employee_Salary_Ratio', 'Operational_Expense_Ratio']].mean()

    # Save the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(ratios, labels=labels, autopct='%1.1f%%', startangle=140, colors=['salmon', 'lightblue', 'lightgreen', 'yellow'])
    plt.title('Expense Share of Each Category')
    plt.savefig('bld/expense_share_pie_chart.png')  # Save to bld directory
    return ratios

# Function to generate the line plot for financial metrics
def generate_line_plot(data):
    # Prepare the data
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Save the line plot of financial metrics
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='Date', y='Revenue', data=data, label='Revenue')
    sns.lineplot(x='Date', y='Cost', data=data, label='Cost')
    sns.lineplot(x='Date', y='Marketing_Spend', data=data, label='Marketing Spend')
    sns.lineplot(x='Date', y='Employee_Salary', data=data, label='Employee Salary')
    sns.lineplot(x='Date', y='Operational_Expense', data=data, label='Operational Expense')
    sns.lineplot(x='Date', y='Profit', data=data, label='Profit', linestyle='--')

    plt.title('Financial Metrics Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount (€)')
    plt.xticks(rotation=0)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('bld/financial_metrics_trend.png')  # Save to bld directory

# Function to generate the bar chart for average expenses breakdown
def generate_bar_chart(data):
    avg_expenses = data[['Cost', 'Marketing_Spend', 'Employee_Salary', 'Operational_Expense']].mean()

    # Save the average expenses bar chart
    plt.figure(figsize=(8, 6))
    avg_expenses.plot(kind='bar', color=['salmon', 'lightblue', 'lightgreen', 'yellow'])
    plt.title('Average Expenses Breakdown')
    plt.ylabel('Amount (€)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('bld/average_expenses_breakdown.png')  # Save to bld directory
    return avg_expenses

# Function to save results into a text file
def save_results_to_file(ratios, avg_expenses, desc_stats):
    result_str = (
        f"Cost Expense Ratio: {ratios['Cost_Expense_Ratio']:.1f}%\n"
        f"Marketing Spend Ratio: {ratios['Marketing_Spend_Ratio']:.1f}%\n"
        f"Employee Salary Ratio: {ratios['Employee_Salary_Ratio']:.1f}%\n"
        f"Operational Expense Ratio: {ratios['Operational_Expense_Ratio']:.1f}%\n\n"
    )

    # Convert the summary statistics to a string format
    desc_stats_str = f"Summary Statistics:\n{desc_stats[['mean', '50%', 'std', 'min', 'max']].to_string()}\n\n"

    # Save all the results to a text file
    with open('bld/financial_analysis_results.txt', 'w') as f:  # Save to bld directory
        f.write(result_str)
        f.write(desc_stats_str)
        f.write(f"Average Expenses: {avg_expenses.to_string()}\n")

    print("Analysis complete. Results saved to files.")

# Main function to run the entire analysis
def generate_financial_report(csv_file_path):
    # Load the data
    data = pd.read_csv(csv_file_path)

    # Generate pie chart and get ratios
    ratios = generate_pie_chart(data)

    # Generate line plot
    generate_line_plot(data)

    # Generate bar chart and get average expenses
    avg_expenses = generate_bar_chart(data)

    # Generate summary statistics
    desc_stats = data.describe().T

    # Save the results to a file
    save_results_to_file(ratios, avg_expenses, desc_stats)

# Example usage of the function:
generate_financial_report('financial_data.csv')
