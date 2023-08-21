with stg_products as (

    select *
    from {{ ref('stg_products') }}

),

final as (

    select
        product_sk,
        name,
        round(unit_cost, 2) as unit_cost,
        round(unit_price, 2) as unit_price

    from stg_products

)

select * from final
