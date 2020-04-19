#from collections import deque

# resume keywords


class JobPortal:

    def __init__(self):
        super().__init__()

    db = ['Chavoris', 'John', 'Sarah', 'Hancock', 'Mario']
    db = [x.upper() for x in db]

    # if 'Chavoris'.upper() in db:
    #     print(db.__len__())

    def findJob(self, name='Chavoris', *skills, jobDescrip=("Python","java")):
        name = input("Enter your usename:")

        while (not self.db.(name)) or (type(name) != str):
            name = input("Enter a valid usename:")

        print('You are now successfully logged in.')

        while not jobDescrip.__contains__(skills[0]) or jobDescrip.__contains__(skills[1]):

            response = print("Your skills did not match. Would you like to try again?")

            if(response.__eq__("YES") or response.__eq__("yes") or response.__eq__("Yes") or response.__eq__("y") or response.__eq__("Y")): # going to learn about regular expressions for this
                keywords = input("Enter a valid skill:")

            else:
                print("Your skills don't match the minimal job requirements. GoodBye.")
                exit(code=0)

        print("Your skills match the minimal job requirements. You will be selected for an interview soon. Goodbye.")
        exit(code=0)
    
    
        
                
# def findJob2(name='Chavoris', *keywords, **jobDescrip):
#         name = str(input("Enter your usename:"))

#         while not db.__contains__(name):
#             name = input("Enter a valid usename:")

#         print('You are now successfully logged in.')

#         while not jobDescrip.__contains__(keywords[0]):

#             response = str(print("Your skills did not match. Would you like to try again?"))

#             if(response.lower().__eq__("yes")):

#             if jobDescrip.__contains__(keywords[0]):
#                 print(
#                     "Your skills match the minimal job requirements. You will be selected for an interview soon.")
#                 exit(code=0)
#             else:






# while(i < 2):

# findJob('','skill','Statistics',skill='Python')

# len, sum, range, list, input, int, str, in, _ <- don't know if can be used out of the interactive shell

# print('Are you in the db? Let\'s see!')
# name = input('What\'s your name?')

# name = name.upper()
# print(name)
# for i in range(len(db)):
#     if db[i] != name:
#         continue
#     else:
#         print('Success!')
#         exit(code=0)

# print('Better luck next time!')

# List as stack
# What stack could I implement?

# list as queue, need to do import because lists are slow at that.
# Implement waiting in line or to do list.

# List comprehensions - create lists using some operation

# squares = list(map(lambda x: x**2, range(10)))
# above creates a list from mapping the lambda function to square a given input
# to each increment in the range method, so I end up with squared numbers
# up to 81 because it's 0-9. Lambda is most likely overkill in most situations
#print(squares)
# equivalently
# square = [x**2 for x in range(10)]
# print(square)

# comb = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(comb)

# equivalently but longer
# combs = list()

# for x in [1, 2,3]:
#     for y in [3, 1,4]:
#         if x != y:
#             combs.append({x: y}) #I can have a list of dictionaries and a list of tuples

# print(combs)

# print(list(zip(comb)))

# print(tuple(list(square)))

# db2 = dict("Chavo's Contacts",(dict("Number",678899463),dict("Address",2309)))
# db3 = dict("Chavo's Contacts":67687878)
# db4 = {"ty":566767}
# db5 = {"Chavo's Contacts": ({"Number":678899463},{"Address":2309})}
# print(db2,db3,db4)
# print(db4, db5)
# print(db5["Chavo's Contacts"][0]["Number"])  # Fye, but tedious

# db6 = ({"Name": "Chavoris"},{"Contact":6787899463},{"Address":2309}),({"Name":"Destiny"},{"Contact":6787899462},{"Address":2308})
# print(db6)
# print(type(db6))
# print(db6[1][1]["Contact"])

# print([[[[x[i][j] for x in range(len(db6))]for i in range(len(db6[i]))]for j in range(len(db6[i][j]))]])
# print([[x[i] for x in range(len(db6))]for i in range(len(db6[]))])
# print([x for x in range(len(db6))])

# if __name__ == "__main__":  # Makes this module a script to be run in the command line
#     import sys
#     findJob(str(sys.argv[1]), 'Skills',Skills='Statistics')
