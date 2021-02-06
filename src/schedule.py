class Schedule:
    def __init__(self, start_hour, end_hour, day):
        self.day = day
        self.start_hour = start_hour
        self.end_hour = end_hour

    def __repr__(self):
        return self.day + " from " + str(self.start_hour) + " to " + str(self.end_hour)

    def conflicts(self, other):
        if self.day == other.day:
            if other.start_hour <= self.start_hour and self.start_hour < other.end_hour:
                return True
            elif other.start_hour < self.end_hour and self.end_hour <= other.end_hour:
                return True
            else: return False
        else: return False