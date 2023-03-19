# Step 1 : Import Flask
from flask import Flask,request,render_template
import re

# Step 2 : Create a Object with Parameter __name__
app=Flask(__name__)

# Step 3 : Create an END POINT usingroutes and bind then with a Functionally

@app.route('/')
def home():
    return render_template('regex101.html')

@app.route('/result',methods=['POST'])
def result():
      test_string=request.form.get('test_string')
      regex=request.form.get('regex')
      matchedstrings=re.findall(regex,test_string)
      length=len(matchedstrings)
      return render_template('results.html', matchedstrings=matchedstrings,length=length)

# Step 5 : Run the Flask
if __name__ == "__main__":
    app.run(debug=True)