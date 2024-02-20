# Type your code here.
# All formatting in this program is done at the requirement of my classes autograder.
""" Assignment: Social network
    PA2SocialNetwork.py

    Name: Tayven Stover 

    File Created on February 19, 2024   
    Integrity is demonstrated at NOVA through adherence to principles and
    actions that foster accountability, honesty and trustworthiness;
"""

"""

    - Get number of friends on network
	- Enter names of friends
    - Output rows and colums with each friends name and one or zero depending on if they are friends with that person
    - Output rows with each friends name and how many friends they have on the network, this is just going to be n(friends)-1
        
    
"""
num_users = 0  # Must be positive
users = []  # Gets users
# Adds sub-lists so we can append to them later on.


class InputError(Exception):
    pass

# Calculates lexicographical difference of first non-matching char.


def lexicographical_difference(string1, string2):
    for i in range(min([len(string1), len(string2)])):
        if string1[i] == string2[i]:
            pass

        elif string1[i] != string2[i] and (abs(ord(string1[i]) - ord(string2[i]))) <= 12:
            return 1

        else:
            return 0

    return 1


# Gets number of users
print("What is the total number of friends in the network:", end='')
while True:
    try:
        num_users = input()
        print()
        num_users = int(num_users)

        if num_users <= 0:
            raise InputError

        break

    except(ValueError):
        print(f"{num_users}is an incorrect input! Please enter an integer.")

    except(InputError):
        print("You need to have at least one friend in the network. Please enter again:", end='')

lexicographic_list = [[] for i in range(num_users)]

# Gets users
for i in range(num_users):
    users.append(input("Enter name:"))
    print()

# Populates 2D list.
for i in range(len(users)):
    for j in range(len(users)):
        if i == j:
            lexicographic_list[i].append(str(0))
        else:
            lexicographic_list[i].append(
                str(lexicographical_difference(users[i], users[j])))

# Outputs list in table format using tabs.
for name in users:
    print(f"\t{name}", end='')

print()
x='\t'
for (index, element) in enumerate(lexicographic_list):
    print(f"{users[index]}\t{x.join(element)}")
print()
print("Total Friends Count:")
# Outputs total num of friends
for n in range(num_users):
    integer_lexicographical_list = [eval(i) for i in lexicographic_list[n]]
    print(f"{users[n]}\t{sum(integer_lexicographical_list)}")
