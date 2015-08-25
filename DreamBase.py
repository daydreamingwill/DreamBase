import sys
sys.path.insert(0, 'C:\Users\willi_000\Desktop\Project DreamBase\People')
from People_classes import *

with open('Saved_objects.txt', 'r') as Saved_objects:

    object_dictionary =  eval('Saved_objects').read()


