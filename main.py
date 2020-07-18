class Perception():

       def __init__(self, threshold, learning_rate):
              self.threshold = threshold
              self.learning_rate = learning_rate
              self.weight_a = 1
              self.weight_b = 1

       def neuron_data(self, input_a, input_b, output):
              for i in range(len(output)):
                     self.sigma = (self.weight_a*input_a[i]) + (self.weight_b*input_b[i])

                     if self.sigma <= self.threshold:
                            self.fire = 0

                     else:
                            self.fire = 1

                     while self.fire != output[i]:
                            self.delta = (output[i] - self.fire) * self.learning_rate
                            self.weight_a = self.weight_a + self.delta
                            self.weight_b = self.weight_b + self.delta
                            self.sigma = (self.weight_a * input_a[i]) + (self.weight_b * input_b[i])

                            if self.sigma <= self.threshold:
                                   self.fire = 0

                            else:
                                   self.fire = 1

                            print(self.weight_a, self.weight_b, self.delta)

              print("First weight is: {weight_1}, \n Second weight is: {weight_2}".format(weight_1=self.weight_a,
                                                                                                 weight_2=self.weight_b))