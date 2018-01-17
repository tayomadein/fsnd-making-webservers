from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

## import for CRUD operations
from database_setup import Restaurant, Base, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant = restaurant, items = items)

#Task 1: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name = request.form['name'], description = request.form['desc'], price  = request.form['price'], restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
         return render_template('newmenuitem.html', restaurant_id = restaurant_id)

#Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "Page to edit a menu item."

#Task 3: Create route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "Page to delete a menu item."

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
