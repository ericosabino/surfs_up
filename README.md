# Surf's Up

## Overview of the Analysis

This analysis consists of gathering the temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

With that in mind, two queries were used on the given data base to find the results.Queries:

`june_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==6).all()`

`december_temps = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==12).all()`

## Results

By querying the data, transforming the results in data frames and describing the statistical data for the temperature, the results found are below:

June Temperatures | December Temperatures
:-------------------------:|:-------------------------:
![](/Resources/June_Temps.png)  |  ![](/Resources/December_Temps.png)

Some results are listed below:
* The average temp in June is 75F while in December it is 71F, which means it's not very cold in December and business can be ran at that time, on average.
* The min temp is 64F in June and 56F in December, which indicates a potential drop in ice cream sales and surfers frequency in the colder days.
* The max temp is 85F in June and 83F in December, which indicates a great weather for both surfing and ince cream sales in both months.


## Summary

Based only on the weather data, it looks that both June and December are good months to make business in Surf and Ice Cream in Oahu, with an execption for the cold days in December. In order to expand this analysis, additional data could be gathered:

1. Wind: wind data could determine how the wind affects the variance of the temperature for these months.

2. Precipitation: this would give more insights on the number of cloudy days in these months, which could also influence sales.

Besides weather information, I would also collect tourism data to understand what are the periods of the year which there is an increase in the number of tourists, or even the number of bathers on the beach.