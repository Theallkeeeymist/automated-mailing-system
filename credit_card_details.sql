USE customer_credit_card;

SELECT 'customer_name', 'email_id', 'credit_card_number', 'flag'
UNION ALL
SELECT Customer.customer_name, Customer.email_id, Credit_card.credit_card_number, Credit_card.flag
FROM Customer
LEFT JOIN Credit_card ON Customer.customer_id = Credit_card.customer_id
-- WHERE Credit_card.flag = 'Y'
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/credit_card_details.csv'
FIELDS ENCLOSED BY '\"'
TERMINATED BY ','
LINES TERMINATED BY '\n';