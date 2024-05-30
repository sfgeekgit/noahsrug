


select count(*), custid, sum(tot_paid), sum(whcost) 
from (

select o.orderid, o.customerid as custid,  count(*) as numitems, o.total as tot_paid, 
sum(qty* unit_price) as stdprice, sum(qty * wholesale_cost) as whcost
, p.wholesale_cost, unit_price,  qty
 from orders o,  orders_items oi , products p 
 where  
 o.orderid = oi.orderid and
 p.sku = oi.sku 
group by o.orderid
having total  < sum(qty* wholesale_cost) 
) q group by q.custid order by sum(whcost) desc



#######

select count(*), custid, sum(tot_paid), sum(whcost) 
from (

select o.orderid, o.customerid as custid,  count(*) as numitems, o.total as tot_paid, 
sum(qty* unit_price) as stdprice, sum(qty * wholesale_cost) as whcost
, p.wholesale_cost, unit_price,  qty
 from orders o,  orders_items oi , products p 
 where  
 o.orderid = oi.orderid and
 p.sku = oi.sku 
group by o.orderid
having total  < sum(qty* wholesale_cost) 
) q group by q.custid order by count(*) desc


######

select o.orderid, o.customerid,  count(*) as numitems, o.total, 
sum(qty* unit_price) as stdprice, sum(qty * wholesale_cost) as whcost
, p.wholesale_cost, qty
 from orders o,  orders_items oi , products p 
 where  
 o.orderid = oi.orderid and
 p.sku = oi.sku 
group by o.orderid
having total + 1 < sum(qty* wholesale_cost) 


#######

SELECT * FROM orders_items oi, products p where p.sku=oi.sku and unit_price < wholesale_cost

##########



select o.orderid, o.customerid,  count(*) as numitems, o.total, 
sum(qty* unit_price) as stdprice, sum(qty * wholesale_cost) as whcost
, p.wholesale_cost, qty
 from orders o,  orders_items oi , products p 
 where  
 o.orderid = oi.orderid and
 p.sku = oi.sku 
group by o.orderid
having total <> sum(qty* unit_price) 

########




select o.orderid, o.customerid,  o.total, p.wholesale_cost, qty, 
count(*) as numitems,
sum(qty* unit_price) as stdprice, sum(qty * wholesale_cost) as whcost

 from orders o,  orders_items oi , products p 
 where  
 
 o.orderid = oi.orderid and
 p.sku = oi.sku and
o.orderid +1 <= 9016
group by o.orderid
having total - 1 < sum(qty* unit_price) 


##############

select o.orderid, o.customerid,  o.total, p.wholesale_cost, qty, 
count(*) as numitems,
sum(qty* unit_price) as stdprice, sum(qty * wholesale_cost) as whcost

 from orders o,  orders_items oi , products p 
 where  
 
 o.orderid = oi.orderid and
 p.sku = oi.sku and
o.orderid +1 <= 9016
and total - 1 < sum(qty* unit_price) 
group by o.orderid



########


select o.orderid, o.customerid,  o.total, p.wholesale_cost, qty, 
count(*) as numitems,
sum(qty* unit_price) as stdprice, sum(qty * wholesale_cost) as whcost

 from orders o,  orders_items oi , products p 
 where  
 
 o.orderid = oi.orderid and
 p.sku = oi.sku and
o.orderid +1 <= 1016
group by o.orderid



######

select o.orderid, o.customerid,  o.total, p.wholesale_cost, qty, 

qty* unit_price as stdprice, qty * wholesale_cost as whcost

 from orders o,  orders_items oi , products p  # , customers c 
 where  
 # c.customerid = o.customerid and
 o.orderid = oi.orderid and
 p.sku = oi.sku and
o.orderid +1 < 1016


