#!/usr/bin/env python3

## Example program using the other classes in this directory
#
# @author Jens Dede <jd@comnets.uni-bremen.de>
# @date 2018-05-25 Initial commit
#
# @copyright GNU General Public License v3.0


import random

from human import Human
from student import Student
from teacher import Teacher

FIRST_NAMES = ["Marie", "Maximilian", "Sophie", "Alexander", "Maria", "Paul"]
LAST_NAMES = ["Müller", "Schmidt", "Meyer", "Schneider", "Wagner"]

NUM_STUDENTS = 10
NUM_TEACHERS = 1

classroom = list()

for i in range(NUM_STUDENTS):
    name = random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES)
    age = random.randrange(18, 30)
    classroom.append(Student(age, name))

for i in range(NUM_TEACHERS):
    name = random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES)
    age = random.randrange(30, 60)
    classroom.append(Teacher(age, name))



for person in classroom:
    print(person)
