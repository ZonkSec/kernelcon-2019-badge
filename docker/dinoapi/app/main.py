from flask import Flask, request, render_template_string
import requests

app = Flask(__name__, static_url_path='/static')
ids =	{
  "60551a081babe": ["Tyrannosaurus","Bingo! Dino DNA! #1: kernel{c877b82a6d92fd0105410072f51464d3}"], #freebie exmaple
  "4c09dcb3f923a": ["Stegosaurus","Bingo! Dino DNA! #5: kernel{145a8226a9982f0e9c295c54f0e158d8}"], #silkscreen
  "69631e0070": ["Velociraptor","Bingo! Dino DNA! #2: kernel{36b44b75349159e6be80ddf21433853d}"], #hacker badge
  "d09468528e": ["Brachiosaurus","Bingo! Dino DNA! #4: kernel{8c1f6fbf12d5f56c19a381666a14cfd0}"], #org&crew badge
  "1825981d38": ["Dilophosaurus","Bingo! Dino DNA! #3: kernel{1825981d38dc49290dc1db6fb11f7605}"] #speaker badge
  }

@app.route("/",methods=['GET'])
def hello():
	DinoID = request.args.get('DinoID')
	if DinoID:
		if DinoID in ids:
			message = "DinoID: " + DinoID + " recognized!"
			message1 = "Name: " + ids[DinoID][0]
			message2 = ids[DinoID][1]
			return render_template_string("""
			<h1>ULTRA SECRET DINO DNA SERVICE</h1>
			<h3>only host this service api on localhost to make sure we dont expose our proprietary dino DNA to external competitors</h3>
			
			{{message}}
			</br>
			{{message1}}</br>
			DNA: </br>
			<pre>
			CAACCTCCAATACCTCGTATCATTGTGCACCTGCCGGTGACCACTCAACG
			GTGGGGACGCCGTTGCAACTTCGAGGACCTAATGTGACCGACCTAGATTCGGCAT
			TGTGGGCAGAATGAAGTATTGGCAGACATTGAGTGCCGAACAAGACCTGACCTAA
			CGGTAAGAGAGTCTCATAATACGTCCGGCCGCATGCGCAGGGTATATTTGGACAG
			TATCGAATGGACTCTGATGAACCTTTACACCGATCTAGAAACGGGTGCGTGGATT
			AGCCAGGTGCAAACCAAAAATCCTGGGCTACTTGATGTTTTGTGACGTTCTAAGA
			GTTGGACGAAATGTTTCGCGACCTAGGATGAGGTCGCCCTAGAAAATAGATTTGT
			GCTACTCTCCTCATAAGCAGTCCGGTGTATCGAAAGTACAAGACTAGCCTTGCTA
			GCAACCGCGGGCTGGGAGCCTAAGGTATCACTCAAGAAACAGGCTCGGTAACATA
			CGCTCTAGCTATCTGACTATCCCCTACGTCATATAGGGACCTATGTTATCTGCGT
			GTCCAACCTTAGGATTCACTTCAGCGCGCAGGCTTGGGTCGAGATAAAATCTCCA
			GTGCCCAAGACCACGGGCGCTCGGCGCCTTGGCTAATCCCCGTACATGTTGTTAT
			AATAATCAGTAGAAAGTCTGTGTTAGAGGGTGGAGTGACCATAAATCAAGGACGA
			TATTAATCGGAAGGAGTATTCAACGTGATGAAGTCGCAGGGTTAACGTGGGAATG
			GTGCTTCTGTCCTAACAGGTTAGGGTATAATGCTGGAACCGTCCCCCAAGCGTTC
			AGGGTGGGCTTTGCTACGACTTCCGAGTCCAAAGACTCCCTGTTTTCGAAATTTG
			CGCTCAAGGGCGAGTATTGGACCTGGCTTACGCCTTAGTACGTAGCAAGGTGACA
			CAAGCACAGTAGATCCTGCCCGCGTTTCCTATGTATCAAGTTAGAACTTATGGAA
			TATAATAACATG</pre></br>
			
			{{message2}}
			""",message=message,message1=message1,message2=message2)
		else:
			message = "DinoID not recognized!"
			return """
			<h1>ULTRA SECRET DINO DNA SERVICE</h1>
			<h3>only host this service api on localhost to make sure we dont expose our proprietary dino DNA to external competitors</h3>
			
			<p>DinoID not recognized!</p>
			
			"""
	else:
		return """
		<h1>ULTRA SECRET DINO DNA SERVICE</h1>
		<h3>only host this service api on localhost to make sure we dont expose our proprietary dino DNA to external competitors</h3>
		<p>to use this API, pass the dinosaur ID (looks like: DinoID=60551a081babe) as a param.</p>
		
		
		
		kernel{26abf0045be8eaf39b2d6ece49f1be7b}
		"""


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=1337)