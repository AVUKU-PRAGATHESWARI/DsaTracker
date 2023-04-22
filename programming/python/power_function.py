def pow(base,power):
    power_of_number=1
    for i in range(power):
        power_of_number*=base
    return power_of_number
print("Enter the base")
base=int(input())
print("Enter the power")
power=int(input())
result=pow(base,power)
print(result)