with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'shifts') }}

),

final as (

    select
        cast(date as date) as date,
        cast(weekday as string) as weekday,
        cast(position as string) as position,
        cast(employee_name as string) as employee_name,
        cast(employee_id as float64) as employee_id,
        cast(shift_hours as string) as shift_hours

    from raw_source

)

select * from final
