class ControlSystem:
    def __init__(self, elevators, strategy):
        self.elevators = elevators
        self.strategy = strategy
        
    def request_elevator(self, floor, direction):
        """处理外部呼梯请求"""
        elevator = self.strategy.select_elevator(floor, direction, self.elevators)
        elevator.add_external_request(floor, direction)
        return elevator.id

    def get_status(self):
        return {e.id: e.status() for e in self.elevators}
    
     