with stg_sales as (

    select *
    from {{ ref('stg_sales') }}

),

products as  (
    select
        stg_sales.sale_id,
        stg_sales.sale_date,
        stg_sales.sale_time,
        stg_sales.sale_weekday,
        stg_sales.employee_id,
        stg_sales.quantity_sold,
        stg_sales.unit_price,
        stg_sales.total_price

        dim_products.product_id,
        dim_products.product_name,

    from stg_sales
    left join dim_product on stg_sales.product = dim_product.product
)

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

        product_id,
        product_name,

    from stg_sales

)

select * from final
