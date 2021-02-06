class Hour:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        return str(self.hours) + ":" + str(self.minutes)

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
    
    def __add__(self, other):
        minutes = self.minutes + other.minutes 
        overflow = int(minutes/60)
        minutes = minutes % 60

        hours = self.hours + other.hours + overflow

        hours = hours % 24

        return Hour(hours, minutes)
