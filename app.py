from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask Calculator Application'

@app.route('/calculate',methods=['POST','GET'])
def calculate():

    if request.method=='GET':
        return render_template('calculate.html')
    
    else:
        operation=request.form['operation']
        n1=float(request.form['number1'])
        n2=float(request.form['number2'])
        
        if operation=='add':
            result=n1+n2
        elif operation=='subtract':
            result=n1-n2
        elif operation=='multiply':
            result=n1*n2
        else:
            result=n1/n2

        return render_template('calculate.html',results=result)


if __name__=='__main__':
    app.run()