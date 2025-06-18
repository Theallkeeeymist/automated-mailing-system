select Customer.customer_name, Customer.email_id, Credit_card.credit_card_number, Credit_card.flag from Customer
left join Credit_card on Customer.customer_id=Credit_card.customer_id
where Credit_card.flag='Y'
into outfile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\have_credit_card.csv'
fields enclosed by '\"'
terminated by ','
lines terminated by '\n';