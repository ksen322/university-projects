#include <iostream>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include<math.h>
using std::cin;
using std::cout;
using std::endl;
#include "Windows.h"
#pragma warning(disable : 4996)

void eatspaces(char* s); //функция для удаления пробелов
double expr(char* s); //функция, вычисляющая выражение
double term(char* s, int& index); //функция для анализа элемента
double trigon(char* s, int& index); //функция для вычисления функций логарфима, корня и тригонометричских функций
double power(char* s, int& index); //функция для извлечения степени
double number(char* s, int& index); //функция, распознающая число
char* extract(char* s, int& index); //функция для извлечения подстроки

const int max = 80; //максимальный размер буфера

int main()
{
	setlocale(0, "Russian");
	char buf[max] = { 0 }; //область хранения вычисляемого входного выражения
	cout << endl << "Калькулятор" << endl
		<< "Для вычисления квадратного корня наберите sqrt" << endl
		<< "Для вычисления функции синуса, косинуса и тангенса введите sin, cos и tg соответственно" << endl
		<< "Для возведения в степень введите ^" << endl
		<< "Для вычисления натурального логарифма введите ln" << endl
		<< "Введите выражение или пустую строку (для завершения)" << endl;
	for (; ; )
	{
		cin.getline(buf, sizeof buf); //читаем входную строку
		eatspaces(buf); //удаляем все пробелы из строки
		if (!buf[0]) //если пустая строка
			return 0;
		cout << "= " << expr(buf)
			<< endl << endl;
	}
}

void eatspaces(char* s)
{
	int i = 0;                          //индекс места в строке "куда копировать"
	int j = 0;                          //индекс места в строке "откуда копировать"
	while ((*(s + i) = *(s + j++)) != '\0') //цикл, пока очередной символ не '\0'
		if (*(s + i) != ' ')  //увеличиваем i, если символ не пробел
			i++;
	return;
}

double expr(char* s)
{
	double a = 0.0;         //здесь сохраняем результат
	int index = 0;              //текущая позиция символа
	a = term(s, index);   //получить первый элемент
	for (; ; )                 //бесконечный цикл, выход внутри
	{
		switch (*(s + index++)) //выбрать действие на основе текущего символа
		{
		case '\0':          //конец строки, возвращаем значение
			return a;
		case '+':           //знак плюс, прибавляем элемент к value
			a += term(s, index);
			break;
		case '-':           //знак минус, вычитаем элемент из value
			a -= term(s, index);
			break;
		default:            //все остальное не котируется
			int i = index;
			while (--i > 0)
				cout << " ";
			cout << "Вы ввели неверное значение функции " << endl;
			exit(1);
		}
	}
}

double term(char* s, int& index)
{
	double a = 0.0;             //здесь накапливается значение результата
	a = power(s, index);      //получить первое число элемента
	//выполняем цикл до тех пор, пока имеем допустимую операцию
	while ((*(s + index) == '*') || (*(s + index) == '/'))
	{
		if (*(s + index) == '*')
			a *= power(s, ++index);
		if (*(s + index) == '/')
		{
			a /= power(s, ++index);
			return a;
		}
	}
}


double power(char* s, int& index)
{
	double a = 0.0;
	a = trigon(s, index);
	while (*(s + index) == '^')
	{
		a = pow(a, trigon(s, ++index)); //возводим в степень
	}
	return a;
}

double trigon(char* s, int& index)
{
	int buf_i = 0;
	int stor_i = index; //переменная для хранения индекса (чтобы если что вернуть индекс без изменений)
	char* p = 0;    //временный указатель для сравнения символов
	double a = 0;
	while (isalpha(*(s + stor_i)))
	{
		buf_i++;    //сколько букв
		stor_i++;   //текущий индекс
	}
	if (!buf_i)     //если нет ни одной буквы, то возвращаем число
	{
		a = number(s, index);
		return a;
	}
	else                //иначе смотрим, являются ли буквы чем-нибудь этим
	{
		p = new char[buf_i + 1];  //а для этого создаем временную строку, чтобы сравнить
		p[buf_i] = '\0';
		strncpy(p, s + index, buf_i);
	}
	if (strcmp(p, "sin") == 0)      //синус в градусах
	{
		a = sin(3.141592 / 180 * number(s, stor_i));
		index = stor_i;
		delete[] p;     //не забываем удалить временную строку
		return a;
	}
	else if (strcmp(p, "cos") == 0) //косинус в градусах
	{
		a = cos(3.141592 / 180 * number(s, stor_i));
		index = stor_i;
		delete[] p;     //не забываем удалить временную строку
		return a;
	}
	else if (strcmp(p, "tg") == 0) //тангенс в градусах
	{
		a = tan(3.141592 / 180 * number(s, stor_i));
		index = stor_i;
		delete[] p;     //не забываем удалить временную строку
		return a;
	}
	else if (strcmp(p, "ln") == 0)
	{
		a = log(number(s, stor_i));
		index = stor_i;
		delete[] p;     //не забываем удалить временную строку
		return a;
	}
	else if (strcmp(p, "sqrt") == 0)
	{
		a = sqrt(number(s, stor_i));
		index = stor_i;
		delete[] p;     //не забываем удалить временную строку
		return a;
	}
	else
	{
		return a;
	}
}

double number(char* s, int& index)
{
	double a = 0.0;                 //хранит результирующее значение
	if (*(s + index) == '(')
	{
		char* p_sub = 0;
		p_sub = extract(s, ++index);
		a = expr(p_sub);
		delete[] p_sub;
		return a;
	}
	//продуманский цикл, превращает символы в число
	while (isdigit(*(s + index)))       //цикл накапливает ведущие цифры 
		a = 10 * a + (*(s + index++) - '0');
	if (*(s + index) != '.')          //если не цифра, проверяем на десятичную точку
		return a;
	double d = 1.0;                //множитель для десятичных разрядов
	//еще один продуманский цикл, возвращает десятичную часть
	while (isdigit(*(s + (++index)))) //выполнять цикл, пока идут цифры 
	{
		d *= 0.1;
		a = a + (*(s + index) - '0') * d;
	}
	return a;
}

char* extract(char* s, int& index)
{
	char buf[max];       //временное пространство для подстроки
	char* p = 0;        //указатель на новую строку для возврата
	int left = 0;           //счетчик найденных левых скобок
	int buf_i = index;  //сохранить начальное значение index
	do
	{
		buf[index - buf_i] = *(s + index); //копируем символ текущей строки в подстроку
		switch (buf[index - buf_i]) //смотрим, что это за символ
		{
		case ')':
			if (left == 0)
			{
				buf[index - buf_i] = '\0'; //если счетчик скобочек верный, ставим символ конца строки
				++index;    //устанавливаем индекс на следующий за скобочкой элемент
				p = new char[index - buf_i];
				if (!p)
				{
					cout << "Выделение памяти не удалось, программа прервана.";
					exit(1);
				}
				strcpy_s(p, index - buf_i, buf); //и копируем подстроку в новую память
				return p;
			}
			else
				left--;     //уменьшаем счетчик скобок
			break;
		case '(':
			left++;         //соответственно увеличиваем
			break;
		}
	} while (*(s + index++) != '\0');     //устанавливаем индекс в следующий элемент
	cout << "Вывод за пределы выражения, возможно, плохой ввод." << endl;
	exit(1);
	return p;
}