# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input (question).lower()

        if response == "yes" or response =="y":
            response = "yes"
            return response

        elif response =="no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print ("The rules of the game go here")
    print()
    return " "

# Main Routine goes here
played_before = yes_no ("Have you played the game before? ")
print("You chose {}".format(played_before))
print()
having_fun = yes_no ("Are you having fun? ")
print ("you said {} to having fun".format(having_fun))

if played_before == "no":
    instructions()

print("Programs Continues")
