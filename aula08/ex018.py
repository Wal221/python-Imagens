import math

ang = int(input('Angulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
senoo = math.sin(math.radians(ang))

print('sen: {} cos: {} tg: {}'.format(senoo, cosseno, tangente))

