class Instruction(object):

    def __init__(self, rotation, distance):
        self.rotation = rotation
        self.distance = distance

    def __str__(self):
        return "Rotate: {} deg; Move; {} px".format(self.rotation, self.distance)
