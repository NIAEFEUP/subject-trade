class Schedule:
    def __init__(self, start_hour, end_hour, day):
        self.day = day
        self.start_hour = start_hour
        self.end_hour = end_hour

    def __repr__(self):
        return self.day + " from " + str(self.start_hour) + " to " + str(self.end_hour)

    def conflicts(self, other):
        if self.day != other.day:
            return False

        return (other.start_hour <= self.start_hour < other.end_hour) or \
               (other.start_hour < self.end_hour <= other.end_hour)
