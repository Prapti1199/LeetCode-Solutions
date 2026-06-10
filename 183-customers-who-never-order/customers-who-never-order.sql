-- Write your PostgreSQL query statement below
SELECT c.name as Customers from Customers c 
    LEFT JOIN Orders o on  o.customerId = c.id 
where o.id is NULL;