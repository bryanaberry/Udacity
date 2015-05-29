import cgi
import urllib

from google.appengine.api import users

from google.appengine.ext import ndb


import webapp2

HTML_PAGE_MAIN = """\
    <body bgcolor="#E6E6FA">
    <title>BERRY's BLOG</title>
    <div>Welcome the Berry's Blog Spot.  Please Login and spill your guts!
    </div><hr>

    <div><form action="/sign?%s" method="post">
      <div><textarea name="content" rows="15" cols="120"></textarea></div>
      <div><input type="submit" value="Post to Blog"></div>
    </form>
    <hr>
    <form>Berry's Blog Name:
      <input value="%s" name="berry_blog_name">
      <input type="submit" value="switch">
    </form>
    <a href="%s">%s</a></div>
  </body></body>
</html>
"""

Default_berry_blog_name = 'Berry Blog'



def berryblog_key(berry_blog_name=Default_berry_blog_name):
  
    return ndb.Key('berryblog', berry_blog_name)



class Author(ndb.Model):
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Blogger(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)




class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>')
        berry_blog_name = self.request.get('berry_blog_name',
                                          Default_berry_blog_name)

        
        bloggers_query = Blogger.query(
            ancestor=berryblog_key(berry_blog_name)).order(-Blogger.date)
        bloggers = bloggers_query.fetch(10)

        

        user = users.get_current_user()
        for blogger in bloggers:
            if blogger.author:
                author = blogger.author.email
                if user and user.user_id() == blogger.author.identity:
                    author += ' (You)'
                self.response.write('<b>%s</b> wrote:' % author)
            else:
                self.response.write('An anonymous blogger wrote:')
            self.response.write('<blockquote>%s</blockquote>' %
                                cgi.escape(blogger.content))

        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        sign_query_params = urllib.urlencode({'berry_blog_name':
                                              berry_blog_name})
        self.response.write(HTML_PAGE_MAIN %
                            (sign_query_params, cgi.escape(berry_blog_name),
                             url, url_linktext))



class berryblog(webapp2.RequestHandler):
    def post(self):
        
        berry_blog_name = self.request.get('berry_blog_name',
                                          Default_berry_blog_name)
        blogger = Blogger(parent=berryblog_key(berry_blog_name))

        if users.get_current_user():
            blogger.author = Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

        blogger.content = self.request.get('content')
        blogger.put()

        query_params = {'berry_blog_name': berry_blog_name}
        self.redirect('/?' + urllib.urlencode(query_params))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', berryblog),
], debug=True)
