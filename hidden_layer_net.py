import numpy as np
from scipy import optimize

class NeuralNetwork:
	def __init__(self):
		#Define Hyperparameters
		self.inputLayerSize = 2
		self.outputLayerSize = 1
		self.hiddenLayerSize = 3

		#Weights (parameters)
		self.w1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
		self.w2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)

	# Forward propogation 
	def forward(self, X):
		# Propogate forward for z2
		z2 = np.dot(X, self.w1)
		z3 = np.dot(z2, self.w2)
		return z3

class Trainer:
	def __init__(self, nn):
		self.nn = nn

	def train(self, X, y):
		self.X = X
		self.y = y

		# List to store costs
		self.costs = []

# Create the neural network
nn = NeuralNetwork()

# Make test data
X = np.matrix('50 50')


print(nn.forward(X))