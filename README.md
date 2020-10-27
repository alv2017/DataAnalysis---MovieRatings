# Movie Ratings

The notebooks presented in this project follow the labs from the course on
"Introduction to Recommender Systems" taught by the University of Minnesota at Coursera:
https://www.coursera.org/learn/recommender-systems-introduction

I'm not exactly following the course labs, however I'm inspired by the ideas behind them and the course
in general, and I hope that by the end of the course
I will gain enough skills and knowledge to convert this into a Big Data project on Recommender Systems.

## List of Notebooks:

- [Average (Mean Value) Ratings](https://github.com/alv2017/DataAnalysis---MovieRatings/blob/master/notebooks/MovieRatings_MeanRating.ipynb)
- [Popularity Ratings](https://github.com/alv2017/DataAnalysis---MovieRatings/blob/master/notebooks/MovieRatings_PopularityRating.ipynb)
- [Positivity Ratings](https://github.com/alv2017/DataAnalysis---MovieRatings/blob/master/notebooks/MovieRatings_PositivityRating.ipynb)
- [Association Metrics](https://github.com/alv2017/DataAnalysis---MovieRatings/blob/master/notebooks/MovieRatings_AssociationMetrics.ipynb)


## Data

Before creating the workbooks, we are going to tidy up our data and prepare it for the 
analysis. We are going to create the following datasets:

Movies: movie_id, movie_name, movie_year
Users: user_id, user_gender
Ratings: movie_id, user_id, rating

We will create a SQLite database to store our analysis data. It might seem a redundant
procedure, however, I think, that it is quite good and useful exercise, and it is always a good idea 
to keep analysis data well structured and conveniently organized.

The code for this part of the exercise will be stored in a directory called
**data_preparation**.

	
	