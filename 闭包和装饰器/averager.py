class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    serious = []

    def averager(new_value):
        serious.append(new_value)
        total = sum(serious)
        return total / len(serious)

    return averager
