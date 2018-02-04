import gmail
import datetime
from summa import summarizer
from flask import Flask, render_template
app = Flask(__name__)
username = 'daaksterangel@gmail.com'
password = **Password**
g = gmail.login(username, password)
dd = datetime.date.today()
mails = g.inbox().mail(after=dd)
mbody = []
msubj = []
rawsender = []
msend = []
msendmail = []
ans = []
for i in mails:
	i.fetch()
	mbody.append(i.body)
	rawsender.append(i.fr)
	msubj.append(i.subject)

for i in rawsender:
	i=i.replace("<","'")
	i=i.replace(">","")
	y=i.split("'")[0]
	msend.append(y[0])
	msendmail.append(i.split("'")[1])

for i in mbody:
	try:
		summ = summarizer.summarize(i)
		pass
	except Exception:
		summ = i
		pass
	ans.append(i)
	
for i in ans:
	print i
msubj.reverse()
msend.reverse()
ans.reverse()
mbody.reverse()
@app.route("/pro")
def home():
  return render_template("inbox.html", subjects=msubj, name=msend)
@app.route('/<i>')
def mail(i): 
  i = int(i)-1
  #print len(resu)
  #print i
  #print resu[i]
  #print subjects[i]
  #print orig[i]
  return render_template("mails.html",content=ans[i],subjects=msubj[i],origmail=mbody[i],name=msend[i])
app.run()
