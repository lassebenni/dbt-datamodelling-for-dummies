with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'types') }}

),

final as (

    select
        FARM_FINGERPRINT(product_name) as product_id,
        cast(product_name as string) as product_name,
        cast(unit_cost as float64) as unit_cost,
        cast(unit_price as float64) as unit_price,
        cast(ingredients as string) as ingredients

    from raw_source

)

select * from final
