def list_product(my_list):
    result = 1
    for number in my_list:
        result *= number
    return result

if __name__ == 'main':
    print(list_product([2, 3]))
    print(list_product([2, 10, 15]))