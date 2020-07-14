y = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]

for x in y:
    print(x)

# Can also be ran as shown below!
# print(*y, sep = "\n")

z = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]


def print_list(lst):
    for i in lst:
        if type(i) is not type([]):
            print(i)
        else:
            print_list(i)

print_list(z)