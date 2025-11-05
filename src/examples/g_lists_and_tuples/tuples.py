#
def create_tuple():
    my_tuple = (8, 5, 9, 1, 4)
    print(my_tuple)

def loop_tuple_w_while():
    my_tuple = (8, 5, 9, 1, 4)
    index = 0

    while(index < len(my_tuple)):
        print(my_tuple[index])
        index += 1 

def loop_tuple_w_for_range():
    my_tuple = (8, 5, 9, 1, 4)

    for i in range(0, len(my_tuple)):
        print(my_tuple[i])

    
def loop_tuple_for():
    my_tuple = (8, 5, 9, 1, 4)

    for element in my_tuple:
        print(element)
