#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''Divides elements in first list by corresponding elements in second

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: number of elements to divide
    Returns: a new list of list_length length containing the division result
    '''
    new_list = []
    for i in range(0, list_length):
        try:
            n = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            n = 0
            print("division by 0")
        except TypeError:
            n = 0
            print("wrong type")
        except IndexError:
            n = 0
            print("out of range")
        finally:
            new_list.append(n)
    return new_list
