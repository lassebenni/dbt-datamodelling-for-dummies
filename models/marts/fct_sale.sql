with stg_sales as (

    select *
    from {{ ref('stg_sales') }}

),

dim_employee as (

    select
        employee_id,
        employee_name
    from {{ ref('dim_employee') }}

),

joined as  (
    select
        stg_sales.sale_id,
        stg_sales.sale_date,
        stg_sales.sale_time,
        stg_sales.sale_weekday,
        stg_sales.employee_id,
        stg_sales.quantity_sold,
        stg_sales.unit_price,
        stg_sales.total_price,

        dim_employee.employee_name

    from stg_sales
    left join dim_employee on stg_sales.employee_id = dim_employee.employee_id
),

final as (

    select
        sale_id,
        sale_date,
        sale_time,
        sale_weekday,
        employee_id,
        quantity_sold,
        unit_price,
        total_price

    from stg_sales

)

select * from joined
