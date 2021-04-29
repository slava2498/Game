import random
import time
from threading import Thread

from config import (vehicle_characteristics as v_charact, 
                    race_characteristics as r_charact)

from classes.vehicle import Truck, Car, Motorcycle
from classes.race import Race


vehicle_array = []
race = Race(r_charact['distance_circle'])

# генерится количество грузовиков
name = 'truck'
range_v = range(v_charact[name]['count']['min'], 
    random.randint(
        v_charact[name]['count']['min']+1,
        v_charact[name]['count']['max']
    )+1
)

for x in range_v:
    vehicle_array.append(
        Truck(
            name='{} №{}'.format(v_charact[name]['name'], x),
            speed=random.uniform(v_charact[name]['speed']['min'], v_charact[name]['speed']['max']),
            puncture=random.uniform(v_charact[name]['puncture']['min'], v_charact[name]['puncture']['max']),
            elimination=random.uniform(v_charact[name]['elimination']['min'], v_charact[name]['elimination']['max']),
            weight=random.uniform(v_charact[name]['weight']['min'], v_charact[name]['weight']['max']),
        )
    )

# генерится количество мотоциклов
name = 'motorcycle'
range_v = range(v_charact[name]['count']['min'], 
    random.randint(
        v_charact[name]['count']['min']+1,
        v_charact[name]['count']['max']
    )+1
)

for x in range_v:
    vehicle_array.append(
        Motorcycle(
            name='{} №{}'.format(v_charact[name]['name'], x),
            speed=random.uniform(v_charact[name]['speed']['min'], v_charact[name]['speed']['max']),
            puncture=random.uniform(v_charact[name]['puncture']['min'], v_charact[name]['puncture']['max']),
            elimination=random.uniform(v_charact[name]['elimination']['min'], v_charact[name]['elimination']['max']),
            stroller=random.randint(v_charact[name]['stroller']['min'], v_charact[name]['stroller']['max'])
        )
    )

# генерится количество машин
name = 'car'
range_v = range(v_charact[name]['count']['min'], 
    random.randint(
        v_charact[name]['count']['min']+1,
        v_charact[name]['count']['max']
    )+1
)

for x in range_v:
    vehicle_array.append(
        Car(
            name='{} №{}'.format(v_charact[name]['name'], x),
            speed=random.uniform(v_charact[name]['speed']['min'], v_charact[name]['speed']['max']),
            puncture=random.uniform(v_charact[name]['puncture']['min'], v_charact[name]['puncture']['max']),
            elimination=random.uniform(v_charact[name]['elimination']['min'], v_charact[name]['elimination']['max']),
            people=random.randint(v_charact[name]['people']['min'], v_charact[name]['people']['max'])
        )
    )

def ticker(vehicle):
    # while, пока объект не финишировал
    while not vehicle.moving(distance_circle=race.distance_circle):
        print('{} проехал {} м.'.format(
            vehicle.name, 
            round(vehicle.distance, 3))
        )
        # прокол колеса
        if vehicle.is_puncture(puncture=random.uniform(0, 1)):
            print('------{} проколол колесо. Остановился на {} сек------'.format(
                vehicle.name, 
                round(vehicle.puncture, 3))
            )
            time.sleep(vehicle.elimination)
    else:
        race.update_finished(vehicle)
        print('!!!!!!! {} проехал {} м и финишировал !!!!!!!'.format(
            vehicle.name, 
            round(vehicle.distance, 3))
        )

# наблюдатель за гонкой
def observer():
    while True:
        if Race.is_finish(vehicle_array):
            print('% Наблюдатель: Гонщики проехали круг и {} м %\n' \
                'Пустить игроков ещё на один круг?\nДа/Нет'.format(race.distance)
            )
            def question():
                answer = input().lower()
                if answer not in ['да', 'нет']:
                    print('Введите Да/Нет')
                    question()
                    return
                else:
                    return 'да' in answer

            if question():
                # обнуляем у vehicle finish и добавляем новый круг 
                for x in vehicle_array:
                    x.reset_finish()
                race.next_circle()
                main()
            else:
                print('!!!Гонка закончилась!!!\nПорядок финиширования:\n{}'.format(
                    race.get_result())
                )
            return

def main():
    for vehicle in vehicle_array:
        Thread(target=ticker, args=(vehicle, )).start()

    Thread(target=observer).start()

if __name__ == "__main__":
    main()



            
            