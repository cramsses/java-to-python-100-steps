def print_squares_of_numbers_up_to(number):
    r = range(number+1)
    for n in r:
        # print(n+"*"+n+"=")
        print(n*n)

def print_squares_of_even_numbers_up_to(number):
    r = range(2, number+1, 2)
    for n in r:
        # print(n+"*"+n+"=")
        print(n*n)

def print_numbers_in_reverse(number):
    r = range(number, 0-1, -1)
    for n in r:
        # print(n+"*"+n+"=")
        print(n)


#print_squares_of_numbers_up_to(10)
#print_squares_of_even_numbers_up_to(10)
print_numbers_in_reverse(10)