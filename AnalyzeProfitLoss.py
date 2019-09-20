import numpy as np
#
# Scenario: You are a Data Scientist working for a consulting firm. One of your
# colleagues from the Auditing department has asked you to help them assess the
# financial statement of organisation X.
# You have been supplied with two vectors of data: monthly revenue and monthly
# expenses for the financial year in question. Your task is to calculate the following
# financial metrics:
# - profit for each month
# - profit after tax for each month (the tax rate is 30%)
# - profit margin for each month - equals to profit after tax divided by revenue
# - good months - where the profit after tax was greater than the mean for the year
# - bad months - where the profit after tax was less than the mean for the year
# - the best month - where the profit after tax was max for the year
# - the worst month - where the profit after tax was min for the year
# R Programming A-Z™ © Kirill Eremenko
# All results need to be presented as vectors.
# Results for dollar values need to be calculated with $0.01 precision, but need to be
# presented in Units of $1,000 (i.e. 1k) with no decimal points.
# Results for the profit margin ratio need to be presented in units of % with no
# decimal points.
# Note: Your colleague has warned you that it is okay for tax for any given month to be
# negative (in accounting terms, negative tax translates into a deferred tax asset)


revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
profit=[]
profitAfterTax=[]
goodMonths=[]
badMonths=[]
length=len(revenue);
print(length);

for index in range(0,length):
   # profit.insert(index,round(revenue[index]-expenses[index],2))
   # profitAfterTax.insert(index,round(profit[index]*0.7,2))
   profit.append( round(revenue[index] - expenses[index], 2))
   profitAfterTax.append(round(profit[index] * 0.7, 2))

mean=np.mean(profitAfterTax)
print ("Profit for each month ===>")
print (profit)

print ("Profit after tax for each month ===>")
print (profitAfterTax)

print ("Mean value for profit after tax for each month ===>",round(mean,2))
print ("Best month for profit after tax ===>",np.max(profitAfterTax))
print ("Worst month for profit after tax ===>",np.min(profitAfterTax))

for index in range(length):
   if (mean>profitAfterTax[index]):
       count=0
       badMonths.append(profitAfterTax[index])
       count=count+1
   else:
       goodCounter=0
       goodMonths.append( profitAfterTax[index])
       goodCounter=goodCounter+1

print("Bad months",badMonths)
print("Good months",goodMonths)
