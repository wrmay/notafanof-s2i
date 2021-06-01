from flask import Flask

application = Flask(__name__)

@application.route("/")
def main():
    return "<html><body><div style=\"width:800px;font-size:x-large\"><div>Webhook Test 2</div><div>Now, instead of \"having to understand Docker files\", <span style=\"font-style:italic;color:blue\">I have to understand the undocumented conventions baked into many different s2i images.</span></div></div></body></html>"
