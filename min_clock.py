import time 

seconds = int(input("Enter the seconds\t"))

for i in range (seconds, 0, -1 ):
    min = i // 60
    seconds = i%60
    print(f"\rTime remaining : {min:02d} : {seconds:02d}", end="")
    time.sleep(1)

print("Time's Up!!!")

