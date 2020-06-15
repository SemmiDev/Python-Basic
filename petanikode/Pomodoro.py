import time

def countDowmTimer(start_minute,start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins,secs = divmod(total_second,60)
        print(f'{mins:02d} : {secs:02d}', '\r')
        time.sleep(0.90)
        total_second -= 1
    print("time out!! deformation")

if __name__ == '__main__':
    countDowmTimer(0,5) #pomodoo timer