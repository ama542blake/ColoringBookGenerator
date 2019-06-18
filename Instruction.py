class Instruction(object):
    def __init__(self, rotation, distance):
        self.rotation = rotation
        self.distance = distance

    # used in the ListBox to make instructions user-readable
    def __str__(self):
        return "Rotate: {} deg; Move; {} px".format(self.rotation, self.distance)
