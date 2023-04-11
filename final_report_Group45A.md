### **1. Introduction**

This project looked at how people in Washington used rental bikes from 2011 to 2012. The source data is a large dataset that includes weather information such as temperature, humidity, and wind speed for each day from 2011 to 2012, as well as whether it was a weekday, holiday, etc., and the number of casual users, registered users, and total users who used the rental bikes that day. My research question is how weather conditions affect the use of rental bikes by both casual and registered users.

The reason I am interested in this topic is that renting a bike is something that is common in everyone's life, especially in the country where I was born. In China, renting a bike had quickly become a popular way to get around. I was curious about what factors influenced people in Washington to choose rental bikes.




### **2. Exploratory Data Analysis**
1. I used heatmap to initially look at the relationships between my variables to see if they were positively or negatively correlated
![EDA1](/images/FinalReport-EDA1.png)

2. I used pairplots to further observe the relationship between my variables of interest: temperature, humidity, wind speed, weather conditions and the number of users in each of the three categories
![EDA1](/images/FinalReport-EDA2.png)


### **3. Question and Results**

My research question is to find the conditional preferences of two categories of users, CASUAL, REGISTERED, and all users (that is, the sum of these two categories) in using bike-sharing, and to analyze how weather conditions affect their preferences in terms of humidity, wind speed, and temperature.

**3.1 Weather condition** 

![Q1](/images/FinalReport-Q1.png)

 In terms of approximate weather conditions, all users prefer to use rental bikes in weather condition 1, followed by condition 2 and then condition 3. No one like to travel in weather condition 4.

**3.2 Temperature, Wind speed and Humidity** 
![Q4](/images/FinalReport-total.png)

As can be seen from the graph, from all users, people prefer to travel on non-rainy days when the temperature is higher and wind speed is not a determining factor.This may be because registered users make up the majority of users and therefore influence the preference of total users.



**(1) Casual users and Temperature, Wind speed and Humidity** 
![Q2](/images/FinalReport-Q2.png)

   As can be seen from the graph, in terms of casual users, people prefer to travel on non-rainy days when the temperature is higher, but at the same time prefer low wind speed.


**(2) Registered users and Temperature, Wind speed and Humidity**

![Q3](/images/FinalReport-Q3.png)
As can be seen from the graph, in terms of registered users, people prefer to travel on non-rainy days when the temperature is higher and wind speed is not a determining factor.





### **4. Summary**
For all types of users, people prefer weathercondition 1 and non-rainy days, and prefer to travel when the temperature is higher.

For casual users, they prefer low wind speed, but for registered users, wind speed is not a significant influencing factor.

From the project, through EDA I learned how to initially filter the data to get what I wanted and look at the connections between the data, then by visualizing the data, I learned more about how to create appropriate charts and use the seaborn library charts to interpret the data and answer my research questions.








