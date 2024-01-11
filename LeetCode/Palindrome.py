def isPalindrome(x):
    listed = []
    for z in str(x):
        listed.append(z)
    if list(reversed(listed)) == listed:
        return(True)
    else:
        return(False)