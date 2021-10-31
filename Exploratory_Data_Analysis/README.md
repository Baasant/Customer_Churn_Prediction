## Conclusion
 **Exploratory Data Analysis**

EDA helps us to understand the data set and its relations with each other 
By making EDA at this data I find out that 

**By looking at the data**
1-9.3% of clint will churn 

2_49.6% of customers are living in the area code area_code_415.

3_most of the client didn't have an international plan

4_73.8% of clients has no voice plan 

5-14.1%  churn 

6-number_customer_service_calls,total_intl_calls,number_vmail_messages have no normal distribution and will convert it to normal 

After exploring the data to find the highest period of time the churn happens 

**for numerical data**

I found out that 
the account length is between 90 to 130 has a high value of churn 

1-More churn rate when the number_vamil_messages is 0

2-More churn rate when the total day minutes between 210 to 300 

3-ore churn rate when the total day calls is 85 to 120

4-More churn rate when the total day charge between  45 to 50

5-More churn rate when the total day charge between  160 to 200

6-More churn rate when the total_eve_call between  60 to 120

7-More churn rate when the total_eve_charge between  15 to 18

8-Churn rate is high when the total_night_minutes is lies between 190 to 200 min

9-Churn rate is high when the total_night_calls is lies between 90 to 115

10-churn rate is high when total_night_charge lies between 7.5 to 10.

11-churn rate is high when total_int_min lies between 7 to 12.

12-churn rate is high when total_int_claas are,4,5

13-churn rate is high when the total international charge is 2.5 to 3.

14-churn rate is high when the number of customer service calls is 1.

After exploring the data we need to handle it to five to the model 
By converting categorical data to numerical and normalized categorical data and remove outliers 
 
**Categorical data**

converting the area_code to a numerical variable using a one-hot encoder
Convert yes, no to 1,0
Handling the state feature using HashingEncoder

 **After handeling the data**
 
 save features and labels data to csv files 
 

