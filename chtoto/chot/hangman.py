import tkinter as tk
import random
WORDS = ["минекарп","ФеНеФе","эпигандо"]

# 1) выбираем случайное слово
# 2) создаем окошко, настраиваем его
# 3) создаем холст canvas в котором у нас будет отрисовываться человечек
# 4) пишем функцию для рисования виселицы
# 5) пишем функцию для рисования человечка
# 6) функция для обработки вводимой буквы
# 7) в зависимости от буквы выводим верно или нет и раскрываем букву в слове

word = random.choice(WORDS)
print(word)

attempts = 6
guessed_letters = []
root = tk.Tk()
root.title("веселимся")
root.geometry("500x500")

canvas = tk.Canvas(root, width=400, height=400,background="yellow")
canvas.pack()

canvas.create_oval(150,90, 250,180,width=4,fill="green")
canvas.create_line(200,100, 200,250,width=4,fill="green")
canvas.create_line(140,250, 200,200,width=4,fill="green")
canvas.create_line(200,200, 260,250,width=4,fill="green")
canvas.create_line(160,300, 200,250,width=4,fill="green")
canvas.create_line(230,360, 80,50,width=4,fill="green")



canvas.create_line(100,20, 100,300, width=10, fill="black")
canvas.create_line(60,300, 140,300, width=10, fill="black")
canvas.create_line(100,25, 200,25, width=10, fill="black")
canvas.create_line(200,20, 200,100, width=10, fill="black")


def draw_hangman(attempt):
    # головав
    if attempt == 1:  
        canvas.create_oval(150,90, 250,180,width=4,fill="green")
        # Тэло
    elif attempt == 2:  
        canvas.create_line(200,100, 200,250,width=4,fill="green")
draw_hangman(2)










root.mainloop()
