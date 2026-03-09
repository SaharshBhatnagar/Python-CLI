def is_valid_number():

    card_number = input("Enter a card number ##: ")

    card_number = card_number.replace("-", "")
    card_number = card_number.replace(" ", "")

    # Reverse Card Number
    rev_card_number = card_number[::-1]

    sum_odd_digits = 0
    sum_even_digits = 0
    for num  in rev_card_number[::2]:
          sum_odd_digits += int(num) 

    for num in rev_card_number[1::2]:
        num = int(num) * 2
        if num > 9:
            sum_even_digits += (num - 9)
        else:
            sum_even_digits += num

    total_sum = sum_odd_digits + sum_even_digits

    if total_sum % 10  == 0:
        return f"{card_number} is a Valid Card Number"
    else: 
        return f"{card_number} is Not A Valid Card Number"

print(is_valid_number())