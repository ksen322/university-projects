# Первая работа с SQL
Это первая работа с SQL. Работа проводилась в рамках университета  
# Ход работы  
Для начала были созданы 4 таблицы с помощью запросов, представленных ниже. Соответственно, были созданы таблицы для ноутбуков, ПК, смартфонов и общая таблица с предстваленными продуктами  

```

CREATE TABLE notebook(model_name VARCHAR(20), cpu_core INT, cpu_speed INT, disk_type VARCHAR(20), disk_size INT, screen_size REAL, price INT);
INSERT INTO notebook VALUES('VivoBookPro', 4, 10, 'HDD/SSD', 4, 15.6, 1000);
INSERT INTO notebook VALUES('Pavillion', 4, 5, 'HDD', 1, 15.6, 500);
INSERT INTO notebook VALUES('ZenBook14', 4, 2, 'SSD', 2, 14, 900);
INSERT INTO notebook VALUES('GF93', 6, 4, 'HDD/SSD', 1, 15.6, 1000);
INSERT INTO notebook VALUES('ExpertBook', 4, 4, 'SSD', 1, 15.6, 500);

CREATE TABLE pc(model_name VARCHAR(20), cpu_core INT, cpu_speed INT, ram INT, disk_size INT, price INT);
INSERT INTO pc VALUES('Pandora', 8, 20, 32, 4, 3000);
INSERT INTO pc VALUES('88D-11 6ur', 6, 10, 16, 2, 1500);
INSERT INTO pc VALUES('IdeaCentre', 6, 3, 8, 1, 700);
INSERT INTO pc VALUES('PavillionTP01', 6, 4, 8, 1, 600);
INSERT INTO pc VALUES('R0G', 6, 5, 8, 1, 1000);

CREATE TABLE smartphone(model_name VARCHAR(20), cpu_core INT, cpu_speed INT, flash_size INT, OS VARCHAR(20), lte VARCHAR(5), screen_size REAL, price INT);
INSERT INTO smartphone VALUES('Galaxy S10', 16, 20, 128, 'Android', 'YES', 6.1, 1000);
INSERT INTO smartphone VALUES('Galaxy S20', 8, 20, 256, 'Android', 'YES', 6.7, 1200);
INSERT INTO smartphone VALUES('iPhone 12', 8, 18, 128, 'iOS', 'YES', 6.1, 1000);
INSERT INTO smartphone VALUES('iPhone 11', 8, 18, 256, 'iOS', 'YES', 5.8, 900);
INSERT INTO smartphone VALUES('Reno Z', 8, 15, 128, 'Android', 'YES', 5.8, 300);

CREATE TABLE product(vendor VARCHAR(20), model_name VARCHAR(20), type_thing VARCHAR(15));
INSERT INTO product VALUES('Invasion', 'Pandora', 'PC');
INSERT INTO product VALUES('Omen', '88D-11 6ur', 'PC');
INSERT INTO product VALUES('Asus', 'VivoBookPro', 'LAPTOP');
INSERT INTO product VALUES('HP', 'Pavillion', 'LAPTOP');
INSERT INTO product VALUES('Asus', 'ZenBook14', 'LAPTOP');
INSERT INTO product VALUES('Lenovo', 'IdeaCentre', 'PC');
INSERT INTO product VALUES('Asus', 'R0G', 'PC');
INSERT INTO product VALUES('HP', 'PavillionTP01', 'PC');
INSERT INTO product VALUES('MSI', 'GF93', 'LAPTOP');
INSERT INTO product VALUES('Asus', 'ExpertBook', 'LAPTOP');
INSERT INTO product VALUES('Samsung', 'Galaxy S10', 'SMARTPHONE');
INSERT INTO product VALUES('OPPO', 'Reno Z', 'SMARTPHONE');
INSERT INTO product VALUES('Apple', 'iPhone 11', 'SMARTPHONE');
INSERT INTO product VALUES('Apple', 'iPhone 12', 'SMARTPHONE');
INSERT INTO product VALUES('Samsung', 'Galaxy S20', 'SMARTPHONE');

```

