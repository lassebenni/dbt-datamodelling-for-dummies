with stg_shifts as (

    select *
    from {{ ref('stg_shifts') }}

),


final as (

    select
        shift_sk,
        date,
        start_hour,
        end_hour,

        {{ dbt_utils.generate_surrogate_key(['date']) }} as date_sk,
        {{ dbt_utils.generate_surrogate_key(['employee_id']) }} as employee_sk

    from stg_shifts
)

select * from final
