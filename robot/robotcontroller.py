class RobotController(oblect):
    def __init__(self, robots):
        self.robots = robots

    def update(self, deltaTime):
        for robot in self.robots:
            robot.timer += deltaTime
            if robot.getTimer() >= 0.125:
                robot.nextFrame()

            velocity = self.multiply(robot.getVelocity(), deltaTime)
            pos = robot.getPosition()

            x, y = self.add(pos, velocity)

            sx, sy = robot.getVelocity()

            if x < 0:
                x = 0
                sx *= -1
            elif x > 607:
                sx *= -1
            
            if y < 0:
                y = 0
                sy *= -1
            elif y > 447:
                y = 447
                sy *= -1

            robot.setPosition((x, y))
            robot.setVelocity((sx, sy))
    
    def multiply(self, velocity, deltaTime):
        x = velocity[0] * deltaTime
        y = velocity[1] * deltaTime

        return (x, y)

    def add(self, position, velocity):
        x = position[0] + velocity[0]
        y = position[1] + velocity[1]

        return (x, y)

        



