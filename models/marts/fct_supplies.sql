with stg_supplies as (

    select *
    from {{ ref('stg_supplies') }}

),

final as (

    select
        supplies_sk,
        initial_quantity,
        quantity_supplied,
        quantity_used,
        end_quantity,
        unit_cost,
        date,

        {{ dbt_utils.generate_surrogate_key(['supplier']) }} as supplier_sk,
        {{ dbt_utils.generate_surrogate_key(['ingredient']) }} as ingredient_sk

    from stg_supplies
)

select * from final
