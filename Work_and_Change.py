import time
import os
focusing_duration=int(input("how many seconds do yu want to work? : ")) 
changing_time = int(input("how many seconds do yu want when changing your task? : "))


while True: #infinite loop
    for i in range (focusing_duration + 1): 
        print("work time..." + " " + str(focusing_duration-i) + " seconds remaining")
        time.sleep(1)

    os.system( "say change subject" )

    for i in range (changing_time + 1):
        print("change subject..." +" " + str(changing_time-i) + " seconds remaining") 
        time.sleep(1)

    os.system( "say start" )

