''' Program for string '''

fname=input("Enter first Name: ")
lname=input("Enter last Name: ")

print("--------------------- ---------")
print("- ",fname.capitalize(), lname.capitalize())

find_lenth_of_surname=len(lname)

no_of_strings_to_remove=find_lenth_of_surname-1


print("Best possible initials of",fname.capitalize(), lname.capitalize(),"is :", fname[0:-no_of_strings_to_remove].capitalize(), lname[0].upper())

