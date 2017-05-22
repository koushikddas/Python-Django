try:
    1/0
except ZeroDivisionError:
    print('You can\'t divide one by zero')

lst = [1,2,3,4,5]

try:
    lst[7]
except IndexError:
    print('That index is not in the list')

my_dict = {"a":1, "b":2, "c":3}
try:
    val = my_dict["d"]
except KeyError:
    print('The key is not present in the dictionary')
finally:
    print('Finally the final statemment is excuted')