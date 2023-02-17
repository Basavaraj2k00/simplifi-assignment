def inr_notation(number):
    # Convert the number to a string
    number_string = str(number)

    if '.' in number_string:
        # if number has decimal point then split and assign to new vars
        number = number_string.split('.')
        num_part = number[0]
        dec_part = number[1]
        last_3 = num_part[-3:]
    else:
        num_part = number_string
        dec_part = False

    if len(num_part) > 3:
        num_str = num_part[:-3]
        last_3 = num_part[-3:]
    else:
        num_str = num_part
        


    # Split the integer string into groups of 2 from the right
    num_groups = []
    while num_str:
        num_groups.append(num_str[-2:])
        num_str = num_str[:-2]

    if len(num_part) > 3:
    # Join the groups of 2 with a comma separator
        int_part = ",".join(reversed(num_groups))
    else:
        #if number is less than 3 digits no need of ,
        int_part = "".join(reversed(num_groups))


    #if u want the dec digits to be only first two digits then
    # dec_part = dec_part[:2]



    #note ₹ symbol only works in vs code
    if dec_part and len(num_part) <= 3: 
        inr_str = "₹" + int_part  + "." + dec_part
    elif dec_part and len(num_part) > 3:
        inr_str = "₹" + int_part + "," + last_3 + "." + dec_part
    elif len(num_part) > 3:
        inr_str = "₹" + int_part + "," + last_3
    else:
        inr_str = "₹" + int_part
    return inr_str

number = 1234567.89
result = inr_notation(number)
print(result)

