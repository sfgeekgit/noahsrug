SELECT * FROM products where sku like 'COL%'

SELECT count(*), customerid, count(distinct(oi.sku)) as uniitems , count(distinct(o.orderid)) as uniorders FROM orders_items oi, orders o where oi.sku like 'COL%' and oi.orderid=o.orderid group by o.customerid order by count(distinct(oi.sku)) desc

SELECT count(*), o.customerid, count(distinct(oi.sku)) as uniitems , c.name, c.phone, count(distinct(o.orderid)) as uniorders FROM orders_items oi, orders o, customers c  where c.customerid = o.customerid and oi.sku like 'COL%' and oi.orderid=o.orderid group by o.customerid order by count(distinct(oi.sku)) desc

# the end! :)
