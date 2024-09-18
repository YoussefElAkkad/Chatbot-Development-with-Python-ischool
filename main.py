# a=[]
# for x in range(1,11):
#     a.append(x*x)
# print("List a: %s"%a)

# b=[x**2 for x in range(1,11)] #list comprehension
# print("List b: %s"%b)

# #normal division
# result=5/3
# print(result)
# #integer division(floor division)
# result=5//3
# print(result)

# #f-strings(formatted StringLiterals )
# name="Alice"
# print(f"Hello, {name}!")
# print(f"List a: {a}")

# def double(x):
#     return x*2

# number=7
# print(f"Double of {number} is {double(number)}.")

# pi=3.14159265359
# print(f"pi = {pi:.4f}")


# #chained comparision
# x=5
# if 1<x<10:
#     print("x is between 1 and 10.")
# else:
#     print("x is not between 1 and 10.")


# #List comprehension
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_numbers=[number for number in numbers if number%2==0]
# print(f"Even Numbers of {numbers} is {even_numbers}")


import pygame
import sys
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
SHAPE_SIZE = 100
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Clicking Game")
shape_x, shape_y = SCREEN_WIDTH // 2 - SHAPE_SIZE // 2, SCREEN_HEIGHT // 2 - SHAPE_SIZE // 2
shape_color = RED
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if shape_x <= mouse_x <= shape_x + SHAPE_SIZE and shape_y <= mouse_y <= shape_y + SHAPE_SIZE:
                shape_color = BLUE if shape_color == RED else RED
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, shape_color, (shape_x, shape_y, SHAPE_SIZE, SHAPE_SIZE))
    pygame.display.flip()