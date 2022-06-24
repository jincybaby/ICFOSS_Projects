from flask import Flask, render_template, flash, request, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from markupsafe import Markup

from resultnew import *

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
	name = TextField('Name:', validators=[validators.required()])

@app.route('/', methods=['GET', 'POST'])
def my_form():
	form = ReusableForm(request.form)
	print (form.errors)
    
	if request.method == 'POST':
		oldword=request.form['name']
		word=oldword.replace("ർ","ര്‍").replace("ൾ","ള്‍").replace("ൽ","ല്‍").replace("ൺ","ണ്‍").replace("ൻ","ന്‍")
		flash (word)
        
	if form.validate():
		FINAL=root(word)
		flash (' '.join(str(x) for x in FINAL))
		out=[]
		rt=FINAL[0]
		cleanedList=FINAL[1:]
		if rt.endswith("\u0d4d"):
			wort=re.sub("\u0d4d"+'$',"\u0d41"+"ക",rt)
			if wort in vedict:
				rt=wort
		else:
			wor=rt+"\u0d02"
			if wor in mydict:
				rt=wor
		roots=NV(rt,cleanedList)
		if roots!=[rt]:
			tag1=roots[1]
		else:
			tag1=None
		flash(' '.join(str(x) for x in roots))

		if cleanedList!=[]:
			for wo in cleanedList:
				indwo=cleanedList.index(wo)
				wonew=[]
				if wo.endswith("\u0d4d"):
					wor=re.sub("\u0d4d"+'$',"\u0d41"+"ക",wo)
					if wor in vedict:
						wonew=[wor]
				if wonew==[wo] or wonew==[]:
					wonew=verb(wo,myloop2,filee,stop1)
				if wonew[0] in mydi:
					wonewli = clean(wonew)
					if wonewli!=[wo]:
						del cleanedList[indwo]
						cleanedList[indwo:indwo] = wonewli

			for i in li:
				if tag1=="Verb" and cleanedList==i[:-1]:
					tag2=[i[-1]]
					out=cleanedList+tag2
					flash (' '.join(str(x) for x in out))
					break

			outp=[]
			if out==[]:
				for i in cleanedList:
					out=tag(i)
					if out==None:
						out=[i]
					d=' '.join(str(x) for x in out)
					outp.append(d)

				flash ('  '.join(map(str,outp)))

	return render_template('home1.html', form=form)


if __name__ == '__main__':
    app.run()