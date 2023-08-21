with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'suppliers') }}

),

final as (

    select
        {{ dbt_utils.generate_surrogate_key(['string_field_0']) }} as supplier_sk,
        cast(string_field_0 as string) as supplier_name,
        cast(string_field_1 as string) as supplier_type,
        cast(string_field_2 as string) as supplier_address,
        cast(string_field_3 as string) as supplier_contact

    from raw_source

)

select * from final
