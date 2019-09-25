"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""
    edit=0
    for i, letters in enumerate(w1):
        if w1[i] != w2[i]:
            edit+=1
    if edit<=1:
        return True
    else:
        return False

    #turn w1 and w2 to lists

    #track edits indices
    #if w1 and w2 are equal
        #return True
        #break

    #if w1 and w2 are not equal 
        #if len of w1 not equal to len of w2
            #record edit
            #if w1 < w2
                # if start w1 and w2 are equal
                    #iterate through list of longest len
                        #if an index does NOT match
      


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
