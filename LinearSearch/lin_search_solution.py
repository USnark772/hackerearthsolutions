"""
Author: Phillip Riskin
Date: 2020
Project: hackerearth.com practice.
Problem: Tutorial practice problem on Linear Search.

You have been given an array of size N consisting of integers. In addition you have been given an element M you need
 to find and print the index of the last occurrence of this element M in the array if it exists in it, otherwise
  print -1. Consider this array to be 1 indexed.

Input Format:
The first line consists of 2 integers N and M denoting the size of the array and the element to be searched for in the
 array respectively . The next line contains N space separated integers denoting the elements of of the array.

Output Format
Print a single integer denoting the index of the last occurrence of integer M in the array if it exists, otherwise
 print -1.

1 <= N <= 10^5
1 <= A[i] <= 10^9
1 <= M <= 10^9

Sample input:
5 1
1 2 3 4 1

Expected output
5
"""


def find_last_index_of_num(len: int, num: int, nums: list) -> int:
    """
    Calculate the index of the last occurrence of the target number in the given list of numbers. -1 if no occurrence.
    The return value of this function assumes 1 based list indexing.
    :param len: The length of the list of numbers.
    :param num: The target number.
    :param nums: The list of numbers.
    :return int: The index of the last occurrence of the target number. -1 if no occurrence.

    >>> find_last_index_of_num(5, 1, [1, 2, 3, 4, 1])
    5

    >>> find_last_index_of_num(5, 1, [2, 3, 4, 5, 6])
    -1

    >>> find_last_index_of_num("hello", "world", ["hi", "hi", "hello", "world"])
    Traceback (most recent call last):
        ...
    ValueError: n must be integer.
    >>> find_last_index_of_num(5, "Hi", [5, 2, 2, "Bye"])
    Traceback (most recent call last):
        ...
    ValueError: m must be integer.
    >>> find_last_index_of_num(5, 1, [5, 2, 2, "Bye"])
    Traceback (most recent call last):
        ...
    ValueError: nums must all be integers.
    """
    ret = -1
    if type(len) != int:
        raise ValueError("n must be integer.")
    if type(num) != int:
        raise ValueError("m must be integer.")
    for x in nums:
        if type(x) != int:
            raise ValueError("nums must all be integers.")
    for i in range(len):
        if nums[i] == num:
            ret = i + 1
    return ret


def get_input() -> (int, int, list):
    """
    Get user input in the form of two lines, the first being n and m, the second being the array of numbers.
    :return (int, int, list): (n, m, num_list)
    """
    usr_input_1 = input()
    n, m = usr_input_1.split(" ")
    n = int(n)
    m = int(m)
    user_input_2 = input()
    str_list = user_input_2.split(" ")
    num_list = [int(x) for x in str_list]
    return n, m, num_list


def main():
    """
    Get input, calculate result, and print output.
    :return None:
    """
    n, m, num_list = get_input()
    output = find_last_index_of_num(n, m, num_list)
    print(output)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()
