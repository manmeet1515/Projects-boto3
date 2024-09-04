import os


folders = input("Enter the folder names with space in between: ").split()
print(folders)

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please enter a valid folder name, the folder name - " + folder + " is not valid.")
        #break
        continue
    
    print("===  Listing files for the folder -" + folder + "  ==== ")
    
    for file in files:
        print("-" + file)
    