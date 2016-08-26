 
class Clock:
    def __init__(self, h, m):
        self.hours = h
        self.minutes = m    
        
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        
        if self.hours > 23:
            self.hours = self.hours % 24
        
        while self.minutes < 0:
            self.minutes += 60
            self.hours -= 1
        
        if self.hours < 0:
            self.hours = self.hours % 24
            
    def __str__(self):
        if self.hours < 10:
            hours_str = '0' + str(self.hours)
        else:
            hours_str = str(self.hours)
        
        if self.minutes < 10:
            minutes_str = '0' + str(self.minutes)
        else:
            minutes_str = str(self.minutes)
        
        return hours_str + ':' +  minutes_str
    
    def __eq__(self, other):
        if self.hours != other.hours: return False
        if self.minutes != other.minutes: return False
        return True

    def add(self, m):
        tot_min = (self.hours * 60) + self.minutes
        tot_min += m
        self.hours = (tot_min / 60) % 24
        self.minutes = tot_min % 60
        
        return Clock(self.hours, self.minutes)
