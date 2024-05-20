create database car_rental;
use car_rental;

create table cars (
car_id integer primary key auto_increment, 
manufacturer varchar(25), 
model varchar(25), 
year smallint,
horse_power smallint,
price_per_day mediumint);

create table clients (
client_id integer primary key auto_increment,
first_name varchar(25),
last_name varchar(25),
address varchar(25),
city varchar(25));

create table bookings (
booking_id integer primary key auto_increment,
client_id integer,
car_id integer,
start_date date,
end_date date,
total_amount integer);

ALTER TABLE bookings ADD CONSTRAINT
client_id_fk FOREIGN KEY (client_id)
REFERENCES clients(client_id);

ALTER TABLE bookings ADD CONSTRAINT
car_id_fk FOREIGN KEY (car_id)
REFERENCES cars(car_id);

select * from clients;
insert into clients (first_name, last_name, address, city) values ('John', 'Smith', 'Front Street 12', 'Los Angeles');
insert into clients (first_name, last_name, address, city) values ('Andrew', 'Jones', 'Back Street 43', 'New York');
select * from clients;

select * from cars;
insert into cars (manufacturer, model, year, horse_power, price_per_day) values ('Seat', 'Leon', 2016, 80, 200);
insert into cars (manufacturer, model, year, horse_power, price_per_day) values ('Toyota', 'Avensis', 2014, 72, 100);
select * from cars;

select * from bookings;
insert into bookings (client_id, car_id, start_date, end_date, total_amount) values (1, 2, '2020-07-05', '2020-07-06', 100);
insert into bookings (client_id, car_id, start_date, end_date, total_amount) values (2, 2, '2020-07-10', '2020-07-12', 200);
select * from bookings;

UPDATE clients SET first_name='Michal', last_name='Maliszewski', address='adresa', city='Těrlicko' where client_id=1;
select * from clients;

DELETE FROM bookings where client_id > 0;
DELETE FROM clients where client_id > 0;
select * from clients;

insert into clients (first_name, last_name, address, city) values ('Ondrej', 'Prekazka', 'Front Street 14', 'Los Angeles');
insert into clients (first_name, last_name, address, city) values ('Vilém', 'Skočdopole', 'Back Street 13', 'New York');
select last_name, city from clients where first_name="Vilém" order by city desc;

INSERT INTO clients (first_name, last_name, address, city) VALUES
 ('Michal', 'Taki', 'os. Srodkowe 12', 'Poznan'),
 ('Pawel', 'Ktory', 'ul. Stara 11', 'Gdynia'),
 ('Anna', 'Inna', 'os. Srednie 1', 'Gniezno'),
 ('Alicja', 'Panna', 'os. Duze 33', 'Torun'),
 ('Damian', 'Papa', 'ul. Skosna 66', 'Warszawa'),
 ('Marek', 'Troska', 'os. Male 90', 'Radom'),
 ('Jakub', 'Klos', 'os. Polskie 19', 'Wadowice'),
 ('Lukasz', 'Lis', 'os. Podlaskie 90', 'Bialystok'); 
 
insert into clients (first_name, last_name, address, city) values ('John', 'Smith', 'Front Street 12', 'Los Angeles');
insert into clients (first_name, last_name, address, city) values ('Andrew', 'Jones', 'Back Street 43', 'New York');
 
 INSERT INTO cars (manufacturer, model, year, horse_power, price_per_day) VALUES
 ('Mercedes', 'CLK', 2018, 190, 400),
 ('Hyundai', 'Coupe', 2014, 165, 300),
 ('Dacia', 'Logan', 2015, 103, 150),
 ('Saab', '95', 2012, 140, 140),
 ('BMW', 'E36', 2007, 110, 80),
 ('Fiat', 'Panda', 2016, 77, 190),
 ('Honda', 'Civic', 2019, 130, 360),
 ('Volvo', 'XC70', 2013, 180, 280);
 
insert into cars (manufacturer, model, year, horse_power, price_per_day) values ('Seat', 'Leon', 2016, 80, 200);
insert into cars (manufacturer, model, year, horse_power, price_per_day) values ('Toyota', 'Avensis', 2014, 72, 100);
 
select client_id from clients;
 
INSERT INTO bookings (client_id, car_id, start_date, end_date, total_amount) VALUES
 (3, 3, '2020-07-06', '2020-07-08', 400),
 (6, 10, '2020-07-10', '2020-07-16', 1680),
 (4, 5, '2020-07-11', '2020-07-14', 450),
 (5, 4, '2020-07-11', '2020-07-13', 600),
 (7, 3, '2020-07-12', '2020-07-14', 800),
 (5, 7, '2020-07-14', '2020-07-17', 240),
 (3, 8, '2020-07-14', '2020-07-16', 380),
 (5, 9, '2020-07-15', '2020-07-18', 1080),
 (6, 10, '2020-07-16', '2020-07-20', 1120),
 (8, 1, '2020-07-16', '2020-07-19', 600),
 (9, 2, '2020-07-16', '2020-07-21', 500),
 (10, 6, '2020-07-17', '2020-07-19', 280),
 (1, 9, '2020-07-17', '2020-07-19', 720),
 (3, 7, '2020-07-18', '2020-07-21', 240),
 (5, 4, '2020-07-18', '2020-07-22', 1200);

select * from cars where year > 2015;
select * from bookings where total_amount between 1000 and 2555;
select client_id from clients where first_name like "M%" and last_name like "%ka";

SELECT cl.first_name, cr.manufacturer
FROM clients AS cl, cars AS cr;

SELECT clients.last_name, clients.city, bookings.total_amount
FROM clients
right JOIN bookings ON
bookings.client_id=clients.client_id;

select avg(year), sum(price_per_day) * sum(horse_power) from cars;

with mezivysledek as (
select bookings.client_id, avg(bookings.total_amount) as prumer
from bookings
where bookings.client_id > 3 
group by bookings.client_id 
having avg(bookings.total_amount) > 500)
select min(prumer) from mezivysledek;

SELECT clients.last_name, bookings.total_amount
FROM clients
inner JOIN bookings ON
bookings.client_id=clients.client_id
where bookings.total_amount > 1000;

SELECT clients.last_name, sum(bookings.total_amount)
FROM clients
left JOIN bookings ON
bookings.client_id=clients.client_id
group by clients.last_name
having sum(bookings.total_amount) > 1000;

SELECT clients.city, bookings.start_date, bookings.end_date, cars.horse_power, cars.price_per_day
FROM bookings
inner JOIN clients ON
bookings.client_id=clients.client_id
inner JOIN cars ON
bookings.car_id=cars.car_id
where bookings.start_date >= '2020-07-12' and bookings.start_date <= '2020-07-20' and cars.horse_power <= 120
order by cars.price_per_day desc;

select horse_power, count(car_id)
from cars 
where price_per_day >= 300 
group by horse_power 
order by horse_power asc;

select sum(total_amount) as soucet 
from bookings 
where bookings.start_date between '2020-07-14' and '2020-07-18';

select clients.last_name as surname, clients.first_name as name, avg(bookings.total_amount) as Average_reservations_price, count(cars.car_id) as number_of_rented_cars
FROM bookings
inner JOIN clients ON
bookings.client_id=clients.client_id
inner JOIN cars ON
bookings.car_id=cars.car_id
group by clients.last_name, clients.first_name
having count(cars.car_id) > 1
order by count(cars.car_id) desc;
