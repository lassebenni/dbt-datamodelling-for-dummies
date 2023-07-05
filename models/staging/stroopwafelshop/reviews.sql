with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'reviews') }}

),

final as (

    select
        cast(description as string) as description,
        cast(stars as int64) as stars,
        cast(date as date) as date,
        cast(rating_id as int64) as rating_id

    from raw_source

)

select * from final
