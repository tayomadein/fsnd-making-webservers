from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "This page shows all restaurants plus a button to add a new restaurant"

@app.route('/restaurant/new')
def newRestaurant():
    return "This page will be for making a new restaurant"

@app.route('/restaurant/edit')
def editRestaurant(restaurant_id):
    return "This page will be for editing %s restaurant's details" % restaurant_id

@app.route('/restaurant/delete')
def deleteRestaurant(restaurant_id):
    return "This page will be for deleting %s restaurant" % restaurant_id

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return "This page show the menu for %s restaurants" % restaurant_id

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "This page is for adding a new menu item for %s restaurants" % restaurant_id

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This page is for editing %s menu item for %s restaurant" % (menu_id, restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "This page is for deleting %s menu item for %s restaurant" % (menu_id, restaurant_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