И мы получили следующие таблицы:  
![image](https://github.com/ksen322/university-projects/assets/119673458/d15e936a-86d0-4f74-9bb2-5d69b758b28d)  
![image](https://github.com/ksen322/university-projects/assets/119673458/88144f38-c3cf-4247-ba3c-ce38cdfc81ad)  
![image](https://github.com/ksen322/university-projects/assets/119673458/6ca49900-e741-43ee-b46f-34e977dc6f5e)  
![image](https://github.com/ksen322/university-projects/assets/119673458/6bdb9f07-ec17-47b0-89e3-695eacb15a31)  

В течение курса по SQL в университете нам выдали 20 заданий, для которых и нужно было написать запросы  

## Первый запрос: вывести всех производителей из таблицы Smmartphone  

```
SELECT distinct vendor from product where type_thing = "SMARTPHONE";
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/8b9e0f13-2e72-414f-82bc-1ddaf44d9434)  

## Второй запрос: вывести всех производителей из таблицы Notebook, у которых есть модели ноутбуков с SSD хранилищем

```
SELECT distinct vendor from product, notebook where product.model_name = notebook.model_name AND (notebook.disk_type = 'SSD' OR notebook.disk_type = "HDD/SSD");
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/33fcc36d-34ff-4325-9c57-b5332579c208)

## Третий запрос: вывести уникальные значения производителя, название модели ноутбука, название модели ПК, размер диска ноутбука и размер диска ПК из таблиц product, notebook и pc, где модель товара является либо моделью ноутбука, либо моделью ПК, и размеры дисков ноутбука и ПК совпадают
```
SELECT distinct product.vendor, notebook.model_name, pc.model_name, notebook.disk_size, pc.disk_size FROM product, notebook, pc 
	where (product.model_name = notebook.model_name OR product.model_name = pc.model_name) AND pc.disk_size = notebook.disk_size;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/98677718-ec5d-434b-a156-779eda7afb2a)  
![image](https://github.com/ksen322/university-projects/assets/119673458/87da2dc7-1274-402b-9fa8-80b153449cec)  
![image](https://github.com/ksen322/university-projects/assets/119673458/007ace01-6537-4674-884d-dda9975f514f)  

## Четвертый запрос: объединить данные из таблиц product, smartphone и notebook, где выбираются уникальные значения производителя, название модели товара, тип товара и размер экрана 
```
SELECT distinct vendor, product.model_name, type_thing, (notebook.screen_size * 2.54) as display_size from product, notebook where product.model_name = notebook.model_name 
	union SELECT distinct vendor, product.model_name, type_thing, (smartphone.screen_size * 2.54) as display_size from product, smartphone 
	where product.model_name = smartphone.model_name;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/36f8b757-8aae-4ff4-a14c-ee27a71b34db)  
![image](https://github.com/ksen322/university-projects/assets/119673458/58f561de-1d59-4fd2-a3cf-7f1ceca8bef2)  

## Пятый запрос: вывести уникальные значения производителя, название модели ПК и цену из таблиц product и pc, где цена ПК выше средней цены по ПК
```
SELECT distinct product.vendor, pc.model_name, pc.price FROM product, pc where product.model_name = pc.model_name AND pc.price > (SELECT AVG(price) FROM pc);
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/75dc0535-021a-4cb4-809e-b7131e64b837)  

## Шестой запрос: вывести количество строк в таблице smartphone, где значение столбца lte равно 'YES'
```
SELECT count(*) FROM smartphone WHERE lte = 'YES';
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/158f9d44-0c51-47e0-b7d6-fea561e9bcbe)  

## Седьмой запрос: вывести уникальные значения производителя из таблиц product и notebook, где цена ноутбука равна максимальной цене в таблице notebook
```
SELECT vendor FROM product, notebook WHERE product.model_name = notebook.model_name AND price = (SELECT MAX(price) FROM notebook);
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/5571166a-a6ae-4292-9c43-2f06eef6e35e)  

## Восьмой запрос: вывести название модели и размер флеш-памяти смартфона из таблицы smartphone, где размер флеш-памяти минимальный, и операционная система - 'Android'
```
SELECT model_name, flash_size FROM smartphone WHERE flash_size = (SELECT MIN(flash_size) FROM smartphone) AND smartphone.OS = 'Android';
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/5ae81cae-30ee-4351-99ce-a85fe0528e43)  

## Девятый запрос: вывести уникальные значения проивзодиеля из таблиц product и notebook, а также сумму цен ноутбуков, сгруппированных по производителю
```
SELECT vendor, SUM(notebook.price) FROM product, notebook WHERE product.model_name = notebook.model_name group by vendor;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/f6fdb4f0-4d0e-4568-a7a7-ae68087e7be2)  

## Десятый запрос: вывести уникальные значения производителя из таблиц product и notebook, где данные группируются по поставщику и выводятся только те, у которых средняя цена по ноутбукам меньше 1000
```
SELECT vendor FROM product, notebook WHERE product.model_name = notebook.model_name group by vendor having AVG(notebook.price) < 1000;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/c76fc9c1-7a44-4eb1-b752-50adf415a1a1)  

## Одиннадцатый запрос: вывести уникальные значения производителя, название модели товара и цену из таблиц product, notebook, pc и smartphone, объединенных операцией UNION, затем отсортировать результат по поставщику и цене в порядке убывания
```
SELECT product.vendor, product.model_name, notebook.price FROM product, notebook WHERE product.model_name = notebook.model_name 
	union SELECT product.vendor, product.model_name, pc.price FROM product, pc WHERE product.model_name = pc.model_name 
	union SELECT product.vendor, product.model_name, smartphone.price FROM product, smartphone WHERE product.model_name = smartphone.model_name order by vendor, price DESC;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/e69ba9db-56ae-40da-a919-c9b5c16ee0a8)  
![image](https://github.com/ksen322/university-projects/assets/119673458/0343bff9-025f-448f-b459-ef1cb692cac2)  

## Двеннадцатый запрос: вывести среднюю скорость ЦП в ПК, где производитель - 'Asus'
```
SELECT AVG(pc.cpu_speed) FROM product, pc WHERE product.model_name = pc.model_name AND product.vendor = 'Asus';
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/45853be2-cad9-4001-946c-eac4b8257dbb)  

