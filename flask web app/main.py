from website import create_app

app = create_app()

#only if we run this file, not import file, will we then execute the line below
#only to run the web server if you actually run this file directly
if __name__ == '__main__':
    app.run(debug=True)

"""
FLASK_APP=hello.py flask run
"""