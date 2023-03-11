# Step 1 : Import Flask
from flask import Flask,request

# Step 2 : Create a Object with Parameter __name__
sai = Flask(__name__)

# Step 3 : Create an END POINT usingroutes and bind then with a Functionally
@sai.route('/')
def home_page():
    return "Welcome to the Home Page"


@sai.route('/fun')
def fun():
    user_name = request.args.get('user_name')
    return "Welcome "+user_name+"!, How are you ? This is a Fun Page"


@sai.route('/add')
def addition():
    a=request.args.get('a')
    b=request.args.get('b')
    return "Addition of "+a+" + "+b+" : "+str(int(a)+int(b))


@sai.route('/upper')
def upper_case():
    user_name = request.args.get('user_name')
    return "Upper Case of "+user_name+" : "+user_name.upper()


@sai.route('/lower')
def lower_case():
    user_name=request.args.get('user_name')
    return "Lower Case of "+user_name+" : "+user_name.lower()


@sai.route('/sub')
def subtraction():
    a=request.args.get('a')
    b=request.args.get('b')
    return "Subtraction of "+a+" - "+b+" : "+str (int (a) - int (b))


@sai.route('/factorial')
def fact():
    a=request.args.get("a")
    n=int(a)
    sum_=1
    for i in range(1,n+1):
     sum_=sum_*i
    return "Factorial of "+a+"! : "+str(int(sum_))

# Step 5 : Run the Flask
if __name__=='__main__':
    sai.run(debug=True)                                                         

'''
Input and Output

http://127.0.0.1:5000/fun?user_name=Siva
Welcome Siva!, How are you ? This is a Fun Page

http://127.0.0.1:5000/upper?user_name=sai
Upper Case of sai : SAI

http://127.0.0.1:5000/lower?user_name=SAI
Upper Case of SAI : sai

http://127.0.0.1:5000/add?a=5&b=6
Addition of 5 + 6 : 11

http://127.0.0.1:5000/sub?a=5&b=6
Subtraction of 5 - 6 : -1

http://127.0.0.1:5000/factorial?a=5
Factorial of 5! : 120
'''