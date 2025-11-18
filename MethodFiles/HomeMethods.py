from MethodFiles.Interfaces import GetDaysLeftInterface
from datetime import datetime

class GetDaysLeft(GetDaysLeftInterface):
    @staticmethod
    def getDaysLeft(**kwargs):
        #get the current time
        now = datetime.now()

        #find the next friday that comes after our current day (friday == 4)
        weekday = now.weekday()
        if weekday > 4:
            daysLeft = 11 - weekday
        else:
            daysLeft = 4 - weekday

        #if we are at or past 5:30 PM then subtract 1 from our day
        if (now.hour - 6) >= 17 and now.minute >= 30:
            daysLeft -= 1

        print(daysLeft)
        return daysLeft