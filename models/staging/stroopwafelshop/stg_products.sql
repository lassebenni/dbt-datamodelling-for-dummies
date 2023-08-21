with
    raw_source as (select * from {{ source("stroopwafelshop", "types") }}),

    final as (

        select
            {{ dbt_utils.generate_surrogate_key(["product_name"]) }} as product_sk,
            cast(product_name as string) as name,
            cast(unit_cost as float64) as unit_cost,
            cast(unit_price as float64) as unit_price

        from raw_source

    )

select *
from final
