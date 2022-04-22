import numpy as np 
import matplotlib.pyplot as plt

import sys
import os

class Animal:
	def output():
		print(f"Length of arms: {self.lengtharm}")
		print(f"Length of legs: {self.lengthleg}")
		print(f"Number of eyes: {self.eyecount}")
		print(f"Does it have a tail?: {self.tailanswer}")
		print(f"Does it have fur?: {self.furanswer}")

	def __init__(self, lengtharm=3,lengthleg=1.,eyecount=2,tailanswer=1,duranswer=1):
		self.lentharm= length_arm
		self.lengthleg= length_leg
		self.eyecount= eye_count
		self.tailanswer= tail_answer
		self.furanswer= fur_answer
def main():
	length_arm= 38.0
	length_leg= 38.0
	eye_count= 2
	tail_answer= "Yes"
	fur_answer= "Yes"
	
	print(f"Length of arms: {length_arm}")
	print(f"Length of legs: {length_leg}")
	print(f"Number of eyes: {eye_count}")
	print(f"Does it have a tail?: {tail_answer}")
	print(f"Does it have fur?: {fur_answer}")


if __name__ == '__main__':
	main()