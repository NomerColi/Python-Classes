#Alarm Project

print("Welcome to Alarm Project")
current_hour = int(input("Enter current hour: "))
alarm_hour = int(input("Enter alarm hours: "))

day = 0
total_time = current_hour + alarm_hour            #calculate total time by summing current hour and alarm hours

while total_time >= 24:                 #repeat if total_time is greater than or equal to 24
    day = day + 1                       #add 1 to day
    total_time = total_time - 24        #subtract 24 from total_time

print(f"The alarm will sound in {day} day(s) at {total_time} hours")
