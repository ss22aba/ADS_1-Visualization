#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:53:23 2022

@author: asus
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#imported modules
import pandas as pd
import matplotlib.pyplot as plt


# function for line plot
def linePlot() :
    """
     Function for the line plot. It plots the maximum, minimum and average 
     
     temperatures of 8 different cities.
    """
# Plot the figure
    plt.figure(figsize = (10,12))
# plot the temperatures of different cities.
    plt.plot(top_10["Station.City"], top_10["Data.Temperature.Max Temp"], 
             label = "Data.Temperature.Max Temp")
    plt.plot(top_10["Station.City"], top_10["Data.Temperature.Min Temp"], 
             label = "Data.Temperature.Min Temp")
    plt.plot(top_10["Station.City"], top_10["Data.Temperature.Avg Temp"], 
             label = "Data.Temperature.Avg Temp")

# set labels and show the legend
    plt.xlabel("Station.City")
    plt.ylabel("Data.Temperature")
    plt.legend()
    plt.title("Line plot showing temperatures")
# saving figure
    plt.savefig("linegraph.png")
    plt.show()
    

# function for bar chart
def barChart() :
    """
    Function for the bar chart for plotting the maximum and minimum temperature
    """
# Plot the figure
    plt.figure(figsize = (10,10))
# plot the temperatures of different cities.
    plt.bar(top_10["Station.City"], top_10["Data.Temperature.Max Temp"], 
            label = "Data.Temperature.Max Temp", alpha = 1.0, color = 'orange')
    plt.bar(top_10["Station.City"], top_10["Data.Temperature.Min Temp"], 
            label = "Data.Temperature.Min Temp", alpha=0.6, color = 'yellow')
   
# set labels and show the legend    
    plt.xlabel("Station.City")
    plt.ylabel("Data.Temperature")
    plt.title("Bar graph showing minimum and maximum temperature")
# saving figure
    plt.savefig("barchart_png")
    plt.legend()
    plt.show()
    

# function for the box plot
def boxPlot() :
    """
    Function for the box plot. It plots the maximum, minimum and average 
    
    temperatures of 8 different cities.
    """
# plot the figure
    plt.figure(figsize = (8,9))
# plot the temperatures of different cities.
    plt.boxplot([top_10["Data.Temperature.Max Temp"],
                 top_10["Data.Temperature.Min Temp"],
                 top_10["Data.Temperature.Avg Temp"]], 
                labels = ["Data.Temperature.Max Temp",
                          "Data.Temperature.Min Temp",
                          "Data.Temperature.Avg Temp"])
 
# set labels and show the legend
    plt.xlabel("Station.City")
    plt.ylabel("Data.Temperature")
    plt.title("Box plot showing temperatures")
# saving figure
    plt.savefig("boxfig_png")
    plt.legend()
    plt.show()
 

# read file into dataframe and print
df = pd.read_csv("weather.csv")
print(df)

# data selected from the dataset
top_10 = df[0:8]

#Calling the functions for plotting line plot, bar chart and box plot.
linePlot()
barChart()
boxPlot()


#https://corgis-edu.github.io/corgis/csv/weather/ : csv data