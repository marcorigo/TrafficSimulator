AUTO = False

config = {
    'BLOCK_SIZE': 50,
    'DEBUG': False,
    'MAX_VEICHLE_NUMBER': 200,
    'VEICHLES_SPAWN_INTERVAL': AUTO,
    'BACKGROUND_COLOR': (120, 226, 104),
    'SIDE_WALK_SIZE': AUTO,
    'ROAD_COLOR': (170, 170, 170),
    'SIDE_WALK_COLOR': (94, 94, 94),
    'ROAD_LINE_QUANTITY': 5,
    'TRAFFIC_LIGHT_BORDER_SIZE': 1,
    'TRAFFIC_LIGHT_BORDER_COLOR': (96, 96, 96),
    'TRAFFIC_LIGHT_YELLOW_TIME': 4,
    'TRAFFIC_LIGHT_MIN_TIME_CHANGING': 15,
    'TRAFFIC_LIGHT_MAX_TIME_CHANGING': 20,
    'CAR_WIDTH': AUTO,
    'CAR_HEIGHT': AUTO,
    'TRUCK_WIDTH': AUTO,
    'TRUCK_HEIGHT': AUTO,

    'EXPLOSION_PERSISTANCE': 3,

    'VEICHLE_VISION_FIELD_WIDTH': AUTO,

    'TRAFFIC_LIGHT_COLORS': {
        'red' : (255, 0, 0),
        'yellow': (247, 228, 86),
        'green': (87, 226, 40)
    }
}