def isValid(self, s: str) -> bool:
    valid = {"()", "[]", "{}"}
    max_count = (len(s) // 2)
    count = 0
    while count <= max_count:
        for x in valid:
            if x in s:
                s = s.replace(x, "")
        count += 1
    if len(s) == 0:
        return True
    else:
        return False