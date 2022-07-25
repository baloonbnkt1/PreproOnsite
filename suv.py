"suv"
def main():
    "suv"
    bkk = input()
    bkk = bkk
    world = input()
    time = input()
    timehr = int(time[:2])
    timemn = int(time[3:5])
    if world == "To Sydney (SYD)":
        print("BKK - SYD")
        timehr += 9
        if timehr > 12 and time[6:8] == "PM":
            print("%02d:%02d AM" %(timehr+3-12, timemn))
        elif timehr > 12 and time[6:8] == "AM":
            print("%02d:%02d PM" %(timehr+3-12, timemn))
        elif timehr <= 12 and time[6:8] == "AM":
            print("%02d:%02d AM" %(timehr+3, timemn))
        elif timehr <= 12 and time[6:8] == "PM":
            print("%02d:%02d PM" %(timehr+3, timemn))
    elif world == "To Ho Chi Minh (SGN)":
        print("BKK - SGN")
        timehr += 1
        timemn += 50
        if timemn >= 60:
            timehr += 1
            timemn -= 60
        if timehr > 12 and time[6:8] == "PM":
            print("%02d:%02d AM" %(timehr-12, timemn))
        elif timehr > 12 and time[6:8] == "AM":
            print("%02d:%02d PM" %(timehr-12, timemn))
        elif timehr <= 12 and time[6:8] == "AM":
            print("%02d:%02d AM" %(timehr, timemn))
        elif timehr <= 12 and time[6:8] == "PM":
            print("%02d:%02d PM" %(timehr, timemn))
    elif world == "To Atlanta Georgia  (ATL)":
        print("BKK - ATL")
    elif world == "To Vancouver Canada(YVR)":
        print("BKK - YVR")
    elif world == "To Kathmandu (KTM)":
        print("BKK - KTM")
main()