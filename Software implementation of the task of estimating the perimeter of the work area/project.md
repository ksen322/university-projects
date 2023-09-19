# Software implementation of the task of estimating the perimeter of the work area  

Программное обеспечение предназначено для определения площади многоугольника по заданным длинам его сторон. Решение основывается на реализации бинарного поиска для нахождения радиуса описанной окружности и нахождения площади с помощью метода Гаусса (алгоритм шнурования).  

При выполнении программа использует не более 4 Мб оперативной памяти и работает не более 0.2 секунды.  

Входные данные предполагаются корректными, поэтому никаких проверочных действий не производится. На любом корректном наборе входных данных программа заканчивает работу безаварийно.  

Язык разработки – Python 3.6. Гарантированно компилируется в интегрированной среде разработки JetBrains Community Edition 2020.2.1 x64.  

## Общая постановка задачи  
Рабочие собираются оградить забором новую рабочую зону. Для их удобства закрытая территория должна быть как можно больше. У них есть N прямоугольных блоков, чтобы построить забор. Длина i-го блока - Li метров. Все блоки имеют одинаковую высоту - 1 метр. Рабочим не разрешается разбивать блоки на части. Все блоки должны быть использованы для строительства забора.  
### Исходные данные  
В первой строке записано одно целое число N (3 ≤ N ≤ 100). Следующие N строк описывают блоки забора. Каждый блок представлен своей длиной в метрах (целое число, 1 ≤ Li ≤ 100).  
### Результат  
Выведите одно неотрицательное число S - максимально возможную площадь рабочей области (в квадратных метрах). S следует вывести с двумя цифрами после десятичной точки. Если невозможно построить забор из указанных блоков, выведите 0.00.  

## Общие сведения и алгоритм решения  
Для более конкретного понимания условия задачи перефразируем его:  

Имеется N блоков, каждый из блоков имеет одинаковую высоту – 1 метр. Отсюда уже следует, что работаем в двухмерном пространстве. Далее, каждый блок имеет свою длину, разбивать блок нельзя – работаем только с целым блоком. Необходимо составить такой многоугольник, в условии – рабочее пространство, чтобы его площадь, т.е. рабочая поверхность, была максимальна.  

Для удобства использован класс point, т.к. будем работать в декартовой системе координат XY, будем считать площадь с помощью определения координат вершин многоугольника.  

Суть программы в том, чтобы построить многоугольник, вокруг которого можно было бы описать окружность (так как площадь фигуры вокруг которой можно описать окружность - максимальна), а затем посчитать данную площадь. Поиск радиуса такой окружности будет осуществляться с помощью бинарного поиска.  

<details><summary><b>Этапы программы:</b></summary>  

- Ввод и инициализация переменных
- Бинарный поиск радиуса описанной окружности, подсчет площади и точности в функции area_calculator
- Проверка точности и вывод ответа
  
</details>

