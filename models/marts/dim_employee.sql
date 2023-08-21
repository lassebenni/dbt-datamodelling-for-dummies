with stg_employee as (

    select *
    from {{ ref('stg_employees') }}

),

final as (

    select
        employee_sk,
        employee_name,
        employee_last_name,
        employee_contact,
        employee_date_of_birth,
        employee_since,
        position

    from stg_employee

)

select * from final
