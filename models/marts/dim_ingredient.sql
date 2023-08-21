with stg_ingredients as (

    select *
    from {{ ref('stg_ingredients') }}

),

final as (

    select
        ingredient_sk,
        ingredient,
        quantity,

    {{ dbt_utils.generate_surrogate_key(['product_name']) }} as product_sk

    from stg_ingredients

)

select * from final
