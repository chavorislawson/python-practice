from learnPython import JobPortal as lp #this will faill if the other class has an error
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
    #def __init__(self):
        #super().__init__()
    
    def findJob(self, *name):
        usernameattempt = input("Enter a username:")
        db = ["Chavoris","John","Cole"]
        if(db.__contains__(usernameattempt)):
            print(self)
            print(name)
            print("Congrats")

#lp.findJob(name = "Chavoris","python","c-sharp","java")
lp = learnPython2()
lp.findJob("Chavoris","John","Cole")# I think one of the issues I was running into with the other program is related to kwargs.