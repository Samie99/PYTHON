def longestCommonPrefix(strs):
    x = 0
    prefix = ""
    while True:
        if "" in strs:
            break
        minstrs = min(strs)
        maxstrs = max(strs)
        if ord(minstrs[x]) == ord(maxstrs[x]):
            prefix += str(minstrs[x])
            x += 1
        else:
            break
        if x >= len(minstrs):
            break
    return(prefix)