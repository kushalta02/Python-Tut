def print_formatted(number):
    # your code goes here
    width=len(bin(number))-2
    for i in range(1,number+1):
        decimal = str(i)
        octal = oct(i)[2:]  # Remove '0o' prefix
        hexadecimal = hex(i)[2:].upper()  # Remove '0x' prefix and capitalize
        binary = bin(i)[2:]  # Remove '0b' prefix
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n) 