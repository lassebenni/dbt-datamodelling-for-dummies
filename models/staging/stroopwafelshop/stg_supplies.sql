with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'supplies') }}

),

final as (

    select
        {{ dbt_utils.generate_surrogate_key(['ingredient']) }} as supplies_sk,
        cast(date as date) as date,
        cast(weekday as string) as weekday,
        cast(ingredient as string) as ingredient,
        cast(supplier as string) as supplier,
        cast(initial_quantity as float64) as initial_quantity,
        cast(quantity_supplied as float64) as quantity_supplied,
        cast(quantity_used as float64) as quantity_used,
        cast(end_quantity as float64) as end_quantity,
        cast(unit_cost as float64) as unit_cost

    from raw_source

)

select * from final
