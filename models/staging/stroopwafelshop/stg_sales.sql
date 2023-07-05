with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'sales') }}

),

final as (

    select
        cast(transaction_id as int64) as transaction_id,
        cast(date as date) as date,
        cast(time as time) as time,
        cast(weekday as string) as weekday,
        cast(employee_id as int64) as employee_id,
        cast(product as string) as product,
        cast(quantity_sold as float64) as quantity_sold,
        cast(unit_price as float64) as unit_price,
        cast(total_price as float64) as total_price

    from raw_source

)

select * from final
