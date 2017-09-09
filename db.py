class User(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Db(object):
    def __init__(self):
        self.contents = []
        self.next_id = 1
    def create(self,name):
        newUser = User(name,self.next_id)
        self.next_id += 1
        self.contents.append(newUser)
        print "create working"
    def All(self):
        return self.contents
    def get(self,id):
        for user in self.contents:
            if user.id == id:
                return user
    def filter(self,name):
        temp = []
        for user in self.contents:
            if user.name == name:
                temp.append(user)
        return temp
    def exclude(self,name):
        temp = []
        for user in self.contents:
            if user.name != name:
                temp.append(user)
        return temp




userDb = Db()
print userDb
#print User("paul",12)
print userDb.create('paul')
print userDb.contents[0].name
users = userDb.All()
userDb.get(1)