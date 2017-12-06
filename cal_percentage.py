''' Program to calculate total percentage marks and rank '''

def perform_action():
    if percentage>= 90:
        print("\nYou passed exam in FIRST CLASS with ",percentage)
    elif percentage>= 75:
        print("\nYou passed exam in Second CLASS with ", percentage)
    elif percentage>=35:
        print("\nYou passed exam with AVERAGE percentage ", percentage)
    elif percentage<=35:
        print("\nYou FAILED !!!",percentage)


def get_marks():
    eng_marks=int(input("Enter marks scored in Englist out of 80: "))
    sci_marks = int(input("Enter marks scored in Englist out of 90: "))
    math_marks = int(input("Enter marks scored in Englist out of 100: "))
    total= eng_marks+sci_marks+math_marks
    return total


final_total= get_marks()
percentage = (final_total/270)*100
perform_action()
