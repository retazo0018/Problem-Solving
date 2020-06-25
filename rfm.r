# RFM (Recency, Frequency, Monitary Value) Modal 

# Problem Statement
# Given any sales data of a company, problem is to cluster the customers based on recency, frequency and monitary value.

# Use
# Each customers in a cluster can be targetted with appropriate promotions and advertisements to improve the sales.


setwd("")
library(xlsx)
library(lubridate)
library(dplyr)
library(stringr)
library(corrplot)
library(PerformanceAnalytics)
cust_details <- read.xlsx("Details.xlsx" , sheetIndex = 1)
cust_details$Invoicedate_1 = substr(cust_details$Invoicedate,1,10)
final_Data = cust_details %>%
  group_by(CustomerID) %>%
  summarise(latest_order_date = max(Invoicedate)) %>%
  mutate(recency = as.integer(difftime(ymd("2009-01-01"), (latest_order_date), units = "days")))
final_Data_1 = cust_details %>%
  group_by(CustomerID, Invoicedate_1) %>%
  summarise(no_of_orders =n()) %>%
  group_by(CustomerID) %>%
  summarise(frequency = n())
final_Data_2 = cust_details %>%
  group_by(CustomerID) %>%
  summarise(Monetary_val = sum(Unitprice * Quantity))
final_Data =merge(final_Data, final_Data_1, by ="CustomerID",all.x = TRUE)
final_Data =merge(final_Data, final_Data_2, by ="CustomerID",all.x = TRUE)
boxplot(final_Data$Monetary_val)
boxplot(final_Data$recency)
boxplot(final_Data$frequency)
fun <- function(x){
  quantiles <- quantile(x, c(.05, .95))
  x[ x < quantiles[1] ] <- quantiles[1]
  x[ x > quantiles[2] ] <- quantiles[2]
  x
}
final_Data$recency = fun(final_Data$recency)
final_Data$recency = fun(final_Data$frequency)
