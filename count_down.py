import time

time_my = input("Enter time like 4 min,4 sec or 4 hrs:")
time_1 = time_my.split(' ')
final_list = [int(time_1[0]),time_1[1]]

if final_list[1] == "min":
    total_time = final_list[0]*60
    for x in range (total_time,0,-1):
        second = x%60
        minutes = int(x/60)%60
        time.sleep(1)
        print(f"00:{minutes:02}:{second:02}")
    
    print("time up")

elif final_list[1]=="sec":
    for x in range (final_list[0],0,-1):
        second = x%60
        time.sleep(1)
        print(f"00:00:{second:02}")
    
    print("time up")

elif final_list[1]== "hrs":
    total_time = final_list[0]*60*60
    for x in range (total_time,0,-1):
        second = x%60
        minutes = int(x/60)%60
        hour = int(x/3600)
        time.sleep(1)
        print(f"{hour:02}:{minutes:02}:{second:02}")
        
    
    print("time up")

else:
    print("Please read the above sentence cearfully")