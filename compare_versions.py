
# compare_versions.py
# software library for question B

def compare_versions(string1, string2):
    seperator = "."
    # first load the strings and then seperate the individual numbers into a list by
    # using the split function
    string1 = string1.split(seperator)
    string2 = string2.split(seperator)

    # loop through all the version levels
    for level in range(0, len(string1)):
        # if the current two levels are equal, then continue in the loop
        if string1[level] == string2[level]:
            continue
            # if all the levels are the same, then return that the versions are equal
            return print("Version %s is equal to version %s. " %(seperator.join(string1), seperator.join(string2)))


        # if the current level of string1 one is higher than string 2, return
        # string 1
        elif string1[level] > string2[level]:
            return print("Version %s is greater than %s. " %(seperator.join(string1), seperator.join(string2)))
            break
        # else, return string2
        else:
            return print("Version %s is greater than %s. " %(seperator.join(string2), seperator.join(string1)))
            break


# Another cool way to answer this question:
# Use python tuples! There is built in logic when comparing them

def compare_tuples(string1, string2):
    seperator = "."
    # convert the strings to tuples
    string1 = tuple(string1.split(seperator))
    string2 = tuple(string2.split(seperator))

    # compare the tuples to each other and return whichever one is greater
    if (string1 == string2):
        return print("Version %s is equal to version %s. " %(seperator.join(string1), seperator.join(string2)))
    elif string1 > string2:
        return print("Version %s is greater than %s. " %(seperator.join(string1), seperator.join(string2)))
    else:
        return print("Version %s is greater than %s. " %(seperator.join(string2), seperator.join(string1)))
