with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'promotions') }}

),

final as (

    select
        cast(promotion_name as string) as name,
        cast(start_date as date) as start_date,
        cast(end_date as date) as end_date,
        cast(description as string) as description,
        cast(discount_rate as float64) as discount_rate,
        cast(is_holiday as boolean) as is_holiday

    from raw_source

)

select * from final