### Первый этап  
Вводятся переменные blocks_quantity – это количество блоков и blocks_array – список значений этих блоков. Далее небольшой цикл для заполнения списка значениями, сортируем его по возрастанию (чтобы знать, что последний элемент списка – самый большой блок). Вводим 2 границы бинарного поиска left_border = 0 и right_border = 10^6. Далее идут переменные, отвечающие за правильный вывод ответа: accuracy – точность (изначально 0), area_answer – искомая площадь и предел точности accuracy_limit = 10^(-6).  
### Второй этап  
Это основная часть программы. Весь данный этап исполняется в цикле 64 раза, так как опытным путем было проверено, что среднее количество прогонов для нахождения числа на интервале [0; 10^6] лежит примерно от 42 до 64. С каждым проходом в этом цикле происходит перерасчет среднего значения middle. Каждый раз предполагается, что middle – это радиус той самой окружности, которая может описать многоугольник из введенных блоков. Далее происходит вызов функции area_calculator со следующими значениями: (blocks_array, middle) – список размеров блоков и предполагаемый радиус. Работа данной функции будет описана отдельно. Функция подсчитывает площадь и возвращает параметр точности, по которому определяется будет ли сдвиг границ. Сам же сдвиг границ происходит по двум параметрам: если точность меньше 0 или самый большой блок больше диаметра окружности – увеличиваем радиус, то есть двигаем левую границу: left_border = middle, иначе уменьшаем радиус, двигая уже правую границу right_border = middle.  
### Разбор работы функции area_calculator(blocks, radius)  
Функция требует на вход размеры блоков и предполагаемый радиус, с которым работаем в данной итерации цикла. Вводятся переменные area – площадь, sum_of_angles – сумма углов – все равно 0.  
Далее в этой функции будет использоваться объект класса point. Для простоты будем называть его точкой. У точки 2 параметра – 2 координаты x и y. А также 2 внутренние функции, которые используются для расчета точности.  
Функция d(self) – рассчитывает длину вектора, а функция minus(self, checkpoint) – рассчитывает координаты вектора.  
Для того чтобы найти координаты вектора, нужно из одной координаты вычесть другую, а поэтому на вход функции minus дается такая же точка класса point с координатами x и y.  
Эту точку функция будет получать из введенной переменной points_array = [point(radius, 0)] – это список точек нашего будущего многоугольника, в котором уже лежит точка с координатами (R;0). Эта точка нужна для стяжки точек в многоугольник и проверки точности.  
Далее в цикле ищем координаты точек многоугольника. Так как в список уже включена одна точка, то будем искать координаты на 1 меньше от количества блоков. Введем длину конкретного блока для данной итерации – block_length = blocks[i]. Реализуем формулу, которая ищет стягивающий угол для каждой стороны нашего блока и числовое значение записываем в constricting_angle_num. Его преобразуем в радианы с условием, что косинус данного угла лежит на интервале [-1;1] и переведем его в радианы методом acos, значение запишем  в constricting_angle_rad. Складываем получившиеся углы и интуитивно становится понятно, что их сумма не должна превышать 360° если мы хотим вписать многоугольник в окружность. Однако если сумма углов больше 2π, функция вернет значения [-1;0] – что в конце даст ответ “0.00” – значит такой многоугольник невозможно построить.  
Если же все в порядке, то посчитаем значения координат при каждом угле, на протяжении цикла и добавим их в points_array. Далее в цикле по методу Гаусса посчитаем площади всех треугольников, получившихся в нашем многоугольнике, но делим на 2, так как мы находимся в цикле, значение записывается в area.  
Затем посчитаем точность. Для этого используем 2 функции из класса point. Из точки с координатами (R;0) вычитаем координаты последней найденной точки забора и считаем длину полученного отрезка, значение записывается в accuracy_checkpoint. Данное значение должно быть приближено к значению максимального блока, этот последний отрезок замкнет или почти замкнет фигуру.  
В конце возвращаем значение accuracy_checkpoint - blocks[-1] в переменную accuracy, получаем высокую точность с большим количеством знаков после запятой (в этом случае понимаем, что многоугольник замкнется, даже если длина блока немного не совпала с первоначальным значением, и площадь возможно найти), и возвращаем area / 2  в area_answer, ту самую площадь делим на 2 и находим искомую площадь.  
### Третий этап  
Простые проверки и сравнения перед выводом ответа.  
1.	Первое условие, если самый большой блок больше или равен сумме всех остальных блоков – такого многоугольника не существует, выводим “0.00”. 
2.	Второе условие – проверка точности, если точность меньше (меньше знаков после запятой), чем 10^(-6), то есть abs(accuracy) > accuracy_limit – то из-за низкой точности стороны многоугольника не сойдутся и площадь найти будет невозможно, выводим “0.00”. 
3.	Во всех других случаях, выводим area_answer с точностью до 2 знаков после запятой, как было сказано в условии задачи.

## Порядок тестирования и приемки  
Для проверки правильности работы программы были разработаны 3 теста: проверка примера из условия задачи (четырехугольник со сторонами 4, 5, 5, 10), египетский треугольник (с соотношениями сторон 3:4:5) и квадрат со стороной 5.  

### Тест №1. Четырехугольник со сторонами 4, 5, 5, 10  
Ввод: 4 10 5 5 4  
Вывод: 28.00  
Интуитивно понимаем, что это равнобокая трапеция. Найдем радиус описанной около нее окружности:  

![image](https://github.com/ksen322/university-projects/assets/119673458/513cac43-da54-4d0b-8fd9-a9b97427c29a)  

Найдем диагональ трапеции AC через прямоугольный треугольник по теореме Пифагора, получим, что AC ≈ 8,1.  
Далее находим полупериметр p, равный:

$$ p = {(AC + CD + AD) \over 2} ≈ 11.55 $$

Теперь находим радиус описанной окружности R:  

$$ R = {AD * AC * CD \over 4* \sqrt{p * (p - AD) * (p - AC) * (p - CD)}} ≈ 5 $$

Далее, имея уже одну точку, находим следующую за ней:  
1)	подсчитываем угол в радианах, стягивающий первую сторону, равную 4, т.к. массив отсортировали по возрастанию. Пусть α – угол, стягивающий данную вершину, тогда $$α = {2 * R^2 - l^2 \over 2 * R^2} = 0.68$$ где l = 4 – текущая сторона четырехугольника. 
2) считаем arccos от получившегося значения, получаем угол, примерно равный 47°
3) подсчитываем координаты точки с помощью тригонометрических соотношений: $R * cos(arccos(α))$ для координаты по x, $R * sin(arccos(α))$ для координаты по y. Получаем (3,4; 3,6) и строим эту точку на окружности с R=5. Также поступаем с координатами сторон 5 и 5. 
Получаем координаты 4-ех точек: [(5; 0), (3,4; 3,6), (-1,4; 4,7), (-4,9; 1,12)]. Строим и получаем следующую картину:

