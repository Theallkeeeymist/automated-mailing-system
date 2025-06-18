create database customer_credit_card;

use customer_credit_card;

create table Customer (
       customer_id INT AUTO_INCREMENT,
       customer_name VARCHAR(255), -- VARCHAR is a data type that represents string of size 255 
       email_id VARCHAR(255),
       PRIMARY KEY (customer_id) -- uniquely defines row of each table 
       );
create table Credit_card (
       customer_id INT,
       credit_card_number VARCHAR(255),
       flag ENUM('Y','N'), -- data type that represents a fixed set of values here Y or N
       foreign key (customer_id) references Customer(customer_id) -- inreference to primary key
       );