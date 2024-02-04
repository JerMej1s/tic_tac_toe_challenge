import time

from enum import Enum

class TimeUnit(Enum):
    SECONDS = 's'
    MILLISECONDS = 'ms'
    NANOSECONDS = 'ns'

class Timer:
    def __init__(self, unit: TimeUnit = TimeUnit.SECONDS):
        self.unit = unit
        self.start_time = None
        self.end_time = None
        self.duration = None
    
    def start(self) -> None:
        if self.unit is TimeUnit.MILLISECONDS:
            self.start_time = time.time() * 1000
        elif self.unit is TimeUnit.NANOSECONDS:
            self.start_time = time.perf_counter_ns()
        else:
            self.start_time = time.time()
        
        self.end_time = None
        self.duration = None
    
    def stop(self) -> float:
        if  self.unit is TimeUnit.MILLISECONDS:
            self.end_time = time.time() * 1000
        elif self.unit is TimeUnit.NANOSECONDS:
            self.end_time = time.perf_counter_ns()
        else:
            self.end_time = time.time()

        self.duration = self.end_time - self.start_time
        
        return self.duration
