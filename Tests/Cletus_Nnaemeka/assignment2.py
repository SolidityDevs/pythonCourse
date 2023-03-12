x = 10
def complex_number_task():

    def multiply_by_y(y):
        global x
        x *= y

    multiply_by_y(3)
    answer = x + 2j

    my_array = [1, 'two', 5 + 3j, 'six', 7 - 2j, 'nine', 8]

    numbers = []
    strings = []

    for cont in my_array:
        if type(cont) == int or type(cont) == complex:
            numbers.append(cont)
        elif type(cont) == str:
            strings.append(cont)
    print("numbers:", numbers)
    print("strings:", strings)

complex_number_task()

