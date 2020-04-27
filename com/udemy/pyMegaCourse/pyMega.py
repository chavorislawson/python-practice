def repeat():
    db =[]
    string = input("Say somethng:")
    while((string.__ne__("\end")):
        db.append(string.title)

    for i in db:
        print(i+", ")

repeat()