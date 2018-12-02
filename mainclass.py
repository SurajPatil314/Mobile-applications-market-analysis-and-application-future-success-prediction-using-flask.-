import mysql.connector
import pandas as pd
import pyodbc
from flask import Flask
import pymysql
from flask import redirect
from flask import render_template
from flask import url_for, request
from sklearn.linear_model import LogisticRegression
from numpy import *

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():   
    return render_template('index.html')
    
@app.route('/display',methods = ['POST', 'GET'])
def output():
    if request.method == 'POST':  
        os = request.form['os']
        os1=0
        genre1=0
        print(os)
        if(os=='Android'):
        	os1=0
        else:
        	os1=1
        genre = request.form['genre']
        if(genre=='Games'): 
        	genre1=0
        elif(genre=='Productivity'):
        	genre1=1
        elif(genre=='Weather'):
        	genre1=2
        elif(genre=='Shopping'):
        	genre1=3
        elif(genre=='Lifestyle'):
        	genre1=4
        elif(genre=='Finance'):
        	genre1=5
        elif(genre=='Music'):
        	genre1=6
        elif(genre=='Utilities'):
        	genre1=7
        elif(genre=='Travel'):
        	genre1=8
        elif(genre=='Social Networking'):
        	genre1=9
        elif(genre=='Sports'):
        	genre1=10
        elif(genre=='Business'):
        	genre1=11
        elif(genre=='Health & Fitness'):
        	genre1=12
        elif(genre=='Entertainment'):
        	genre1=13
        elif(genre=='Photo & Video'):
        	genre1=14
        elif(genre=='Navigation'):
        	genre1=15
        elif(genre=='Education'):
        	genre1=16        	
        elif(genre=='Food & Drink'):
        	genre1=17
        elif(genre=='News'):
        	genre1=18
        elif(genre=='Book'):
        	genre1=19
        
        else: 
        	genre1=0
        
        print(genre)
        size2 = double(request.form['size'])
        price2 = double(request.form['price'])
        result=request.form
        conn = pymysql.connect(user='root', password='root',host='127.0.0.1', db='appdata')
        a = conn.cursor()
        sql = 'select ratings from appdata1 limit 1;'
        a.execute(sql)
        data = a.fetchone()

        sql1= ("SELECT genre,size,ratings,price,os,downloads FROM appdata1 where os= %s AND genre= %s ;" %(os1,genre1))
        a.execute(sql1)
        df = pd.read_sql(sql1, conn)
        logicv= LogisticRegression()
        logicv1= LogisticRegression()
        logicv.fit(df[['genre','size','price','os']], df['ratings'])
        logicv1.fit(df[['genre','size','price','os']], df['downloads'])
        Xnew = [[os1,genre1,size2,price2]]
        Xnew1= [[os1,genre1,size2,price2]]
        res1= logicv.predict(Xnew)
        res2= logicv1.predict(Xnew1)
        result.rating=res1
        result.downloads= res2
        return render_template('display.html', result=result)
   



if __name__ == '__main__':  
	app.run(debug=True)


