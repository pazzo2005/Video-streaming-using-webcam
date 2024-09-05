from flask import Flask,redirect,url_for,render_template,request
app= Flask (__name__)
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score >= 50:
        res='pass'
    else:
        res='fail'
    return render_template('result.html',result=res)
@app.route('/members')
def members():
    return 'welcome namste'
@app.route('/fail/<int:score>')
def fail(score):
    return 'the score of the match is :'+str(score)
@app.route('/check/<int:marks>')
def check(marks):
    return "<html><body><div class='<h1 style='color:red;'>the result is passed </h1></body></html>"
                       
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        eng=request=float(request.form['eng'])
        social=float(request.form['social'])
        total_score=(science+maths+eng+social)/4
    res=""
    if total_score>=50:
        res="success"
    else:
        res="fails"
    return redirect(url_for(res,score=total_score))
if __name__=='__main__':
    app.run(debug=True)

