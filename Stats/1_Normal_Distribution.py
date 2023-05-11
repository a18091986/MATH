import math

"""
mu - среднее
sigma - стандартное отклонение, sigma ** 2 - дисперсия. Чем меньше сигма, тем быстрее меняется функция с изменением 
аргумента. чем меньше сигма, тем уже колокол. малые сигмы говорят о том, что среднее значение более вероятно, чем в 
ситуации с большим значением сигмы. 

"""

class NormalDistribution:

    def __init__(self, sigma, mu, x):
        self.x = x
        self.sigma = sigma
        self.mu = mu

    def prob_density(self):
        return (1 / (self.sigma * math.sqrt(2 * math.pi))) * math.exp(- (self.x - self.mu) ** 2 / 2 * self.sigma ** 2)


