from turtle import Turtle
import random

class Square(Turtle):
	def __init__ (self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")

	def random_color(self):
		red = random.randint(0, 255)
		green = random.randint(0, 255)
		blue = random.randint(0, 255)
		self.color(red, green, blue)
