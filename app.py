import ptvsd
try:
    ptvsd.enable_attach(address=('0.0.0.0', 4000))
    ptvsd.wait_for_attach()
except Exception as ex:
    raise e


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = "Hello there!"
    return message


if __name__ == "__main__":
    app.run()