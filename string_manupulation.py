''' Program for string manupulation and practice'''

sentence=input("Enter any long sentence: ")
print("------------------------------")

lenth=len(sentence)
center=int(lenth/2)

print("Last character in the sentence is:",sentence[-1:])
print("Last 5 characters in the sentence are:",sentence[-5:])
print("characters that are present in 2nd and 5th position of the sentence are: ",sentence[1],"and",sentence[4])
print("character at the center of the string, along with the 2 adjoining characters are: ",sentence[center-1:center+2])
