with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'employees') }}

),

final as (

    select
        cast(employee_id as int64) as employee_id,
        cast(employee_name as string) as employee_name,
        cast(employee_last_name as string) as employee_last_name,
        cast(employee_contact as string) as employee_contact,
        cast(employee_date_of_birth as date) as employee_date_of_birth,
        cast(employee_since as date) as employee_since,
        cast(position as string) as position

    from raw_source

)

select * from final
