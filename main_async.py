import random
import time
import asyncio

from config import (vehicle_characteristics as v_charact, 
                    race_characteristics as r_charact)

from classes.vehicle import Truck, Car, Motorcycle
from classes.race import Race


vehicle_array = []
race = Race(r_charact['distance_circle'])

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

async def ticker(vehicle):
    while not vehicle.moving(distance_circle=race.distance_circle):
        print('{} проехал {} м.'.format(
            vehicle.name, 
            round(vehicle.distance, 3))
        )
        if vehicle.is_puncture(puncture=random.uniform(0, 1)):
            print('------{} проколол колесо. Остановился на {} сек------'.format(
                vehicle.name, 
                round(vehicle.puncture, 3))
            )
            await asyncio.sleep(vehicle.elimination)  
    else:
        race.update_finished(vehicle)
        print('!!!!!!! {} проехал {} м и финишировал !!!!!!!'.format(
            vehicle.name, 
            round(vehicle.distance, 3))
        )
    

async def observer():
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
                for x in vehicle_array:
                    x.reset_finish()
                race.next_circle()
                await main()
            else:
                print('!!!Гонка закончилась!!!\nПорядок финиширования:\n{}'.format(
                    race.get_result())
                )
            return
        else:
            await asyncio.sleep(1)  


async def main():
    tasks = [asyncio.create_task(ticker(vehicle)) for vehicle in vehicle_array] 
    tasks.append(asyncio.create_task(observer()))
    await asyncio.gather(*tasks)
    

asyncio.run(main())


            
            