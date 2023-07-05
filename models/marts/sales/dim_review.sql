with stg_reviews as (

    select *
    from {{ ref('stg_reviews') }}

),

final as (

    select
        review_id,
        description,
        stars,
        date,

    from stg_reviews

)

select * from final
