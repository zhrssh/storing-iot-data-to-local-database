# structure of the data
class Data:
    def __init__(self, mylist):
        self.device_id = mylist[0]
        self.temp_value = mylist[1]
        self.ldr_value = mylist[2]

    def convert_to_high_low(self):
        if self.ldr_value == "1":
            return "High"
        elif self.ldr_value == "0":
            return "Low"

    def get_datalist(self):
        mylist = [self.device_id, self.temp_value, self.ldr_value]
        return mylist

    def display_data(self):
        print("Device ID: " + self.device_id)
        print("Temperature: " + self.temp_value)
        print("LDR: " + self.convert_to_high_low())