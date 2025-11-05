Problem Statement

Electric Vehicle Charging Prediction

As electric-vehicle (EV) infrastructure expands, large datasets are collected from public and private charging stations. However, this raw data is often unstructured, contains missing values, and lacks uniform formatting. Without proper cleaning and analysis, it becomes difficult to understand real charging behavior or support energy-management decisions.

The focus  is to transform the raw EV-charging dataset into a usable form through data cleaning and exploratory data analysis (EDA). Cleaning the dataset ensures that inaccurate or incomplete records are corrected or removed. EDA then helps uncover hidden usage trends such as demand fluctuations across days, typical charging durations, and variations in energy consumption.

This stage is essential to build a reliable foundation for predictive modeling in upcoming weeks.

✅ Objectives

✔ Clean the dataset for quality and consistency
✔ Convert timestamps into usable formats
✔ Generate new time-based features (Hour, Day)
✔ Explore and visualize charging behavior
✔ Understand patterns in energy consumption
✔ Prepare final structured data for Week-3 modeling

📊 Dataset Used

Name: Electric Vehicle Charging Dataset
Source: Kaggle
Description:
A structured dataset containing EV charging session records, including start time, end time, session duration, and energy consumed. Used to analyze user demand and charging patterns.

Approx. Records: ~1,000+
Format: CSV

🔍 Key Attributes
Feature	Description
StartTime	Time when charging began
EndTime	Time when charging ended
ChargingDuration	Session duration (hrs/mins)
EnergyConsumption	Energy consumed (kWh)
DayNumber / Day	Day of week for pattern recognition
StationID	Charging location
Hour (derived)	Hour extracted from timestamp

✅ Data Pre-processing

Checked and removed missing/invalid records

Standardized time fields into datetime format

Eliminated duplicate entries

Extracted new features (Hour, Day)

Exported cleaned dataset for model training

✅ Exploratory Data Analysis

Studied distribution of charging duration

Visualized energy consumption spread

Identified peak charging time by hour

Compared weekday vs weekend usage

Analyzed energy vs duration relationship

📈 Key Findings

Evening hours show higher charging demand

Weekdays have more active charging sessions

Longer charging durations generally mean more energy usage

Data is now uniform, consistent, and model-ready

🚀 Outcome

 the dataset has been:
✔ Cleaned
✔ Transformed
✔ Enriched with new features
✔ Analyzed for insights
