def statement_generator(text, decoration) :

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

def intructions():
    statement_generator("intructions / information", "=")
    print()
    print("please choose a data type (image / text / integer)")
    print()
    print("this program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assyne that ascii endoding is being used (8 bits per character).")
    print()
    print("complete as many calculations as necessary, pressing <enter> at end of each calculation or any key to quit.")
    print()
    return ""

def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter an integer that is more than "
        "(or equal to) {}".format(low)

        try: 

            response = float(input(question))

            if response > low:
                return response
            
            else:
                print(error)
                print() 

        except ValueError: 
            print(error)

def get_factors (to_factor): 

    stop = int(to_factor**(0.5))

    factors_list = []

    for item in range(1, stop + 1):
        is_factor =to_factor % item

        if is_factor == 0:

            factor_2 = int(to_factor / item)

            factors_list.append(item)

            if factor_2 not in factors_list:
                factors_list.append(factor_2)

    factors_list.sort()
    return(factors_list)


statement_generator("factors calculator", "-")

first_time = input("press <enter> to see the instructions or any key to continue")

if first_time == "":
    intructions()

keep_going = ""
while keep_going == "":

    comment = ""

    var_to_factor = num_check("number?, 0 ")

    if var_to_factor !=1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "one is unity! it only has one factor. itself :)"
    
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) %2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    if var_to_factor == 1:
        heading = "one is special..."
    
    else:
        heading = "factors of {}".format(var_to_factor)

    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("press <enter to continue or any key to quit ")
    print()

print()
print("thank you for using the factors calculator")
print()