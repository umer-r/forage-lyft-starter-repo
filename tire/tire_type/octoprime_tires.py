from tire.tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        sum = 0
        for i in self.tire_wear:
            sum = sum + i
            if sum >= 3.0:
               return True
            
        return False