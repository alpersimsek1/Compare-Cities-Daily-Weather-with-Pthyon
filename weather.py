import datetime

now = datetime.datetime.now()

class City:

    def __init__(self):
        self.city_id = int()
        self.city_name = ""
        self.temperature = int()
        self.temp_min = int()
        self.temp_max = int()
        self.datenow = now.strftime("%d-%m-%y")

    def __str__(self):

        return print(" Date     : "+str(self.datenow) +
                     " \n Name     : " + self.city_name +
                     " \n Temp     : " + str(self.temperature) +
                     " \n Min Temp : " + str(self.temp_max) +
                     " \n Max Temp : " + str(self.temp_min))




