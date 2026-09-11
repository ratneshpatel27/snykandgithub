# VULNERABLE CODE
user_input = input("Enter an expression: ")
result = eval(user_input)  # An attacker can pass __import__('os').system('rm -rf /')
