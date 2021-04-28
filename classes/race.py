class Race:
	def __init__(self, distance_circle=3000):
		self.circle = 1
		self.distance_circle = distance_circle
		self.distance = distance_circle
		self.finished_array = []

	def next_circle(self):
		self.circle += 1 
		self.distance = self.distance_circle * self.circle
		self.finished_array = []

	def update_finished(self, vehicle):
		self.finished_array.append(vehicle)

	@staticmethod
	def is_finish(vehicle_array):
		return not [x for x in vehicle_array if not x.finish]

	def get_result(self):
		return '\n'.join(['{} {}'.format(i + 1, x.name) for i, x in enumerate(self.finished_array)])