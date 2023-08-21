select 
    {{ dbt_utils.star(from=ref('fct_supplies'), relation_alias='supplies', except=[
        "supplies_sk", "supplier_sk", "ingredient_sk"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_ingredient'), relation_alias='ingredient', except=[
        "ingredient_sk", "product_sk"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_product'), relation_alias='product', prefix='product_', except=[
        "product_sk"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_supplier'), relation_alias='supplier', except=[
        "supplier_sk"
    ]) }}

from {{ref("fct_supplies")}}  supplies
inner join {{ref("dim_supplier")}} supplier ON supplies.supplier_sk = supplier.supplier_sk
inner join {{ref("dim_ingredient")}} ingredient ON supplies.ingredient_sk = supplies.ingredient_sk
inner join {{ref("dim_product")}} product ON ingredient.product_sk = product.product_sk
