def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
      
number = float(input("Enter a number: "))
print(check_number(number))
