import numpy as np
import pygame
import time

def insertion_sort(arr, win, h, rect_w):
    for i in range(1, len(arr)):
        win.fill((0,0,0))
        draw_blue_rect(arr, win, h, rect_w)

        j = i - 1
        element = arr[i]
        while j >= 0 and element < arr[j]: #checks and swaps with the previous elements
            pygame.draw.line(win, (255,0,0), ((j*10)+5, h - arr[j]), ((j*10)+5, h), rect_w)
            pygame.draw.line(win, (75, 255, 100), (((j+1)*10)+5, h - arr[j+1]), (((j+1)*10)+5, h), rect_w)
            pygame.display.update()
            arr[j+1] = arr[j]
            j -= 1
            play_sound(j-1)
            play_sound(j)
            time.sleep(0.05)
        arr[j+1] = element

def draw_blue_rect(arr, win, h, rect_w):
    blue = (65, 105, 225)
    for j in range(len(arr)):
        start_pos = (j * 10 + 5, h - arr[j])
        end_pos = ((j * 10 + 5), h)
        pygame.draw.line(win, blue, start_pos, end_pos, rect_w)

def play_sound(f):
    sampling_rate = 44100
    f = f * 25
    duration = 0.05
    frames = int(duration * sampling_rate)
    arr = np.sin(2 * np.pi * f * np.linspace(0, duration, frames))
    sound = np.asarray([32767 * arr, 32767 * arr]).T.astype(np.int16)
    sound = pygame.sndarray.make_sound(sound.copy())
    sound.play()

if __name__ == "__main__":
    #Initialising pygame
    pygame.init()
    pygame.mixer.init()
    WIDTH, HEIGHT = 640, 480
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Insertion sort")

    #Initialising attributes for the rectangles
    rect_w = 9
    num_rect = int(WIDTH / 10)
    rect_h = np.random.randint(1, HEIGHT, num_rect)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                insertion_sort(rect_h, win, HEIGHT, rect_w) #drawing rects
                win.fill((0,0,0))
                for i in range(len(rect_h)):
                    pygame.draw.line(win, (75, 100, 255), ((i*10)+5, HEIGHT - rect_h[i]), ((i*10)+5, HEIGHT), rect_w)
                
                pygame.display.update()

                for i in range(len(rect_h) ):
                    start_pos = (i * 10, HEIGHT - rect_h[i])
                    end_pos = (i * 10, HEIGHT)
                    pygame.draw.line(win, (0, 255, 0), start_pos, end_pos, rect_w) 
                    play_sound(i)
                    time.sleep(0.05)
                    pygame.display.update()  

    pygame.quit()