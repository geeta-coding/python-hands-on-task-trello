# Create a Dog class with name, breed, age attributes

class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed =breed
        self.age = age
    def bark(self):
        print(self.name,"is bark ")
    def describe(self):
        print("dog name is: ",self.name,"dog's breed is : ",self.breed,"dog's age is : ",self.age)

# Add methods: bark(), describe(), birthday()
dog_1 = Dog("loki","haski",21)
dog_2 = Dog("seemba","yodha",11)
dog_3 = Dog("joy","gali",9)

dog_1.bark()
dog_1.describe()
print("*"*100)
dog_2.bark()
dog_2.describe()
print("*"*100)
dog_3.bark()
dog_3.describe()
print("*"*100)


# Create 3 Dog objects and call their methods


# Add str method for readable output


# Add repr for debugging output


# Create a class variable to count total dogs


# Understand self parameter


# Use isinstance() to check object types
a =isinstance(dog_2,Dog)
print(a)
# 📚 Learning Resources