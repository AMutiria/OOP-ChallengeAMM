class Pet:
    def __init__(self, name):
        """
        Initializes a Pet object.

        Args:
            name (str): The name of the pet.
        """
        self.name = name
        self.hunger = 5  # Initial hunger level
        self.energy = 5  # Initial energy level
        self.happiness = 5  # Initial happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """
        Reduces hunger and increases happiness.
        """
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate and feels a little happier!")

    def sleep(self):
        """
        Increases energy.
        """
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap and feels more rested!")

    def play(self):
        """
        Decreases energy, increases happiness, and increases hunger.
        """
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played and had fun, but is a bit more tired and hungry!")

    def get_status(self):
        """
        Prints the current status of the pet.
        """
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Learned Tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        print("-------------------------\n")

    def train(self, trick):
        """
        Teaches the pet a new trick.

        Args:
            trick (str): The name of the trick to teach.
        """
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        """
        Prints all the learned tricks of the pet.
        """
        if self.tricks:
            print(f"\n--- {self.name}'s Tricks ---")
            for i, trick in enumerate(self.tricks):
                print(f"{i+1}. {trick}")
            print("-------------------------\n")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Example usage:
my_pet = Pet("Buddy")

my_pet.get_status()

my_pet.eat()
my_pet.play()
my_pet.sleep()

my_pet.get_status()

my_pet.train("Sit")
my_pet.train("Fetch")
my_pet.train("Roll Over")
my_pet.train("Sit") # Trying to teach an existing trick

my_pet.show_tricks()

my_pet.get_status()