#------------------------------ArticleFlaskApp.py------------------------------#

'''
Importing Modules:
-Flask, jsonify, request :- flask
-csv
'''
from flask import Flask, jsonify, request
import csv

#Declaring a new variable to house all the articles
articles_a=None

#Opening and Reading from the file containing the articles, with utf-8 encoding to assure a smooth process
with open("articles.csv",encoding="utf-8") as file:
    reader=csv.reader(file)
    reader=list(reader)
    reader.pop(0)
    articles_a=reader

#Declaring new variable meant for categorizing the articles each assigned with articles like, articles disliked, articles not read and articles save for reading later respectively   
articles_l=[]
articles_ul=[]
articles_nr=[]
articles_rl=[]

    


#Creating a new flask app
app=Flask(__name__)

#Initiating the first route
@app.route('/')

#Function of the first route
def returnMovies():

    #Returning the original data
    return jsonify({
        "data":articles_a[1],
        "success":True
    },200)

#Initiating the second route
@app.route('/like-article',methods=["POST"])

#Function of the second route
def returnLikedArticles():

    #Identifying the article desired to be marked as "liked"
    article_id=request.args.get('id')
    index_r,stats=next([index,final] for index,final in enumerate(articles_a) if str(final[2])==article_id)
    articles_l.append(stats)
    articles_a.pop(index_r)

    #Returning  the abstracted specifics
    return jsonify({
        "Title":stats[10],
        "URL":stats[9],
        "Description":stats[11],
        "data":articles_l,
        "id":stats[2],
        "success":True
    })

#Initiating the third route
@app.route('/dislike-article',methods=["POST"])

#Function of the third route
def returnDislikedArticles():

    #Identifying the article desired to be marked as "unliked"
    article_id=request.args.get('id')
    index_r,stats=next([index,final] for index,final in enumerate(articles_a) if str(final[2])==article_id)
    articles_ul.append(stats)
    articles_a.pop(index_r)

    #Returning the abstracted specifics
    return jsonify({
        "Title":stats[10],
        "URL":stats[9],
        "Description":stats[11],
        "data":articles_ul,
        "id":stats[2],
        "success":True
    })

    

#Initiating the fourth route
@app.route('/not-read-article',methods=["POST"])

#Function of the fourth route
def returnUnReadArticles():
    article_id=request.args.get('id')
    index_r,stats=next([index,final] for index,final in enumerate(articles_a) if str(final[2])==article_id)
    articles_nr.append(stats)
    articles_a.pop(index_r)

    #Returning the abstracted specifics
    return jsonify({
        "Title":stats[10],
        "URL":stats[9],
        "Description":stats[11],
        "data":articles_nr,
        "id":stats[2],
        "success":True
    })


#Initiating the fifth route
@app.route('/read-later-article',methods=["POST"])

#Function of the fifth route
def returnReadLaterArticles():
    article_id=request.args.get('id')
    index_r,stats=next([index,final] for index,final in enumerate(articles_a) if str(final[2])==article_id)
    articles_rl.append(stats)
    articles_a.pop(index_r)

    #Returning the abstracted specifics
    return jsonify({
        "Title":stats[10],
        "URL":stats[9],
        "Description":stats[11],
        "data":articles_rl,
        "id":stats[2],
        "success":True
    })

#Verifying whether the variable "__name__" is equal to "__main__"
if __name__ == "__main__":

    #Running the app, with debug settings active
    app.run(debug=True)

#Verified through Postman    

#------------------------------ArticleFlaskApp.py------------------------------#