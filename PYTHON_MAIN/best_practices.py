"""

07-07-2022

what is __name__ = "__main__" ?

double underscore name double underscore name -> dunder name

####################################################################################

When this file is imported as a module, only the second line above is executed

However, when this file is executed as a script the main() function is executed.

Therefore, the if dunder name condition allows for the exclusion of certain sections
of a code when it is imported as a module.

It specifies what sections of the code to be imported as a module and
what sections of the code to be executed as a script.

Use the dunder name condition to make your python files dual purpose:

1. As a module
2. As a script

#####################################################################################

Read more: https://realpython.com/python-main-function/

"""

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished")
    return modified_data

def read_data_from_web():
    print("Reading data from web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to database")
    print(data)
    
def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()
