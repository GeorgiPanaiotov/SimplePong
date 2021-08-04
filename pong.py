import turtle


def settings():
    window = turtle.Screen()
    window.title('Classic Pong')
    window.setup(width=800, height=600)
    window.bgcolor('black')
    window.tracer(0)
    return window


class FirstPlayer:
    starting_position = [-350, 0]
    player_color = 'white'
    player_shape = 'square'
    player_size = [4, 1]

    @staticmethod
    def settings():
        fp = turtle.Turtle()
        fp.color(FirstPlayer.player_color)
        fp.shape(FirstPlayer.player_shape)
        fp.shapesize(stretch_wid=FirstPlayer.player_size[0], stretch_len=FirstPlayer.player_size[1])
        fp.speed(0)
        fp.penup()
        fp.goto(FirstPlayer.starting_position[0], FirstPlayer.starting_position[1])
        return fp


class ScoreBoard:
    color = 'white'
    position = [0, 250]
    player_1_points = 0
    player_2_points = 0

    @staticmethod
    def settings():
        sb = turtle.Turtle()
        sb.color(ScoreBoard.color)
        sb.hideturtle()
        sb.goto(ScoreBoard.position[0], ScoreBoard.position[1])
        sb.penup()
        sb.speed(0)
        sb.write(f'Player 1: {ScoreBoard.player_1_points}   Player 2: {ScoreBoard.player_2_points}', align='center',
                 font=('Arial', 20, 'normal'))
        return sb


class Ball:
    starting_position = [0, 0]
    ball_color = 'white'
    ball_shape = 'circle'
    y_speed = 0.5
    x_speed = 0.5

    @staticmethod
    def settings():
        b = turtle.Turtle()
        b.color(Ball.ball_color)
        b.shape(Ball.ball_shape)
        b.goto(Ball.starting_position[0], Ball.starting_position[1])
        b.speed(0)
        b.penup()
        return b


class SecondPlayer:
    starting_position = [350, 0]
    player_color = 'white'
    player_shape = 'square'
    player_size = [4, 1]

    @staticmethod
    def settings():
        sp = turtle.Turtle()
        sp.color(SecondPlayer.player_color)
        sp.shape(SecondPlayer.player_shape)
        sp.shapesize(stretch_wid=SecondPlayer.player_size[0], stretch_len=SecondPlayer.player_size[1])
        sp.speed(0)
        sp.penup()
        sp.goto(SecondPlayer.starting_position[0], SecondPlayer.starting_position[1])
        return sp


class Movement:
    def __init__(self, first, second, ball):
        self.fp = first
        self.sp = second
        self.b = ball

    def first_player_movement_up(self):
        y = self.fp.ycor()
        if y >= 250:
            y = 250
        else:
            y += 10
        self.fp.sety(y)

    def first_player_movement_down(self):
        y = self.fp.ycor()
        if y <= -250:
            y = -250
        else:
            y -= 10
        self.fp.sety(y)

    def second_player_movement_up(self):
        y = self.sp.ycor()
        if y >= 250:
            y = 250
        else:
            y += 10
        self.sp.sety(y)

    def second_player_movement_down(self):
        y = self.sp.ycor()
        if y <= -250:
            y = -250
        else:
            y -= 10
        self.sp.sety(y)

    def second_player_collision(self):
        if (340 < self.b.xcor() < 350) and (self.sp.ycor() + 50 > self.b.ycor() > self.sp.ycor() - 80):
            return True

    def first_player_collision(self):
        if (-340 > self.b.xcor() > -350) and (self.fp.ycor() + 50 > self.b.ycor() > self.fp.ycor() - 80):
            return True


def game_loop():
    window = settings()
    b = Ball.settings()
    fp = FirstPlayer.settings()
    sp = SecondPlayer.settings()
    sb = ScoreBoard.settings()
    a = Movement(fp, sp, b)
    while True:
        window.listen()
        window.onkeypress(a.first_player_movement_up, 'w')
        window.onkeypress(a.first_player_movement_down, 's')
        window.onkeypress(a.second_player_movement_up, 'Up')
        window.onkeypress(a.second_player_movement_down, 'Down')
        b.setx(b.xcor() + Ball.x_speed)
        b.sety(b.ycor() + Ball.y_speed)

        if b.ycor() >= 290:
            b.sety(290)
            Ball.y_speed *= -1
        elif b.ycor() <= -290:
            b.sety(-290)
            Ball.y_speed *= -1
        if b.xcor() >= 390:
            ScoreBoard.player_1_points += 1
            sb.clear()
            sb.write(f'Player 1: {ScoreBoard.player_1_points}   Player 2: {ScoreBoard.player_2_points}', align='center',
                     font=('Arial', 20, 'normal'))
            b.goto(0, 0)
            Ball.x_speed *= -1
        elif b.xcor() <= -390:
            ScoreBoard.player_2_points += 1
            sb.clear()
            sb.write(f'Player 1: {ScoreBoard.player_1_points}   Player 2: {ScoreBoard.player_2_points}', align='center',
                     font=('Arial', 20, 'normal'))
            b.goto(0, 0)
            Ball.x_speed *= -1

        if a.second_player_collision():
            b.setx(340)
            Ball.x_speed *= -1
        elif a.first_player_collision():
            b.setx(-340)
            Ball.x_speed *= -1
        window.update()


game_loop()
