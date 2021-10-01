accepted_species = ['dog', 'cat', 'horse', 'hamster']
user_pets = {'dogs': [], 'cats': []}
dog_list = []
cat_list = []


class Pet:
    def __init__(self, species=None, name=""):
        if species.lower() not in accepted_species:
            raise ValueError
        else:
            self.species = species.lower()
        self.name = name.lower()

    def __str__(self):
        if self.name == "":
            return "Species of {}, unnamed".format(self.species)
        else:
            return "Species of {}, named {}".format(self.species, self.name)


class Dog(Pet):
    def __init__(self, name="", chases='Cats'):
        super(Dog, self).__init__('Dog', name)
        self.chases = chases

    def __str__(self):
        if self.name == "":
            return "Species of Dog, unnamed, chases {}".format(self.chases)
        else:
            return "Species of Dog, named {}, chases {}".format(self.name, self.chases)


class Cat(Pet):
    def __init__(self, name="", hates='Dogs'):
        super(Cat, self).__init__('Cat', name)
        self.hates = hates

    def __str__(self):
        if self.name == "":
            return "Species of Cat, unnamed, hates {}".format(self.hates)
        else:
            return "Species of Cat, named {}, hates {}".format(self.name, self.hates)


def adopt_dogs():
    while True:
        try:
            number_of_dogs = int(input("Enter the number of dogs you wish to adopt : "))
            for index in range(number_of_dogs):
                dog_name = input("Enter name : ")
                dog_chases = input("Enter the name of the chased one : ")
                if dog_name == "" and dog_chases == "":
                    user_pets['dogs'].append(Dog())
                elif dog_name == "":
                    user_pets['dogs'].append(Dog(chases=dog_chases))
                elif dog_chases == "":
                    user_pets['dogs'].append(Dog(name=dog_name))
                    dog_list.append(dog_name.lower())
                else:
                    user_pets['dogs'].append(Dog(dog_name, dog_chases))
                    dog_list.append(dog_name.lower())
        except ValueError:
            print("Invalid Value")
        else:
            break


def adopt_cats():
    while True:
        try:
            number_of_cats = int(input("Enter the number of cats you wish to adopt : "))
            for index in range(number_of_cats):
                cat_name = input("Enter name : ")
                cat_hates = input("Enter the name of the hated one : ")
                if cat_name == "" and cat_hates == "":
                    user_pets['cats'].append(Cat())
                elif cat_name == "":
                    user_pets['cats'].append(Cat(hates=cat_hates))
                elif cat_hates == "":
                    user_pets['cats'].append(Cat(name=cat_name))
                    cat_list.append(cat_name.lower())
                else:
                    user_pets['cats'].append(Cat(cat_name, cat_hates))
                    cat_list.append(cat_name.lower())
        except ValueError:
            print("Invalid Value!!!")
        else:
            break


if __name__ == "__main__":
    adopt_dogs()
    adopt_cats()
    print("Dogs")
    for item in user_pets['dogs']:
        print(item)
    print("Cats")
    for item in user_pets['cats']:
        print(item)
    while True:
        name_of_species = input("Enter species of the pet whose information is required (Dogs/Cats): ")
        name_of_pet = input("Enter name of the pet whose rival is to be seen : ")
        if name_of_species.lower() == 'dogs':
            if name_of_pet.lower() not in dog_list:
                print("You do not have a named Dog called {}".format(name_of_pet))
            else:
                for item in user_pets['dogs']:
                    if item.name == name_of_pet:
                        print("{} Chases {}".format(item.name, item.chases))
        elif name_of_species.lower() == 'cats':
            if name_of_pet not in cat_list:
                print("You do not have a named Cat called {}".format(name_of_pet))
            else:
                for item in user_pets['cats']:
                    if item.name == name_of_pet:
                        print("{} Hates {}".format(item.name, item.hates))
        choice = input("Do you wish to continue(y/n) : )").lower()
        if choice == 'n':
            break
