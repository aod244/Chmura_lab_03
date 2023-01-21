import random

def password_generator():
    while(True):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
        big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        print("Welcome to the PyPassword Generator!")
        nr_letters= int(input("How many small letters would you like in your password?\n"))
        nr_bigletters = int(input("How many big letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        sum_of_letters = ""
        for letter in range(0, nr_letters):
            l = random.choice(letters)
            sum_of_letters = sum_of_letters + l
        
        sum_of_big_letters = ""
        for big_letter in range(0, nr_bigletters):
            l = random.choice(big_letters)
            sum_of_big_letters = sum_of_big_letters + l
        
        sum_of_symbols = ""
        for symbol in range(0, nr_symbols):
            s = random.choice(symbols)
            sum_of_symbols = sum_of_symbols + s

        sum_of_numbers = ""
        for number in range(0, nr_numbers):
            n = random.choice(numbers)
            sum_of_numbers = sum_of_numbers + n
        
        password_lenght = nr_letters + nr_bigletters + nr_symbols + nr_numbers
        if password_lenght<8:
            print("Password must be at least 8 elements long")
        elif nr_letters < 1:
            print("Password must have at least one small letter")
        elif nr_bigletters< 1:
            print("Password must have at leat one capital letter")
        elif nr_symbols<1:
            print("Password must have at least one symbol")
        elif nr_numbers<1:
            print("Password must have at least one number")
        else:
            password = sum_of_letters + sum_of_symbols + sum_of_numbers + sum_of_big_letters
            password_list = list(password)
            random.shuffle(password_list)
            password = "".join(password_list)
            print(password)
            return password

if __name__ == "__main__":
    password_generator()