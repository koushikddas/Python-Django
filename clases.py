class Bird:
    def __init__(self,color,sound,height):
        self.color = color
        self.sound = sound
        self.height = height

    def flying(self):
        return "%s is flying" % self.sound

    def shining(self):
        return "%s is shinny color really it is" % self.color

if __name__== "__main__":
    crow = Bird('black','ka ka ka',12)
    print(crow.flying())
    print(crow.shining())