# Q1. Basic Read & Write
# Create a file `notes.txt` and write:
#   My name is Ankit.
#   I am learning Python File I/O.
# Now read the file and print its contents.
print("\n")
with open("notes.txt","w") as f :
    f.write("My Name is Ankit \n")
    f.write("I am learning Python Files I_O")

with open("notes.txt","r") as f :
    print(f.read())

# Q2. Append Data
# Open `notes.txt` in append mode.
# Add a new line: 
#   I am consistent with my learning.
# Verify by reading the entire file again.
print("\n")
with open("notes.txt","a") as f :
    f.write("\nI am consistent with my learning ")

with open("notes.txt","r") as f :
    print(f.read())


# Q3. Count Words in a File
# Write a program that counts the number of words in `notes.txt`.
# Example output:
#   Total words = 12
print("\n")
with open("notes.txt","r") as f :
    content=f.read()
    print(f"Total Words : {len(content)}")


# Q4. Read Line by Line
# Read `notes.txt` line by line and print only the lines containing the word "Python".
print("\n")
with open("notes.txt","r") as f:
    for line in f:
        a="python"
        b=line.lower()
        if a in b:
            print(line)



# Q5. Copy File (Text Mode)
# Copy the contents of `notes.txt` into a new file `copy.txt`.
# Ensure both files contain the same content.
print("\n")
with open("notes.txt", "r") as n:
    with open("coy.txt", "w") as c:
        c.write(n.read())


# Q6. Copy File (Binary Mode)
# Copy an image (say `photo.png`) into `photo_copy.png` using binary mode (`rb` and `wb`).
print("\n")
with open("image.jpg", "rb") as nb:
    with open("copy.jpg", "wb") as cb:
        cb.write(nb.read())


# Q7. Using seek() and tell()
# Open `notes.txt`.
# Read the first 10 characters and print the cursor position (tell()).
# Move cursor back to the start (seek(0)) and re-read the first 10 characters.
print("\n")

with open("notes.txt","r") as f :
    
    print(f.read(10))
    print(f"{f.tell()}")
    f.seek(0)
    print(f.read(10))
    


# Q8. Exception Handling
# Try opening a file `missing.txt` in read mode.
# Catch the exception if the file doesn’t exist and print "File not found!".
print("\n")

'''with open("missing.txt","r") as f :

    f.read()
    FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
'''


# Q9. Large File Efficient Reading
# Create a file `big.txt` with at least 100 lines (you can loop & write dummy text).
# Write a program that reads it line by line and counts how many lines contain the word "Python".
print("\n")
with open("big.txt","r") as f:
    count=0
    for line in f:
        a="python"
        b=line.lower()
        if a in b:
            count+=1
    print(f"Python apperead in {count} lines")


# Q10. File Exists Check
# Write a program that checks if `notes.txt` exists.
# If yes → print "File exists".
# If no → create the file and write "New file created".
print("\n")
try:
    with open("notes.txt", "r") as f:
        print("File exists")
except FileNotFoundError:
    with open("notes.txt", "w") as f:
        f.write("New file created")
    print("New file created")
