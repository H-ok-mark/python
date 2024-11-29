import turtle

# 设置窗口
screen = turtle.Screen()
screen.bgcolor("white")

# 创建turtle对象
t = turtle.Turtle()
t.speed(5)

# 画图a：菱形
def draw_rhombus():
    t.color("blue")
    for _ in range(2):
        t.forward(200)  # 长边
        t.left(45)
        t.forward(200)  # 长边
        t.left(135)

# 画图b：五角星和外接圆
def draw_star():
    t.color("red")
    radius = 80
    # 画外接圆
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)

    # 画五角星
    angle = 144
    for _ in range(5):
        t.forward(radius * 2)  # 五角星的边长
        t.right(angle)

# 设置起始位置
t.penup()
t.goto(-100, 100)  # 图形a的起始位置
t.pendown()

# 画图a：菱形
draw_rhombus()

# 设置图形b的位置
t.penup()
t.goto(50, -50)  # 图形b的位置
t.pendown()

# 画图b：五角星和外接圆
draw_star()

# 隐藏海龟
t.hideturtle()

# 完成
turtle.done()
