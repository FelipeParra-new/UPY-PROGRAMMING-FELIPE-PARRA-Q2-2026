import random
import stddraw
from color import Color 

def bubble_sort(numbers):
    #get the lenght of the array
    n = len(numbers)
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers [pair+1], numbers[pair]

# Selection sort 
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        if min_idx != i:
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

# Insertion sort
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
            
def draw_bars(numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)
    
#Animated bubble sort
def bubble_sort_animated(numbers):
    # CONIG - Canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    #get the lenght of the array
    n = len(numbers)
    
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            #Draw the rectangles before the swap
            draw_bars(numbers, selected= (pair, pair +1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers [pair+1], numbers[pair]
                #Draw the rentangles after the swap
                draw_bars(numbers, selected= (pair, pair +1))
                
    draw_bars(numbers)
    stddraw.show(2000)

#Selection sort animated
def selection_sort_animated(numbers):
    # config canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_bars(numbers, selected=(min_idx, j))
            if numbers[j] < numbers[min_idx]:
                min_idx = j
                
        if min_idx != i:
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
            draw_bars(numbers, selected=(i, min_idx))
            
    draw_bars(numbers)
    stddraw.show(2000)

# Insertion sort animated
def insertion_sort_animated(numbers):
    # Config canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(1, n):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            draw_bars(numbers, selected=(j, j - 1))
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            draw_bars(numbers, selected=(j, j - 1))
            j -= 1
            
    draw_bars(numbers)
    stddraw.show(2000)


# Ejecución
numbers = [random.randint(0,100) for x in range(10)]
print(f"Before sort: {numbers}")

bubble_sort_animated(numbers)
# selection_sort_animated(numbers)
#insertion_sort_animated(numbers)

print(f"After sort: {numbers}")
stddraw.show()