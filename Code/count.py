"""
Print the 10 most frequently occurring words in a text file.

Author: Rodney Topor
Last updated: 28 July 2009
"""

from re import split

dict = {} # word-frequency dictionary

def count(filename):
    """
    Print the number of occurrences of each word in fileName.
    """
    try:
        for line in open(filename, "rb"):
            process(line)
    except IOError: # Basic error checking
        print 'IO Error in %s' % filename
        return
    # sort dict by value (dict.sort() sorts by key)
   # pairs = [(count,word) for (word,count) in dict.iteritems()]
   # pairs.sort()    # standard list processing function
   # pairs.reverse() # ditto
    # select first 10 items of dict
   # pairs = [pairs[n] for n in range(0,10)]
    # print first 10 items
    #for count, word in pairs:
       # print "%s: %d" % (word, count)

    return dict


def process(line):
    """
    Add the number of occurrences of each word in line to dict.
    """
    # split line into (alphanumeric) words 
    # (\w=alphanumeric character, \W=nonalphanumeric character)
    words = split('\W+', line.strip())
    for word in words:
        # increment count for nonempty word in dict
        if word != "": # skip empty words (unfortunately necessary)
            if dict.has_key(word):
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1




count("J:\PDM\SpamFilter\spam-filter\train\regular\regular-0001.txt")

