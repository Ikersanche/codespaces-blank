e = input('Equip: ')
p = int(input('puntuació: '))
robot = {
      e:p,
}
r = p
while len(robot) <= 3:
 e = input('Equip:')
 p = int(input('Puntuació: '))
robot[e] = p
r = r + p
print(r)

