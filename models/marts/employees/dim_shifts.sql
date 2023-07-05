with stg_shifts as (

    select *
    from {{ ref('stg_shifts') }}

),

dim_employee as (

    select *
    from {{ ref('dim_employee') }}

),

joined as (

    select
        date,
        weekday,
        position,
        employee_id,
        shift_hours

    from stg_shifts
    left join dim_employee
        on stg_shifts.employee_id = dim_employee.employee_id

)

select * from joined
