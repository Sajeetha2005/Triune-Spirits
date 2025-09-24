def check_password_strength(pwd: str ):
        length_ok = len(pwd) >= 8 
        has_digit = any(ch.isdigit() for ch in pwd) 
        has_upper = any(ch.isupper() for ch in pwd) 
        has_lower = any(ch.islower() for ch in pwd)
        has_special = any(not ch.isalnum() for ch in pwd)
        if length_ok and has_digit and has_upper and has_lower and has_special: 
                   return "Strong Password" 
        else: 
                   return "Weak Password"
Password = input("Enter password:")
strength = check_password_strength(Password) 
print(strength)
