with stg_reviews as (

    select *
    from {{ ref('stg_reviews') }}

),

final as (

    select
        {{ dbt_utils.generate_surrogate_key(['review_id']) }} as review_sk,
        description,
        stars,
        date,

    from stg_reviews

)

select * from final
