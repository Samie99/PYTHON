import time

while True:
    hrs = input("Hours: ")
    if not hrs.isdigit():
            continue
    hrs = int(hrs)
    if hrs < 0:
          continue
    break

while True:
    mins = input("Minutes: ")
    if not mins.isdigit():
            continue
    mins = int(mins)
    if mins < 0:
          continue
    break

while True:
    secs = input("Seconds: ")
    if not secs.isdigit():
            continue
    secs = int(secs)
    if secs < 0:
          continue
    break

total = secs + (hrs * 3600) + (mins * 60)

input("Press ENTER To Start")

while total:
    hrs, mins = divmod(total, 3600)
    mins, secs = divmod((total - (3600 * hrs)), 60)
    timer = "{:02d}:{:02d}:{:02d}".format(hrs, mins, secs)
    print(f"{timer}", end="\r")
    time.sleep(1)
    total -= 1

print("BEEP BEEP DONE")