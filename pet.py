class Pet:
    
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.spd = 15
        self.hunger = [5,5]
        self.health = [10,10]
        self.direction = 0

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def play(self):
        print("Yipee!")

    def turn_left(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction = 3

    def turn_right(self):
        self.direction += 1
        if self.direction > 3:
            self.direction = 0

    def move(self,distance):
        if self.direction == 0:
            self.y -= distance
        elif self.direction == 1:
            self.x += distance
        elif self.direction == 2:
            self.y += distance
        elif self.direction == 3:
            self.x -= distance

    def kill(self,other):
        if abs(self.x - other.x) <= 1 \
           and abs(self.y - other.y) <=1:
            other.health[0] = 0
        else:
            print("Not in kill range.")
        

    def eat(self):
        print("Nom Nom Nom...")
        self.hunger[0] = self.hunger[1]

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"

bill = Pet("Bill")
steve = Pet("Steve")
    
