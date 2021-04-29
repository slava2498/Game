vehicle_characteristics = {
    'truck': {
        'name': 'Грузовик',
        'count': {'min': 1, 'max': 4},
        'speed': {'min': 0, 'max': 120},
        'puncture': {'min': 0.4, 'max': 1},
        'elimination': {'min': 3, 'max': 10},
        'weight': {'min': 2500, 'max': 5000},
    },
    'motorcycle': {
        'name': 'Мотоцикл',
        'count': {'min': 1, 'max': 5},
        'speed': {'min': 0, 'max': 300},
        'puncture': {'min': 0, 'max': 1},
        'elimination': {'min': 1, 'max': 4},
        'stroller': {'min': 0, 'max': 1},
    },
    'car': {
        'name': 'Легковушка',
        'count': {'min': 1, 'max': 6},
        'speed': {'min': 0, 'max': 200},
        'puncture': {'min': 0.2, 'max': 1},
        'elimination': {'min': 1, 'max': 7},
        'people': {'min': 1, 'max': 5},
    },
}

race_characteristics = {
    'distance_circle': 500
}