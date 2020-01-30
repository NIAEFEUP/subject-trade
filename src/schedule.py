class Schedule:
    def __init__(self, start_hour, end_hour):
        self.start_hour = start_hour
        self.end_hour = end_hour

    def conflicts(self, other):
        if other.start_hour <= self.start_hour and self.start_hour < other.end_hour:
            return True
        elif other.start_hour < self.end_hour and self.end_hour <= other.end_hour:
            return True
        else: return False