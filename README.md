# ATM_Storage_Interface 
By: JH.Park, 2022.08.21

This project was developed as a middleware concept for interworking between future ATM HW and banking system.
The structure of the currently developed source consists of middleware + temporary application for testing.

The items included are as follows.

1. main.py : Console executable file for temporary testing

2. broker.py : A class for data transmission and reception and interworking with ATM applications

3. paramlib.py : A file that defines fixed constant values ​​in the source

4. loglib.py : log list and log generation file for actions on the source

5. web_manager.py : A class that accesses the server of the banking system through a URL and receives user information in the form of a csv file.

* Test Method

1. Copy the project, build and run main.py from the console.

2. During execution, a temporary test thread called updater of broker.py is executed, and through the input method, it waits for temporary command data input. 
It is developed to output the result when input in the console window in the form of 
"PIN reader detection, PIN number validity, URL containing personal information, command type".

The structure of the command data is commented out in broker.py.

ex) "True,True,~~~.csv,1"

3. As there is currently no specific csv file, I wanted to aim, and the options for user's balance/deposit record/withdrawal record are commented out. 
If you need information about a specific header of csv, edit the comment section and test it.
