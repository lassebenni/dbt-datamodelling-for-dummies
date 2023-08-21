select 
    {{ dbt_utils.star(from=ref('fct_sales'), relation_alias='sale', except=[
        "sales_sk", "employee_sk", "product_sk"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_product'), relation_alias='product', prefix='product_', except=[
        "product_sk"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_employee'), relation_alias='employee', except=[
        "employee_sk"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_shift'), relation_alias='shift', except=[
        "employee_sk", "shift_sk"
    ]) }},

from {{ref("fct_sales")}} sale
inner join {{ref("dim_product")}} product ON sale.product_sk = product.product_sk
inner join {{ref("dim_employee")}} employee ON sale.employee_sk = employee.employee_sk
left join {{ref("dim_shift")}} shift ON sale.employee_sk = shift.employee_sk 
    and sale.sale_date = shift.date
    and extract(HOUR FROM sale.sale_time) between shift.start_hour and shift.end_hour
