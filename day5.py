

'''

# Oh! BKY bakery, stop looking at the kinishes

select count(*), q.* from (
select  min(oi.orderid) as moid, date(ordered), time(ordered), ordered, 
count(distinct(oi.orderid)) as uni, count(distinct(o.customerid)) as unic, 
o.customerid , c.* from  orders o, orders_items oi, customers c  
where c.customerid = o.customerid and oi.sku like 'BKY%' 
and time(ordered) > '01:55' and time(ordered) < '06:00' and  date(ordered) < '2018-04-01'
 and oi.orderid = o.orderid  group by o.orderid 
) q group by q.customerid order by count(*) desc;


######################

### Ignore the below, I was looking for Knishes, not Pasteries



Select substr(sku,1,3) as scode, count(*) from products group by  substr(sku,1,3);

What is a pastry? 
Knish
anything else?
blintz???  Nah? 
Kugel? Nah.


grep Knish noahs-products.csv
"DLI3740","Kasha Knish",1.10,18.6|15.6|9.2
"DLI5878","Broccoli Knish",1.10,14.0|4.8|2.1


select * from orders_items oi where oi.sku in ('DLI3740', 'DLI5878') limit 4;

select  min(oi.orderid) as moid, date(ordered), time(ordered), ordered, count(*), 
count(distinct(oi.orderid)) as uni, count(distinct(customerid)) as unic, customerid 
from orders o, orders_items oi where oi.sku in ('DLI3740', 'DLI5878') and oi.orderid = o.orderid  
group by o.orderid having time(ordered) > '03:55' order by time(ordered) limit 40;


select  min(oi.orderid) as moid, date(ordered), time(ordered), ordered, 
count(distinct(oi.orderid)) as uni, count(distinct(o.customerid)) as unic, 
o.customerid , c.* from  orders o, orders_items oi, customers c  
where c.customerid = o.customerid and oi.sku in ('DLI3740', 'DLI5878') 
and c.citystatezip like '%NY%' and oi.orderid = o.orderid  group by o.orderid 
having time(ordered) > '02:55' and time(ordered) < '09:00' and  
date(ordered) < '2019-01-01' order by time(ordered) limit 40;



select  min(oi.orderid) as moid, date(ordered), time(ordered), ordered, 
count(*), count(distinct(oi.orderid)) as uni, count(distinct(customerid)) as unic, 
customerid from orders o, orders_items oi where oi.sku in ('DLI3740', 'DLI5878') 
and oi.orderid = o.orderid  group by o.orderid having time(ordered) > '02:55' 
and date(ordered) < '2018-01-01' order by time(ordered) limit 40;



select  min(oi.orderid) as moid, date(ordered), time(ordered), ordered, 
count(distinct(oi.orderid)) as uni, count(distinct(o.customerid)) as unic, 
o.customerid , c.* from  orders o, orders_items oi, customers c  
where c.customerid = o.customerid and oi.sku in ('DLI3740', 'DLI5878') 
and c.citystatezip like '%NY%' and oi.orderid = o.orderid  group by o.orderid 
having time(ordered) > '01:55' and time(ordered) < '09:00' and  date(ordered) < '2019-01-01'
order by time(ordered) limit 40;




select  min(oi.orderid) as moid, date(ordered), time(ordered), ordered, 
count(distinct(oi.orderid)) as uni, count(distinct(o.customerid)) as unic, 
o.customerid , c.* from  orders o, orders_items oi, customers c  
where c.customerid = o.customerid and oi.sku in ('DLI3740', 'DLI5878') 
and time(ordered) > '01:55' and time(ordered) < '09:00' and  date(ordered) < '2019-01-01'
and c.citystatezip like '%NY%' and oi.orderid = o.orderid  group by o.orderid 
order by time(ordered) limit 40;



# Oh! BKY bakery, stop looking at the kinishes

select count(*), q.* from (
select  min(oi.orderid) as moid, date(ordered), time(ordered), ordered, 
count(distinct(oi.orderid)) as uni, count(distinct(o.customerid)) as unic, 
o.customerid , c.* from  orders o, orders_items oi, customers c  
where c.customerid = o.customerid and oi.sku like 'BKY%' 
and time(ordered) > '01:55' and time(ordered) < '06:00' and  date(ordered) < '2018-04-01'
 and oi.orderid = o.orderid  group by o.orderid 
) q group by q.customerid order by count(*) desc;



'''