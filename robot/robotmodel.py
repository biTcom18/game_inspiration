# Robot model class. Contains data of robots
class RobotModel(object):
    def __init__(self, x, y, frame, speed):
        self.x = x
        self.y = y
        self.frame = frame
        self.speed = speed
        self.timer = 0  
    
    def setPosition(self, newPosition):
        self.x, self.y = newPosition

    def getPosition(self):
        return (self.x, self.y)

    def getFrame(self):
        return self.frame

    def nextFrame(self):
        self.timer = 0
        self.frame += 1
        self.frame %= 4
    
    def getTimer(self):
        return self.timer

    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed
