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