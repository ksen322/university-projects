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






