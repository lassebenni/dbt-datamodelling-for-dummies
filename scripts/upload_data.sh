#!/bin/bash

ls data | grep csv | xargs -I % echo 

bq load --replace --autodetect --source_format=CSV stroopwafelshop.supplies data/supplies.csv
bq load --replace --autodetect --source_format=CSV stroopwafelshop.ingredients data/ingredients.csv
bq load --replace --autodetect --source_format=CSV stroopwafelshop.promotions data/promotions.csv
bq load --replace --autodetect --source_format=NEWLINE_DELIMITED_JSON stroopwafelshop.reviews data/reviews.json
bq load --replace --autodetect --source_format=CSV stroopwafelshop.sales data/sales.csv
bq load --replace --autodetect --source_format=CSV stroopwafelshop.shifts data/shifts.csv
bq load --replace --autodetect --source_format=CSV stroopwafelshop.suppliers data/suppliers.csv
bq load --replace --autodetect --source_format=CSV stroopwafelshop.supplies data/supplies.csv
bq load --replace --autodetect --source_format=CSV stroopwafelshop.types data/types.csv
bq load --replace --autodetect --source_format=CSV stroopwafelshop.employees data/employees.csv