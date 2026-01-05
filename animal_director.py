class AnimalDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_position()
        self.builder.set_images()
        return self.builder.get_result()
