query_templates = {
    "Q1.1": """
select sum(lo_extendedprice * lo_discount) as revenue
from lineorder, date_dim
where
    lo_orderdate = d_datekey
    and d_year = 1993
    and lo_discount between 1 and 3
    and lo_quantity < 25
""",
    "Q1.2": """
select sum(lo_extendedprice * lo_discount) as revenue
from lineorder, date_dim
where
    lo_orderdate = d_datekey
    and d_yearmonthnum = 199401
    and lo_discount between 4 and 6
    and lo_quantity between 26 and 35
""",
    "Q1.3": """
select sum(lo_extendedprice * lo_discount) as revenue
from lineorder, date_dim
where
    lo_orderdate = d_datekey
    and d_weeknuminyear = 6
    and d_year = 1994
    and lo_discount between 5 and 7
    and lo_quantity between 26 and 35
""",
    "Q2.1": """
select
    sum(lo_revenue),
    d_year,
    p_brand
from lineorder, date_dim, part, supplier
where
    lo_orderdate = d_datekey
    and lo_partkey = p_partkey
    and lo_suppkey = s_suppkey
    and p_category = 'MFGR#12'
    and s_region = 'AMERICA'
group by d_year, p_brand
order by d_year, p_brand
""",
    "Q2.2": """
select
    sum(lo_revenue),
    d_year,
    p_brand
from lineorder, date_dim, part, supplier
where
    lo_orderdate = d_datekey
    and lo_partkey = p_partkey
    and lo_suppkey = s_suppkey
    and p_brand between 'MFGR#2221' and 'MFGR#2228'
    and s_region = 'ASIA'
group by d_year, p_brand
order by d_year, p_brand
""",
    "Q2.3": """
select
    sum(lo_revenue),
    d_year,
    p_brand
from lineorder, date_dim, part, supplier
where
    lo_orderdate = d_datekey
    and lo_partkey = p_partkey
    and lo_suppkey = s_suppkey
    and p_brand = 'MFGR#2221'
    and s_region = 'EUROPE'
group by d_year, p_brand
order by d_year, p_brand
""",
    "Q3.1": """
select
    c_nation,
    s_nation,
    d_year,
    sum(lo_revenue) as revenue
from customer, lineorder, supplier, date_dim
where
    lo_custkey = c_custkey
    and lo_suppkey = s_suppkey
    and lo_orderdate = d_datekey
    and c_region = 'ASIA' and s_region = 'ASIA'
    and d_year >= 1992 and d_year <= 1997
group by c_nation, s_nation, d_year
order by d_year asc, revenue desc
""",
    "Q3.2": """
select
    c_city,
    s_city,
    d_year,
    sum(lo_revenue) as revenue
from customer, lineorder, supplier, date_dim
where
    lo_custkey = c_custkey
    and lo_suppkey = s_suppkey
    and lo_orderdate = d_datekey
    and c_nation = 'UNITED STATES'
    and s_nation = 'UNITED STATES'
    and d_year >= 1992 and d_year <= 1997
group by c_city, s_city, d_year
order by d_year asc, revenue desc
""",
    "Q3.3": """
select
    c_city,
    s_city,
    d_year,
    sum(lo_revenue) as revenue
from customer, lineorder, supplier, date_dim
where
    lo_custkey = c_custkey
    and lo_suppkey = s_suppkey
    and lo_orderdate = d_datekey
    and (
        c_city = 'UNITED KI1'
        or c_city = 'UNITED KI5'
    )
    and (
        s_city = 'UNITED KI1'
        or s_city = 'UNITED KI5'
    )
    and d_year >= 1992 and d_year <= 1997
group by c_city, s_city, d_year
order by d_year asc, revenue desc
""",
    "Q3.4": """
select
    c_city,
    s_city,
    d_year,
    sum(lo_revenue) as revenue
from customer, lineorder, supplier, date_dim
where
    lo_custkey = c_custkey
    and lo_suppkey = s_suppkey
    and lo_orderdate = d_datekey
    and (
        c_city = 'UNITED KI1'
        or c_city = 'UNITED KI5'
    )
    and (
        s_city = 'UNITED KI1'
        or s_city = 'UNITED KI5'
    )
    and d_yearmonth = 'Dec1997'
group by c_city, s_city, d_year
order by d_year asc, revenue desc
""",
    "Q4.1": """
select
    d_year,
    c_nation,
    sum(
        lo_revenue
        - lo_supplycost
    ) as profit
from date_dim, customer, supplier,
    part, lineorder
where
    lo_custkey = c_custkey
    and lo_suppkey = s_suppkey
    and lo_partkey = p_partkey
    and lo_orderdate = d_datekey
    and c_region = 'AMERICA'
    and s_region = 'AMERICA'
    and (p_mfgr = 'MFGR#1' or p_mfgr = 'MFGR#2')
group by d_year, c_nation
order by d_year, c_nation
""",
    "Q4.2": """
select
    d_year,
    s_nation,
    p_category,
    sum(lo_revenue - lo_supplycost) as profit
from date_dim, customer, supplier, part, lineorder
where
    lo_custkey = c_custkey
    and lo_suppkey = s_suppkey
    and lo_partkey = p_partkey
    and lo_orderdate = d_datekey
    and c_region = 'AMERICA'
    and s_region = 'AMERICA'
    and (d_year = 1997 or d_year = 1998)
    and (
        p_mfgr = 'MFGR#1'
        or p_mfgr = 'MFGR#2'
    )
group by d_year, s_nation, p_category
order by d_year, s_nation, p_category
""",
    "Q4.3": """select
    d_year,
    s_city,
    p_brand,
    sum(lo_revenue - lo_supplycost) as profit
from date_dim, customer, supplier, part, lineorder
where
    lo_custkey = c_custkey
    and lo_suppkey = s_suppkey
    and lo_partkey = p_partkey
    and lo_orderdate = d_datekey
    and c_region = 'AMERICA'
    and s_nation = 'UNITED STATES'
    and (d_year = 1997 or d_year = 1998)
    and p_category = 'MFGR#14'
group by d_year, s_city, p_brand
order by d_year, s_city, p_brand
""",
    "QV1.1": """
WITH customer_trip_aggregation AS (
    SELECT customer.c_nation
         , part.p_category
         , dates.d_year
         --
         , customer.c_custkey /* Needed b/c we are calculating trips per customer to determine repeat customers */
         --
         , SUM (lineorder.lo_quantity) AS sum_quantity
         , SUM (lineorder.lo_extendedprice) AS sum_sales
         , COUNT (DISTINCT lineorder.lo_orderkey) AS count_distinct_orders
         , COUNT (*) AS count_star
      FROM lineorder
        JOIN customer
      ON lineorder.lo_custkey = customer.c_custkey
        JOIN part
      ON lineorder.lo_partkey = part.p_partkey
        JOIN date_dim dates
      ON lineorder.lo_orderdate = dates.d_datekey
      GROUP BY
           customer.c_nation
         , part.p_category
         , dates.d_year
         --
         , customer.c_custkey
      )
/* Now aggregate the data the rest of the way, removing Customer from GROUP BY */
SELECT c_nation
     , p_category
     , d_year
     --
     , SUM (sum_quantity) AS sum_quantity
     , SUM (sum_sales) AS sum_sales
     , SUM (count_distinct_orders) AS count_distinct_orders /* This is safe b/c an order can only belong to one customer */
     , COUNT (/* DISTINCT */ c_custkey) AS count_distinct_customers /* This is safe, b/c we grouped by all keys + the customer key in the previous query block */
     , COUNT (CASE WHEN count_distinct_orders > 1 THEN c_custkey END) AS count_distinct_repeat_customers
     , SUM (count_star) AS count_star
  FROM customer_trip_aggregation
GROUP BY c_nation
     , p_category
     , d_year
ORDER BY c_nation
     , p_category
     , d_year
   """,
}