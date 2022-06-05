import requests
from flask import Flask, jsonify, render_template
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__,template_folder='templates')



import sqlite3

conn = sqlite3.connect('/Users/franklugola/Desktop/database.db')
print ("Opened database successfully");
# conn.execute('CREATE TABLE Gymnate (person2)')
# print ("Table created successfully");
# conn.close()
# conn.execute('CREATE TABLE Gymbye (person1 TEXT, date1 TEXT, workout1 TEXT, workouttype1 TEXT, time1 TEXT, instructor1 TEXT)')
# print ("Table created successfully");
# conn.close()

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/checkin")
def checkin():
    return render_template('checkin.html')


@app.route("/checkout")
def checkout():
    return render_template('checkout.html')


@app.route("/job")
def job():
    return render_template('job.html')
    
    

@app.route("/admin")
def admin():
    dbsession = sql.connect('/Users/franklugola/Desktop/database.db')        
    dbsession.row_factory = sql.Row
    dbexecute = dbsession.cursor()
    dbexecute.execute("select * from GymRecords")
    rowData = dbexecute.fetchall();
    return render_template("result.html", rowData=rowData)   
    frank.close()



@app.route("/admin1")
def admin1():
    dbsession = sql.connect('/Users/franklugola/Desktop/database.db')       
    dbsession.row_factory = sql.Row
    dbexecute = dbsession.cursor()
    dbexecute.execute("select * from Gymbye")
    rowData = dbexecute.fetchall();
    return render_template("result1.html", rowData=rowData)   
    frank.close()


@app.route("/admin2")
def admin2():
    dbsession = sql.connect('/Users/franklugola/Desktop/database.db')           
    dbsession.row_factory = sql.Row
    dbexecute = dbsession.cursor()
    dbexecute.execute("select * from Gymnate")
    rowData = dbexecute.fetchall();
    return render_template("result2.html", rowData=rowData)   
    frank.close()
    

@app.route("/info", methods=['POST', 'GET'])
def info():

    if request.method == 'POST' :

        pur = request.form.get('fname')
        date = request.form.get('trip-start')
        workout = request.form.get('Workout')
        Type = request.form.get('Type')
        Time =  request.form.get('Time')
        Instructor = request.form.get('Instructor')
                
        with sql.connect('/Users/franklugola/Desktop/database.db') as frank:
            conn = frank.cursor()
            conn.execute("INSERT INTO GymRecords (person,date,workout,workouttype,time,instructor) VALUES (?,?,?,?,?,?)",(pur,date,workout,Type,Time,Instructor))
            frank.commit()


        # if request.method == 'POST' :


        #     pur1 = request.form.get('outname')
        #     date1 = request.form.get('trip-start')
        #     workout1 = request.form.get('Workout')
        #     Type1 = request.form.get('Type')
        #     Time1 =  request.form.get('Time')
        #     Instructor1 = request.form.get('Instructor')
                
        # with sql.connect(('/home/lugofr01/lugofr01/projects/final_project')) as frank:
        #     conn = frank.cursor()
        #     conn.execute("INSERT INTO Gymbye (person1,date1,workout1,workouttype1,time1,instructor1) VALUES (?,?,?,?,?,?)",(pur1,date1,workout1,Type1,Time1,Instructor1))
        #     frank.commit()
            
    info = "Thank you for filling in the Workout form! Please Visit the Workout Recomendation section to get your desired workouts"

    return render_template("msg.html", info=info)
    frank.close()


@app.route("/info1", methods=['POST', 'GET'])
def info1():







    if request.method == 'POST' :


        pur1 = request.form.get('outname')
        date1 = request.form.get('date-start')
        workout1 = request.form.get('Assesment')
        Type1 = request.form.get('Workoutaina')
        Time1 =  request.form.get('Finishtime')
        Instructor1 = request.form.get('Instructor')
            
    with sql.connect('/home/franklugola/lugofr01/projects/database.db') as frank:
        conn = frank.cursor()
        conn.execute("INSERT INTO Gymbye (person1,date1,workout1,workouttype1,time1,instructor1) VALUES (?,?,?,?,?,?)",(pur1,date1,workout1,Type1,Time1,Instructor1))
        frank.commit()
        
    info = "Thank you for filling in the Workout form! Please Visit the Workout Recomendation section to get your desired workouts"

    return render_template("msg.html", info=info)
    frank.close()



@app.route("/info2", methods=['POST', 'GET'])
def info2():

    if request.method == 'POST' :


        pur2 = request.form.get('temail')
        
        with sql.connect('/home/franklugola/lugofr01/projectssdatabase.db') as frank:
            conn = frank.cursor()
            conn.execute("INSERT INTO Gymnate (person2) VALUES (?)",(pur2,))
            frank.commit()
        
    info = "Thank you for filling in the Workout form! Please Visit the Workout Recomendation section to get your desired workouts"

    return render_template("msg.html", info=info)
    frank.close()


@app.route("/api")
def api_func():
    res = requests.get("http://lugola.pythonanywhere.com/api/v1/coreworkout")
    response = res.json()
    return render_template("api.html", data=response)




   

if __name__ == "__main__":
    app.run()
    
    
