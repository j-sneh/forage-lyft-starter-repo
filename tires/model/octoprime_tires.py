from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensors) -> None:
        self.sensors = sensors
    
    def needs_service(self):
        return sum(self.sensors) >= 3