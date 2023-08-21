with stg_products as (

    select *
    from {{ ref('stg_products') }}

),

final as (

    select
        product_sk,
        product_name,
        unit_cost,
        unit_price

    from stg_products

)

select * from final
