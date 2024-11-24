RES = WIDTH, HEIGHT = 1200, 700
FPS = 30


TILE_SIZE = 20
TILE_NUM_WIDTH = WIDTH // TILE_SIZE
TILE_NUM_HEIGHT = HEIGHT // TILE_SIZE

MAX_FOOD = 15       #한번에 있을수있는 음식 제한
FOOD_RATE = 0.15  #음식 생성 빈도율


MAX_MOVEMENT = 150
CELL_NUM =  60
MUTANT_RATE =  0.5     #0~1
SURVIVE_PER = 0.25    #상위 몇퍼가 살아남을건지
SURVIVE_PER = int(100 * SURVIVE_PER)

START_POS =  (TILE_NUM_WIDTH // 2, TILE_NUM_HEIGHT//2)



"""
가능한 키
a
d
w


"""
