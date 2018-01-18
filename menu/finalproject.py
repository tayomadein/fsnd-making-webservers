from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
## shows a list of all restaurants
def showRestaurants():
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurant/new')
## Create a new restaurant
def newRestaurant():
    return render_template('newrestaurant.html')

@app.route('/restaurant/edit')
## Edit a restaurant's info
def editRestaurant(restaurant_id):
    return render_template('editrestaurant.html', restaurant_id=restaurant_id)

@app.route('/restaurant/delete')
## Delete a restaurant
def deleteRestaurant(restaurant_id):
    return render_template('deleterestaurant.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
## Show menu for one restaurant
def showMenu(restaurant_id):
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/restaurant/<int:restaurant_id>/menu/new')
## Add a new menu item to a restaurant's menu
def newMenuItem(restaurant_id):
    return render_template('newmenuitem.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
## Edit a menu item
def editMenuItem(restaurant_id, menu_id):
    return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, i=editedItem)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
## Delete a menu item
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, i=deleteItem)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
