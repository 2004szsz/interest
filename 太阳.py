import turtle as t

t.color('red', 'pink')

t.color('red', 'pink')
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break