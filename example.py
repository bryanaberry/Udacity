
  
notifications of @name mentions, replies to your posts and topics, messages, etc
search topics, posts, users, or categories
go to another topic list or category

Stage 4 Webcasts
 Intro to Programming Broadcast Webcast Notes
Stage 4 Webcasts
 Intro to Programming Broadcast Webcast Notes
3 / 3
 

RandaUdacity CoachApr 28 2 
Air Date: 4/21/2015
Video9

Generate Notes with Google App Engine
What We Will Learn
We will go over 3 main things in this office hours:

How to use webapp2
How to put your notes up on GAE
How *args and **kwargs work as arguments and parameters to functions
How to use webapp2

A few links which will help you learn how webapp2 works:

https://webapp-improved.appspot.com/api/webapp2.html7
https://webapp-improved.appspot.com/guide/handlers.html7
Every url in your website needs a Handler: A handler will specify what code runs when a user goes to a particular url on your website.

On the bottom of your Google App Engine code, you’ll notice something like this:

app = webapp2.WSGIApplication([
    (r'/products/(\d+)', ProductHandler),
    (r’/‘, ‘HelloWebapp2),  
])
Notice the parameter that webapp2.WSGIApplication takes as an input: a list, each containing a tuple matching url paths (or, specifically, regex (regular expressions) that match possible url paths) to class names. This is the ‘routes’ parameter, and it will match each url path set with the class name of the class which specifies the behavior that the particular url path will run on the website.

Each class specified here will also inherit from webapp2 (either directly or indirectly); this time from webapp2.RequestHandler

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write(‘Hello World!’)
These classes will specify HTTP requests and what will be run on those requests; you’ll generally be specifying get() and post() here.

You will normally specify some sort of generic Handler class, which will handle different types of of html generation and which your url path specific classes will inherit from. An example is below:

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Handler(webapp2.RequestHandler): 
    """
    Basic Handler; will be inherited by more specific path Handlers
    """
    def write(self, *a, **kw):
        "Write small strings to the website"
        self.response.out.write(*a, **kw)  

    def render_str(self, template, **params):  
        "Render jija2 templates"
        t = JINJA_ENVIRONMENT.get_template(template)
        return t.render(params)   
    
    def render(self, template, **kw):
        "Write the jinja template to the website"
        self.write(self.render_str(template, **kw))
Putting Your notes online

One thing that you will use GAE for is putting your notes online. The easiest way to this would be to use the above basic Handler, and use a get function like the below:

class SomeHandler(Handler):
    def get(self):
        self.render("your_notes.html")
Now, if you specify a path for your html to live on, you can view them online! Let’s use /notes for our path:

app = webapp2.WSGIApplication([
    ('/notes', SomeHandler)
], debug=True)
If we want to use css styling, we should make sure GAE uses it:

first, add a folder to our .yaml

- url: /static
  static_dir: static
Make sure to do this before this:

- url: .*
  script: main.app
Or the static files won't be read. Then put your css files in that folder you created (which I've named 'static'), and make sure your html references that path.

If you deploy your app from GAE launcher, you can now view your notes directly online!

*args and **kwargs

A useful link explaining how to use them: http://stackoverflow.com/questions/3394835/args-and-kwargs3
*args can be used to pass multiple parameters into a function, while **kwargs can pass an undetermined number of named parameters into a function.

Named parameters

def some_function(param1, param2):
    print param1, param2
Now, we can pass in 2 unnamed parameters and see what we get:

some_function(1,2)
#>>>1, 2
This is the normal way you've been passing in parameters to a function. Parameters can also be specified by name, instead of position:

some_function(param2 = 1, param1 = 2)
#>>>2, 1
Notice that we specified param2, which is the second parameter in the definition, first.

*args

some_list = [1,2]
some_function(*some_list)
#>>>1,2
Here, you see that despite the fact that the function took 2 parameters, it successfully ran with a single unpacked list as input.

**kwargs

