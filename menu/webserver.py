from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

## import for CRUD operations
from database_setup import Restaurant, Base, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h2><a href ='/restaurants/new'>Make a New Restaurant</a></h2>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    output += "<a href ='/restaurants/%s/edit'>Edit</a>" % restaurant.id
                    output += "</br>"
                    output += "<a href ='/restaurants/%s/delete'>Delete</a>" % restaurant.id
                    output += "</br>"
                    output += "</br>"

                output += "</body></html>"
                self.wfile.write(output)
                #print output
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name='newRestaurantName' type='text' placeholder = 'New Restaurant Name' ><input type='submit' value='Create' ></form>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                
                if myRestaurantQuery != [] :
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>Edit Restaurant Name</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath
                    output += "<input name='newRestaurantName' type='text' placeholder = '%s' >" % myRestaurantQuery.name
                    output += "<input type='submit' value='Update' ></form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    return

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                
                if myRestaurantQuery != [] :
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>Delete Restaurant %s permanently?</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<input type='submit' value='Delete' ></form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)
        
    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                restaurantname = fields.get('newRestaurantName')

                #Create new restaurant class
                newRestaurant = Restaurant(name = restaurantname[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()
            
            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                restaurantname = fields.get('newRestaurantName')
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                if myRestaurantQuery != [] :
                    myRestaurantQuery.name = restaurantname[0]
                    session.add(myRestaurantQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type')) #not necessary for solution

                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                if myRestaurantQuery != [] :
                    session.delete(myRestaurantQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            ''' self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += "<h2>Okay, how about this:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit' value='Submit' ></form>"
            output += "</body></html>"
            self.wfile.write(output)
            print output '''

        except:
            pass

def main():
    '''Main Server'''
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
