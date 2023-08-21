```mermaid
---
title: Sample ERD
---
erDiagram
  "MODEL.STROOPWAFELSHOP.STG_PRODUCTS" {
    string product_sk
    string name
    float64 unit_cost
    float64 unit_price
  }
  "MODEL.STROOPWAFELSHOP.STG_INGREDIENTS" {
    string ingredient_sk
    string product_name
    string ingredient
    float64 quantity
  }
  "MODEL.STROOPWAFELSHOP.STG_SUPPLIES" {
    string supplies_sk
    date date
    string weekday
    string ingredient
    string supplier
    float64 initial_quantity
    float64 quantity_supplied
    float64 quantity_used
    float64 end_quantity
    float64 unit_cost
  }
  "MODEL.STROOPWAFELSHOP.STG_SUPPLIERS" {
    string supplier_sk
    string supplier_name
    string supplier_type
    string supplier_address
    string supplier_contact
  }
  "MODEL.STROOPWAFELSHOP.STG_PROMOTIONS" {
    string promotion_sk
    string name
    date start_date
    date end_date
    string description
    float64 discount_rate
    bool is_holiday
  }
  "MODEL.STROOPWAFELSHOP.STG_REVIEWS" {
    int64 review_id
    string description
    int64 stars
    date date
  }
  "MODEL.STROOPWAFELSHOP.STG_EMPLOYEES" {
    string employee_sk
    string employee_name
    string employee_last_name
    string employee_contact
    date employee_date_of_birth
    date employee_since
    string position
  }
  "MODEL.STROOPWAFELSHOP.STG_SHIFTS" {
    string shift_sk
    date date
    string weekday
    string position
    string employee_name
    float64 employee_id
    int64 start_hour
    int64 end_hour
  }
  "MODEL.STROOPWAFELSHOP.STG_SALES" {
    string sales_sk
    date sale_date
    time sale_time
    string sale_weekday
    int64 employee_id
    string product
    float64 quantity_sold
    float64 unit_price
    float64 total_price
  }
  "MODEL.STROOPWAFELSHOP.DIM_PRODUCT" {
    string product_sk
    string name
    float64 unit_cost
    float64 unit_price
  }
  "MODEL.STROOPWAFELSHOP.DIM_EMPLOYEE" {
    string employee_sk
    string employee_name
    string employee_last_name
    string employee_contact
    date employee_date_of_birth
    date employee_since
    string position
  }
  "MODEL.STROOPWAFELSHOP.DIM_SUPPLIER" {
    string supplier_sk
    string supplier_name
    string supplier_type
    string supplier_contact
    string supplier_address
  }
  "MODEL.STROOPWAFELSHOP.DIM_PROMOTION" {
    string promotion_sk
    string name
    date start_date
    date end_date
    string description
    float64 discount_rate
    bool is_holiday
    string product_sk
  }
  "MODEL.STROOPWAFELSHOP.DIM_INGREDIENT" {
    string ingredient_sk
    string ingredient
    float64 quantity
    string product_sk
  }
  "MODEL.STROOPWAFELSHOP.DIM_DATE" {
    unknown date_sk
    unknown date_day
    unknown prior_date_day
    unknown next_date_day
    unknown prior_year_date_day
    unknown prior_year_over_year_date_day
    unknown day_of_week
    unknown day_of_week_iso
    unknown day_of_week_name
    unknown day_of_week_name_short
    unknown day_of_month
    unknown day_of_year
    unknown week_start_date
    unknown week_end_date
    unknown prior_year_week_start_date
    unknown prior_year_week_end_date
    unknown week_of_year
    unknown iso_week_start_date
    unknown iso_week_end_date
    unknown prior_year_iso_week_start_date
    unknown prior_year_iso_week_end_date
    unknown iso_week_of_year
    unknown prior_year_week_of_year
    unknown prior_year_iso_week_of_year
    unknown month_of_year
    unknown month_name
    unknown month_name_short
    unknown month_start_date
    unknown month_end_date
    unknown prior_year_month_start_date
    unknown prior_year_month_end_date
    unknown quarter_of_year
    unknown quarter_start_date
    unknown quarter_end_date
    unknown year_number
    unknown year_start_date
    unknown year_end_date
  }
  "MODEL.STROOPWAFELSHOP.FCT_REVIEWS" {
    string review_sk
    string description
    int64 stars
    date date
    unknown date_sk
  }
  "MODEL.STROOPWAFELSHOP.DIM_SHIFT" {
    string shift_sk
    date date
    string weekday
    int64 start_hour
    int64 end_hour
    string employee_sk
    unknown date_sk
  }
  "MODEL.STROOPWAFELSHOP.FCT_SUPPLIES" {
    string supplies_sk
    date date
    string weekday
    float64 initial_quantity
    float64 quantity_supplied
    float64 quantity_used
    float64 end_quantity
    float64 unit_cost
    string supplier_sk
    string ingredient_sk
    unknown date_sk
  }
  "MODEL.STROOPWAFELSHOP.FCT_SALES" {
    string sales_sk
    date sale_date
    time sale_time
    string sale_weekday
    float64 quantity_sold
    float64 unit_price
    float64 total_price
    string employee_sk
    string product_sk
  }
  "MODEL.STROOPWAFELSHOP.FCT_SALES" }|--|| "MODEL.STROOPWAFELSHOP.DIM_EMPLOYEE": employee_sk
  "MODEL.STROOPWAFELSHOP.FCT_SALES" }|--|| "MODEL.STROOPWAFELSHOP.DIM_PRODUCT": product_sk
```