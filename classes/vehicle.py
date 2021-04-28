import time

class Vehicle:
	def __init__(self, name, speed=1, puncture=1, elimination=1):
		self.name = name
		self.speed = speed
		self.puncture = puncture
		self.elimination = elimination # время устранения прокола, в сек
		self.distance = 0
		self.finish = False
		self.time_start = time.time()

	def moving(self, distance_circle):
		self.distance = self.speed * (time.time() - self.time_start)
		self.finish = self.distance > distance_circle
		return self.finish

	def is_puncture(self, puncture):
		return puncture > self.puncture

	def reset_finish(self):
		self.time_start = time.time()
		self.finish = False

	def get_characteristics(self, **kwargs):
		translater_params = {
			'name': 'Название',
			'speed': 'Скорость',
			'puncture': 'Вероятность прокола',
			'weight': 'Масса',
			'people': 'Кол-во человек',
			'stroller': 'Коляска',
		}
		print(' '.join(
			[
				"{}: {}".format(
					translater_params[key] if key in translater_params else key, value
				) 
				for key, value in kwargs.items()
			]
		))


class Truck(Vehicle):
	def __init__(self, name, speed, puncture, elimination, weight=1):
		Vehicle.__init__(self, name, speed, puncture, elimination)
		self.weight = weight

		Vehicle.get_characteristics(
			self,
			name=self.name,
			speed=self.speed, 
			puncture=self.puncture, 
			weight=self.weight
		)

class Car(Vehicle):
	def __init__(self, name, speed, puncture, elimination, people=1):
		Vehicle.__init__(self, name, speed, puncture, elimination)
		self.people = people

		Vehicle.get_characteristics(
			self,
			name=self.name,
			speed=self.speed, 
			puncture=self.puncture, 
			people=self.people
		)

class Motorcycle(Vehicle):
	def __init__(self, name, speed, puncture, elimination, stroller=False):
		Vehicle.__init__(self, name, speed, puncture, elimination)
		self.stroller = stroller

		Vehicle.get_characteristics(
			self,
			name=self.name,
			speed=self.speed, 
			puncture=self.puncture, 
			stroller=self.stroller
		)