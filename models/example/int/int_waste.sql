
def generate_waste_data(start_date, end_date, df_stroopwafels_made, df_sales_data):
    waste = []

    for single_date in pd.date_range(start=start_date, end=end_date):
        # The number of stroopwafels sold is based on the ingredient that ran out first
        stroopwafels_made = df_stroopwafels_made[
            df_stroopwafels_made["date"] == str(single_date.date())
        ]["made"].values[0]

        # The number of stroopwafels sold is a bit less than the number possible
        stroopwafels_sold = df_sales_data[
            df_stroopwafels_made["date"] == str(single_date.date())
        ]["made"].values[0]

        sale_info = {
            "date": single_date.strftime("%Y-%m-%d"),
            "weekday": single_date.day_name(),
            "stroopwafels_made": stroopwafels_made,
            "stroopwafels_sold": stroopwafels_sold,
        }
        waste.append(sale_info)

    # Convert the list of dictionaries to a DataFrame
    df_sales = pd.DataFrame(waste)
    return df_sales