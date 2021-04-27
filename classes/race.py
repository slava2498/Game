import time

class Race:
	def __init__(self, distance=3000):
		self.time_start = time.time()
		self.circle = 1
		self.distance = distance * self.circle

	def get_timerace(self):
		return time.time() - self.time_start

	def next_circle(self):
		self.circle += 1 
		self.distance *= self.circle

	def is_finish(self, vehicle_array):
		remaining = [x for x in vehicle_array if not x.finish]
		print(remaining)
		return not remaining