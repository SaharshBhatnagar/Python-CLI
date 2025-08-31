import random
import string

def generate_pass():
    character = string.ascii_letters + string.digits + string.punctuation
    generate = "".join(random.choice(character) for i in range(16))
    print(generate)

generate_pass()