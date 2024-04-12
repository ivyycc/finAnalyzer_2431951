import unittest
from io import StringIO

#FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
#This class does not need to be edited
class FinancialTransaction:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        date, type, amount = parts[0], parts[1], float(parts[2])
        return FinancialTransaction(date, type, amount)

class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    #Adds together all transactions labeled "Income"
    def total_revenue(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Income")

    #Adds together all transactions labeled "Expense"
    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense")

    def convertedIncome(self): #added method
        var1 = self.total_revenue()*20 #Converts revenue from dollars to rands
        return(var1)

    def profit(self):
        var1 = self.convertedIncome()  #calls convertedincome so profit is calculated in rands
        var2 = self.total_expenses()
        return(var1 - var2)
    #write code for this method

    def profit_margin(self):
        var1 = self.profit()
        var2 = self.convertedIncome() 
        return(var1/var2)
    #write code for this method
    
    def average_transaction_amount(self):
        var1 = self.profit()
        return(var1/len(self.transactions))  #Comment3: len() Gets length of transactions data array as amount of transactions
    #write code for this method

    #Determines finalncial health and returns the corresponding string
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return("Healthy")
        elif profit<0 and profit >= -1000: #checks that ONLY values from -1 and -1000 are flagged as "warning" using logic operator 'and'
            return("Warning")
        else:
            return("Critical")

class TestFinancialHealthAnalyzer(unittest.TestCase):
    #Setup data allows for code to be tested without manually writing test transaction code for every test function. 
    #setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):

        #items were added to the array and some original values were changed 
        transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 600),
            FinancialTransaction("2024-01-02", "Expense", 15000),
            FinancialTransaction("2024-01-03", "Expense", 20000),
            FinancialTransaction("2024-01-04", "Income", 1500),
            FinancialTransaction("2024-01-05", "Income", 105),
            FinancialTransaction("2024-01-06", "Expense", 10000)
        ]
        self.transactions = transactions_data

    #Test case example that returns total revenue. Inluded as a tutorial for basis of other test cases.
    def test_total_revenue(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_revenue(), 2205)

    #added test for checking conversion method 
    def test_convertedIncome(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.convertedIncome(),44100)

    def test_total_expenses(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_expenses(), 45000)

    #This code needs to be completed
    def test_profit(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit(), -900)
        self.assertNotEqual(analyzer.profit(), 1700) #checking that conversion did happen with assertNotEqual
    #This code needs to be completed

    #added test for checking average transaction method
    def test_averagetransamount(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.average_transaction_amount(),-150)

    #added test for checking profit margin method
    def test_profitmargin(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertAlmostEqual(analyzer.profit_margin(), -0.02, places=2)#checks only to 2dp that the profit margins are as expected

    #added test for checking financial health method
    def test_financialhealth(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.financial_health(), "Warning")
        self.assertNotEqual(analyzer.financial_health(), "Healthy") #checks that the financial health is strictly 'warning' and not 'critical' or 'healthy'
        self.assertNotEqual(analyzer.financial_health(), "Critical")

    #Additional testing methods might be required. test_total_revenue can be changed/expanded



#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main    
if __name__ == '__main__':
    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ]
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)

    #added the calling of the respective methods so that the values are outputed as expected 
    print("Profit: ", analyzer.profit())
    print("Profit margin: " , analyzer.profit_margin())
    print("Average transaction amount: " ,analyzer.average_transaction_amount())
    print("Financial health: " , analyzer.financial_health())
    unittest.main(verbosity=2) #outputs which unit tests were run and the outcome (ok or FAIL) for each one