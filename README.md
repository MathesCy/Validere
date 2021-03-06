# Overview


This report has been created with the objective of identifying which physical or chemical properties of crude oil could be responsible for pipeline incidents. Using data collected by the U.S. Department of Transportation's Pipeline and Hazazardous Materials Safety Administration (PHMSA), this report will first seek to establish the existence of a relationship between crude oil and certain modes of pipeline failure. If this can accomplished, the report will then attempt to determine which physical and/or chemical characteristics of crude oil are resulting in a higher incidence rate of said failure in pipelines carrying crude oil versus other commodities. 

## Background 

The primary dataset used in this report contains a summary of pipeline accidents recorded in the United States spanning from January 2010 to Present Day. Before any kind of analysis can be performed, the limitations of this data, and the circumstances under which it was collected must first be understood. The data sourced from the PHMSA specifically details the incidents reported on Hazardous Liquid or CO2 pipeline systems, this is a broader categorization for pipeline systems carrying any of the following commodities. 

1) Biofuel/Alternative Fuel (Including Ethanol Blends)
2) CO2
3) Crude Oil
4) HVL
5) Refined/Petroluem Products

Although this report will focus specifically on the relationship between crude oil and pipeline accidents, the dataset contains records for other commodities. Also worth noting is that not all pipeline incidents are considered reportable. The PHMSA only requires an operator to report a pipeline incident if any of the following occur. 

1) Fatality or injury requiring hospitalization.
2) Estimated property damage, including cost of clean-up and recovery, value of lost product, and damage to the property of the operator or others, or        both, exceeding $50,000.
3) Highly volatile liquid releases of 5 barrels or more or other liquid releases of 50 barrels or more.
4) Liquid releases resulting in an unintentional fire or explosion.

Finally, before attempting to analyze what attributes of crude oil contribute to pipeline failure, it must first be understood how PHMSA categorizes cause failure in their data collection process. Broadly speaking, the PHMSA recognizes six distinct causes of pipeline failure.

1) Corrosion 
2) Excavation Damage
3) Incorrect Operation
4) Material/Weld/Equipment Failure
5) Natural Force Damage
6) Other Outside Force

For the purposes of this report, it should be noted that some of these categories won't be seen as relevant to the analysis. For instance, the category 'Other Outside Force' which refers to pipeline accidents caused by any non-natural external force (e.g. vandalism, vehicle accident) would not be relevant in this analysis because the frequency of these events is unrelated to the physical or chemical properties of the pipeline's contents. 

In fact, of these six categories, the only one that can be viewed as directly related to the physical contents of the pipeline itself, is Corrosion. Excavation Damage refers to incidents in which pipelines are inadvertently damaged by excavating equiment. Incorrect Operation is the result of operator error, and Natural Force Damage arises from naturally occuring external forces, such earthquakes or hurricanes. Finally, Material/Weld/Equipment failures result from improper maintenance or component selection, or flaws in the construction of the pipeline and supporting apparatus. Since the focus of this report is specifically on the relationship between the physical and chemical properties of crude oil and pipeline failure, the analysis will focus exclusively on Corrosion failures. 

NOTE: There is an arugment to be made that the specific physical and chemical properties of crude oil could indirectly result in an increase in the incidence rate of other failure types by impacting how and where pipelines are built, and as a consequence how they're operated and how their surrounding environment interacts with them. 

## Analysis


When the dataset is broken down by cause of failure, it produces the resulting distribution of accidents reported in the U.S since 2010. 


