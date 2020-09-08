
class Neuron:
    def __init__(self, value, excepted_result):
        self.value = value
        self.weight = 0.5
        self.excepted_result = excepted_result
        self.smoothing = 0.00001
        self.check = 0
        self.next_error = [0]
        self.iter = 0

    def start(self):
        while self.next_error[-1] < self.smoothing or self.next_error[-1] > self.smoothing:
            if (self.value / (self.value * self.weight)) == self.check:
                print('\nНейрон Обучен!\n')
                break

            else:
                print(f'В {self.value} км {self.value / (self.value * self.weight)}'
                      f' мили. Иттерация номер - {self.iter}')
                self.train()

        return (f'В {self.value} км {self.value / (self.value * self.weight)}'f' мили. '
                f'Ответ найден на иттерации - {self.iter - 1}')

    def train(self):
        self.check = self.value / (self.value * self.weight)
        actual_result = self.value * self.weight
        error = self.excepted_result - actual_result
        correction = (error / actual_result) * self.smoothing
        self.weight += correction
        self.next_error.append(error)
        self.iter += 1

a = Neuron(1900, 63.137)
print(Neuron.start(a))



