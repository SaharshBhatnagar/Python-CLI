import random
import string

def generate_pass():

    chars_L = string.ascii_lowercase
    chars_U = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    allowed_lengths = [8, 16, 24, 32]
    
    while True:
        try:
            length_str = input(f"Choose the length for your password {allowed_lengths}: ")
            length = int(length_str)
            if length in allowed_lengths:
                break
            else:
                print("Invalid length. Please choose from the allowed options.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print()

    generate = (random.choices(chars_L, k=length // 4) +
                random.choices(chars_U, k=length // 4) +
                random.choices(digits, k=length // 4) +
                random.choices(punctuation, k=length// 4))

    random.shuffle(generate)

    password = "".join(generate)


    print(f"Your new password is: {password}")
    print(f"Length: {len(password)}")

generate_pass()

