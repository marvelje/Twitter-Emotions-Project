# Twitter-Emotions-Project

## Business problem 
The Google marketing department has asked us to use the tweets from this conference to build a model that can accurately predict tweet sentiment that can be used at future tech conferences or for tweets directed at Google and its competitors more generally. They want to use the model to compare performance across years at SXSW and similar tech conferences to see if their product strategy is driving positive engagement.

Historically, collecting consumer reviews has been a tedious process. Online reviews are useful, but tend to have a bias towards negative reviews. If someone is perfectly fine with a product, they're not as likely to leave a positive review as someone who has had a bad experience. Analyzing tweets is a potential way to bridge this gap, by providing a more unfiltered view into brand sentiment.

## Summary
- Data review
The data was about 9000 crowd sourced tweets from SXSW with 88% brand identifier (Google, Apple and others). Every tweet has #SXSW or #sxsw as an identifier and the data was gotten from [data.world](https://data.world/crowdflower/brands-and-product-emotions).
- We performed basic data analysis . we changed the columns name into something readable. 
- We checked for duplicates and dropped them.
- Explored the distribution of the target variable (emotion)
- And then dropped the null values 

### Data Cleaning and Exploration
We preprocessed the data using Natural Language Processing using the NLTK library.
- To clean the tweets, we removed any hyperlinks and links 
- Created a function for removing stop words and symbols
- We created a sentiment target and mapped it into the data frame.

We explored the data based on the brands especially Apple and Google and also the positive and not positive sentiments looking for keywords that helps the model make a prediction.


### Model Approach 
We ran more than 20 models ranging from Logistic Regression to XG Classifier . we used the best model with the best accuracy and aim to minimize false positives only to 6%. To further improve the model we tuned its parameters to give an accuracy score of 75%. 

 ### Presentation 

https://docs.google.com/presentation/d/1ARQwggwzd7eKsUVqRzYrf9GlM4OsmPJ0955_KJwgAXg/edit#slide=id.g1026bc5f920_0_418

### Navigating the repository 
Twitter sentiment analysis — final notebook
Data - Contains the data used for the project
Notebooks - contains all data analysis ; cleaning  and models for the project
gitignore 
