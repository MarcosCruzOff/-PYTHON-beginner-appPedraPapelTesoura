import tkinter as tk

def handle_click(event):
    # Obtenha as coordenadas x e y do mouse a partir do evento
    x, y = event.x, event.y

    # Verifique qual objeto canvas foi clicado
    for obj in canvas.find_all():
        # Obtenha as coordenadas do objeto canvas
        obj_coords = canvas.coords(obj)
        obj_x1, obj_y1, obj_x2, obj_y2 = obj_coords

        # Verifique se as coordenadas do mouse estão dentro das coordenadas do objeto canvas
        if obj_x1 <= x <= obj_x2 and obj_y1 <= y <= obj_y2:
            print(f"Objeto {obj} clicado")

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

rect1 = canvas.create_rectangle(50, 50, 100, 100, fill="red")
rect2 = canvas.create_rectangle(120, 50, 170, 100, fill="blue")

canvas.bind("<Button-1>", handle_click)

root.mainloop()
