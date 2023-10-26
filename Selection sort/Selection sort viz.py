import numpy as np
import pygame
import time
import random

def selection_sort(arr, win, h, w):
    for i in range(len(arr) - 1):

        elMin = i
        for j in range(i, len(arr)):
            win.fill((0, 0, 0))
            draw_blue_rect(arr, win, h, w)

            pygame.draw.line(win, (255,0,0), ((j*10)+5, h - arr[j]), ((j*10)+5, h), w)
            pygame.draw.line(win, (75, 255, 100), (((elMin)*10)+5, h - arr[elMin]), (((elMin)*10)+5, h), w)
            pygame.display.update()
            time.sleep(0.05)

            play_sound(arr[j])

            if arr[j] < arr[elMin]:
                elMin = j

        if elMin != i:
            arr[i], arr[elMin] = arr[elMin], arr[i]

    return arr

def draw_blue_rect(arr, win, h, rect_w):
    blue = (65, 105, 225)
    for j in range(len(arr)):
        start_pos = (j * 10 + 5, h - arr[j])
        end_pos = ((j * 10 + 5), h)
        pygame.draw.line(win, blue, start_pos, end_pos, rect_w)

def play_sound(f):
    sampling_rate = 44100
    f = f 
    duration = 0.05
    frames = int(duration * sampling_rate)
    arr = np.sin(2 * np.pi * f * np.linspace(0, duration, frames))
    sound = np.asarray([32767 * arr, 32767 * arr]).T.astype(np.int16)
    sound = pygame.sndarray.make_sound(sound.copy())
    sound.play()

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    WIDTH, HEIGHT = 640, 512
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Selection sort")

    rect_w = 9
    num_rect = int(WIDTH/10)

    start_value = 1
    end_value = HEIGHT
    interval = 8

    #Generate a list of numbers with a constant interval
    rect_h = list(range(start_value, end_value + 1, interval))
    random.shuffle(rect_h)
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                sortedArr = selection_sort(rect_h, win, HEIGHT, rect_w)

                win.fill((0,0,0))
                draw_blue_rect(sortedArr, win, HEIGHT, rect_w)

                for i in range(len(sortedArr)):
                    start_pos = (i * 10, HEIGHT - sortedArr[i])
                    end_pos = (i * 10, HEIGHT)
                    pygame.draw.line(win, (0, 255, 0), start_pos, end_pos, rect_w) 
                    play_sound(i)
                    time.sleep(0.05)
                    pygame.display.update()  