### For BSIT 1-1 ###
### Author: Ivan/Kuraiyume ###

banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠤⠤⠤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⢦⣤⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⢋⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠙⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠀⠉⠓⠦⣤⣤⣤⣤⣤⣤⣄⣀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣷⡄⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀
⠀⠀⣠⠞⠁⠀⠀⣀⣠⣏⡀⠀⢠⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⡃⠀⠀⠄⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆
⢀⡞⠁⠀⣠⠶⠛⠉⠉⠉⠙⢦⡸⣿⡿⠀⠀⠀⡄⢀⣀⣀⡶⠀⠀⠀⢀⡄⣀⠀⣢⠟⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃
⡞⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⢳⢀⣠⠀⠀⠀⠉⠉⠀⠀⣀⠀⠀⠀⢀⣠⡴⠞⠁⠀⠀⠈⠓⠦⣄⣀⠀⠀⠀⠀⣀⣤⠞⠁⠀
⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠁⠀⢀⣀⣀⡴⠋⢻⡉⠙⠾⡟⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠉⠉⠀⠀⠀⠀
⠘⣦⡀⠀⠀⠀⠀⠀⠀⣀⣤⠞⢉⣹⣯⣍⣿⠉⠟⠀⠀⣸⠳⣄⡀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠒⠒⠒⠒⠚⠋⠁⠀⡴⠋⢀⡀⢠⡇⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⢀⡾⠋⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠉⠋⠻⣄⠀⠀⠀⠀⠀⣀⣠⣴⠞⠋⠳⠶⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠦⢤⠤⠶⠋⠙⠳⣆⣀⣈⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //=2
    return binary

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    power = 0
    for digit in reversed(hexadecimal):
        if digit.isdigit():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += (ord(digit.upper()) - ord('A') + 10) * (16 ** power)
        power += 1
    return decimal

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def octal_to_decimal(octal):
    for digit in str(octal):
        if digit not in "01234567":
            print("Invalid octal number. Please enter a number within the range of 0-7.")
            return None

    decimal = 0
    power = 0
    for digit in reversed(octal):
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = decimal_to_octal(decimal)
    return octal

def octal_to_binary(octal):
    for digit in str(octal):
        if digit not in "01234567":
            print("Invalid octal number. Please enter a number within the range of 0-7.")
            return None
    decimal = octal_to_decimal(octal)
    binary = decimal_to_binary(decimal)
    return binary

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = decimal_to_binary(decimal)
    return binary

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

def octal_to_hexadecimal(octal_number):
    for digit in str(octal_number):
        if digit not in "01234567":
            print("Invalid octal number. Please enter a number within the range of 0-7")
            return None
    decimal_number = int(str(octal_number), 8)
    hexadecimal_number = hex(decimal_number)[2:].upper()
    return hexadecimal_number

def hexadecimal_to_octal(hexadecimal_number):
    decimal_number = int(str(hexadecimal_number), 16)
    octal_number = oct(decimal_number)[2:]
    return octal_number

def text_to_binary(text):
    binary = ''
    for char in text:
        binary += format(ord(char), '08b') + ' '
    return binary.rstrip()

def binary_to_text(binary):
    binary = binary.replace(' ', '')
    text = ''
    for i in range(0, len(binary), 8):
        char_binary = binary[i:i+8]
        text += chr(int(char_binary, 2))
    return text

def main():
    print(banner)
    print("For BSIT 1-1 lang to bruh")
    print("0. Decimal to Binary")
    print("1. Binary to Decimal")
    print("2. Binary to Hexadecimal")
    print("3. Hexadecimal to Binary")
    print("4. Binary to Octal")
    print("5. Octal to Binary")
    print("6. Decimal to Hexadecimal")
    print("7. Hexadecimal to Decimal")
    print("8. Decimal to Octal")
    print("9. Octal to Decimal")
    print("A. Text to Binary")
    print("B. Binary to Text")
    print("C. Octal to Hexadecimal")
    print("D. Hexadecimal to Octal")
    while True:
        choice = input("Enter your choice: ")
        if choice == '':
            continue
        if choice == '0':
            decimal = int(input("Enter a decimal number: "))
            print(f"Binary: {decimal_to_binary(decimal)}")
        elif choice == '1':
            binary = input("Enter a binary number: ")
            print(f"Decimal: {binary_to_decimal(binary)}")
        elif choice == '2':
            binary = input("Enter a binary number: ")
            print(f"Hexadecimal: {binary_to_hexadecimal(binary)}")
        elif choice == '3':
            hexadecimal = input("Enter a hexadecimal number: ")
            print(f"Binary: {hexadecimal_to_binary(hexadecimal)}")
        elif choice == '4':
            binary = input("Enter a binary number: ")
            print(f"Octal: {binary_to_octal(binary)}")
        elif choice == '5':
            octal = input("Enter an octal number: ")
            print(f"Binary: {octal_to_binary(octal)}")
        elif choice == '6':
            decimal = int(input("Enter a decimal number: "))
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
        elif choice == '7':
            hexadecimal = input("Enter a hexadecimal number: ")
            print(f"Decimal: {hexadecimal_to_decimal(hexadecimal)}")
        elif choice == '8':
            decimal = int(input("Enter a decimal number: "))
            print(f"Octal: {decimal_to_octal(decimal)}")
        elif choice == '9':
            octal = input("Enter an octal number: ")
            print(f"Decimal: {octal_to_decimal(octal)}")
        elif choice.upper() == 'A':
            text = input("Enter text: ")
            print(f"Binary: {text_to_binary(text)}")
        elif choice.upper() == 'B':
            binary = input("Enter binary: ")
            print(f"Text: {binary_to_text(binary)}")
        elif choice.upper() == 'C':
            octal = input("Enter an octal number: ")
            print(f"Hexadecimal: {octal_to_hexadecimal(octal)}")
        elif choice.upper() == 'D':
            hexadecimal = input("Enter a hexadecimal number: ")
            print(f"Octal: {hexadecimal_to_octal(hexadecimal)}")
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()