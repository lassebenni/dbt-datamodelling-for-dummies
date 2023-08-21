with
    raw_source as (select * from {{ source("stroopwafelshop", "shifts") }}),

    final as (

        select
            {{ dbt_utils.generate_surrogate_key(["weekday", "shift_hours"]) }}
            as shift_sk,
            cast(date as date) as date,
            cast(weekday as string) as weekday,
            cast(position as string) as position,
            cast(employee_name as string) as employee_name,
            cast(employee_id as float64) as employee_id,
            safe_cast(
                split(split(shift_hours, '-')[offset(0)], ':')[offset(0)] as int64
            ) as start_hour,
            safe_cast(
                split(split(shift_hours, '-')[offset(1)], ':')[offset(0)] as int64
            ) as end_hour

        from raw_source

    )

select *
from final
