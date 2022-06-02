import urllib.request

# local files
from database import Database
from data import Data

# arduino local ip
url = "http://192.168.1.11"

# database
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "myarduino"

# these must be existing in the database
TABLENAME = "sensors"
COLUMNS = ["DeviceId", "Temperature", "LDR"]

# start of the code
def start():

    # sets up the connection between python and database
    mydb = Database(HOST, USER, PASSWORD, DATABASE)

    while True:
        # promts the user to request or show last five sets of information
        myinput = input(
            "R - Request data, S - Show last five sets of information, D - Delete all rows, E - Exit: "
        )

        if myinput == "R":
            # gets data from the arduino
            get_data()

            # reconstruct each data and stores it in a list
            new_list = reconstruct_data()

            # stores data in its respective variables
            mydata = Data(new_list)

            # stores data in the database
            mydb.insert(TABLENAME, COLUMNS, mydata.get_datalist())

        elif myinput == "S":
            # prints last five data
            mydb.print_last_five(TABLENAME)

        elif myinput == "D":
            # deletes all record
            mydb.deleteall(TABLENAME)

        else:
            # exits the loop
            break

    ### FOR TESTING AND DEBUGGING ###
    # mydb.insert("example", dbcolumns, mydata.get_datalist())
    # mydb.delete("example", "1 = 1")
    # mydb.print_last_five("example")
    #################################

    # closes all connection after using
    mydb.close()


# function to get data from arduino
def get_data():
    global data

    # requests data from the url
    # x = urllib.request.urlopen(url).read()
    # x = x.decode("utf-8")

    # for testing
    x = "2011118$34.84$1"

    data = x


# function to reconstruct data into a list
def reconstruct_data():

    # splits the data into list
    data_list = data.split("$")
    return data_list


# driver code
if __name__ == "__main__":
    start()
