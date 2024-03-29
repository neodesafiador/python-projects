from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []    # list to organize all segments
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:    # when the snake hits the wall or when
            segment.goto(1000, 1000)     # it hits its tail, it actually
        self.segments.clear()            # disappears into a location that's
        self.create_snake()              # off the screen.
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Third segment goes to where the second segment used to be, second goes to
    # # where the one used to be, and then the one is going to turn and move to
    # the left. By using this method, our snake has pretty much straighted out.
    def move(self):
        for seg_num in range(len(self.segments) - 1 , 0 , -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)