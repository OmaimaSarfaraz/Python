# Password Strength Checker

def check_password(password):
    strength = 0

    if len(password) >= 8:    # Rule 1
        strength += 1

    if any(ch.islower() for ch in password):  # Rule 2
        strength += 1
    
    if any(ch.isupper() for ch in password):   # Rule 3
        strength += 1
    
    if any(ch.isdigit() for ch in password):    # Rule 4
        strength += 1
    
    if any(ch in "!@#$%^&*()_+-=" for ch in password):  # Rule 5
        strength += 1

    if strength == 5:
        return "Strong Password"
    elif 3 <= strength < 5:
        return "Medium Password"
    else:
        return "Weak Password"
    
# Main Program
pwd = input("Enter password: ")
print(check_password(pwd))