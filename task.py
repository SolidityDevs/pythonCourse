number = [20,10,5]

number_to_multiply_with = 3

def A(num):
    global number_to_multiply_with
    number_to_multiply_with = num
    
    for n in number:
        print(f' {n} * {number_to_multiply_with} = { n *number_to_multiply_with}\n')

A(5)
