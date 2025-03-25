import tkinter as tk
import random
from tkinter import messagebox
WORDS = ["минекарп","фенефе","эпигандо","опаньки","солевоймарм"]

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

# canvas.create_oval(150,90, 250,180,width=4,fill="green")
# canvas.create_line(200,100, 200,250,width=4,fill="green")
# canvas.create_line(140,250, 200,200,width=4,fill="green")
# canvas.create_line(200,200, 260,250,width=4,fill="green")
# canvas.create_line(160,300, 200,250,width=4,fill="green")
# canvas.create_line(230,300, 200,250,width=4,fill="green")



canvas.create_line(100,20, 100,300, width=10, fill="black")
canvas.create_line(60,300, 140,300, width=10, fill="black")
canvas.create_line(100,25, 200,25, width=10, fill="black")
canvas.create_line(200,20, 200,100, width=10, fill="black")


def draw_hangman(attempt):

    # головав
    if attempt == 5:  
        canvas.create_oval(150,90, 250,180,width=4,fill="green")
        # Тэло
    elif attempt == 4:  
        canvas.create_line(200,100, 200,250,width=4,fill="green")
    elif attempt == 3:  
        canvas.create_line(140,250, 200,200,width=4,fill="green")
    elif attempt == 2:  
        canvas.create_line(200,200, 260,250,width=4,fill="green")
    elif attempt == 1:  
        canvas.create_line(160,300, 200,250,width=4,fill="green")
    elif attempt == 0:  
        canvas.create_line(230,300, 200,250,width=4,fill="green")

def validate_count_symb(e):
    s=entry.get().strip()
    print(s)
    if len(s) >1:
     messagebox.showinfo("ничего себе","куда тебе столько букв, балбес")
    s=s[-1] if s in range(0,1) else ''
    entry.delete('1 ',tk.END)
    entry.insert(tk.INSERT,s)
    print(e.char)


def display_word():
    displayed_word=""
    for letter in word:
        if letter in guessed_letters:
            displayed_word+= " "
        else:
            displayed_word+=" _"
    return displayed_word.strip()


def check_letter():
    global attempts
    letter=entry.get().lower()
    entry.delete(0,tk.END)
    if letter in guessed_letters:
        messagebox.showinfo("Повтр","опа, а буква уже есть")
        return
    guessed_letters.append(letter)

    if letter not in word:
        attempts-=1
        draw_hangman(attempts)
    if attempts ==0:
        messagebox.showinfo("died","балбес")
        root.quit()
    elif all(letter in guessed_letters for letter in word):
         messagebox.showinfo("чел хорош","но всё равно балбес")
         root.quit() 

    else:
        word_label.config(text=display_word())      



word_label=tk.Label(root,text=display_word(),font=30)
word_label.pack()
entry =tk.Entry(root,font=40)
entry.pack(pady=10)

entry.bind('<KeyRelease>',validate_count_symb)

button = tk.Button(root,text="try it", font=25, command=check_letter)
button.pack()






root.mainloop()
