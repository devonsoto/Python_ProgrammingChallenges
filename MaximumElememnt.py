#For each query print the maximum element in the stack
#first input is n number of queries
#the rest n lines are query statements
# 1 x x is the putting on the stack
# 2 delete or pop stack
# 3 is print max


class stack:
    def __init__(self):
        self.array = []
        print("Array: {}".format(self.array))

    def push(self,number):
        self.array.append(number)
        print("After pushing: {}".format(self.array))

    def pop(self):
        return self.array.pop()
        print("After Popping: {}".format(self.array))



hacker = stack()
max_nums = [0]

n = int(input("Enter number of queries"))

for i in range(n):
    user_query = [int(n) for n in input().split()]
    assert user_query[0] <= 3

    if user_query[0] == 1:
        hacker.push(user_query[1])
        if user_query[1] >= max_nums[-1]:
            max_nums.append(user_query[1])

    elif user_query[0] == 2:
        if hacker.pop() == max_nums[-1]:
            max_nums.pop()

    else:
        print(max_nums[-1])
