# -*- coding: utf-8 -*-
"""uavp1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_UvRsNEITB7WuNUVIj05uQ_NGy3yB6_d
"""

import numpy as np
import pandas as pd

# Učitavanje podataka
data = pd.read_csv('dataset.csv')

# Izdvajanje AQI vrijednosti
aqi_values = data['AQI Value']

# 1. Izračun prosječnog AQI
average_aqi = np.mean(aqi_values)
print("Prosječni AQI:", average_aqi)

# 2. Pronalaženje maksimalnog AQI
max_aqi = np.max(aqi_values)
print("Maksimalni AQI:", max_aqi)

# 3. Pronalaženje minimalnog AQI
min_aqi = np.min(aqi_values)
print("Minimalni AQI:", min_aqi)

# 4. Računanje standardne devijacije AQI
std_dev_aqi = np.std(aqi_values)
print("Standardna devijacija AQI:", std_dev_aqi)

# 5. Izračunavanje mediane AQI
median_aqi = np.median(aqi_values)
print("Medijan AQI:", median_aqi)




# Statistika

# Izračunavanje kvantila
quantiles = np.percentile(aqi_values, [25, 50, 75])
print("25. percentil:", quantiles[0])
print("50. percentil (medijan):", quantiles[1])
print("75. percentil:", quantiles[2])


# Brojanje vrijednosti izvan određene granice (npr. AQI > 100)
count_above_100 = np.sum(aqi_values > 100)
print("Broj AQI vrijednosti većih od 100:", count_above_100)

# Brojanje vrijednosti iznad određene granice (npr. AQI < 50)
count_below_50 = np.sum(aqi_values < 50)
print("Broj AQI vrijednosti manjih od 50:", count_below_50)


# Izračun koeficijenta varijacije
cv_aqi = (std_dev_aqi / average_aqi) * 100  # izražen u postotcima
print("Koeficijent varijacije AQI:", cv_aqi)



# Korelacija

# Učitavanje potrebnih podataka
co_values = data['CO AQI Value']
no2_values = data['NO2 AQI Value']
ozone_values = data['Ozone AQI Value']

# Izračun koeficijenta korelacije
correlation_aqi_co = np.corrcoef(aqi_values, co_values)[0, 1]
correlation_aqi_no2 = np.corrcoef(aqi_values, no2_values)[0, 1]
correlation_aqi_ozone = np.corrcoef(aqi_values, ozone_values)[0, 1]

# Ispis rezultata
print("Korelacija AQI i CO:", correlation_aqi_co)
print("Korelacija AQI i NO2:", correlation_aqi_no2)
print("Korelacija AQI i ozona:", correlation_aqi_ozone)




# Grafovi

import matplotlib.pyplot as plt

# Histogram za distribuciju AQI vrijednosti
plt.figure(figsize=(8, 6))
plt.hist(aqi_values, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribucija AQI vrijednosti')
plt.xlabel('AQI vrijednost')
plt.ylabel('Broj mjerenja')
plt.grid(True)
plt.show()



# Stupčasti grafikon za broj AQI vrijednosti većih i manjih od određene granice
plt.figure(figsize=(8, 6))
plt.bar(['Vrijednosti veće od 100', 'Vrijednosti manje od 50'], [count_above_100, count_below_50], color=['red', 'green'])
plt.title('Broj AQI vrijednosti prema granicama')
plt.ylabel('Broj mjerenja')
plt.grid(axis='y')
plt.show()



import matplotlib.pyplot as plt

# Definiranje podataka za grafikon
x_co = co_values
x_no2 = no2_values
x_ozone = ozone_values

# Prikazujemo korelaciju AQI i CO
plt.figure(figsize=(10, 6))
plt.scatter(x_co, aqi_values, color='blue', alpha=0.5)
plt.title('Korelacija AQI i CO')
plt.xlabel('CO AQI Value')
plt.ylabel('AQI Value')
plt.grid(True)
plt.show()

# Prikazujemo korelaciju AQI i NO2
plt.figure(figsize=(10, 6))
plt.scatter(x_no2, aqi_values, color='green', alpha=0.5)
plt.title('Korelacija AQI i NO2')
plt.xlabel('NO2 AQI Value')
plt.ylabel('AQI Value')
plt.grid(True)
plt.show()

# Prikazujemo korelaciju AQI i ozona
plt.figure(figsize=(10, 6))
plt.scatter(x_ozone, aqi_values, color='red', alpha=0.5)
plt.title('Korelacija AQI i ozona')
plt.xlabel('Ozone AQI Value')
plt.ylabel('AQI Value')
plt.grid(True)
plt.show()



# MHeatamap

import seaborn as sns

# Definiranje podataka za matricu korelacije
correlation_data = data[['CO AQI Value', 'NO2 AQI Value', 'Ozone AQI Value']]

# Izračunavanje matrice korelacije
correlation_matrix = correlation_data.corr()

# Vizualizacija matrice korelacije pomoću toplinske karte (heatmap)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Matrica korelacije između CO, NO2 i ozona')
plt.show()

