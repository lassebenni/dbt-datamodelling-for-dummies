with stg_sales as (

    select *
    from {{ ref('stg_sales') }}

),

final as (

    select
        sales_sk,
        sale_time,
        sale_date,
        quantity_sold,
        unit_price,
        total_price,

        {{ dbt_utils.generate_surrogate_key(['employee_id']) }} as employee_sk,
        {{ dbt_utils.generate_surrogate_key(['product']) }} as product_sk

    from stg_sales

)

select * from final
