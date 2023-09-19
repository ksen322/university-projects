import matplotlib
import matplotlib.pyplot as plt
import torch
import math

matplotlib.rcParams['figure.figsize'] = (15.0, 7.0)  # Вывод графика одного размера

#                   --- Создание выборок данных ---

#                   --- Создание train выборки данных ---

x_train = torch.rand(300) * 17 # рандомно 1к значений с последующей нормализацией

y_sub_train = torch.sin(x_train + math.pi/2)  # sin(x + pi/2) , значения слишком очевидны, поэтому делаю шум
plt.figure(1)
plt.plot(x_train.numpy(), y_sub_train.numpy(), 'o')

noise = torch.rand(y_sub_train.shape) / 6  # создание массива точек
plt.figure(2)
plt.plot(x_train.numpy(), noise.numpy(), 'o')

y_train = y_sub_train + noise  # менее очевидный sin(x + pi/2)
plt.figure(3)
plt.title("Train Data")
plt.plot(x_train.numpy(), y_train.numpy(), 'o')

# Для того нейросеть смогла съесть данные, использем метод unsqueeze
# который по сути из тензор-ряда данных, вернет тензор-столбец для этих же данных

x_train.unsqueeze_(1)  # нижнее подчеркивание изменяет сам x_train и y_train
y_train.unsqueeze_(1)

#                   --- Создание test выборки данных ---

x_test = torch.linspace(0, 16, 150)  # Возвращает тензор из 500 равномерно распределенных точек по диапозону [-25 25]
y_test = torch.sin(x_test.data + math.pi/2)  # метод data позволяет забрать данные из tensor
plt.figure(4)
plt.title("Test Data")
plt.plot(x_test.numpy(), y_test.numpy(), 'o')

# Для того нейросеть смогла съесть данные, использем метод unsqueeze

x_test.unsqueeze_(1)
y_test.unsqueeze_(1)

#                 --- Создание нейронной сети ---

class Perceptron(torch.nn.Module):  # класс принимает на вход торч-объект Module

    def __init__(self, input_dim=1, num_layers=1,
                 hidden_dim=30, output_dim=1, device=torch.device("cpu")):
        super(Perceptron, self).__init__()  # Конструктор по канону объекта на котором основан класс

        # Параметры Perceptron:
        #            (input_dim)  Кол-во нейронов входного слоя - 1
        #            (num_layers) Кол-во скрытых слове - 1
        #            (hidden_dim) Кол-во нейронов в каждом скрытом слое - 300:
        #            (output_dim) Кол-во нейронов выходного слоя - 1:
        #            (device)     Обсчитывающее устройство - ЦПУ

        self.layers = torch.nn.Sequential()  # Функция для создания слоев

        prev_size = input_dim  # Для создания входного слоя (указываем кол-во связей с каждым скрытым нейроном)

        #            --- Создание слоев ---

        for i in range(num_layers):  # Создание выходного слоя + создание скрытых слоев
            self.layers.add_module('layer{}'.format(i), torch.nn.Linear(prev_size, hidden_dim))  # Линейный слой
            self.layers.add_module('sigmoid{}'.format(i), torch.nn.Sigmoid())  # Функция активации сигмоида
            prev_size = hidden_dim  # Переписывает кол-во нейронов предыдущего слоя, для связи с последующим

        self.layers.add_module('regressor', torch.nn.Linear(prev_size, output_dim))  # Создание выходного слоя
        self.to(device)  # Ссылка на ЦП

    #   --- Создание функции передачи данных по нейронам ---

    def forward(self, train_data):
        return self.layers(train_data)


our_net = Perceptron()

#       --- Визуализация предсказаиний нейронной сети ---

def prediction(net, x, y):

    y_pred = net.forward(x)  # в переменную внесли прогон x через слои, по сути получили Y

    plt.figure(5)
    plt.plot(x.numpy(), y.numpy(), 'o', c='g', label='Real')
    plt.plot(x.numpy(), y_pred.data.numpy(), 'o', c='m', label='Prediction')
    plt.title("Prediction of sin(x + pi/2)")
    plt.legend(loc='upper left')


# prediction(our_net, x_test, y_test)

#              --- Обучение нейронной сети ---

optimizer = torch.optim.Adam(our_net.parameters(), lr=0.01)  # Улчшенный градиентный спуск, в параметры learning rate


#           --- Расчет функции предсказания ---

def loss(predict, true):
    sq = (predict - true) ** 2  # средне-квадратичная ошибка
    return sq.mean()


#           --- Функция обучения обучения ---

def trainer():
    for epoch in range(5000):

        optimizer.zero_grad()  # Обнуление градиента

        y_predict = our_net.forward(x_train)
        loss_val = loss(y_predict, y_train)

        if not epoch % 1000:
            print(loss_val)

        loss_val.backward()  # Расчет производной
        optimizer.step()


trainer()
prediction(our_net, x_test, y_test)
plt.show()
