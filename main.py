import datetime
import webapp2
import jinja2
import os

from google.appengine.api import users

template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        current_time = datetime.datetime.now()
        self.response.out.write(current_time)
        
application = webapp2.WSGIApplication([('/', MainPage)], debug=True)