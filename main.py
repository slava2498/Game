import random
import time
import asyncio
from classes.vehicle import Truck, Car, Motorcycle
from classes.race import Race


vehicle_array = []

for x in range(1, random.randint(1, 3)+1):
    vehicle_array.append(
        Truck(
            name='Грузовик №{}'.format(x),
            speed=random.uniform(0, 120),
            puncture=random.uniform(0.4, 1),
            elimination=random.uniform(3, 10),
            weight=5000 # кг
        )
    )

for x in range(1, random.randint(1, 5)+1):
    vehicle_array.append(
        Motorcycle(
            name='Мотоцикл №{}'.format(x),
            speed=random.uniform(0, 300),
            puncture=random.uniform(0, 1),
            elimination=random.uniform(1, 4),
        )
    )

for x in range(1, random.randint(1, 6)+1):
    vehicle_array.append(
        Car(
            name='Легковушка №{}'.format(x),
            speed=random.uniform(0, 200),
            puncture=random.uniform(0.2, 1),
            elimination=random.uniform(1, 7),
            people=random.randint(1, 5)
        )
    )

loop = asyncio.get_event_loop()

async def ticker(vehicle, race):
    if not vehicle.moving(clock=race.get_time() - race.time_start, distance_circle=race.distance):
        print('{} прошёл {} м.'.format(vehicle.name, vehicle.distance))
    else:
        print('!!!!!!! {} финишировал !!!!!!!'.format(vehicle.name))
        self.transport.close()

    if vehicle.set_puncture(puncture=random.uniform(0, 1)):
        print('{} проколол колесо'.format(vehicle.name))
        await asyncio.sleep(vehicle.elimination)

    if race.finish(vehicle_array):
        print('Гонщики проехали круг\nПустить игроков ещё на один круг?\nДа/Нет')
        def question():
            answer = input().lower
            if answer not in ['да', 'нет']:
                print('Введите Да/Нет')
                question()
                return
            else:
                return 'да' in answer

        if question():
            for x in vehicle_array:
                x.set_finish(False)

            asyncio.run(main())


async def main():
    race = Race(3000)
    while True:
        tasks = [asyncio.create_task(ticker(vehicle, race)) for vehicle in vehicle_array if not vehicle.finish] 
        await asyncio.gather(*tasks)

asyncio.run(main())


            
            