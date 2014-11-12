import sys
import json
import string
import math
import csv

ratings = {} # initialize an empty ratings dictionary

def main():

    ratings_file = open(sys.argv[1])
    user1 = str(sys.argv[2])
    user2 = str(sys.argv[3])
    item = str(sys.argv[4])
    k = int(sys.argv[5])


    ratings = readRatings(ratings_file)
    print "readRatings output", ratings
    sim = similarity(ratings[user1], ratings[user2])
    print "sim = ", sim
    nearest = nearestNeighbors(user1, ratings, k)
    print "nearestNeighbors: ", nearest
    prediction = predict(item, nearest, ratings)
    print "prediction for item", item, ": ", prediction



def readRatings(ratings_file):
    
    # Write code to read ratings file and construct dictionary of dictionaries

    
    ratings_file = csv.reader(ratings_file, delimiter='\t')
    for row in ratings_file:
        user_id=row[0]
        rating=row[1]
        movie=row[2]
        if not ratings.has_key(user_id):
            ratings[user_id]={}
            ratings[user_id][movie+'\n']=rating
        else:
            ratings[user_id][movie+'\n']=rating
    
    
    return ratings


def similarity(user_ratings_1, user_ratings_2):

    # Write code to implement the Pearson correlation equation
    # Return the similarity of user 1 and user 2 based on tehir ratings


    #average calculation for each user    
    
    sum1=0.0
    sum2=0.0
    c1=0
    c2=0
    for value1 in user_ratings_1:
        sum1+=float(user_ratings_1[value1])
        c1+=1
    for value2 in user_ratings_2:
        sum2+=float(user_ratings_2[value2])
        c2+=1
    r1_avg=sum1/c1
    r2_avg=sum2/c2
    
    #FINDING THE CO RATED ITEMS
    co_rated=[]
    
    for movie_1 in user_ratings_1:
        for movie_2 in user_ratings_2:
            if(movie_1==movie_2):
                co_rated.append((float(user_ratings_1[movie_1]),float(user_ratings_2[movie_2])))
                
   
        
    #NUMERATOR CALCULATION
    num_sum=0.0
    for value in co_rated:
        r1,r2=value
        num_sum+=(r1-r1_avg)*(r2-r2_avg)
   


    #DENOMINATOR CALCULATION
    den_sum1=0.0
    den_sum2=0.0
    for value in co_rated:
        r1,r2=value
        den_sum1+= (r1-r1_avg)*(r1-r1_avg)
        den_sum2+= (r2-r2_avg)*(r2-r2_avg)
    den_total=math.sqrt(den_sum1)*math.sqrt(den_sum2)
    
    sim=0.0
    if(len(co_rated)==0):
        sim=0.0
    else:
        sim=num_sum/den_total


    return sim


def nearestNeighbors(user_id, all_user_ratings, k):

    # Write code to determine the k nearest neighbors for user_id
    nearest=[]
    for each_user in all_user_ratings:
        if user_id!=each_user:
            nearest.append((each_user,similarity(ratings[user_id],all_user_ratings[each_user])))
            
    
    nearest=sorted(nearest, key=lambda user: user[1] ,reverse=True)
        
    return nearest[0:k]


def predict(item, k_nearest_neighbors, all_user_ratings):
    
    # Write code to predict the rating for the item given the k nearest neighbors of the user
    mod_knn=[]
    sum_sim=0.0

    #Remove any of the k-nearest-neighbors who don't have a rating for item.
    item=item+'\n'
    for i in k_nearest_neighbors:
        user,sim=i
        if(item in all_user_ratings[user]):
            mod_knn.append(i)
    for each in mod_knn:        
        user,sim=each
        sum_sim+=sim

    n_sum=0.0
    #print mod_knn   
    for neighbor in mod_knn:
        user,sim=neighbor
        n_sum+=(float(sim)*float(all_user_ratings[user][item]))

    if len(mod_knn)==0:
        prediction=0
    else:
        prediction=float(n_sum/sum_sim)
    
    return prediction

if __name__ == '__main__':
    main()
