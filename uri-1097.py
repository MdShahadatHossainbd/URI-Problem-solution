x = 1
y = 7
for i in range(5):
  for j in range(3):
    print('I=%d J=%d' %(x, y))
    y -= 1
  x += 2
  y += 5