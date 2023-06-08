from market import app, db
from market.models import User
#import applicaiton from market package and run it
#checks if run.py file has executed directly
# Create the application context
with app.app_context():
    # Create the database tables
    db.create_all()
    u1 = User(username='jsc', password_hash='123456', email_address='jsc@jsc.com')
    db.session.add(u1)
    db.session.commit()

if __name__ == '__main__':
  app.run(debug=True)

#TO SETUP A VIRTUAL ENVIRONMENT (as to avoid conflicts)
#python -m venv myenv
#activate virtual environment: source myenv/bin/activate
#deactivate

#export FLASK_APP=market.py
#export DEBUG=1
#flask run