## Триннадцатый запрос: вывести уникальные значения производителя, название модели ПК и размер диска из таблиц product и pc, где размер диска совпадает с размером диска, который встречается как минимум в двух моделях ПК
```
SELECT product.vendor, product.model_name, pc.disk_size FROM product, pc WHERE product.model_name = pc.model_name AND 
	disk_size = (SELECT disk_size FROM pc GROUP BY disk_size HAVING count(pc.model_name) >= 2);
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/cdd7bba3-c79e-49b6-867b-5be47fcdfa4f)  

## Четырнадцатый запрос: вывести уникальные значения типа товара, название модели ноутбука и скорость ЦП из таблиц notebook, product и pc, где скорость ЦП ноутбука меньше минимальной скорости ЦП в ПК
```
SELECT distinct product.type_thing, notebook.model_name, notebook.cpu_speed FROM notebook, product, pc WHERE product.model_name = notebook.model_name 
	AND notebook.cpu_speed < (SELECT MIN(pc.cpu_speed) FROM pc);
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/5bcc077f-61fa-4b15-8fd0-b9c4d7ba584f)  

## Пятнадцатый запрос: вывести уникальные значения название модели из таблиц pc, notebook и smartphone, объединенных операцией UNION, где цена равна максимальной цене по всем товарам
```
SELECT model_name FROM (SELECT model_name, price FROM pc union all SELECT model_name, price FROM notebook union all SELECT model_name, price FROM smartphone) as a 
	WHERE price = (SELECT MAX(price) FROM (SELECT model_name, price FROM pc union all SELECT model_name, price FROM notebook union all SELECT model_name, price FROM smartphone) as b);
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/fd1ba266-af57-4409-a09b-165f64208888)  

## Шестнадцатый запрос: вывести производителя, название модели и цену товара из таблиц pc, notebook и smartphone, где производитель - 'Asus', и объединить эти данные во временную таблицу
```
select vendor, model_name, price from (select price, PC.model_name, product.vendor from pc, product 
	where product.model_name = PC.model_name union select price, notebook.model_name, product.vendor from notebook, product where product.model_name = notebook.model_name 
	union select price, Smartphone.model_name, product.vendor from smartphone, product where product.model_name = Smartphone.model_name ) as a where vendor = "Asus";
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/325eeda2-0732-451d-917e-55ef2360f2e4)  

## Семнадцатый запрос: создать представление (VIEW), которое содержит данные прозводителя, название модели и размер диска ноутбука из таблиц product и notebook, где размер диска равен максимальному размеру в таблице notebook, и затем вывести все данные из этого представления
```
create VIEW a as select product.vendor, product.model_name, notebook.disk_size from product, notebook
	where (product.model_name = notebook.model_name and notebook.disk_size = (select max(disk_size) from notebook));
	select * from a;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/375bedc3-9072-417d-a67d-b64eeccf214a)  

## Восемнадцатый запрос: создать представление (VIEW), которое содержит данные производителя, средние объемы оперативной памяти и минимальные объемы оперативной памяти из таблиц product и PC, сгруппированные по производителю, и затем вывести все данные из этого представления
```
create VIEW b as select product.vendor, AVG(PC.ram), MIN(PC.ram) from product, PC where (product.model_name = PC.model_name) group by vendor;
	select * from b;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/321e0742-3e6d-45f3-8554-5138e9438476)  

## Девятнадцатый запрос: вывести производителя, название модели ПК и цену из таблицы pc с использованием операции INNER JOIN для соединения таблиц pc и product по модели ПК
```
select product.vendor, pc.model_name, pc.price from pc INNER JOIN product ON pc.model_name = product.model_name;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/17bb1212-e25b-4028-96fa-25fecfa8bfce)  

## Двадцатый запрос: вывести название модели, производителя и сумму размеров дисков из временной таблицы, содержащей данные о моделях ПК и ноутбуков, а также их производителях, и объединить эти данные для вычисления общего размера дисков, сгруппированного по производителя
```
SELECT model_name, vendor, sum(disk_size) FROM
	(SELECT pc.model_name, disk_size, vendor FROM PC INNER JOIN PRODUCT ON PC.model_name = product.model_name
	union all
	SELECT notebook.model_name, disk_size, vendor FROM notebook INNER JOIN PRODUCT ON notebook.model_name = product.model_name) as a
	group by vendor;
```
Результат:  
![image](https://github.com/ksen322/university-projects/assets/119673458/9a3b7f30-8c9a-4662-bd18-c3ae1064e11e)
