with stg_promotions as (

    select *
    from {{ ref('stg_promotions') }}

),

final as (

    select
        promotion_sk,
        name,
        start_date,
        end_date,
        description,
        discount_rate,
        is_holiday,

        {{ dbt_utils.generate_surrogate_key(['name']) }} as product_sk

    from stg_promotions

)

select * from final
