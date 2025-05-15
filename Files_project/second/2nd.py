
inp_data = input("Enter data to be stored in file.txt : ")
print("Data successfully written to myfile.txt.\n")
appen_data = input("Enter data to be appended in file.txt : ")
print("Data successfully appended.\n")
next_appen = input("Enter data to be appended in file.txt : ")
print('Data again appended.\n')

print("Final content of myfile.txt : ")
try:
    file = open('04_files and exception\Files projects\second\myfile.txt','w')
    file.write(inp_data)
    file.close()
    
    file = open('04_files and exception\Files projects\second\myfile.txt','a')
    file.write(appen_data)
    file.close()

    file = open('04_files and exception\Files projects\second\myfile.txt','a')
    file.write(next_appen)
    file.close()

    file = open('04_files and exception\Files projects\second\myfile.txt','r')
    reading = file.read()
    print(reading)
    file.close()

except FileNotFoundError:
    print('The given directory does not matches any files.Please enter a real file path.')

finally:
    print('Learning file handeling in python.')