with stg_ingredients as (

    select *
    from {{ ref('stg_ingredients') }}

),

final as (

    select
        product_name,
        ingredient,
        quantity

    from stg_ingredients

)

select * from final
