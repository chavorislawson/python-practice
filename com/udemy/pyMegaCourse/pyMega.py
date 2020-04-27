def repeat():
    db =[]
    string = input("Say something:")
    while(string.__ne__("\end")):
        string = string.capitalize().strip()
        if string.startswith(("How","What","Why", "Is","Are","Can","May")):
            string = string.__add__("?")
        else:
            string = string.__add__(".")

        db.append(string)
        string = input("Say something:")
    
    for i in range(len(db)):
        print(db[i],end=" ")

repeat()