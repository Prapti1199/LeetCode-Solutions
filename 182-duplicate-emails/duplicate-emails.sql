-- Write your PostgreSQL query statement below
SELECT email as  Email from Person  GROUP BY email having  COUNT(email) > 1;