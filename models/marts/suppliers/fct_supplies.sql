with stg_supplies as (

    select *
    from {{ ref('stg_supplies') }}

),

dim_supplier as (

    select *
    from {{ ref('dim_supplier') }}

),

final as (

    select
        date,
        weekday,
        ingredient,
        supplier,
        initial_quantity,
        quantity_supplied,
        quantity_used,
        end_quantity,
        unit_cost

    from stg_supplies
    left join dim_suppliers on stg_supplies.supplier = dim_supplier.supplier_name

)

select * from final
