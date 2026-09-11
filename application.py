# Unsafe use of eval()
user_input = input("Enter a math expression: ")
result = eval(user_input)  # An attacker can input malicious system commands or code
print("Result:", result)
