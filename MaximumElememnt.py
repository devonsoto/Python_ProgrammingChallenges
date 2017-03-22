#For each query print the maximum element in the stack
#first input is n number of queries
#the rest n lines are query statements
# 1 x, x is the putting on the stack
# 2 delete or pop stack
# 3 is print max


class stack:

    #initalizing an empty array
    def __init__(self):
        self.array = []
        print("Array: {}".format(self.array))

    #pushing a number onto the stack
    def push(self,number):
        self.array.append(number)
        print("After pushing: {}".format(self.array))

    #dequeuing a number from the stack
    def pop(self):
        return self.array.pop()
        print("After Popping: {}".format(self.array))


#making a object called hacker, initalizing a max list with 0
hacker = stack()
max_nums = [0]

n = int(input("Enter number of queries: "))

#as stated above we only have 3 options
for i in range(n):
    user_query = [int(n) for n in input().split()]
    assert user_query[0] <= 3

    #pushing x into the stack and adding to list if it the max
    if user_query[0] == 1:
        hacker.push(user_query[1])
        if user_query[1] >= max_nums[-1]:
            max_nums.append(user_query[1])

    #dequeuing the top from the stack using FIFO
    #seeing if that was the max element in the array
    elif user_query[0] == 2:
        if hacker.pop() == max_nums[-1]:
            max_nums.pop()

    #when query is 3 it prints the max in the array
    else:
        print(max_nums[-1])
