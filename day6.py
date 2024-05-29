'''
SELECT * FROM products where sku like 'PET%' and desc like '%Cat%' and desc like '%Senio%'


select count(*), count(distinct(o.orderid)) as numorders, sum(qty), sum(unit_price), 
 substr(ordered,1,4) , 
c.name, c.citystatezip, c.phone, c.birthdate
from orders o, orders_items oi , products p , customers c 
where 
c.customerid = o.customerid and 
o.orderid = oi.orderid and 
p.sku like 'PET%' and p.desc like '%Cat%' and p.desc like '%Senio%'
and oi.sku=p.sku

group by o.customerid , substr(ordered,1,4) order by sum(qty) desc,  count(*) desc




select count(*), count(distinct(o.orderid)) as numorders, sum(qty), sum(unit_price), c.name, c.citystatezip, c.phone, c.birthdate
from orders o, orders_items oi , products p , customers c 
where 
c.customerid = o.customerid and 
o.orderid = oi.orderid and 
p.sku like 'PET%' and p.desc like '%Cat%' and p.desc like '%Senio%'
and oi.sku=p.sku
and o.ordered < '2018-04-01' 

group by o.customerid order by sum(qty) desc,  count(*) desc




select count(*), count(distinct(o.orderid)) as numorders, sum(qty), sum(unit_price), c.name, c.citystatezip, c.phone, c.birthdate
from orders o, orders_items oi , products p , customers c 
where 
c.customerid = o.customerid and 
o.orderid = oi.orderid and 
p.sku like 'PET%' and p.desc like '%Cat%' and p.desc like '%Senio%'
and oi.sku=p.sku
and oi.orderid > '100100'
and oi.orderid < '100190'
group by o.customerid order by count(*) desc


select *
from orders o, orders_items oi , products p , customers c 
where 
c.customerid = o.customerid and 
o.orderid = oi.orderid and 
p.sku like 'PET%' and p.desc like '%Cat%' and p.desc like '%Senio%'
and oi.sku=p.sku
and oi.orderid > '100100'
and oi.orderid < '100190'
order by orderid asc






select count(*), sum(total), sum(unit_price), o.orderid  , c.*, count(distinct(oi.sku)) as uniitems, desc
FROM products p,  orders o, orders_items oi, customers c  
where c.customerid = o.customerid and oi.sku = p.sku
and p.sku like 'PET%' and p.desc like '%Cat%' and p.desc like '%Senio%'
and date(ordered) < '2018-04-01' and oi.orderid = o.orderid  
group by o.customerid
order by count(*) desc


'''