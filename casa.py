import turtle
import math

# Criar uma tela para desenhar
tela = turtle.Screen()
tela.bgcolor("purple")
# Criar uma tartaruga
tartaruga = turtle.Turtle()

#desenhar o quadrado terminando na esquerda sup
tartaruga.fillcolor("yellow")
tartaruga.begin_fill()
for _ in range(4):
    tartaruga.forward(100)  # Avança 100 pixels
    tartaruga.right(90)     # Vira 90 graus à direita
tartaruga.end_fill()

tartaruga.fillcolor("red")
tartaruga.begin_fill()
#desenhar o telhado pintar de vermelho
tartaruga.left(45)
tartaruga.forward(50*math.sqrt(2))
tartaruga.right(90)
tartaruga.forward(50*math.sqrt(2))
tartaruga.end_fill()


#continuar casa
tartaruga.fillcolor("yellow")
tartaruga.begin_fill()
tartaruga.left(75)
tartaruga.forward(100)
tartaruga.right(120)
tartaruga.forward(100)
tartaruga.right(60)
tartaruga.forward(100)
tartaruga.end_fill()
#continuar telhado
#chegar no ponto sup direito da parede
tartaruga.right(120)
tartaruga.forward(100)
tartaruga.right(60)
tartaruga.forward(100)


tartaruga.fillcolor("red")
tartaruga.begin_fill()
#fazer telhado
tartaruga.left(105)
tartaruga.forward(50*math.sqrt(2)*math.cos(math.radians(30)))
tartaruga.left(75)
tartaruga.goto(50,50)
tartaruga.left(105)
tartaruga.forward(50*math.sqrt(2))
tartaruga.left(75)
tartaruga.forward(100)
tartaruga.end_fill()

tartaruga.penup()
tartaruga.goto(30, -100)
tartaruga.pendown()
tartaruga.fillcolor("brown")
tartaruga.begin_fill()
tartaruga.left(60)
tartaruga.forward(60)
tartaruga.right(90)
tartaruga.forward(40)
tartaruga.right(90)
tartaruga.forward(60)
tartaruga.end_fill()

#janela
tartaruga.penup()
tartaruga.goto(150, -50)
tartaruga.pendown()

tartaruga.fillcolor("grey")
tartaruga.begin_fill()
tartaruga.right(60)
tartaruga.forward(40)
tartaruga.right(120)
tartaruga.forward(50)
tartaruga.right(60)
tartaruga.forward(60)
tartaruga.right(120)
tartaruga.forward(50)
tartaruga.right(60)
tartaruga.forward(20)
tartaruga.end_fill()
#cruz
tartaruga.forward(10)
tartaruga.right(120)
tartaruga.forward(50)
tartaruga.right(180)
tartaruga.forward(25)
tartaruga.right(60)
tartaruga.forward(30)
tartaruga.right(180)
tartaruga.forward(60)
# Fechar a tela ao clicar
tartaruga.hideturtle()
tela.exitonclick()