import pandas as pd
import numpy as np

def SleepTracker (awake, sleep):
    if awake >= 17:
        awake_output = 'sleep deprived'
    else:
        awake_output = 'average amount of sleep'
    if sleep <= 7:
        sleep_output = 'sleep deprived'
    else:
        awake_output = 'average amount of sleep'

    output = [awake_output, sleep_output]

    return output


ThisIsANumber = 5

definingSleep = {
    "average": "6 to 8 hours",
    "below_average": "0 to 6 hours",
    "above_average": "9 and above hours"
}

print("What is the average amount of sleep?" , definingSleep["average"])
print("What is a bad amount of sleep?" , definingSleep["below_average"])
print("What is too much sleep" , definingSleep["above_average"])

sleepTime = [
    (16, 8),
    (15, 9),
    (20, 4),
    (18, 6),
    (12, 12),
    (9, 15),
    (17, 7)
]

for sleepTimes in sleepTime:
    print(f'Are you sleeping well enough? hours_awake: {sleepTime[0]}, hours_slept: {sleepTime[1]}')
    hours_awake = sleepTime[0]
    hours_slept = sleepTime[1]