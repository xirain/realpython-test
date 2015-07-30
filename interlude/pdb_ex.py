# pdb_ex.py
import sys
import pdb
from random import choice

random1 = [x for x in range(1,13)]
random2 = [x for x in range(1,13)]

while True:
    print "To exit this game type 'exit'"
    pdb.set_trace()
    answer = raw_input("What is {} times {} ?".format(choice(random2), choice(random1)))

    if answer == "exit":
        print "Now exiting game!"
        sys.exit()

    elif answer == choice(random2) * choice(random1):
        print "Correct!"
    else:
        print "Wrong!"