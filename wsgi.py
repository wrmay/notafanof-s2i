from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<html><body><div style=\"width:800px;font-size:x-large\"><div>Now, instead of \"having to understand Docker files\", <span style=\"font-style:italic\">I have to understand the undocumented conventions baked into many different s2i images.</span></div></body></html>"
