#  =================Task 14================
# Author: Gayathri
# Created Date: 09/04/2023
# Reference: example.py,W3 schools
# This is a Python program, the purpose of this program is to get the data from the text file DOB.txt, 
# Manupliate the data and display the name and birhdate seperatly.
# Tried to display fullname and birthdate in a table.
# Included defensive programing.
#  ======================================
print("----------------------------------------------------------------------------")
print("-----------Working with external data sources-text file - Input-------------")
print("----------------------------------------------------------------------------")
file_name="DOB.txt"
name = []
birthday = []
try:
    #Read the data from the text file
    with open(file_name,"r") as file_object:
        for lines in file_object:        
            details_list = lines.split()
            name.append(details_list[0] + " "+ details_list[1])
            birthday.append(details_list[-3] + " "+ details_list[-2] + " " + details_list[-1])
    #Display the data
    print("\nName:")
    for fullname in name:
        print(fullname)
    print("\n")
    print("Birthday:")
    for dob in birthday:
        print(dob)  

    # My idea of displaying fullname and birthdate in table 
    print("\n")
    row_border = "-------------------------------------------"
    fullname_header = "!{:5}Full Name {:5}!".format("","")
    birthdate_header = "{:5}Birthdate {:5}!".format("","")

    print(row_border)
    print(fullname_header, end="")
    print(birthdate_header)
    print(row_border)

    for items in range(0,len(name)):
        #Formating full name to display in table format
        fullname = "{}{}".format("! ", name[items])
        name_length= len(name[items])
        name_length = 20-name_length
        for space in range(1,name_length):
            fullname +=" "
        fullname += "!"
        #Formating birthdate to display in table format
        dob = "{}{}".format(" ", birthday[items])
        dob_length = len(birthday[items])
        dob_length = 20 - dob_length
        for space in range(1,dob_length):
            dob +=" "
        dob += "!"
        print(fullname, end="")
        print(dob)
        print(row_border)
except Exception as error_message:
    print(error_message)



