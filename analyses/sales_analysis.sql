{# with sales as (


    select * from {{ ref('fct_sales') }}
)
 #}
