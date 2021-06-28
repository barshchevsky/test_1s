import numpy as np

M = int(input("Enter the number of rows:"))
N = int(input("Enter the number of columns:"))


array = np.random.randint(100, size=(M, N))

answer = input("do you want save this file? ")
if answer == 'yes':

    a = str(input("name of csv: "))
    np.savetxt(a, array, delimiter=",", fmt="%d")
    if not ".csv" in a:
        a += ".csv"
elif answer == 'no':
    print(array)
else:
    print("error")