# this will fail if the other class has an error
#from learnPython import JobPortal as lp
from learnPython.JobPortal import findJob as fj
# year = 2020
# event = 'Covid-19'
# print(f'The year {year} will be most remembered for {event}') #f strings, formatted

# d = dict(skills='statistics',porn='porn')
# print('one: {0[skills]}; two: {0[porn]}'.format(d))# access the position of the argument in d
# with open('numbers.txt','w') as n:
#     n.write("Hello World")


# with open('numbers.txt') as n:
#     print(n.read())
class learnPython2:
    # def __init__(self):
        # super().__init__()

    def findJob(self, name, *names, **namey):# I think the self issue has to do with importing
        usernameattempt = name  # input("Enter a username:")
        db = names  # ["Chavoris","John","Cole"]
        print(self)
        print(name)
        print(names)
        print(namey)
        if(db.__contains__(usernameattempt)):

            print("Congrats")


fJ("Chavoris","Chavoris","John","Bob",n = "Chavoris",a = "John")
#lp = learnPython2()
# I think one of the issues I was running into with the other program is related to kwargs.
#lp.findJob("Chavoris", "John", "Cole", n="hello", a="wholesome")
