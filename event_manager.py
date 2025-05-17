class EventManager:
    def __init__(self):
        self.timeline = []
        
    def add_event(self, delay, callback):
        heapq.heappush(self.timeline, (time.time() + delay, callback))

    def process_events(self):
        while self.timeline and self.timeline[0][0] <= time.time():
            _, callback = heapq.heappop(self.timeline)
            callback()