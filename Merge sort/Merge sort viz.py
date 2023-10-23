import random
import pygame
import time
import numpy as np

def merge_sort(arr, win, h, w):
    blue = (65, 105, 225)
    while len(arr) != 1:
        win.fill((0,0,0))
        l = len(arr)

        counter = 0
        for i in range(l): # Draw all the rectangles
            for j in range(len(arr[i])):
                start_pos = ((counter * 10) + 5, h - arr[i][j])
                end_pos = (((counter * 10) + 5), h)
                counter += 1
                pygame.draw.line(win, blue, start_pos, end_pos, w)
        
        pygame.display.update()


        counter = 0
        for i in range(l):
            if len(arr[i]) == len(arr[i+1]):
                tempArr = []

                a = b = 0  

                while a < len(arr[i]) and b < len(arr[i]): 
                    if arr[i][a] < arr[i+1][b]:
                        tempArr.append(arr[i][a])
                        a += 1
                    else:
                        tempArr.append(arr[i+1][b])
                        b += 1
                
                while a < len(arr[i]):
                    tempArr.append(arr[i][a])
                    a += 1
                
                while b < len(arr[i+1]):
                    tempArr.append(arr[i+1][b])
                    b += 1

                for j in range(len(arr[i])):
                    pygame.draw.line(win, (255,0,0), (((counter + j)*10) + 5, h - arr[i][j]), (((counter + j)*10)+5, h), w)
                    play_sound(arr[i][j])

                    pygame.draw.line(win, (75, 255, 100), ((((counter + j + len(arr[i+1])))*10)+5, h-arr[i+1][j]), (((counter + j + len(arr[i+1]))*10)+5, h), w)  
                    play_sound(arr[i+1][j])
                    time.sleep(0.05) 
                    pygame.display.update()

                arr[i] = tempArr
                arr.remove(arr[i+1])
                break
            
            for j in range(len(arr[i])): counter +=1 
    return arr

def play_sound(f):
    sampling_rate = 44100
    f = f *5
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
    WIDTH, HEIGHT = 640, 512
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Insertion sort")

    #Initialising attributes for the rectangles
    rect_w = 9
    num_rect = int(WIDTH / 10)

    # Set parameters
    start_value = 1
    end_value = HEIGHT
    interval = 8

    # Generate a list of numbers with a constant interval
    number_list = list(range(start_value, end_value + 1, interval))
    random.shuffle(number_list)
    rect_h = [[i] for i in number_list]

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                arr = merge_sort(rect_h, win, HEIGHT, rect_w)
                win.fill((0,0,0))
                for i in range(len(arr[0])+1):
                    blue = (65, 105, 225)
                    for j in range(i):
                        start_pos = ((j * 10) + 5, HEIGHT - arr[0][j])
                        end_pos = ((j * 10 + 5), HEIGHT)
                        pygame.draw.line(win, blue, start_pos, end_pos, rect_w)
                
                pygame.display.update()
                
                for i in range(len(arr[0])+1):
                    blue = (65, 105, 225)
                    for j in range(i):
                        start_pos = ((j * 10) + 5, HEIGHT - arr[0][j])
                        end_pos = ((j * 10 + 5), HEIGHT)
                        pygame.draw.line(win, (75, 255, 100), start_pos, end_pos, rect_w)
                        play_sound(arr[0][j])
                        time.sleep(0.05)
                        pygame.display.update()
                

