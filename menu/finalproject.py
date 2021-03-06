from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
## import for CRUD operations
from database_setup import Restaurant, Base, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

#Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
## shows a list of all restaurants
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurant/new', methods = ['GET', 'POST'])
## Create a new restaurant
def newRestaurant():
    if request.method == 'POST':
        newRestaurantEntry = Restaurant(name=request.form['name'])
        session.add(newRestaurantEntry)
        session.commit()
        flash("New Restaurant Created!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newrestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit', methods = ['GET', 'POST'])
## Edit a restaurant's info
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        flash("Restaurant Successfully Edited")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editrestaurant.html', restaurant_id=restaurant_id, i=editedRestaurant)

@app.route('/restaurant/<int:restaurant_id>/delete', methods = ['GET', 'POST'])
## Delete a restaurant
def deleteRestaurant(restaurant_id):
    deletedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedRestaurant)
        session.commit()
        flash("Restaurant Successfully Deleted")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleterestaurant.html', restaurant_id=restaurant_id, i=deletedRestaurant)

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
## Show menu for one restaurant
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/restaurant/<int:restaurant_id>/menu/new', methods = ['GET', 'POST'])
## Add a new menu item to a restaurant's menu
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form['desc'], price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New Menu Item Created!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods = ['GET', 'POST'])
## Edit a menu item
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['desc']:
            editedItem.description = request.form['desc']
        if request.form['price']:
            editedItem.price = request.form['price']
        session.add(editedItem)
        session.commit()
        flash("Menu Item Successfully Edited")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, i=editedItem)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods = ['GET', 'POST'])
## Delete a menu item
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash("Menu Item Successfully Deleted")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, i=deleteItem)

#API Endpoints
@app.route('/restaurants/JSON/')
def restaurantJSON():
    ''' API Endpoint for all restaurants (GET Request) '''
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[restaurant.serialize for restaurant in restaurants])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    ''' API Endpoint for all menus items filtered by restaurant_id (GET Request) '''
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def menuItemJSON(restaurant_id, menu_id):
    ''' API Endpoint for a single menu item'''
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)

if __name__ == '__main__':
    app.secret_key = 'my_super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
