


select name, phone, * from orders o, customers c  where o.customerid = c.customerid and orderid in 
(73257, 73256, 126233, 126236, 107650, 107656) order by orderid


# Jeremy Burch	516-544-4187	73256	9931

select * from orders where orderid in (73257, 73256)

select * from orders where orderid in (126233, 126236)

107650, 107656

select q.desc, p.desc, q.orderid, oi.*, q.*, p.desc from orders_items oi, products p,
(SELECT o.orderid as oid, oi.* , p.desc, p.sku FROM orders o, orders_items oi, products p
where o.customerid = 8884 and oi.orderid = o.orderid and p.sku=oi.sku 
) q
where  q.orderid < oi.orderid
and q.orderid > oi.orderid - 6
and p.sku=oi.sku
and substr(p.desc,1,4) = substr(q.desc,1,4)



# yeah, its gotta be -1

select q.desc, p.desc, q.orderid, oi.*, q.*, p.desc from orders_items oi, products p,
(SELECT o.orderid as oid, oi.* , p.desc, p.sku FROM orders o, orders_items oi, products p
where o.customerid = 8884 and oi.orderid = o.orderid and p.sku=oi.sku 
) q
where  q.orderid in (oi.orderid -1,oi.orderid -2,oi.orderid -3,oi.orderid -4)
and p.sku=oi.sku
and substr(p.desc,1,4) = substr(q.desc,1,4)



### why is it oderid +1, I would think -1...

select q.desc, p.desc, q.orderid, oi.*, q.*, p.desc from orders_items oi, products p, 
(SELECT o.orderid as oid, oi.* , p.desc, p.sku FROM orders o, orders_items oi, products p
where o.customerid = 8884 and oi.orderid = o.orderid and p.sku=oi.sku and p.desc like '%(%'
) q
where oi.orderid +1 = q.orderid
and p.desc like '%(%'  and p.sku=oi.sku
and substr(p.desc,1,4) = substr(q.desc,1,4)


### select * from orders where orderid in (73257, 73256)


#####

select oi.*, q.* from orders_items oi, (SELECT o.orderid as oid, oi.* , p.desc, p.sku FROM orders o, orders_items oi, products p
where o.customerid = 8884 and oi.orderid = o.orderid and p.sku=oi.sku
) q
where oi.orderid -1 = q.orderid

#######




select oi.*, q.* from orders_items oi, (SELECT o.orderid as oid, oi.* , p.desc, p.sku FROM orders o, orders_items oi, products p
where o.customerid = 8884 and oi.orderid = o.orderid and p.sku=oi.sku
) q
where oi.orderid -1 = q.orderid

#####

SELECT o. FROM orders o, orders_items oi where o.customerid = 8884 and oi.orderid = o.orderid


####

select oi.*, q.* from orders_items oi, (SELECT o.orderid as oid, oi.* , p.desc, p.sku FROM orders o, orders_items oi, products p 
where o.customerid = 8884 and oi.orderid = o.orderid and p.sku=oi.sku
) q
where oi.orderid -1 = q.orderid and q.sku=oi.sku

