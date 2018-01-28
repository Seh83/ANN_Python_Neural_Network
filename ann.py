inputs = [0, 0, 1, 0]
weights = [0, 0, 0, 0]
desiredResults = 1
learningRate = 0.20
trials = 0
error = int
neuralNetResult = int


def evaluateNeuralNetwork(inputVector, weightVector):
    result = 0
    for index, value in enumerate(inputVector):
        layerValue = value * weightVector[index]
        result += layerValue
    return (round(result, 2))


def evaluateNeuralNetError(desired, actual):
    sum = desired - actual
    return (round(sum, 2))


def learn(inputVector, weightVector):
    for index, value in enumerate(weightVector):
        if (inputVector[index] > 0):
            weights[index] = (value + learningRate)


def train(trials):
    while trials < 6:
        neuralNetResult = evaluateNeuralNetwork(inputs, weights)
        print("Neural Net output: ", neuralNetResult, " Error: ", evaluateNeuralNetError(desiredResults,
                                                                                            neuralNetResult), " Weight Vector: ", weights)
        learn(inputs, weights)
        trials += 1


train(trials)