some_dict = {"param1" : "parameter 1", "param2": "parameter 2"}
some_function(**some_dict)
#>>>parameter 1 parameter 2
This can also be done in reverse; defining a function to take multiple parameters, whether named (**kwargs) or unnamed (*args)

def some_other_function(*args, **kwargs):
    for arg in args:  #args is like a list
        print arg
    for kwarg in kwargs:  #kwargs is like a dictionary
        print kwarg, kwargs[kwarg]

x = 1
y = 2
z = ['a', 'b']
a_dict = {'hello': 'World!'}
a_tuple = (1,2,3,4,5)

some_other_function(x, y, z, some_dictionary = a_dict, some_tuple = a_tuple)     
#>>>args:
#>>>1
#>>>2
#>>>['a', 'b']
#>>>kwargs:
#>>>some_dictionary  :  {'hello': 'World!'}
#>>>some_tuple  :  (1, 2, 3, 4, 5)
Summary
webapp2 is the main Python module you will be using for Google App engine; it creates a WSGIApplication application which will direct your url paths to the Python code which will handle them.
*args and **kwargs can let you give an indeterminate number of parameters to a function, or pass in lists, tuples, or dictionaries into functions which take multiple specific parameters

1 person liked this. Like it too.

created
Apr 28
last reply
20 hours 2
replies
106
views
1
user
1
like
16
links
3
Stage 2 Webcasts2
Webcast Directory
Reply as linked Topic

RandaUdacity CoachMay 6 2 
Air Date: 4/28/2015
Video2

Using Dictionaries in Python
Review of Lists:
coaches = [["Mark", "Intro to Computer Science"],
           ["Jeff", "Web Development"],
           ["Randa", "Intro to Data Science"]]
