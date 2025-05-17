class ElevatorSystem:
    def __init__(self):
        self.config = Config()
        self.elevators = [Elevator(i, self.config.settings['floor_range'][1]) 
                         for i in range(self.config.settings['num_elevators'])]
        self.scheduler = SCANScheduler()
        self.control = ControlSystem(self.elevators, self.scheduler)
        self.ui = ConsoleUI()
        self.event_manager = EventManager()
        
    def run(self):
        while True:
            self._process_movements()
            self.ui.display(self.control.get_status())
            self._handle_user_input()
            self.event_manager.process_events()
            time.sleep(0.1)