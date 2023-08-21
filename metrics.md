To determine the quantity of ingredients required for the production of a stroopwafel and compare it with the daily delivered quantities, you can consider the following approach:

### Metrics:

1. **Required Ingredients per Stroopwafel**: This will give you an idea of the quantity of each ingredient required to make a single stroopwafel. This metric can be derived from the `stg_ingredients` table.

2. **Daily Stroopwafel Production Goal**: Establish a goal or forecast for how many stroopwafels you aim to produce daily.

3. **Total Daily Ingredients Required**: Multiply the Required Ingredients per Stroopwafel by the Daily Stroopwafel Production Goal. This will provide the total quantity of each ingredient required daily.

4. **Daily Ingredients Delivered**: This metric can be extracted from the `stg_supplies` table to determine how much of each ingredient is supplied daily.

5. **Daily Ingredients Utilized**: This will represent how much of the delivered ingredients are actually used in production daily.

6. **Remaining Inventory**: This metric will consider the ingredients already in stock plus the daily delivered ingredients minus the daily utilized ingredients. 

### Visualization and Insights:

- **Stacked Bar Chart**: For each ingredient, use a stacked bar where:
  - One segment represents the daily required quantity.
  - The second segment represents the daily delivered quantity.
  
  If the delivered segment consistently exceeds the required segment, it indicates overstocking. Conversely, if the required segment is higher, it suggests potential shortages.

- **Line Chart**: 
  - One line represents the cumulative required ingredients over time.
  - The second line represents the cumulative delivered ingredients over time.
  
  This will help in visualizing trends in ingredient requirements versus deliveries.

- **Heatmap**: Show a grid for each day (columns) against each ingredient (rows). The color intensity represents the difference between required and delivered ingredients. Deep red could indicate a big shortage, deep green could indicate overstocking, and neutral colors could represent a balanced state.

### Insights:

- If the Daily Ingredients Delivered consistently exceeds the Total Daily Ingredients Required, you may be overstocking, leading to potential wastage or increased holding costs.

- If the Daily Ingredients Delivered is consistently less than the Total Daily Ingredients Required, it could lead to production halts due to ingredient shortages.

- Monitor the Remaining Inventory metric. If it grows consistently, it indicates that you're not using ingredients as fast as they're being delivered.

- Seasonal or periodic promotions (from `stg_promotions` table) might lead to increased production. Make sure to adjust the Daily Stroopwafel Production Goal during such times and assess the impact on ingredient requirements.

By carefully monitoring these metrics and visualizations, you can optimize ingredient delivery schedules, reduce wastage, and ensure smooth production operations.

Based on the tables you've provided, there are numerous metrics and insights you can derive to better understand and optimize the operations of your stroopwafel shop. Here's a list segmented by business aspect:

### 1. **Sales & Profitability**:

- **Daily/Monthly Sales Volume**: Track the number of stroopwafels sold per day or month.
  
- **Sales Revenue**: Total revenue from stroopwafel sales. This could be further broken down by employee to understand individual performance.

- **Gross Profit**: Revenue minus the cost of goods sold (ingredients and other direct costs).

- **Promotion Effectiveness**: Compare sales during promotional periods vs. non-promotional periods to gauge the success of various promotions.

### 2. **Supply & Inventory**:

- **Ingredient Utilization Rate**: Percentage of delivered ingredients that get used in production.

- **Stock Turnover**: How often the stock or inventory is sold or used in a given period.

- **Wastage Rate**: Quantity of ingredients delivered minus ingredients used in production and the end quantity.

- **Supplier Reliability Index**: How often suppliers deliver on time, the right quantity, and the right quality.

### 3. **Employee Metrics**:

- **Employee Sales Performance**: Stroopwafels sold per employee or revenue generated per employee.

- **Shift Efficiency**: Track sales or production numbers against different shifts to identify the most efficient times.

- **Employee Tenure vs. Performance**: Does longer tenure correlate with better sales or efficiency?

### 4. **Product & Customer Feedback**:

- **Average Review Score**: From the `stg_reviews` table, get an average star rating for your products.

- **Feedback Trends**: Are there common themes in feedback? E.g., are many customers pointing out a specific ingredient or taste they love/hate?

### 5. **Operational Efficiency**:

- **Time to Serve**: Difference between sale time and the start of the shift can give insights into how quickly stroopwafels are being served after the start of a shift.

- **Peak Sale Times**: Identify peak times during the day for sales, helping in shift planning and stock preparation.

### 6. **Promotions & Marketing**:

- **Promotion Uptake**: How many sales occur with a promotion applied? This can be analyzed further by looking at specific types of promotions.

- **Holiday Sales Spike**: Using the `is_holiday` field, analyze if there's a significant increase in sales during holidays.

### 7. **Supplier Management**:

- **Supplier Cost Analysis**: Compare unit costs among different suppliers to find opportunities for cost-saving.

- **Supplier Diversity**: Are you too dependent on one supplier? A diversified supplier base can reduce supply chain risks.

### 8. **Product Insights**:

- **Ingredient-Product Mapping**: Understand which products use which ingredients the most. If an ingredient is in shortage, which products are affected the most?

- **Cost vs. Price Analysis**: For each product, compare the unit cost (sum of ingredient costs) to its selling price to determine profitability.

### Visualization Ideas:

- **Dashboards**: Create comprehensive dashboards for sales, employee performance, supplier metrics, and customer feedback.

- **Trend Lines**: For sales, reviews, and supplies, show trend lines to spot upward or downward movements.

- **Heatmaps**: Visualize peak sale times, employee efficiency, or ingredient usage using heatmaps.

Using these metrics, insights, and visualizations, you can better understand the intricacies of your business operations, make informed decisions, and optimize for profitability and growth.

