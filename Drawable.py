import pygame
import abc


class Drawable(metaclass=abc.ABCMeta):
	def __init__(self, x=0, y=0):
		self.__x = x
		self.__y = y
		
	def getLoc(self):
		return self.__x, self.__y

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def setY(self, y):
		self.__y = self.__y + y
		
	def setLoc(self, p):
		self.__x = p[0]
		self.__y = p[1]

	@abc.abstractmethod
	def draw(self, surface):
		pass


class Rectangle(Drawable):
	def __init__(self, x, y, width, height, color):
		super().__init__(x, y)
		self.__width = width
		self.__height = height
		self.__color = color

	def draw(self, surface):
		pygame.draw.rect(surface, self.__color, (super().getX(), super().getY(), self.__width, self.__height))
		pygame.display.update()


class Snowflake(Drawable):
	def __init__(self, x, y):
		super().__init__(x, y)

	def draw(self, surface):
		white = (255, 255, 255)
		pygame.draw.line(surface, white, (super().getX() - 5, super().getY()), (super().getX() + 5, super().getY()))
		pygame.draw.line(surface, white, (super().getX(), super().getY() - 5), (super().getX(), super().getY() + 5))
		pygame.draw.line(surface, white, (super().getX() - 5, super().getY() - 5), (super().getX() + 5, super().getY() + 5))
		pygame.draw.line(surface, white, (super().getX() - 5, super().getY() + 5), (super().getX() + 5, super().getY() - 5))

