class pinum:
    def __init__(self, grades):
        self.num = grades
        self.pin = 180 / self.num
    def __str__(self):
        return f'PI/{self.pin:.3g}'