![image](https://github.com/ksen322/university-projects/assets/119673458/351b2fea-d5c4-4455-979e-3af8140f8118)

4)	Синим цветом показана оставшаяся сторона, которую находим, вычитая из координаты (5, 0) координату последней найденной точки (-4,9; 1,12). Подставляем координаты в формулу для нахождения длины отрезка по координатам: $$A = \sqrt{(x_{2} - x_{1})^2 - (y_{2} - y_{1})^2} ≈ 9,96$$ Почти равно 10, точность большая, следовательно, фигура замкнется и можно найти площадь этой фигуры по методу Гаусса: $$S = {x_{1} * y_{2} + x_{2} * y_{3} + x_{3} * y_{4} + x_{4} * y_{1} - x_{2} * y_{1} - x_{3} * y_{2} - x_{4} * y_{3} - x_{1} * y_{4} \over 2} = 27,5$$

Ручным подсчетом, неточным, получилось число близкое к 28.00, которое считает программа.  
### Тест №2. Египетский треугольник со сторонами 3, 4, 5  
Ввод: 3 3 5 4  
Вывод: 6.00  
Найдем радиус, описанной около него окружности.  
Сначала находим полупериметр p, равный:
$$p = {a + b + c \over 2} = 6$$
Далее проделываем те же действия, что и в предыдущем тесте и получаем следующие координаты: ([2,5; 0], [0,69; 2,4], [-2,5; 0]).  
По ним чертим рисунок:  

![image](https://github.com/ksen322/university-projects/assets/119673458/2543a41d-d4c7-4d4a-b238-0a97b41c0dca)  

Синим цветом показана оставшаяся сторона, которую находим, вычитая из координаты (2,5, 0) координату последней найденной точки (-2,5; 0). Подставляем координаты в формулу для нахождения длины отрезка по координатам:  
$$A = \sqrt{(x_{2} - x_{1})^2 - (y_{2} - y_{1})^2} = 5$$
Сторона совпала со стороной из входных данных, поэтому фигура замкнется.  
Найдем площадь этой фигуры по методу Гаусса:  
$$S = {x_{1} * y_{2} + x_{2} * y_{3} + x_{3} * y_{1} - x_{2} * y_{1} - x_{3} * y_{2} - x_{1} * y_{3} \over 2} = 6$$
Ручным подсчетом получилось число, равное искомой площади. Это же число выдает программа.  
### Тест №3. Квадрат со стороной 4
Ввод: 4 5 5 5 5  
Вывод: 25.00  
Найдем радиус, описанной около него окружности.  
Сначала находим полупериметр p, равный:  
$$p = {a + b + c \over 2} ≈ 8,54$$
Находим радиус:  
$$R = {a * d * c \over 4* \sqrt{p * (p - a) * (p - d) * (p - c)}} ≈ 3.5$$
Далее проделываем те же действия, что и в предыдущем тесте и получаем следующие координаты: ([3,5; 0], [-0,06; 3,5], [-3,5; -0,1], [0,2; -3,5]).  
По ним чертим рисунок:  

![image](https://github.com/ksen322/university-projects/assets/119673458/d6a558ec-2ac8-4515-a8b7-c49a06dccaf1)  

Синим цветом показана оставшаяся сторона, которую находим, вычитая из координаты (3,5, 0) координату последней найденной точки (0,2; -3,5). Подставляем координаты в формулу для нахождения длины отрезка по координатам:  
$$A = \sqrt{(x_{2} - x_{1})^2 - (y_{2} - y_{1})^2} ≈ 4.8$$
Почти равно 5, точность большая, следовательно, фигура замкнется и можно найти площадь этой фигуры по методу Гаусса:  
$$S = {x_{1} * y_{2} + x_{2} * y_{3} + x_{3} * y_{4} + x_{4} * y_{1} - x_{2} * y_{1} - x_{3} * y_{2} - x_{4} * y_{3} - x_{1} * y_{4} \over 2} = 24,5$$
Ручным подсчетом, неточным, получилось число близкое к 25.00, которое считает программа.  

Окончательное тестирование и приемка программы производятся с помощью автоматической проверочной системы Timus. В случае получения результата проверки Accepted программа считается работоспособной.