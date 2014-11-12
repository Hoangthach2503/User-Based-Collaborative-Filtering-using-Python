User-Based-Collaborative-Filtering-using-Python
===============================================
The program takes as input ratings-dataset.tsv.
The ratings file consists of userid , movie name and rating for that movie
The file consists of one rating event per line. Each rating event is of the form:
user_id\trating\tmovie_title

If you need to have a new dataset ,you must have it the this format
user_id\trating\tmovie_title


INPUT:
As a command line arguments you need to pass the following:
python collabFilter.py ratingsFileName user1 user2 movieName k

OUTPUT:
1)The ratings file ---which is stored as a dictionary of dictionary
2)The similarity of user 1 and user 2
3)The nearest k neighbors
4)The predicted rating of the movieName