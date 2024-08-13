# Beatles exercise

# step 1: create an empty list named beatles;
beatles = []

# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
for i in range(2):
    new_name = input("Enter the next member of the band :")
    beatles.append(new_name)

# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles[4]
del beatles[3]

# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, "Ringo Starr")
print(beatles)
