def some_function(some_list, some_number):
    new_list = []
    for idx in range(len(some_list)):
        new_list.append(some_list[idx] + some_number)
    return new_list