If we want to isolate the information about the first coach, we would use the following line (don't forget that indexes start with 0 in Python):

print coaches[0]
And we would see:

["Mark", "Intro to Computer Science"]
If we now want to isolate Mark's favorite class, we would use:

print coaches[0][1]
"Intro to Computer Science"
We can also add more information about each of our coaches in the list:

coaches = [["Mark", "Intro to Computer Science", "IPND", 13],
           ["Jeff", "Web Development", "FEND", 5],
           ["Randa", "Intro to Data Science", "IPND", 17]]
The problem with this type of data storage is that it is necessary to remember where each type of data is stored. Was the coach's favorite course stored in index 1 or 2?

List do however have their benefits, we don't want to ignore that. Lists are great for storing multiple pieces of information in a single variable.

Using Dictionaries to Avoid the Pitfalls of Lists:
mark = {}
To add information to the Mark's dictionary, we can do the following where the key is 'name' and the value is 'Mark':

mark['name'] = 'Mark'
So now the variable mark contains the following:

{'name': 'Mark'}
Now let's add more information:

mark['course'] = 'Intro to Computer Science'
mark['number'] = 13
The updated dictionary now looks like this:

{'course': 'Intro to Computer Science', 'name': 'Mark', 'number': 13}
Unlike lists, the order in which the information is added to the dictionary is not necessarily the order the dictionary displays.

Accessing information from a dictionary is similar to accessing information from a list, but instead of using an index the key is used instead.

print mark['name']
Would print the following:

'Mark'
Question: What happens if you misspell the key?
If we tried to run the following line:

print mark['nam']
We can expect the following key error:
KeyError: 'nam'

Question: Can you use other types of values as keys in a dictionary?
Yes! You can use integers and tuples1.

mark[13] = 'favorite number'
mark[(1,2)] = 'San Jose'
Question: What happens if you use a list for the key value?
Say we did the following:

pets = ['Rover', 'Goldie']
mark[pets] = 'Mark's favorite pets'
We would get the following error: TypeError: unhashable type:'list'
Python doesn't like this because it's fairly easy for use to change the list stored in pets:

pets.append('Spooky')
print pets
['Rover', 'Goldie', 'Spooky']
Useful Things to Know:
print mark.keys() returns a list of all the keys used in the dictionary `mark'.

Way to define the contents of the dictionary all at once:

mark = {
    'name': 'Mark'
    'course': 'Intro to Computer Science'
}
Nested dictionaries
coaches_dictionary = {
    'mark': {
        'name': 'Mark'
        'course': 'Intro to Computer Science'
    }
    'jeff': {
        'name': 'Jeff'
        'course': 'Web Development'
    }
    'randa': {
        'name': 'Randa'
        'course': 'Intro to Data Science'
    }
}
Accessing information in a nested dictionary:
print coaches_dictionary['mark']['name']
Interested in More Python Practice?
Checkout Learn Python the Hard Way2 and the course material from Intro to Computer Science1.


Stage 4 Webcasts
Webcast Directory
Reply as linked Topic

RandaUdacity Coach20h
Air Date: 6/9/2015
Video1

Google Datastore
Big Picture
Here is a link to a presentation that talks about the bigger picture of Google Datastore. Traditionally, when we think of databases, we think of rows and columns of data in a spreadsheet-like format.

Pasted image585x534 108 KB
Imagine we want to keep a database of image links, comments on the image, and the date that the comment has been made.

In flat-files or relational databases, the data is saved into a table as rows and columns. Instead of storing tables in Google Datastore, each row is instead saved as an object in the Google Datastore.

Everything is an Object
Therefore each row can be thought of as an object of the type "Pictures" and each object will contain the instance variables:

link
comment
datetime
Therefore in order to create Picture objects, we first need to define a class. This class will inherit the methods and properties of the ndb.Model class. Here is how you do it in Python:

from google.appengine.ext import ndb

class Picture(ndb.Model):
    link = ndb.StringProperty()
    comment = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
where we set each attribute a datatype we want such as string and datetime
Here is the documentation to reference the other types of data we can create in an ndb class: reference

Therefore, to create a picture object, we then instantiate an object:

picture = Picture(link='http://addresss.com/image.jpg',comment='Comment here')

We then use the put() method to actually write this object to the Google Datastore servers:

picture.put()

Querying
In order to query or pull the objects from the Google Datastore, we use the class method query() on our target class to pull a reference object to our Picture objects.

query = Picture.query()

This example code queries for all objects in the entire database. If we want to create a query that gets pictures that were created on the day of 6/1/15, we would use this query:

from datetime import datetime
date_begin = datetime(2015,6,1)
date_end = datetime(2015,6,2)

query = Picture.query(Picture.date >= date_begin, Picture.date < date_end)
With this query, we can simply iterate through all pictures in the query with a For loop:

for picture in query:
    # Do stuff with the picture object
To fetch only a limited number of pictures, we use the fetch(number_of_pictures) method:

pictures = query.fetch(10)
Would give us a list of 10 picture objects

More information on other ways to query can be found here.

Writing Out to the Website
With our list of pictures, we can then access the link and comment information inside our picture objects and write the information out to the Web site by converting the information into a string for the self.response.out.write() method.

For example, if we want to write out the link and comment information for the first picture in our pictures list, we can do this in a GET request:

class MainPage(webapp2.RequestHandler):
    def get(self):
        picture = pictures[0]
        message = '<h3>Here is the picture:</h3>\n' 
        message += '<img src="' + picture.link + '" alt="picture">\n'
        message += <h3>And this is the comment of this picture link:</h3>\n'
        message += '<p>' + picture.comment + '</p>'
        self.response.out(message)
Reference
Please refer to a full working example below of a website that allows users to post pictures and post a comment on the site. The site will store the user's post in the Datastore and will produce the submitted content upon a GET request:

import webapp2
from google.appengine.ext import ndb

# Step 1: Define Picture Class to store links of pictures
class Picture(ndb.Model):
    link = ndb.StringProperty()
    comment = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

# Further documentation to find out what other types of properties we can make:
# https://cloud.google.com/appengine/docs/python/ndb/properties

# DEBUG: Step 2: Populate our Datastore for Testing

# pic1 = Picture(link='http://img.bleacherreport.net/img/images/photos/003/357/607/hi-res-216c4eca516bb24626745dc1e9d0f5ab_crop_north.jpg?w=630&h=420&q=75',
#               comment='Love this drawing! Go Golden State!')

# pic2 = Picture(link='http://img.bleacherreport.net/img/images/photos/003/358/305/hi-res-3d12fb6698c432801d1b399ebe3d258f_crop_north.jpg?w=630&h=420&q=75',
#               comment='LeBron going to take it all they way!')

# pic1.put()
# pic2.put()
# Need to wait a little bit for local Datastore to update.
# import time
# time.sleep(.1)

# Our html template
HTML = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>NBA Pictures!</title>
    <style>
        input[type='text'] {
          width: 412px;
        }
        th {
          color: teal;
        }
        td {
          border: 1px solid black;
        }
        img {
          width: 450px
        }
        label {
          font-weight: bold;
        }
        .error {
          color: red;
        }
    </style>
</head>
<body>
    <h1>Hello NBA fans! Go ahead and submit a picture link and comment on the picture!</h1>
    <!-- Insert table of pictures here -->
    %s
    <br>
    <span class="error">%s</span>
    <form method="post" action="/">
        <label>Link</label><br><input type="text" name="link"><br>
        <label>Comment</label><br><textarea name="comment" rows=10 cols=66></textarea><br>
        <input type="submit">
    </form>
</body>
</html>'''

# --------------------------Handler Classes--------------------------------------

class MainPage(webapp2.RequestHandler):
    def get(self):

        # Check for error message
        error = self.request.get('error','')
        # print '#####'
        # print error
        # print '#####'

        # Query the Datastore and order earliest date first
        query = Picture.query().order(Picture.date)

        # Test to see print out the list of picture objects
        # pictures_list = query.fetch(5)

        # print '#####'
        # print len(pictures_list)
        # print pictures_list[0]
        # print '#####'

        # Test to print out all the picture objects
        # print '#####'
        # for picture in query:
        #   print picture
        # print '#####'

        # Step 3: Write information from the Datastore and build the HTML table
        table = '<table>\n<tr><th>Link</th><th>Comment</th></tr>\n'
        for picture in query:
            link = picture.link
            comment = picture.comment

            row = '<tr>\n'
            row += '<td><img src="' + link + '" alt="picture"></td>\n'
            row += '<td>' + comment + '</td>\n'
            row += '</tr>\n'

            table += row
        table += '</table>\n'

        rendered_html = HTML % (table,error)

        self.response.out.write(rendered_html)

    def post(self):
        link = self.request.get('link')
        comment = self.request.get('comment')

        # Test to see link and comment
        # print '#####'
        # print link, comment
        # print '#####'

        # Step 4: Allow ability to create picture objects and save to Datastore

        if link and comment:
            picture = Picture(link=link, comment=comment)
            picture.put()
            # DEBUG: For local development. Need to wait a little bit for the 
            # local 
            # Datastore to update
            import time
            time.sleep(.1)
            self.redirect('/')
        else:
            self.redirect('/?error=Please fill out the link and comment sections!')


router = [('/',MainPage)]

app = webapp2.WSGIApplication(router,debug=True)
For a full reference of all of the methods and instances relating to the ndb class, please go here1


Reply as linked Topic
BookmarkShareFlag
 Tracking
You will receive notifications because you read this topic.

Suggested Topics
Topic	Category	Replies	Views	Activity
Webcast Directory new	 Webcast Notes	0	8	19h
General Information	 Webcast Notes	2	31	8d
Stage 2 Webcasts	 Webcast Notes	6	196	14d
Stage 3 Webcasts	 Webcast Notes	1	103	19h
There are 6 unread and 155 new topics remaining, or browse other topics in  Webcast Notes
