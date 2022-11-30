
# The model class, contains just the data for the robot
class RobotModel(object):

    def __init__(self, x, y, frame, velocity):
        self.x = x
        self.y = y
        self.frame = frame
        self.speed = velocity
        self.timer = 0
        # We will use 'timer' member field to control the current frame of the robot 

    def setPosition(self, newPosition):
        self.x, self.y = newPosition

    def getFrame(self):
        return self.frame
    
    def nextFrame(self):
        self.timer = 0
        self.frame += 1
        self.frame %= 4

    def getTimer(self):
        return self.timer

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, velocity):
        self.velocity = velocity


