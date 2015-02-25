# -*- coding: utf-8 -*-

"""
Introduction to debugging in Python (+ CodeFights!). Pyladies February 2015 meetup.

INSTRUCTIONS:

This script contains 3 different classes: LevelOne for some easy exercises,
LevelTwo for more complex exercises and CodeFights for some exercises proposed
by CodeFights, to warm up.

Each class contains functions corresponding to the exercises to solve. Their
docstrings describe what you are suposed to do. Some of them are not working at
all, others are showing wrong results. Your job is to take a look and fix them!

To do so, we recommend you that you work one function at a time, commenting the
others so you can focus on one problem at a time. Comment and uncomment lines
of the main function as you go.

To execute the file:
$ python debugging_exercises.py


Solve all the exercises in pairs or by yourself, ask all the questions you have
and HAVE FUN!
"""

import sys


class LevelOne:
    """
    """

    def exercise1(self, length):
        """ creates a list of length 'length' with numbers in range(length) and
        prints the content of the last position
        """
        a_list = range(length)
        print a_list[length]
        return

    def exercise2(self, param1, param2):
        """ prints the division of the two input parameters
        """
        print param1 / param2
        return

    def exercise3(self, param1, param2, param3):
        """ prints the maximum number of the three input parameters
        """
        if param1 > param2:
            if param1 > param3:
                maximum = param1
            maximum = param2
        if param2 > param3:
            maximum = param2
        maximum = param3
        print "max(", param1, ", ", param2, ", ", param3, ") = ", maximum


class LevelTwo:
    """
    """

    def auxiliar_exercise1(self, param1, param2, param3):
        """ returns the sum of the squares of the three input parameters
        """
        result = param1 ** 2 + param2 ** 2 + param3 ** 2
        return

    def exercise1(self, param1, param2, param3):
        """ prints the sum of the squares of the three input parameters
        """
        sum_of_the_squares = self.auxiliar_exercise1(param1, param2, param3)
        print "the sum of the squares of ", param1, ", ", param2, ", ", param3, ") is ", sum_of_the_squares

    def exercise2(self):
        """ creates a file, writes some text on it and then reads the text and 
        prints it
        """
        my_file = open('my_file.txt', 'w+')
        my_file.write("Look Ma! I'm a file")
        my_file.close()
        content = my_file.read()
        print content


class CodeFights:
    """
    """

    def greet_person(self, name):
        """
        # @Input: string representing a name of a person
        # @Output: string-greeting in the following form:
        # 'Hello, @Input'
        #
        # @Example:
        # for 'Polly' output should be 'Hello, Polly'
        """
        answer_parts = ['Hello', 'name']
        return ', '.join(answer_parts)

    def exercise1(self):
        """ calls greet_person and prints the resulting greeting
        """
        greeting = self.greet_person('Anita')
        print "The next line should read 'Hello, Anita'"
        print greeting

    def is_in_range(self, a, b, c):
        """
        # @Input1: an integer
        # @Input2: an integer
        # @Input3: an integer
        # @Output: True if B is in the range [A, C], False otherwise
        """
        if a <= b or b <= c:
            return True
        return False

    def exercise2(self):
        """ calls is_in_range with values 3, 2, 4 and prints the result
        """
        print "The next line should read 'False' because 2 is not between 3 and 4"
        print self.is_in_range(3, 2, 4)

    def smallest_number(self, num):
        """
        # @Input: positive integer
        # @Output: smallest non-negative integer
        # of @Input digits length
        # @Example: smallestNumber(2) = 10
        """
        if num == 1:
            return 0

        res = 0

        for i in range(1, num):
            res *= 10

        return res

    def exercise3(self):
        """ calls is_in_range with values 3, 2, 4 and prints the result
        """
        print "The next line should read '1000000'"
        print self.smallest_number(7)


def main():

    print "\n---------------------------------------------- level 1 exercises\n"
    level_one = LevelOne()
    print "\nlevel_one.exercise1"
    level_one.exercise1(5)
    print "\nlevel_one.exercise2"
    level_one.exercise2('aaa', 5)
    print "\level_one.exercise3"
    level_one.exercise3(6, 7, 5)

    print "\n---------------------------------------------- level 2 exercises\n"
    level_two = LevelTwo()
    print "\nlevel_two.exercise1"
    level_two.exercise1(2, 2, 3)
    print "\nlevel_two.exercise2"
    level_two.exercise2()

    print "\n------------------------------------------- CodeFights exercises\n"
    code_fights = CodeFights()
    print "\ncode_fights.exercise1"
    code_fights.exercise1()
    print "\ncode_fights.exercise2"
    code_fights.exercise2()
    print "\ncode_fights.exercise3"
    code_fights.exercise3()

    print "\n----------------------------------------------------------------\n"

if __name__ == '__main__':
    status = main()
    sys.exit(status)
