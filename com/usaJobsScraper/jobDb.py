import pymongo as pm
import pprint as pp

myclient = pm.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]  # not created yet

mycol = mydb["customers"] # creates a collection inside the database

mydict = {"name": "chavoris", "age": "23","address":"2309"}
# is it all text/string? and does it have to be enclosed in double quotes?
#This creates a document 

posts = mydb.posts
post_id = posts.insert_one(mydict).inserted_id
post_id #displays the id associated with the document

mydb.list_collection_names()# lists all objects in db

pp.pprint(posts.find_one())

