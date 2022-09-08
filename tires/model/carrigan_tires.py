from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, sensors) -> None:
        self.sensors = sensors
    
    def needs_service(self):
        return any(sensor >= 0.9 for sensor in self.sensors) 