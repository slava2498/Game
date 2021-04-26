import time

class Race:
	def __init__(self, distance=3000):
		self.distance = distance
		self.time_start = time.time()

	def get_time(self):
		return time.time()

	def finish(self, vehicle_array):
		remaining = [x for x in vehicle_array if not x.finish]
		return not bool(remaining)