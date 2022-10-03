from flask import Flask,render_template,request# flask import statement

app = Flask(__name__) #creating the Flask class object   

@app.route('/') #decorator defines route
def calculator():  
    return render_template('index.html')

@app.route('/calculate/',methods = ['POST'])
def calculate():
    fnum = int(request.form['fnum'])
    snum = int(request.form['snum'])
    res = 0
    if request.form.get('addBtn'):
        res = fnum + snum
        response = f"{fnum} + {snum} = {res}"
    elif request.form.get('subBtn'):
        res = fnum - snum
        response = f"{fnum} - {snum} = {res}"
    elif request.form.get('multiBtn'):
        res = fnum * snum
        response = f"{fnum} X {snum} = {res}"
    elif request.form.get('divBtn'):
        res = fnum / snum
        response = f"{fnum} / {snum} = {res}"
    return render_template("index.html",fnum = fnum,snum = snum,result = response)


    
    

if __name__ =='__main__':  
    app.run(debug = True)  