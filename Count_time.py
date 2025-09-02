import time

def count_time():

    count = int(input("Enter 'TIME' :  "))

    for timecount in range(count, -1, -1):

        seconds = timecount % 60
        minutes = (timecount // 60) % 60
        hours = timecount // 3600
        print(f"{hours} hr: {minutes} min : {seconds} sec")

        time.sleep(1)


count_time()