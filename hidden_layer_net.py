import numpy as np

class NeuralNetwork:
	def __init__(self, w1, w2):
		self.w1 = w1
		self.w2 = w2

	# Forward propogation 
	def forward(self, X):
		# Propogate to find z2
		z2 = []

		for xRowIndex in range(len(X)):
			# The row of data
			row = X[0]

			# Build the next entry in
			entry = [row[0] * w1[0][0] + row[1] * w1[1][0] + row[2] * w1[2][0], row[0] * w1[0][1] + row[1] * w1[1][1] + row[2] * w1[2][1]]

			z2.append(z2)

		return z2

# Create the neural network
initW1 = []
nn = NeuralNetwork()

print("Hello")