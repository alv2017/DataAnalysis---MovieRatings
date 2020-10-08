# Movie Ratings

In this lab we will present three Jupyter notebooks, and each notebook will
elaborate on one of the ratings: mean rating, popularity rating, positivity rating.

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


## Analysis Notebooks

1) Mean Rating:

	a) We will calculate a mean rating for each movie, and order the movies with
	the highest rank first. We will display a list of top three movies by the mean rating.
	
	b) We will compute the mean rating for males and females separately, and display it.
	We will show three top rated movies for male and female audience.
	
	c) We will show two movies with the greatest difference among the male and female
	audiences: 
	 - male audience rating is higher than female audience rating;
	 - female audience rating is higher that male audience rating.
	 
	d) We will compute the mean rating provided by male and female audiences.
	
2) Rating Count (Popularity):
	
	a) We will count the number of ratings for each movie, and display the most popular 
	first. We will show three the most popular movies.
	
	b) We will compute the popularity separately for male and female audience. 
	
	c) We will 	display two movies that differs most by popularity among males and females.
	
	d) We will show how many male and female votes/ratings we have in total.
	
3) Positivity Rating (4+ liking):

	a) We will calculate the percentage of ratings of 4 stars or higher for each movie.
	We will order the movies with the highest positive percentage first, and display
	top three movies with the highest positive rating. 
	
	b) We will compute the positive rating for males and females separately.
	
	c) We will compute the total positive rankings percentage for male and female audiences. 
	
	
	