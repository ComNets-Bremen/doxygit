#!/usr/bin/env python3

## @package doxygit
# This is an example package demonstrating Doxygen
#
# Written for the CS tutorial
#
# @author Jens Dede <jd@comnets.uni-bremen.de>
# @date 2018-05-25

from human import Human

## A class representing a student derived from the human class
class Student(Human):

    ## The default constructor
    # @param age    Age of the student
    # @param topic  The main topic of the student
    # @param name   The name of the student
    # @param topic  Set the  topic
    def __init__(self, age=0, name="", topic=""):
        Human.__init__(self, age, name)

        ## This is the topic the student is currently working on
        self.topic = topic

    ## Return the topic of the student
    #
    # @return The topic
    def getTopic(self):
        return self.topic

    ## Set the topic of the student
    #
    # This method can be used to set the topic of the student work
    #
    # @param topic  The topic
    def setTopic(self, topic):
        self.topic = topic


if __name__ == "__main__":
    print("Testing", __file__)
    s = Student()
    print(s)
    s.setTopic("Computer Science")
    print("Topic:",s.getTopic())
