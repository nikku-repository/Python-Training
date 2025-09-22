# Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found
 
 
# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
 
 
# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890
import glob
import re

# Assignment 1 -------------------------------------------->
txt_files = glob.glob("*.txt")

for file in txt_files:
    try:
        with open(file, "r") as f:
            content = f.read()
            if re.search(r"Python", content, re.IGNORECASE):
                print(f"Found 'Python' in: {file}")
            else:
                print(f"No 'Python' found in: {file}")
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Assignment 2   --------------------------->

files = glob.glob("*")

for file in files:
    
    if re.match(r"^data(_.*)?\.csv$", file):
        print(f"CSV Match: {file}")

# Assignment 3-------------------------------->
phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "(987) 654-3210",
    "9876543210"
]

for number in phone_numbers:
    if re.match(r"^\(\d{3}\) \d{3}-\d{4}$", number):
        print(number)