import random
import time
from threading import Thread
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
            weight=5000
        )
    )

for x in range(1, random.randint(1, 5)+1):
    vehicle_array.append(
        Motorcycle(
            name='Мотоцикл №{}'.format(x),
            speed=random.uniform(0, 300),
            puncture=random.uniform(0, 1),
            elimination=random.uniform(1, 4),
            stroller=bool(random.randint(0, 1))
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

def ticker(vehicle, race):
    while not vehicle.moving(clock=race.get_timerace(), distance_circle=race.distance):
        print('{} прошёл {} м.'.format(vehicle.name, round(vehicle.distance, 3)))
        if vehicle.is_puncture(puncture=random.uniform(0, 1)):
            print('------{} проколол колесо. Остановился на {} сек------'.format(vehicle.name, round(vehicle.puncture, 3)))
            time.sleep(vehicle.elimination)

    print('!!!!!!! {} финишировал !!!!!!!'.format(vehicle.name))

def main():
    race = Race(500)
    for vehicle in vehicle_array:
        th = Thread(target=ticker, args=(vehicle, race))
        th.start()
    
    if race.is_finish(vehicle_array):
        print('Гонщики проехали круг\nПустить игроков ещё на один круг?\nДа/Нет')
        def question():
            answer = input().lower()
            if answer not in ['да', 'нет']:
                print('Введите Да/Нет')
                question()
                return
            else:
                return 'да' in answer

        if question():
            for x in vehicle_array:
                x.reset_finish()
            race.next_circle()
            main()
        else:
            print('Гонка закончилась')

if __name__ == "__main__":
    main()



            
            