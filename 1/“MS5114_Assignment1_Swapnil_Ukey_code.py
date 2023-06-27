# Name : Swapnil Ukey
# Student id : 22220959
# Module Code : 2223-MS5114 Advanced Programming for Business Analytics

# Expected knowledge to resolve the assignment:
#  functions
#  strings
#  lists
#  tuples
#  dictionaries
#  conditionals
#  operators


# 1. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    if count < 1:
        answer = 'Number has to be greater than 0'
    elif count >= 10:
        answer = 'Number of donuts: many'
    else:
        answer = 'Number of donuts:' + ' ' + str(count)
    return answer


# 2. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s) < 2:
        return ''
    return s[0:2] + s[-2:]


# 3. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    # +++your code here+++
    first_char = s[0]
    answer = s.replace(first_char, '*')
    answer = first_char + answer[1:]
    return answer


# 4. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
    x = a[:2] + b[2:]
    y = b[:2] + a[2:]
    answer = y + " " + x
    return answer


# 5. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count = 0
    for ith in words:
        if len(ith) >= 2 and ith[-1:] == ith[:1]:
            count = count + 1
    return count


# 6. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyzxy', 'applap', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    first_list = sorted([x for x in words if "x" == x[0]])
    second_list = sorted(list(set(first_list) ^ set(words)))
    return first_list + second_list


# 7. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    len_tup = len(tuples)
    for ith in range(0, len_tup):
        for jth in range(0, len_tup - ith - 1):
            if tuples[jth][-1] > tuples[jth + 1][-1]:
                temp = tuples[jth]
                tuples[jth] = tuples[jth + 1]
                tuples[jth + 1] = temp
    return tuples


# 8. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    a_len = len(a)
    b_len = len(b)
    if a_len % 2 == 0:
        ath_index = a_len // 2
    else:
        ath_index = (a_len // 2) + 1

    if b_len % 2 == 0:
        bth_index = b_len // 2
    else:
        bth_index = (b_len // 2) + 1

    a_front = a[0:ath_index]
    a_back = a[ath_index:]

    b_front = b[0:bth_index]
    b_back = b[bth_index:]

    return a_front + b_front + a_back + b_back


# 9. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

def linear_merge(list1, list2):
    merge_list = list1 + list2

    def insertion_sort(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    return insertion_sort(merge_list)


# 10.
#  Write a function called accept_login(users, username, password) with three parameters:
# users a dictionary of username keys and password values (already created below),
# username a string for a login name and password a string for a password.
# The function should return
# True if the user exists and the password is correct and False otherwise.

users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}


def accept_login(users, user, password):
    if user in users.keys() and users[user] == password:
        return True
    else:
        return False


# 11.
# Write a function called
# find_value(mydict, val)
# that accepts a dictionary called mydict (already created below) and a variable of any type called
# val. The function should return a list of keys that map to the value val in mydict.
mydict = {
    "day1": "sunny",
    "day2": "rainy",
    "day3": "sunny"
}


def find_value(mydict, val):
    answer = []
    for day, weather in mydict.items():
        if weather == val:
            answer.append(day)
    return answer


# 12. Write a function to invert a dictionary. It should accept a dictionary as a parameter and return a
# dictionary where the keys are
# values from the input dictionary and the values are lists of keys from the input dictionary.
# For example, this input:
# { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
# should return this dictionary:
# { "value1" : ["key1", "key3"], "value2" : ["key2"] }

my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value1"
}


def invert_dict(my_dict):
    inverse_dict = {}
    for key, value in my_dict.items():
        inverse_dict[value] = inverse_dict.get(value, []) + [key]
    return inverse_dict


# 13.
# Write a function called word_frequencies(mylist) that accepts a list of strings
# called mylist and returns a dictionary where
# the keys are the words from mylist and the values are the number
# of times that word appears in mylist:
# INPUT
mylist = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e']


# OUTPUT
# {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}


def word_frequencies(mylist):
    output_dict = {}
    for item in mylist:
        if item in output_dict:
            output_dict[item] += 1
        else:
            output_dict[item] = 1

    return output_dict
