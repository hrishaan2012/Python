import random
import time
def getRandomDate(stardate, enddate):
    time.fomat= "%m/%d/%Y"
    print("Printing random dates between", stardate, "and", enddate)
    random_generator = random.random()
    starttime=time.mktime(time.strptime(stardate, time.fomat))
    endtime=time.mktime(time.strptime(enddate, time.fomat))
    random_time=starttime+ random_generator*(endtime-starttime)
    random_date=time.strftime(time.fomat, time.localtime(random_time))
    
    return random_date
print("random date between 01/01/2020 and 12/31/2020 is",(getRandomDate("01/01/2020", "12/31/2020")))