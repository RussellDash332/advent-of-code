import os, time, sys
d = int(sys.argv[1]) if len(sys.argv) > 1 else 1
with open('basilisk.py') as f: lines = f.readlines()
for day in range(d, 13):
    print(f'Day {day:02d}')
    t = time.time()
    os.system(f'''python -W ignore -c "{lines[2*day-1].replace(chr(34),3*chr(39))}" < Day-{day:02d}/{day:02d}.in''')
    print(f'Time: {round(time.time()-t, 3)} seconds\n')