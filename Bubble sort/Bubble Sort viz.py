import pygame
import random
import time
import numpy as np

def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

def bubble_sort(arr):
    while not isSorted(arr):
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1] #swap elements
            
    return arr

def play_sound(f):
    sampling_rate = 44100 
    f = f * 50
    duration = 0.05
    frames= int(duration*sampling_rate)
    arr = np.sin(2*np.pi*f*np.linspace(0,duration,frames))
    sound = np.asarray([32767*arr, 32767*arr]).T.astype(np.int16)
    sound = pygame.sndarray.make_sound(sound.copy())
    sound.play()

def draw_rect(win, h, rect_w, rect_h):
    blue = (65, 105, 225)    

    while not isSorted(rect_h):
        #Swapping elements
        for j in range(1, len(rect_h)):
            win.fill((0,0,0))
            for i in range(len(rect_h)): #Drawing the rect
                start_pos = (i * 10, h - rect_h[i])
                end_pos = (i * 10, h)
                pygame.draw.line(win, blue, start_pos, end_pos, rect_w)

            if rect_h[j - 1] > rect_h[j]:
                pygame.draw.line(win, (255,0,0), ((j-1) * 10, h - rect_h[j-1]), ((j-1) * 10, h), rect_w)
                pygame.draw.line(win, (0,255,0), (j * 10, h - rect_h[j]), (j * 10, h), rect_w)
                rect_h[j - 1], rect_h[j] = rect_h[j], rect_h[j - 1] #swap elements
                play_sound(j-1)
                play_sound(j)
                time.sleep(0.05)
            pygame.display.update() 

    for i in range(len(rect_h)): #Drawing the rect
        start_pos = (i * 10, h - rect_h[i])
        end_pos = (i * 10, h)
        pygame.draw.line(win, (0, 255, 0), start_pos, end_pos, rect_w) 
        play_sound(i)
        time.sleep(0.05)
        pygame.display.update()      
    

def main():
    pygame.init()
    pygame.mixer.init()
    WIDTH, HEIGHT = 480, 360
    WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Initiating window
    pygame.display.set_caption("Bubble sort")

    rect_w = 9
    num_rect = int(WIDTH / 10)
    rect_h = random.sample(range(0, HEIGHT), num_rect)

    running = True

    while running:
        # Quitting window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                draw_rect(WIN, HEIGHT, rect_w, rect_h)

        pygame.display.update()

    pygame.quit()

    # arr = [3, 8, 1, 9, 5, 6]
    # print(f"original array: {arr}")
    # sorted_arr = bubble_sort(arr)
    # print(f"Sorted array: {sorted_arr}")
    
if __name__ == "__main__":    
    main() 