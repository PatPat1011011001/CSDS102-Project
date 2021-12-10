from tabulate import tabulate
import os



#Input User




#Output Print
ds = "\u03B4"
table = [['x', 'P(x)', 'x\u00b2', 'x\u00b2*P(x)'],  [ds, 'Jane', 25, 56], ['Jennifer', 'Doe', 28, 45]]

print(tabulate(table, headers='firstrow', tablefmt='grid'))
os.system('cls') #Terminal Clear