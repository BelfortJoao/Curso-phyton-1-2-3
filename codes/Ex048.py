import time

for i in range(1, 500, 2):
    if i % 3 == 0:
        print(i)
        time.sleep(0.2)
