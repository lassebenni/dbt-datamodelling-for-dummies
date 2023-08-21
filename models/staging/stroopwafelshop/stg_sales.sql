with
    raw_source as (select * from {{ source("stroopwafelshop", "sales") }}),

    final as (

        select
            {{ dbt_utils.generate_surrogate_key(["transaction_id"]) }} as sales_sk,
            cast(date as date) as sale_date,
            cast(time as time) as sale_time,
            cast(weekday as string) as sale_weekday,
            cast(employee_id as int64) as employee_id,
            cast(product as string) as product,
            cast(quantity_sold as float64) as quantity_sold,
            cast(unit_price as float64) as unit_price,
            cast(total_price as float64) as total_price

        from raw_source

    )

select *
from final
