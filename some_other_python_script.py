def some_function(some_list, some_number):
    new_list_for_person_a = []
    for idx in range(len(some_list)):
        new_list_for_person_a.append(some_list[idx] + some_number)
    return new_list_for_person_a