from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


app = Flask(__name__)


# Create connection variable
conn = 'mongodb://localhost:27017/'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
db=client.missiontomars
collection=db.missiontomarsifo

@app.route('/')
def home():
    mars_data = client.db.missiontomarsinfo.find_one()
    #mars_data= db.missiontomars.find_one()
    #mars_data=list(db.collection.find())
    return render_template("index.html", mars=mars_data )

#def index():
#    mars = client.db.missiontomars.find_one()
#    return render_template('index.html', missiontomars=mars)


@app.route('/scrape')
def scrape():
    mars = client.db.missiontomarsinfo
    mars_data = scrape_mars.scrape()
    #mars.insert_one(mars_data)
    mars.update({}, mars_data, upsert=True)
    return redirect("http://localhost:5000/", code=302)

# Port number is optional
if  __name__ == "__main__":
    app.run(port=5000,debug=True)