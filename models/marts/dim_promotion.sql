with stg_promotions as (

    select *
    from {{ ref('stg_promotions') }}

),

final as (

    select
        name,
        start_date,
        end_date,
        description,
        discount_rate,
        is_holiday

    from stg_promotions

)

select * from final
