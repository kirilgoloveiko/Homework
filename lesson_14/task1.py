class Robot:
    def __init__(self, start_x: int, start_y: int):
        self.start_x = start_x
        self.start_y = start_y

    def move(self, commands: str):
        for com in commands.upper():
            if com == "N":
                self.start_y += 1
            elif com == "S":
                self.start_y -= 1
            elif com == "E":
                self.start_x += 1
            elif com == "W":
                self.start_x -= 1
            if self.start_x < 0 or self.start_x > 100 or self.start_y < 0 or self.start_y > 100:
                return "Out of field"
        return [self.start_x, self.start_y]


Charlie = Robot(0, 0)
