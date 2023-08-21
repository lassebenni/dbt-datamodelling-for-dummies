with raw_source as (

    select *
    from {{ source('stroopwafelshop', 'reviews') }}

),

final as (

    select
        cast(rating_id as int64) as review_id,
        cast(description as string) as description,
        cast(stars as int64) as stars,
        cast(date as date) as date

    from raw_source

)

select * from final
