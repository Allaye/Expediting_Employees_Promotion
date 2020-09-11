# Project Title:
**Expediting Employees Promotion**

This project was developed to tackle the long delays in promoting a qualified employee to a managerial position and below. 
Currently, the process an employee goes through to get promoted to his/her new role leads to a delay in the transition process. 
Our task was to analyze the data and develop an accurate model to help the organization fast track its promotion cycle. 
The project made use of a machine learning framework that goes through the features for the promotion of an employee. 
Using the binary logistic regression, the model is able to predict whether an employee is promoted or not.


# Demo

A demo has been created to show you how the model works.
We have created an interface where you can interact with the model in making prediction.
This shows how the model was deployed in Microsoft Azure and using Microsoft Azure Web App to develop an app for users to interact with it

Check [**DEMO.md**](https://web.microsoftstream.com/video/8cfd4696-fab0-4fd9-beb1-3a79426de16) for more.

Here is a random GIF as a placeholder.

![Random GIF](https://media.giphy.com/media/L2r3WglNffC25Zem0P/giphy.gif) 

# Table of contents

- [Project Title](#project-title)
- [Demo](#demo)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Contribute](#contribute)
    - [Sponsor](#sponsor)
    - [Adding new features or fixing bugs](#adding-new-features-or-fixing-bugs)
- [Privacy](#privacy)

# Installation
[(Back to top)](#table-of-contents)

Below you can find an outline of how to reproduce the solution for the project.
If you run into any trouble with the setup/code or have any questions please contact;

Ethel.Hehetror@azubiafrica.org 

Gideon.Kolade@azubiafrica.org or

Evans.Matey@azubiafrica.org .

## Hardware: 
The following specs were used to create the original solution;

The requirements:

•	Any Standard Personal Computer will do 

## Software 
The following python packages were used in the original solution; 

The requirements:

•	Python 3.7

•	Flask Web Framework

•	Azure Web service

•	HTML, CSS and Bootstrap4

## Data Setup

Dataset

The dataset was obtained from the company. 
The training database contains 54,808 observation and 14 columns. 
The training database contained missing data in two columns which were education and previous_year_rating. 
It is a good database for people who want to try machine learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.


## Data Processing:
The dataset contains various categorical variables which was converted using one-hot encoding. For the labelled data, it has already been converted into a nominal variable.
The employee ID gave a distinct dataset making it impossible to get a duplicated observation. 

Lets deal with the missing value in the dataset now, there are many options we can use to solve missing value problem, each one has its benefit and cons, instead of just finding the mean, median, etc or dropping the rows all together we will predict this values using datawig.

We went on to perform data visualization on the dataset.

For the univariate analysis, we take the individual features and plot them to see how they were distributed.
Using plots such as the bar plot, pie chart, boxplot and also a distribution plot to better understand the data at hand.

For the bivariate analysis, we used the seaborn package to plot a pairplot which gave us an overview of how the each feature was related to eachother. Then moved on to find whether there was a strong correlation between the feature values and the label value.The heatmap was a better option to give us that pictorial view of the correlation.

We continued to explore the dataset to find how the feature variables are affected by the label variable.

Our first option is not to encode the categorical data. From our visualization, we know our label is highly imbalanced but for now we will just ignore it and move on, if this iteration fails to produce better result then we will apply other engineeering to it.

## Model Build:
These are the options used to produce the solution.

In our first model build up, we used the CatBoostClassifier to build the model. This classification method tends to leave the categorical variable as it is, so instead of creating a dummy for them we just go ahead with the modlelling to see what we could derive from it.

From the first model build, our F1 score and recall was low which was due to the imbalance in our label values.

We move on to perform a label encoding to transform the catergorical variables into a numerical variable.
To correct the imbalanced label values, we used the Synthetic Minority Over-sampling Technique(SMOTE) which created new data instances of the minority groups by copying existing minority instances and making small changes to them.

We went on to build our second model, our test scores from the accuracy score, F1 score, precision, recall were all performing great.
But our curiosity made us try to still get a better or higher performance.

Moving on the third model, the region, recruitment channel was dropped because they were not significant to the label variable(promotion).
In this model, we scale the dataset with the StandardScaler module. We train the model to see if the test scores were better than the previous models. It showed a very good performance compared to the rest.

Using the LGBMClassifier for the fourth model, it performed well compared with the previous iterations.

We also tried the Decision Tree Classifier and that was also better than the others.
Finally, we use the decision tree model in our model build.    


# Contribute
[(Back to top)](#table-of-contents)

We will like to say a big thank you to Ethel Hehetror(Project Manager), Gideon Kolade(Data Scientist) and Evans Teye Matey(Data Analyst).
This project follows the all-contributors specification. 
Contributions of any kind welcome!

<!-- This is where you can let people know how they can **contribute** to your project. Some of the ways are given below.

Also this shows how you can add subsections within a section. -->

### Sponsor
[(Back to top)](#table-of-contents)

This is a completely Open Source project and it is free for use.
Help us in keeping this project maintained.


# License
[(Back to top)](#table-of-contents)






