**Cart Analysis**—more commonly known in data science and retail as **Market Basket Analysis (MBA)**—is a data mining technique used to uncover relationships between products. It looks at the items customers buy together in a single transaction (their "shopping cart") to identify hidden purchasing patterns.
The core idea is simple: **"If a customer buys Item A, how likely are they to also buy Item B?"**
## How it Works: The Association Rule
Market Basket Analysis uses **Association Rules** to establish relationships. A rule is structured as an **"If-Then"** statement:
 * **Antecedent:** The item(s) already in the cart (e.g., *Cereal*).
 * **Consequent:** The item the customer is likely to add next (e.g., *Milk*).
To separate meaningful patterns from random coincidence, algorithms (like the *Apriori algorithm*) measure rules using three core metrics:
### 1. Support
This measures how popular an itemset is, calculated by the percentage of total transactions that contain both items.

### 2. Confidence
This measures how reliable the rule is. It calculates how often item B is bought *given that* item A has already been purchased.

### 3. Lift
This is the most important metric. It tells you how much *more* likely a customer is to buy item B because they bought item A, compared to how often they buy item B randomly anyway.

 * **Lift > 1:** Item A and B are highly associated (a strong rule).
 * **Lift = 1:** The items are independent of each other.
 * **Lift < 1:** The items substitute or repel each other (e.g., buying Pepsi makes someone *less* likely to buy Coca-Cola).
## Real-World Applications
Once a business uncovers these patterns, they can use them to drive revenue in several ways:
 * **Physical Product Placement:** Placing frequently co-purchased items together (like putting chips right next to the salsa) or strategically placing them far apart to force the shopper to walk through other aisles.
 * **E-commerce Recommendation Engines:** Powering Amazon's *"Frequently bought together"* or *"Customers who bought this also bought..."* features.
 * **Product Bundling:** Creating promotional packages (e.g., selling a printer bundled with ink cartridges at a slight discount).
 * **Targeted Marketing:** Sending personalized coupons or email reminders to a customer who bought the antecedent but skipped the consequent (e.g., "We noticed you bought a flashlight, need batteries?").
Are you looking to implement a market basket analysis using a specific tool (like Python/R, SQL, or PowerBI), or are you exploring this for a specific business use case?