![alt text](https://github.com/MathesCy/Validere/blob/main/FailureType.png)


It can be seen that over the past 12 years, equipment failure has been the leading cause of pipeline failure, accounting for 45.7% of all reported events. Behind equipment failure, corrosion has been identified as the cause for 20.5% of reported incidents.

This can be broken down further by looking at each cause of failure based on the type of commodity carried in the pipeline where the accident occured. Of the five commodity types, pipelines carrying crude oil have experienced over half of the reported accidents since 2010, with 50.7% occuring in crude oil Hazardous Liquid pipeline systems. 


|  Commodity       | Corrosion      | Material/Weld/Equipment Failure | Excavation Damage | Incorrect Operation  | Natural Force | Other Force  | 
| ------------ |---------------| -----------------------  |------------       |---------------     | ----------    | ------------ | 
| Biofuel       | 1            | 3                        | 0                 | 2                  | 0             |0      | 
| CO2           | 7            |   44                     | 0                 | 10                  |   1         | 1     |  
| Crude Oil     | 675          | 1083                     | 79                 | 354                | 102          |44     | 
| HVL           | 65           |   505                     | 33                | 76                 |   30         | 19      |  
| Refined Products | 218       |   832                     | 54               | 240                 |     86          | 29     |   


Since the focus of this report is specifically on crude oil and corrosion failures, the dataset will be reduced down to look only at cases where the cause of failure was identified as 'Corrosion'. However, within each cause category there exists a sub category that needs to be considered. In the case of the 'Corrosion' category, the sub-categories are 'Internal' and 'External'. Internal corrosion failure refers to pipeline accidents resulting from corrosion on the inside of the pipeline due to chemical interactions between the pipeline metal and the contents of the pipe. External corrosion is the result of interactions between the outside of the pipe and its surrounding. Since the physical/chemical properties of the contents of the pipe would have no impact on how the pipe interacts with its external surroundings, the dataset will be reduced even further to look only at cases resulting from Internal Corrosion.

Commodity Type | Internal Corrosion| External Corrosion
-------------  | ------------- | -------------
Biofuel        | 0             | 1
CO2            | 0             |    7
Crude Oil      | 516           | 159
HVL            | 5             | 60
Refined Product | 83              | 135


Looking purely at the number of occurences of a certain type of failure experienced by pipelines carrying a given commodity would produce distorted results. From the data shown above, it's apparent that crude oil pipelines have experienced significantly more internal corrosion failures than any other sub category of Hazardous Liquid pipeline system over the past 12 years. However, this fails to account for the the fact that certain types of pipeline systems are more prevalent than others. 100 miles of pipeline represents more opportunity for failure than 10. To account for this, PHMSA data on pipeline mileage going back to 2010 was used to calculate failure incidence rates on a per mile basis for each commodity type. 

The graph below shows the comparative incidence rates observed for internal corrosion failures broken down by the commodity type of the pipeline. It can be seen than on average, even when normalizing to account for pipeline mileage, systems carrying crude oil experience internal corrosion incidents at more than twice the rate of any other system.

![alt text](https://github.com/MathesCy/Validere/blob/main/FailureRate.png)

Averaging the incidence rate over the course of the full term of the available data, the resulting average rate of internal corrosion failure is calculated for each pipeline system

Commodity Type | Failure Rate 
-------------  | ------------- 
Biofuel        | 0             
CO2            | 0             
Crude Oil      | 0.000608           
HVL            | 7.33e-06             
Refined Product | 0.000113              

Based on these results it can be definitively stated that pipeline systems carrying crude oil experience failure due to internal corrosion at a far higher rate than any other sub category of Hazardous Liquid pipeline.

Another point worth noting, is that if this exercise is repeated in order to calculate incidence rates on a per mile basis for other failure types it results in the table shown below. It can be seen that crude oil pipelines don't experience any other kind of failure at an above average rate when compared to other types of pipeline systems. This also supports the initial assumption to look exclusively at internal corrosion failures. 

NOTE: Due to a lack of data the Biofuel/Ethanol pipeline incidents were not considered in the creation of this table.


|  Failure Type      | Crude Oil      | HVL  | Refined Products  | CO2 | 
| ------------       |---------------| -----------------------   |---------------     | ----------    | 
| Material/Weld/Equipment Failure | 0.001056       | 0.000615                        | 0.001073                 | 0.000893           | 0             | 
| Excavation          | 8.09e-05            |   4.01e-05                     | 6.47e-05                  | 0.001262                  |   1         |   
| Incorrect Operation  | 0.000352          | 8.35e-05                     | 0.000309                 | 0.005689                | 102          | 
| Natural Force        | 9.97e-05           |   3.34e-05                     | 0.000118                | 0.001650                 |   30         | 
| Other Force           | 5.043-05      |   3.21e-05                     | 4.11e-05               | 0.000834                |     86          | 29     |   


With these results indicating an apparent relationship between the presence of crude oil in a pipeline system and the incidence rate of internal corrosion, the task becomes identifying which physcial or chemical properties of crude oil contribute to this corrosion. 

In order to accomplish this, a secondary dataset was used that catalogues the various physical and chemical properties for crude oil and other refined petroleum products. By looking at what characteristics crude oil possess when compared to refined products, it may be possible to determine which factors are contributing to the increase in corrosion incidence. This dataset was collected by Environment Canada and contains information gathered from crude oil and refined product samples from around the world.  

In order to narrow the scope of the search, consideration was given to the traditional causes of corrosion. In general, corrosion can result from excessive humidity or condensation on a metal surface, or the presence of corrosive chemicals such as chlorine, hydrogen oxides or sulfur oxides. In the context of crude oil, water and sulfur content are important product characteristics, so the data provided by Environment Canada includes these specifications for each of the products listed. 

By looking at the water and sulfur content of the crude oil products included in the dataset versus the refined petroleum products it can be seen that on average crude oil products possess a substantially higher content of both water and sulfur.  

![alt text](https://github.com/MathesCy/Validere/blob/main/ChemCont.png)

Calculating the average sulfur and water content for crude/unrefined products versus refined produces the table below.

Characteristic | Crude Oil| Refined Products
-------------  | ------------- | -------------
Sulfur %w/w       | 1.55            | 0.31
Water %w/w            | 1.37             |    0.79

## Conclusion

Although this does not conclusively confirm that the sulfur and water content in crude oil is exclusively responsible for pipeline accidents, it does provide a positive indication that it could be a significant source of the problem. Implementing stricter quality controls concerning the water and sulfur content of crude entering certain pipelines may potentially help to limit the rate at which these events occur. 

## Data Sources

https://www.phmsa.dot.gov/data-and-statistics/pipeline/annual-report-mileage-hazardous-liquid-or-carbon-dioxide-systems

https://open.canada.ca/data/en/dataset/53c38f91-35c8-49a6-a437-b311703db8c5

https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data



