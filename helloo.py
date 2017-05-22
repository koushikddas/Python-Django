my_list = ['python','ruby','java','php']


def print_list():
    for item in range(5):
        print(item)


print_list()

print('My Fav Programming Lang Is: ', my_list[0])

my_list.insert(0,'javascript')
print(my_list)