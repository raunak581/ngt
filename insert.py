from pymongo import MongoClient
client = MongoClient('localhost:27017')
print("sucess")
db=client.college
def insert():
    id=input("enter id")
    name=input("enter name")
    db.st.insert_one(
        {
            "id": id,
            "name": name,

        })
    print(
    '\nInserted data successfully\n')

def update():
    id=input("enter the id")
    name=input("enter the name to be chnaged")
    db.st.update_one(
        {"id": id},
        {
            "$set": {
                "name": name,

            }
        }

    )
    print("sucess updated")

def read():
    empcol=db.st.find()
    for emp in empcol:
        print(emp)


def delte():
    id=input("enter id to be deleted")
    db.st.delete_one({"id": id});

delte()



