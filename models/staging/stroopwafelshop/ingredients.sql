with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'ingredients') }}

),

final as (

    select
        cast(product_name as string) as product_name,
        cast(ingredient as string) as ingredient,
        cast(quantity as float64) as quantity

    from raw_source

)

select * from final
