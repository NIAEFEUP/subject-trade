class Hour:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        if self.hours == other.hours:
            return self.minutes < other.minutes
        return self.hours < other.hours

    def __le__(self, other):
        if self.hours == other.hours:
            return self.minutes <= other.minutes
        return self.hours <= other.hours

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes:
            return True
        else:
            return False