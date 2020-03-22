
def binary_search(array, number, result_index=0):
    search_index = int(round((len(array))/2))
    if number < array[search_index]:
        array = array[:search_index]
        if len(array) == 0:
            return False, -1
        else:
            return binary_search(array, number, result_index)
    elif number > array[search_index]:
        array = array[search_index:]
        if len(array) == 1:
            return False, -1
        else:
            result_index += search_index
            return binary_search(array, number, result_index)
    else:
        result_index += search_index
        return True, result_index


array = [x for x in range(1, 100, 2)]

search = binary_search(array, 89)
print(search, array[search[1]])
