class SCANScheduler:
    def select_elevator(self, floor, direction, elevators):
        # 实现SCAN算法
        return min(elevators, key=lambda e: self._calculate_cost(e, floor))

class NearestScheduler:
    def select_elevator(self, floor, direction, elevators):
        # 最近电梯优先
        return min(elevators, key=lambda e: abs(e.current_floor - floor))