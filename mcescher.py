from turtle import Screen, Turtle

outer_radius = 100
inner_radius = 3 ** 0.5 * outer_radius / 2
sides = 6
extent = 360 / sides


def tessellation(depth):
    """
    """

    turtle.right(extent / 2)

    for _ in range(sides):
        turtle.circle(outer_radius, extent, 1)

        if depth:
            heading = turtle.heading()

            turtle.right(90)
            tessellation(depth - 1)

            turtle.setheading(heading)

        else:
            pass


screen = Screen()
turtle = Turtle(visible=False)

screen.tracer(False)

turtle.penup()
turtle.color("blue")
turtle.goto(-outer_radius / 2, -2 * inner_radius / 2)
turtle.pendown()
turtle.setheading(0)
tessellation(2)

turtle.penup()
turtle.color("red")
turtle.goto(outer_radius / 4, -1 * inner_radius / 2)
turtle.pendown()
turtle.setheading(0)
tessellation(2)

turtle.penup()
turtle.color("yellow")
turtle.goto(outer_radius / 4, -3 * inner_radius / 2)
turtle.pendown()
turtle.setheading(0)
tessellation(2)

turtle.penup()
turtle.color("green")
turtle.goto(-outer_radius / 2, -4 * inner_radius / 2)
turtle.pendown()
turtle.setheading(0)
tessellation(2)

screen.tracer(True)

screen.exitonclick()
