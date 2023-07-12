def get_second_element(mylist):
    if len(mylist) > 1:
        return mylist[1]
    else:
        return 'List was too small"'
    
mylist = get_second_element([2,4,7])
print(mylist)

mylist = get_second_element([7])
print(mylist)