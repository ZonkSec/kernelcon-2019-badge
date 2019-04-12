from flask import Flask, request, render_template_string
import requests

app = Flask(__name__, static_url_path='/static')

@app.route("/",methods=['GET','POST'])
def home():
	if request.method == 'POST':
		try:
			URL = request.form.get('url')
			headers = {'X_DINO_AUTH_FLAG': 'kernel{f5ddb063e92808b472c31d82c887d791}'}
			r = requests.get(url = URL,headers=headers)
			body = r.text
			header = r.headers
		except:
			URL = "nowhere. you broke me!"
			body = ""
			header = ""
		return render_template_string("""
		<img align="left" src="/static/image.png" height="300"><h1>Hello! I'm Denis Nedry!</h1>
		<p>I made a data fetching application!</p>
		<p>It will...ummm... help us inovate better!</p>
		<p>I hope I built it right so that it doesnt expose any sensative data! ;)</p></br>
		<!--hey its denis. my dumb colleagues wont see this secret note. this data fetcher should get you the local access you need ;) -->
		<p>kernel{0caa7cca96914a00aaf1367542610487}</p>
		</br></br></br></br></br></br></br>
		<form action="/" method="post">
			<h3>What data should I fetch?</h3><br>
			URL:  <input type="text" name="url" value="{{URL}}" size="70">
			<input type="submit" value="Submit">
		</form> 

		<h3>I fetched data from: {{URL}}!</h3>
		<h3>headers</h3>
		<pre>{{header}}</pre></br>
		<h3>body</h3>
		<pre>{{body}}</pre>
		""",body=body,URL=URL,header=header)
	else:
		return """
		<img align="left" src="/static/image.png" height="300"><h1>Hello! I'm Denis Nedry!</h1>
		<p>I made a data fetching application!</p>
		<p>It will...ummm... help us inovate better!</p>
		<p>I hope I built it right so that it doesnt expose any sensative data! ;)</p></br>
		<!--hey its denis. my dumb colleagues wont see this secret note. this data fetcher should get you the local access you need ;) -->
		<p>kernel{0caa7cca96914a00aaf1367542610487}</p>
		</br></br></br></br></br></br></br>
		<form action="/" method="post">
			<h3>What data should I fetch?</h3><br>
			URL:  <input type="text" name="url" value="https://en.wikipedia.org/wiki/List_of_dinosaur_genera" size="70">
			<input type="submit" value="Submit">
		</form> 
		"""


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)