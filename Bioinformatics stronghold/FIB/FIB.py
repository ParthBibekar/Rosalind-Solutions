number_of_months = int(input("Number of months: "))
k = int(input("Number of pairs every pair produces: "))
n1,n2 = 1,1
counted = 0

while counted < number_of_months:
    print(n1)
    new_number = k*n1 + n2
    n1 = n2
    n2 = new_number
    counted += 1
