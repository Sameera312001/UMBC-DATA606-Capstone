## Sreesai Sameera Koppana, Spring_2024

# Title and Author
 - **Project Title:** Telecom Customer Churn Prediction
 - Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
 - **Author:** Sreesai Sameera Koppana
 - **Github Profile:** https://github.com/Sameera312001/UMBC-DATA606-Capstone
 - **Final Presentation Link:** 
 - **Youtube Video Link:** 
 - **LinkedIn Profile:** https://www.linkedin.com/in/sameerakoppana/

# Background
- In the dynamic landscape of the telecommunications industry, customer churn presents a formidable challenge for service providers. With an annual churn rate ranging from 15-25 percent, companies face the constant threat of losing customers to competitors in this fiercely competitive market. Despite recognizing the importance of individualized customer retention efforts, the sheer scale of customer bases makes it impractical for firms to dedicate significant resources to each customer. However, by identifying high-risk clients—those likely to churn—companies can strategically focus retention efforts to maximize revenue and minimize costs.

- To effectively combat churn, telecom companies must adopt a holistic approach to understanding customer behavior across multiple touchpoints. By analyzing customer interactions such as store visits, purchase histories, customer service calls, online transactions, and social media engagement, companies can gain valuable insights into potential churn indicators. This comprehensive view enables proactive intervention to mitigate customer attrition and preserve market position.

- Moreover, addressing churn not only safeguards existing market share but also paves the way for growth and profitability. As companies retain more customers within their network, the cost of customer acquisition decreases, and profitability increases. Therefore, reducing client attrition and implementing effective retention strategies emerge as pivotal factors for success in the telecommunications industry. By leveraging predictive analytics and actionable insights, companies can cultivate customer loyalty, drive sustainable growth, and thrive in this competitive landscape.

# Data
- **Data Source:** Kaggle
- **Data Size:** 955 KB
- **Data Shape:** 7044*21
- Each row represents customer
- **Data type:** Numerical and Categorical
- **Target:** Churn

# Data Elements
- **customerID:** Unique identifier for each customer.
- **gender:** Gender of the customer (categorical: "Male" or "Female").
- **SeniorCitizen:** Whether the customer is a senior citizen (binary: 0 for No, 1 for Yes).
- **Partner:** Whether the customer has a partner (binary: "Yes" or "No").
- **Dependents:** Whether the customer has dependents (binary: "Yes" or "No").
- **tenure:** Number of months the customer has been with the company (numerical).
- **PhoneService:** Whether the customer has a phone service (binary: "Yes" or "No").
- **MultipleLines:** Whether the customer has multiple lines (categorical: "Yes", "No", or "No phone service").
- **InternetService:** Type of internet service the customer has (categorical: "DSL", "Fiber optic", or "No").
- **OnlineSecurity:** Whether the customer has online security service (categorical: "Yes", "No", or "No internet service").
- **OnlineBackup:** Whether the customer has online backup service (categorical: "Yes", "No", or "No internet service").
- **DeviceProtection:** Whether the customer has device protection service (categorical: "Yes", "No", or "No internet service").
- **TechSupport:** Whether the customer has tech support service (categorical: "Yes", "No", or "No internet service").
- **StreamingTV:** Whether the customer has streaming TV service (categorical: "Yes", "No", or "No internet service").
- **StreamingMovies:** Whether the customer has streaming movie service (categorical: "Yes", "No", or "No internet service").
- **Contract:** Type of contract the customer has (categorical: "Month-to-month", "One year", or "Two year").
- **PaperlessBilling:** Whether the customer uses paperless billing (binary: "Yes" or "No").
- **PaymentMethod:** Payment method used by the customer (categorical: "Electronic check", "Mailed check", "Bank transfer (automatic)", or "Credit card (automatic)").
- **MonthlyCharges:** Monthly charges for the customer (numerical).
- **TotalCharges:** Total charges for the customer (numerical).
- **Churn:** Whether the customer churned (binary: "Yes" or "No").