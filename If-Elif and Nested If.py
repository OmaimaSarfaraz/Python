# If-Elif-Else
marks = 90  

# Check multiple conditions one by one
if marks >= 90:  
    print("Grade: A+")   # Runs if marks are 90 or above
elif marks >= 75:  
    print("Grade: A")    # Runs if marks are 75 or above
elif marks >= 60:  
    print("Grade: B")    # Runs if marks are 60 or above
else:  
    print("Grade: C")    # Runs if none of the above conditions are True


# Nested If
num = -15  

# First check if number is positive
if num > 0:  
    # If number is positive, check if it is even or odd
    if num % 2 == 0:  
        print("Positive Even Number")   # Runs if divisible by 2
    else:  
        print("Positive Odd Number")    # Runs if not divisible by 2
else:  
    print("Negative Number")   # Runs if number is not positive


#Nested If-Elif
age = 20  
citizen = False  

# First check if user is a citizen
if citizen:  
    # Now check different age categories
    if age >= 18:  
        print("You are eligible to vote")  
    elif age >= 15:  
        print("You are a young citizen, wait until 18")  
    else:  
        print("You are too young to vote")  
else:  
    print("Only citizens can vote")  # Runs if main condition is False