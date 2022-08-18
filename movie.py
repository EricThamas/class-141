from flask import Flask,jsonify,request
import csv
allMovies=[]
with open("finalMovie.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    allMovies=data[1:]
#print(allMovies)
likedMovies=[]
didnotlikeMovies=[]
didnotmatch=[]

app=Flask(__name__)
@app.route("/getMovies")
def getMovies():
    return jsonify({
        "data":allMovies[0],
        "status":"success"
    })
@app.route("/likedMovies",methods=["POST"])
def likedMovies():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status":"success"
    })
@app.route("/didnotlikeMovies",methods=["POST"])
def didnot_likedMovies():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    didnotlikeMovies.append(movie)
    return jsonify({
        "status":"success"
    })
@app.route("/didnot",methods=["POST"])
def not_matched_Movies():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    didnotmatch.append(movie)
    return jsonify({
        "status":"success"
    })

if __name__=="__main__":
    app.run()