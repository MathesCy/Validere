
import pandas as pd
import numpy as np

from scipy.stats import chisquare
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Pulling in relevant data
accident_data = pd.read_csv('/Users/cyrusmatheson/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/37CDF5E3-2091-469E-AE89-3AA7698E48BD/AccidentData.csv',encoding = 'latin',dtype = 'string')
age_data = pd.read_csv('/Users/cyrusmatheson/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/BC0A86EE-6D5F-4CD8-9033-D077BEBA1416/AgeData.csv')
chem_data = pd.read_csv('/Users/cyrusmatheson/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/DEFF052C-92F4-4F3B-A6EB-EE8169FB705B/ChemicalCont.csv',encoding = 'latin')

# Selecting Desired Columns for analysis
columns = ['REPORT_RECEIVED_DATE','IYEAR', 'COMMODITY_RELEASED_TYPE', 'COMMODITY_SUBTYPE', 'CAUSE', 'CAUSE_DETAILS']
accident_data = accident_data[columns]
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Scoping Out Accident Data Set
causes = accident_data['CAUSE'].value_counts()
causes.to_frame()

causes.plot(kind='barh', fontsize=7)
plt.show()
cross = pd.crosstab(accident_data['CAUSE'], accident_data['COMMODITY_RELEASED_TYPE'])

# Filtering data for Corrosion Cases/Subcases

corrosion_cause = accident_data['CAUSE'] == 'CORROSION FAILURE'
corrosion_data = accident_data[corrosion_cause]
cross2 = pd.crosstab(corrosion_data['COMMODITY_RELEASED_TYPE'], corrosion_data['CAUSE_DETAILS'])

icorrosion = corrosion_data['CAUSE_DETAILS'] == 'INTERNAL CORROSION'
icorrosion_data = corrosion_data[icorrosion]


# Creating historical pipeline mileage DataFrame
years=['2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010']

miles = {'Refined Products': [64123.0,63117.0,67721.0,62721.0,62370.0,62461.0,62634.0,61768.0,63251.0,64042.0,64124.0],
           'HVL':[74762.0,72632.0,70306.0,69163.0,68729.0,67676.0,65792.0,62768.0,59861.0,58599.0,57980.0],
         'Crude Oil' : [85201.0,84111.0,80899.0,79268.0,75764.0,73057.0,66943.0,61087.0,57463.0,56100.0,54631.0],
         'CO2': [5150.0,5147.0,5206.0,5237.0,5195.0,5241.0,5276.0,5190.0,4840.0,4735.0,4560.0],
         'Biofuel':[17.0,16.0,15.0,15.0,15.0,15.0,16.0,16.0,16.0,16.0,16.0]}

mileage = pd.DataFrame(data = miles, index = years )


#Calculating Incidence Rates per year

accident_array = np.empty([11,5])

commodities = ['CRUDE OIL','REFINED AND/OR PETROLEUM PRODUCT (NON-HVL) WHICH IS A LIQUID AT AMBIENT CONDITIONS','CO2 (CARBON DIOXIDE)','HVL OR OTHER FLAMMABLE OR TOXIC FLUID WHICH IS A GAS AT AMBIENT CONDITIONS','BIOFUEL / ALTERNATIVE FUEL(INCLUDING ETHANOL BLENDS)']
for i in range(len(mileage)):
    for j in range(len(commodities)):
        accident_array[i,j] = len(icorrosion_data[(icorrosion_data['IYEAR'] == years[i]) & (icorrosion_data['COMMODITY_RELEASED_TYPE'] == commodities[j])])

accidents = pd.DataFrame(data = accident_array, index= years, columns= commodities)

# Calculating comparative incidence rates

accidents['Crude Oil'] = accidents['CRUDE OIL']/mileage['Crude Oil']
accidents['Refined Products'] = accidents['REFINED AND/OR PETROLEUM PRODUCT (NON-HVL) WHICH IS A LIQUID AT AMBIENT CONDITIONS']/mileage['Refined Products']
accidents['CO2'] = accidents['CO2 (CARBON DIOXIDE)']/mileage['CO2']
accidents['HVL'] = accidents['HVL OR OTHER FLAMMABLE OR TOXIC FLUID WHICH IS A GAS AT AMBIENT CONDITIONS']/mileage['HVL']
accidents['Biofuel/Ethanol'] = accidents['BIOFUEL / ALTERNATIVE FUEL(INCLUDING ETHANOL BLENDS)']/mileage['Biofuel']
accidents.reindex(index=accidents.index[::-1])
accidents.index.astype('int64')

CO = accidents['Crude Oil'].mean()
RP = accidents['Refined Products'].mean()
CO2 = accidents['CO2'].mean()
HVL = accidents['HVL'].mean()
Bio = accidents['Biofuel/Ethanol'].mean()

ax = plt.gca()
accidents.plot(kind = 'line',y='Crude Oil', ax=ax,color = 'blue')
accidents.plot(kind = 'line',y='Refined Products', ax=ax,color = 'red')
accidents.plot(kind = 'line',y='HVL', ax=ax,color = 'green')
accidents.plot(kind = 'line',y='CO2', ax=ax,color = 'yellow')
accidents.plot(kind = 'line',y='Biofuel/Ethanol', ax=ax,color = 'brown')
plt.xlabel("Year")
plt.ylabel("Corrosion Failures per Mile of Pipeline")
plt.show()
plt.plot

# Chemical Analysis

# Filtering Refined Data from Unrefined Data

chem_ref = chem_data['Class'] == 'Refined'
chem_ref1 = chem_data[chem_ref]
chem_uref = chem_data['Class'] == 'Unrefined'
chem_uref1 = chem_data[chem_uref]

print(chem_uref1)

ax = plt.gca()
chem_ref1.plot(kind = 'scatter', x= 'Sulfur', y = 'Water', ax=ax,color = 'blue',label = 'Refined Product')
chem_uref1.plot(kind = 'scatter', x ='Sulfur',y = 'Water', ax=ax,color = 'red',label ='Unrefined Product')
plt.xlabel("Sulfur %w/w")
plt.ylabel("Water %w/w")
plt.yticks(np.arange(0, 30, 2))
plt.show()

urs = chem_uref1['Sulfur'].mean()
urw =chem_uref1['Water'].mean()
rw = chem_ref1['Water'].mean()
rs = chem_ref1['Sulfur'].mean()

print(urs)
print(urw)
print(rs)
print(rw)


















