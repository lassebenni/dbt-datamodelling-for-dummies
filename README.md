## Storyline


Title: "The Stroopwafel Shop Sales Saga: A Tale of Data and Dough"

1. **Introduction and Setup:**
   - We open our story in the heart of Amsterdam, at a local favourite, the "Stroopwafel Delight" shop. However, the shop owner is concerned: there's been a consistent drop in sales, and it seems to coincide with the days when the newest employee, Emma, is working. 

2. **First Clue – Sales Data:**
   - To begin our investigation, we first take a look at the sales data. The raw numbers seem to confirm the owner's suspicion. Every day Emma works, the sales are down. 

3. **Second Clue – Ingredient Delivery:**
   - We then turn our attention to the delivery of ingredients. Perhaps there's a disruption? But the data doesn't support this theory. The same number of ingredients are delivered every day, regardless of who's working.

4. **Third Clue – Customer Reviews:**
   - Our next stop is customer feedback. But even here, the waters are calm. Reviews on the days Emma works are not worse than other days. Customers still love their stroopwafels!

5. **Fourth Clue – Promotions:**
   - We then explore the shop's promotions. Could a special offer on other days be pulling up average sales, making Emma's days look bad? But again, the data doesn't back up this hypothesis. There are no major promotions that would account for such a difference.

6. **A Twist in the Tale – The Competitor:**
   - Just as we're about to suggest a difficult conversation with Emma, a new piece of information comes to light. There's a new competitor in town: "Wafel Wonder", and it operates only on the same days that Emma works. 

7. **Data Validation – Competitor Sales:**
   - To confirm our new suspicion, we acquire some data on the competitor's sales. Lo and behold, their sales surge aligns perfectly with the dip in sales at "Stroopwafel Delight". The competitor is indeed pulling away customers!

8. **Solution – The Sweet Comeback:**
   - With this revelation, we advise the owner on a strategic counter-move. We propose an irresistible promotion on the days Emma works to lure back our loyal stroopwafel fans from "Wafel Wonder".

9. **Conclusion – Triumph of Data:**
   - Armed with this newfound data-driven insight, the shop owner implements the plan. The success of the story underscores the power of comprehensive data analysis, reminding us all never to jump to conclusions until all the data is in. 

And thus, we save both Emma's job and the sales at "Stroopwafel Delight", ensuring that everyone continues to enjoy their favourite stroopwafels. A sweet ending indeed!


### Sources

- https://www.getdbt.com/blog/how-do-you-decide-what-to-model-in-dbt-vs-lookml/ 

- https://www.holistics.io/books/setup-analytics/kimball-s-dimensional-data-modeling/

- 

### More ideas


    Employee Schedule Data:
        This is necessary to know when each employee, particularly Emma, is working.

    Sales Data:
        You need the sales data to observe the drop in sales. This data should be timestamped and detailed enough to allow you to compare sales on different days and at different times.

    Delivery and Stock Data:
        You need data on the deliveries of ingredients to the shop, including when they arrive and in what quantity. This could come from delivery receipts or an inventory management system.

    Customer Review Data:
        You need customer reviews from various platforms where the shop is rated or reviewed. The reviews should be timestamped so that they can be associated with specific days and shifts.

    Promotional and Marketing Data:
        You need data on when each promotion was run, what it involved, and how successful it was. This could come from your own records and sales data.

    Competitor Presence Data:
        You need to know when the competitor started their operations. You can get this data from various sources like news articles, public business records, or their own promotional materials.

    Competitor Sales Data:
        While obtaining this data can be challenging, you might use indirect measures like foot traffic, crowd size, or even online reviews and social media chatter about the competitor. The key is to look for an increase in their business that corresponds to the decrease in yours.

    Customer Behaviour Data (post-promotion):
        After implementing the new promotion, you would need to gather sales data and customer feedback to measure the effectiveness of the promotion.

Each type of data will allow you to verify or discard a possible reason for the drop in sales, leading you step by step closer to the real cause and its solution.


### Dims and Facts

    Employee Schedule Data:
        Fact: Hours worked
        Dimensions: Employee ID, Employee Name, Shift Type (Morning, Evening, Night), Day of the Week

    Sales Data:
        Facts: Total Sales, Number of Transactions, Items per Transaction
        Dimensions: Product ID, Product Category, Time (Hour, Day, Week, Month), Employee ID

    Delivery and Stock Data:
        Facts: Quantity of Ingredients Delivered, Quantity of Ingredients Used
        Dimensions: Ingredient ID, Ingredient Type, Supplier ID, Delivery Date and Time

    Customer Review Data:
        Facts: Review Rating, Number of Reviews
        Dimensions: Customer ID, Review Date and Time, Employee on Duty, Product Reviewed

    Promotional and Marketing Data:
        Facts: Number of Promotions Run, Sales during Promotion, Number of Customers during Promotion
        Dimensions: Promotion ID, Type of Promotion, Duration of Promotion, Product(s) Involved in Promotion

    Competitor Presence Data:
        Fact: Competitor's Opening Date
        Dimensions: Competitor ID, Competitor Name, Competitor Location

    Competitor Sales Data:
        Facts: Estimated Competitor Sales, Competitor Customer Traffic
        Dimensions: Time (Hour, Day, Week, Month), Competitor ID, Event (if any)

    Customer Behaviour Data (post-promotion):
        Facts: Total Sales, Number of Transactions, Items per Transaction, Number of Returning Customers
        Dimensions: Promotion ID, Product ID, Time (Hour, Day, Week, Month), Employee ID

#### Misc Ideas

- Ingredient Supply Data: Tracking data on your ingredients (quantity on hand, cost, supplier, etc.) can help ensure you never run out of what you need to bake your stroopwafels. This can also help with budgeting and cost control.

- Employee Data: Information about your employees, such as hours worked, roles, and performance, can help with staffing decisions and performance management.

- Customer Feedback Data: Collecting and analyzing customer feedback can provide valuable insights into how your products are received and how you might improve.

- Marketing and Advertising Data: If you do any marketing or advertising, tracking this data can help you understand which efforts are most effective at driving sales.

- Sales Trends: In addition to individual sales data, you might want to analyze trends over time. For example, you could look at how sales vary by time of day, day of the week, or season of the year.

- Waste and Efficiency Data: Tracking data on waste (e.g., how many stroopwafels are thrown away without being sold, or how much raw material is wasted) can help you improve your efficiency and reduce costs.

- Website and Online Sales Data: If you sell stroopwafels online, data about your website traffic, online sales, and digital marketing efforts could be very useful.

- Competitor Data: While this can be harder to come by, any information you can gather about your competitors can also provide valuable insights for your business.

- See the sales per day, per employee, to see if certain employees sell more. Perhaps look at the waster per day per employee as well.

- See profitability per location. 

- See waste per location.