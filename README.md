# Twitter-Emotions-Project
- Flatiron Phase 4 Project
- Authors: Jeff Marvel, Michael Ajayi

## Business problem 
SXSW is a annual festival held in Austin, TX, encompassing a wide range of topics from film / music to text conferences. At the 2013 tech conference, tweets with the hashtag #SXSW directed at Google or Apple were aggregregated, and attendees were asked to classify the tweets as having a Positive, Negative, or Neutral sentiment. This manual classification can be used to train models to predict sentiment based on the contents of the tweets.

The Google marketing department has asked us to use the tweets from this conference to build a model that can accurately predict tweet sentiment that can be used at future tech conferences or for tweets directed at Google and its competitors more generally. They want to use the model to compare performance across years at SXSW and similar tech conferences to see if their product strategy is driving positive engagement.

Historically, collecting consumer reviews has been a tedious process. Online reviews are useful, but tend to have a bias towards negative reviews. If someone is perfectly fine with a product, they're not as likely to leave a positive review as someone who has had a bad experience. Analyzing tweets is a potential way to bridge this gap, by providing a more unfiltered view into brand sentiment.

## Summary
- Data review
The data was about 9000 crowd sourced tweets from SXSW with 88% brand identifier (Google, Apple and others). Every tweet has #SXSW or #sxsw as an identifier and the data was gotten from [data.world](https://data.world/crowdflower/brands-and-product-emotions).
- We performed basic data analysis. We changed the columns name into something readable. 
- We checked for duplicates and nulls and dropped them
- Explored the distribution of the target variable (emotion)

## Navigating the repository
twitter_sentiment_analysis.ipynb — final notebook (includes all data processing and modeling)

Data - Contains the data used for the project

util.py - contains function for evaluating model performance (docstring included)


## Data Cleaning and Exploration
We preprocessed the data using Natural Language Processing from the NLTK library.
- To clean the tweets, we removed any hyperlinks and links 
- Created a function for removing stop words and symbols (there were several non-ASCII characters generated when the tweets were scraped)
- We created a sentiment target and mapped it into the data frame.

We generated word clouds from data based on the brands Apple and Google and also the positive and not positive sentiments looking for keywords that helps the model make a prediction.

## Modeling Approach
We created a binary classification problem, categorizing tweets as Positive or Not Positive. Our primary evaluation metric was Accuracy, with a secondary goal of minimizing False Positives. For the business problem, we would rather take a conservative approach and not mislabel tweets as Positive.

We ran more than 20 models ranging from Logistic Regression to XG Classifier. For each model, we tested Count and TF-IDF vectorizers in addition to Stemming vs. not Stemming the words.

We used the best model with the best accuracy and aim to minimize false positives only to 6%. To further improve the model we tuned its parameters to give an accuracy score of 75%. Generally, the Count Vectorizer performed better along with Stemmitization.

## Recommendations / Conclusions

With basic cleaning steps and testing a variety of models, we were able to improve model accuracy materially above baseline. 67% -> 75%.
- Our recommendation is that this model can be used to track brand sentiment at future tech events similar to SXSW
- The model, along with word freq distributions, can serve as an "early warning" system for potential brand issues, e.g., Google Circles / Google+

**Next steps**:
- Tweets are messy, and there is likely substantially more cleaning that can be performed on them.
- Additional feature engineering can be useful too, such as exploring Bigrams and Word2Vec (the value of these approaches increases the cleaner the data gets)
- Additionally, the model can continue to be tuned with additional tweets from other past conferences

**Final Model**:
- While SVM did perform the best and produced the best split of False Positive to False Negative, the model may perform worse at more tweets from future events are added to tune the model.
- SVM runs more slowly as you increase dimensions, so at a certain point, it may make sense to revert back to XGBoost or other models that are better equipped to handle high dimensionality (e.g., Naive Bayes)


### Presentation 

https://docs.google.com/presentation/d/1ARQwggwzd7eKsUVqRzYrf9GlM4OsmPJ0955_KJwgAXg/edit#slide=id.g1026bc5f920_0_418
