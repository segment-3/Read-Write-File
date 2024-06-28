# Drew Rochford
#AIST 2120
#Lab Exercise 15
#04/23/2021
# Assignment_6.py

# =======================================================================

# Welcome Message
print()
print('---------------------------------'.center(40))
print('---          AIST 2120        ---'.center(40))
print('---  Programming Assignment 6 ---'.center(40))
print('---         CSV & JSON        ---'.center(40))
print('---         Make a File       ---'.center(40))
print('---------------------------------'.center(40))
print()

# =======================================================================

#import statements
import csv
import sys
import os
import json

#-----------------------------------------------------------------------

#create new csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

#-----------------------------------------------------------------------

#Write rows to cvs file
row1 = outputWriter.writerow(['Alice', 'Bob', 'Chuck', 'Dan'])
row2 = outputWriter.writerow(['Eve', 'Frank', 'Grace', 'Heidi'])
outputFile.close()

#-----------------------------------------------------------------------

#Print the CSV file to the screen
print('CSV file contains:')
row1 = ['Alice', 'Bob', 'Chuck', 'Dan']
row2 = ['Eve', 'Frank', 'Grace', 'Heidi']
with open('output.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                print('Row#1 ',(row1))
                print('Row#2 ',(row2))
print('*** CSV file operations complete ***')
print()

#-----------------------------------------------------------------------
                
#Create a JSON file that contains a dictionary
jsoncalender = '{"Month": "May", "Day": 4, "Year": 2021}'
with open('file.txt', 'w') as file:
        file.write(str(json.loads(jsoncalender)))
        file.close()
print('*** JSON file operations complete ***')

#-----------------------------------------------------------------------

# DoNotChange
# Exit Message
print()
print('---------------------------------'.center(40))
print('--- Programming Assignment 6  ---'.center(40))
print('---          Complete         ---'.center(40))
print('---------------------------------'.center(40))

#-----------------------------------------------------------------------

# End Assignment 6

