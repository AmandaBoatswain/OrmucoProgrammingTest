# CREATED BY: Amanda Boatswain Jacques, Thursday November 28th, 2019
# LAST MODIFIED: Wednesday December 4th, 2019

# Question A
""" Your goal for this question is to write a program that accepts two lines (x1,x2)
and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5)
and (2,6) overlaps but not (1,5) and (6,8).

Assumptions for this question:
 - There are no library restrictions
 - A line overlaps with another if they have at least one point in common """

# import necessary libraries
import numpy as np  # numerical python
from matplotlib import pyplot as plt # python plotting library

# generate the lines
(x1, x2) = (1, 5)
(x3, x4) = (5, 10)
(y) = (0, 0)  # the lines remain flattened on the x-axis

# plot the lines to see what they look like, we will use dashed lines so that the overlap (if present) is visible.
plt.plot((x1, x2), (y), "r--", (x3, x4), (y), "b--")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.title("Two Lines")
plt.legend(['First Line', 'Second Line'], loc=1)
plt.show()


# find the point coordinates of all the points on the line
def find_coordinates(x0, xN):
    # map the points to a list and then convert them to a set
    coordinates = set([i for i in range(x0, xN+1)])
    return coordinates

# create point sets for the first line and the second line
line1 = find_coordinates(x1, x2)
line2 = find_coordinates(x3, x4)

print("Points on the first line:", line1)
print("Points on the second line:", line2)

# See if they overlap:
# check if there are any common elements in the first or second line
def check_overlap(line1, line2):
    if (line1 & line2):
        print("These lines overlap at: ", (line1&line2))
    else:
        print("These lines do not overlap.")

    print("\n")

check_overlap(line1, line2)

# Question B
""" The goal of this question is to write a software library that accepts 2 version
string as input and returns whether one is greater than, equal, or less than the
other. As an example: “1.2” is greater than “1.1”. Please provide all test cases
you could think of.

Assumptions for this question:
 - There are no library restrictions """

from compare_versions import *

string1 = "3.4.2.1.5"
string2 = "3.4.2.1.5"

# import the functions and do the comparison
compare_versions(string1, string2)

# Another cool way to answer this question:
# Use python tuples! There is built in logic when comparing them

compare_tuples(string1, string2)
print("\n")


# Question C
""" Your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration.
This library will be used extensively by many of our services so it needs to meet the following criteria:

    1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema
    7 - Cache can expire

As a hint, we are not looking for quantity, but rather quality, maintainability, scalability, testability and a code that you can be proud of.
When submitting your code add the necessary documentation to explain your overall design and missing functionalities.  Do it to the best of your knowledge.

Assumptions for this question:
 - There are no library restrictions """

# import necessary libraries
import time
from datetime import datetime
from LRUCache import *

args = []
# generate 20 random numbers between 0 and 10 and append them to a list
for i in range(0, 20):
    num = np.random.randint(0, 10)
    args.append(num)
print("Argument list: ", args)

# set the cache limit, default limit is None. As we increase the size of the cache, the speed will also increase
# but will require more memory storage
LRUCache.cache_limit = 10

@LRUCache
def function1(num):
    print(f"Computing the square of {num}...")
    time.sleep(1)
    return num*num

# time the use of the function with the LRU cache
start_time = datetime.now()
for i in range(len(args)):
    print(function1(args[i]))

delta_time = (datetime.now()-start_time).seconds
print("Time elapsed: ", delta_time)
