def romanToInt(s):
    fours_nines = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    stops = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    check = 0
    if len(s) == 1:
        return stops.get(s)
    for x in s:
        if int(s.index(x, check, check + 1)) < int(len(s) - 1):
            next_rom = s[((s.index(x, check, check + 1)) + 1)]
            duo = x + next_rom
        if int(s.index(x, check, check + 1)) > 0:
            last_rom = s[((s.index(x, check, check + 1)) - 1)]
            past_duo = last_rom + x
            if past_duo in fours_nines:
                check += 1
                continue
        if x == "I" and next_rom in "VX":
            total += (fours_nines.get((duo)))
            check += 1
            continue
        if x == "X" and next_rom in "LC":
            total += (fours_nines.get((duo)))
            check += 1
            continue
        if x == "C" and next_rom in "DM":
            total += (fours_nines.get((duo)))
            check += 1
            continue
        if x in stops:
            total += (stops.get(x))
            check += 1
    print(total)