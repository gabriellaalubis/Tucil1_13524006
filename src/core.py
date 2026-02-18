import tkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import time
import random

def load(file):
    try:
        with open(file, "r") as f:
            rows = f.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error","File not found.")
        return None
    
    board = []

    for row in rows:
        row = row.strip()
        if not row:
            continue

            
        val_row = []
        for char in row:
            if char == " ":
                continue

            if not char.isalpha():
                messagebox.showerror("Error","Board must contain only alphabetic characters.")
                return None
            
            val_row.append(char.upper())
    
        board.append(val_row)

    if not board:
        messagebox.showerror("Error","The file is empty.")
        return None
    
    n = len(board)

    colors = []
    for row in board:
        if len(row) != n:
            messagebox.showerror("Error","The board must be square")
            return None
        for char in row:
            if char not in colors:
                colors.append(char)
    if len(colors) != n:
        messagebox.showerror("Error","The number of regions must be equal to the board dimension.")
        return None

    return board

def iterate (queens, n, nBoard):
    if (n == 0):
        return False
    queens[n-1] += 1
    if queens[n-1] == nBoard:
        queens[n-1] = 0
        return iterate (queens, n-1, nBoard)
    return True

        
home = tkinter.Tk()
home.title("QUEENS")
home.geometry("700x730")

top_frame = tkinter.Frame(home)
top_frame.pack()

bottom_frame = tkinter.Frame(home)
bottom_frame.pack(pady=20)

title_frame = tkinter.Frame(top_frame)
title_frame.pack(pady=30)

icon_label = tkinter.Label(title_frame, text="♛", font=("Arial", 250))
icon_label.pack()

title_label = tkinter.Label(title_frame, text="QUEENS GAME SOLVER", font=("Arial", 32, "bold"))
title_label.pack()

canvas = tkinter.Canvas(top_frame, width=500, height=500)

colors_showed = {}
def get_color(x):
    if x not in colors_showed:
        r = random.randint(120, 255)
        g = random.randint(120, 255)
        b = random.randint(120, 255)
        colors_showed[x] = f"#{r:02x}{g:02x}{b:02x}"
    return colors_showed[x]

def result_img(board, queens, n):
    canvas.delete("all")

    size = 500 / n

    for i in range (n):
        for j in range (n):
            x1 = j * size
            y1 = i * size
            x2 = x1 + size
            y2 = y1 + size

            color = get_color(board[i][j])

            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
            if queens[i] == j:
                canvas.create_text(
                    (x1+x2)//2,
                    (y1+y2)//2,
                    text="♛",
                    font=("Arial", int(size * 0.5), "bold"),
                    fill="black"
                )

def save_txt(board, queens, n):
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            for i in range (n):
                for j in range (n):
                    if queens[i] == j:
                        f.write("#")
                    else:
                        f.write(board[i][j])
                    if (j<n):
                        f.write(" ")
                f.write("\n")

def save_img(board, queens, n):
    file = filedialog.asksaveasfilename(defaultextension=".png")
    size = 500  
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)
    cell = size / n
    font = ImageFont.truetype("arialbd.ttf", size=int(cell*0.5))


    for i in range(n):
        for j in range(n):
            x1 = j * cell
            y1 = i * cell
            x2 = x1 + cell
            y2 = y1 + cell

            color = get_color(board[i][j])
            draw.rectangle([x1, y1, x2, y2], fill=color, outline="black")

            if queens[i] == j:
                draw.text(
                    (x1 + cell/2, y1 + cell/2),
                    "#",
                    fill="black",
                    font=font,
                    anchor="mm" 
                    ) 

    img.save(file)

def result_popup(home, time, iter, board, queens, n):
    popup = tkinter.Frame(home, bd=2, relief="ridge")
    popup.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

    title = tkinter.Label(popup, text="SOLUTION FOUND!", font=("arial", 14, "bold"))
    title.pack(pady=10)

    info = tkinter.Label(popup, text=f"Search time: {time*1000:.0f} ms\nConfigurations tested: {iter}", font=("arial", 12))
    info.pack(pady=5)

    save_frame = tkinter.Frame(popup)
    save_frame.pack(pady=10)

    btn_txt = tkinter.Button(save_frame, text="Save as .txt", command=lambda:save_txt(board, queens, n), width=12)
    btn_txt.pack(side="left", padx=5)
    
    btn_img = tkinter.Button(save_frame, text="Save as .png", command=lambda:save_img(board, queens, n), width=12)
    btn_img.pack(side="left", padx=5)

    btn_close = tkinter.Button(popup, text="close", command=popup.destroy, width=8)
    btn_close.pack(pady=5)


def solve ():  
    title_frame.pack_forget()
    canvas.pack(pady=10)

    file_name = input.get()
    board = load(file_name)

    if board is None:
        return

    n = len(board)
    queens = [0]*(n-1)
    queens.append(-1)

    iter = 0
    start = time.perf_counter()
    last = start
    result_img(board, [0]*n, n)
    home.update()
    while True:
        if not iterate (queens, n, n):
            result_img(board, queens, n)
            home.update()
            messagebox.showinfo("NO SOLUTION", "No solution exists for this board.")
            print(iter)
            return

        now = time.perf_counter()
        if (now-last >= 1):
            result_img(board, queens, n)
            home.update()
            last = now
        iter += 1
        solved = True

        cols = []
        colors = []
        for i in range (n):
            column_i = queens[i]
            color_i = board[i][column_i]
            if column_i in cols:
                solved = False
                break
            if color_i in colors:
                solved = False
                break
            if i<n-1 and abs(column_i - queens[i+1]) == 1:
                solved = False
                break
                
            cols.append(column_i)
            colors.append(color_i)
        
        if solved:
            end = time.perf_counter()
            result_img(board, queens, n)
            home.update()
            result_popup(home, end-start, iter, board, queens, n)
            return

subtitle_label = tkinter.Label(bottom_frame, text="Upload your board below", font=("Arial", 14))
subtitle_label.pack(pady=10)

input = tkinter.Entry(bottom_frame, width=50)
input.pack(pady=5)

def input_file():
    name = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if name:
        input.delete(0, tkinter.END)
        input.insert(0, name)

btn_choose_file = tkinter.Button(bottom_frame, text="Choose File", command=input_file)
btn_choose_file.pack()

btn_solve = tkinter.Button(bottom_frame, text="Solve", command=solve)
btn_solve.pack(pady=20)
        

home.mainloop()
