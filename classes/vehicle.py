class Vehicle:
	def __init__(self, name, speed=1, puncture=1, elimination=1):
		self.name = name
		self.speed = speed
		self.puncture = puncture
		self.elimination = elimination # время устранения прокола, в сек
		self.distance = 0
		self.finish = False

	def moving(self, clock, distance_circle):
		self.distance = self.speed * clock
		self.finish = self.distance > distance_circle
		return self.finish

	def is_puncture(self, puncture):
		return puncture > self.puncture

	def reset_finish(self):
		self.finish = True


class Truck(Vehicle):
	def __init__(self, name, speed, puncture, elimination, weight=1):
		Vehicle.__init__(self, name, speed, puncture, elimination)
		self.weight = weight

class Car(Vehicle):
	def __init__(self, name, speed, puncture, elimination, people=1):
		Vehicle.__init__(self, name, speed, puncture, elimination)
		self.people = people

class Motorcycle(Vehicle):
	def __init__(self, name, speed, puncture, elimination, stroller=False):
		Vehicle.__init__(self, name, speed, puncture, elimination)
		self.stroller = stroller