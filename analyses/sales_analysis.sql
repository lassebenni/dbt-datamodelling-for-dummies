with
    sales as (select * from `xd-analytics-engineers`.`stroopwafelshop_mart`.`fct_sale`),

    average_sold_per_day as (
            select
                sale_date,
            sum(quantity_sold) as total_sold
        from sales
        group by 1
    ),

    sales_per_employee as (

        select
            employee_name,
            date_diff(max(sale_date), min(sale_date), day) as days,
            sum(quantity_sold) as total_sold
        from sales
        group by 1
    ),

    average_per_day_sold_per_employee as (
        select *, total_sold / days as average_per_day_sold from sales_per_employee
    ),

    sold_per_weekday as (
        select
            sale_weekday,
            sum(quantity_sold) as total_sold,
            count(*) as sales
        from sales
        group by 1
    ),

    sold_per_day as (
        select sale_weekday
        from sales

    ),

    promotions as (select * from `xd-analytics-engineers`.`stroopwafelshop_mart`.`dim_promotion`),

    active_promotions as (

        select *
        from promotions
    ),

    supplies as (select * from `xd-analytics-engineers`.`stroopwafelshop_mart`.`fct_supplies`),

    ingredients_supplied as (
        select 
            weekday,
            sum(initial_quantity) as initial_quantity,
            sum(quantity_supplied) quantity_supplied,
            sum(quantity_used) quantity_used,
            sum(end_quantity) end_quantity
         from supplies
         group by 1
    ),
    reviews as (select * from `xd-analytics-engineers`.`stroopwafelshop_mart`.`dim_review`),

    sunday_reviews as
    (
        select
            date,
            count(*) as n_reviews
        from reviews
        group by 1
        order by 1
    ),

    reviews_by_name as (

        select *
        from reviews
        where description like '%Nina%'
        order by date
    )

select *
from average_sold_per_day
