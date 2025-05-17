class Config:
    def __init__(self):
        self.settings = {
            'floor_range': (1, 20),
            'elevator_speed': 2,  # 秒/层
            'door_time': 3,        # 秒
            'num_elevators': 4
        }
    
    def load_from_file(self, path):
        # 从配置文件加载
        pass