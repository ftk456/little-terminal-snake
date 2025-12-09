

import curses
import random
import time

stdsrc = curses.initscr()
curses.cbreak()
curses.noecho()
curses.newwin(480, 620, 50, 50)
stdsrc.nodelay(True)
stdsrc.keypad(True)
stdsrc.border()

score = 0
snake = [[20, 10], [20, 11], [20, 12], [20, 13], [20, 14]]
apple_x, apple_y = 20, 40
direction = 0

while True:
    stdsrc.addstr(0, 10, f"Score : {score}")
    pad = stdsrc.getch()
    stdsrc.refresh()
    time.sleep(0.1)

    stdsrc.addch(apple_x, apple_y, "@")

    for i in snake:
        stdsrc.addch(i[0], i[1], '*')
        if snake[0][0] == i[0] and snake[0][1] == i[1]:
            break

    if pad == curses.KEY_EXIT:
        break

    if pad == curses.KEY_UP:
        direction = 1
    elif pad == curses.KEY_DOWN:
        direction = 2
    elif pad == curses.KEY_LEFT:
        direction = 3
    elif pad == curses.KEY_RIGHT:
        direction = 4

    if direction == 1:
        snake[0][0] -= 1
    elif direction == 2:
        snake[0][0] += 1
    elif direction == 3:
        snake[0][1] -= 1
    elif direction == 4:
        snake[0][1] += 1

    if snake[0][0] <= 0 or snake[0][0] >= 24 or snake[0][1] <= 0 or snake[0][1] >= 80:
        break

    snake.insert(1, [snake[0][0], snake[0][1]])

    if snake[0][0] == apple_x and snake[0][1] == apple_y:
        apple_x = random.randint(2, 22)
        apple_y = random.randint(2, 79)
        if apple_x == snake and apple_y == snake:
            apple_x = random.randint(2, 22)
            apple_y = random.randint(2, 79)
        score += 1
    else:
        popped = snake.pop()
        stdsrc.addch(popped[0], popped[1], ' ')

stdsrc.nodelay(False)
curses.echo()
curses.endwin()

