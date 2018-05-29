#!/usr/bin/env python3

## @package doxygit
# This is an example package demonstrating Doxygen
#
# Written for the CS tutorial
#
# @author Jens Dede <jd@comnets.uni-bremen.de>
# @date 2018-05-25 Initial commit
#
# @license GNU General Public License v3.0

## A class which represents a human
#
# @date 2018-05-28 Last final changes
# @date 2018-05-26 Another test
#
class Human(object):
    ## The Constructor
    # @param age    Age of the human. Default: 0
    # @param name   Name of the human. Default: None
    def __init__(self, age=0, name=None):

        ## @brief The age of the human
        self.__age=age

        ## @brief The name of the human
        self.__name=name

    ## String representation of the class
    def __str__(self):
        return type(self).__name__ + " with the name " \
                + str(self.__name) + " (" + str(self.__age) + " years old)"

    ## Return the age of the human
    #
    # @return The age
    def getAge(self):
        return self.__age

    ## Set the age of the human
    # @param age    Age of the human
    def setAge(self, age):
        self.__age = age

    ## Get the name of the human
    # @return The name
    def getName(self):
        return self.__name

    ## Set the name of the human
    # @param name   The name
    def setName(self, name):
        self.__name=name


if __name__ == "__main__":
    # Test this class
    print("Testing ", __file__)
    h = Human()
    print(h.getAge())
    h.setAge(12)
    print(h.getAge())
    print(h)
