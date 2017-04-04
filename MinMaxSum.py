# Author Devon Soto
# HackerRank Challenge


# Description
# Given five positive integers, find the minimum and maximum values that can
# be calculated by summing exactly four of the five integers. Then print the
# respective minimum and maximum values as a single line of two space-separated
# long integers.


def min_max_sum():

    # getting input of 5 integers
    print("Enter number greater than 0")
    a,b,c,d,e = input("Enter 5 integer seperated by a space: ").strip().split(' ')
    a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

    assert a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0

    # sum of the five integers
    total = a + b + c + d + e
    print("Total: {total}".format(total=total))
    num_list = [a, b, c, d, e]
    num_integers = 5

    # set max and min num to the first difference of the list
    min_num = total - num_list[0]
    max_num = total - num_list[0]

    # loop through the created list and subtract each postion
    for i in range(1, num_integers):
        sum_num = total - num_list[i]
        print("New sum: {}".format(sum_num))

        # check to if the difference is now the min or max
        if sum_num < min_num:
            min_num = sum_num
            print("min_num is now: {}".format(min_num))

        if sum_num > max_num:
            max_num = sum_num
            print("max_num is now: {}".format(max_num))


    print("{min} {max}".format(min=min_num, max=max_num))

min_max_sum()
