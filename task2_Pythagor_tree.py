import turtle

def pythagoras_tree(t, depth, length):
    if depth == 0:
        return
    t.color("green") 
    t.forward(length)
    t.left(45)
    pythagoras_tree(t, depth - 1, length / (2 ** 0.5))
    t.right(90)
    pythagoras_tree(t, depth - 1, length / (2 ** 0.5))
    t.left(45)
    t.backward(length)

def draw_pythagoras_tree(depth, length=300):
    window = turtle.Screen()
    window.bgcolor("black")
    
    window.setworldcoordinates(-length*2, -length*2, length*2, length*2)

    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(0, -length)
    t.pendown()
    t.left(90)  # Почати з вертикального напрямку

    pythagoras_tree(t, depth, length)  # Виклик функції для малювання дерева

    window.mainloop()  # Головний цикл подій

recursion_level = int(input("Введіть бажаний рівень рекурсії: "))
draw_pythagoras_tree(recursion_level)
