class Elevator:
    def __init__(self, id, max_floor):
        self.id = id
        self.current_floor = 1
        self.target_floors = []
        self.direction = 0  # 0: 停止, 1: 上行, -1: 下行
        self.door_open = False
        self.max_floor = max_floor

    def add_request(self, floor):
        if 1 <= floor <= self.max_floor and floor not in self.target_floors:
            bisect.insort(self.target_floors, floor)
            self._update_direction()

    def move(self):
        if self.direction == 1:
            self.current_floor += 1
        elif self.direction == -1:
            self.current_floor -= 1
        self._check_arrival()

    def _update_direction(self):
        # 更新电梯运行方向逻辑
        pass