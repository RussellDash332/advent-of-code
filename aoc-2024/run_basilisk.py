import os, time
with open('basilisk.py') as f: lines = f.readlines()
for day in range(1, 26):
    print(f'Day {day:02d}')
    t = time.time()
    os.system(f'''python3.8 -c "{lines[2*day-1].replace(chr(34),3*chr(39))}" < Day-{day:02d}/{day:02d}.in''')
    print(f'Time: {round(time.time()-t, 3)} seconds\n')