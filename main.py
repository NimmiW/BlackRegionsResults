from show_results import plot_results
"""
year = 2012
from_month = 2
to_month = 5
currency = "EURUSD"
"""

print("Please Enter the Range of months")
year = int(input("Year : "))
from_month = int(input("From Month : "))
to_month = int(input("To Month : "))
currency = "EURUSD"
print("Currency : EURUSD (by default)")
print("Generating the graph...")
#currency = input("Currency : EURUSD / GBPUSD ?")

plot_results(year, from_month, to_month, currency)
