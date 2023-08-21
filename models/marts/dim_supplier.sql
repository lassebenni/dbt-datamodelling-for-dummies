with stg_suppliers as (

    select *
    from {{ ref('stg_suppliers') }}

),

final as (

    select
    supplier_name,
    supplier_type,
    supplier_contact,
    supplier_address

    from stg_suppliers

)

select * from final
