
try:
    file = open('04_files and exception\Files_project\First\handeling.txt','w')
    appending = file.write("Hello, this is my first time handeling file through python.")
    file.close()
    
    file = open('04_files and exception\Files_project\First\handeling.txt','a')
    appending = file.write('This is my first time appending a data into the file with the help of python. ')
    file.close()

    file = open('04_files and exception\Files_project\First\handeling.txt', 'r')
    reading = file.read()
    print(reading)
    file.close()

except FileNotFoundError:
    print('Error : The given directory does not contains the file.Please add a proper directory path.')

finally:
    print("Thank you.")