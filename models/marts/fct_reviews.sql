with stg_reviews as (

    select *
    from {{ ref('stg_reviews') }}

),

final as (

    select
        {{ dbt_utils.generate_surrogate_key(['review_id']) }} as review_sk,
        description,
        stars,

        {{ dbt_utils.generate_surrogate_key(['date']) }} as date_sk

    from stg_reviews

)

select * from final
