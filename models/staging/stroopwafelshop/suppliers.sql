with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'suppliers') }}

),

final as (

    select
        cast(string_field_0 as string) as string_field_0,
        cast(string_field_1 as string) as string_field_1,
        cast(string_field_2 as string) as string_field_2,
        cast(string_field_3 as string) as string_field_3

    from raw_source

)

select * from final
