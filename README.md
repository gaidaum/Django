
# Eatatdcu ReadMe

#### Synopsis

The project allows for the search of restaurants and cafes in DCU campus'. The main function of the site is to help students, staff and visitors to find opened dining places. As it shows the opening and closing times. All restaurants come with a spacial today meal. Which can be accessed by clicking the "specials" button.

#### Code Example

This is one of the main logic in this project. Starting from the top it checks if there's an error with the search. If it passes then it goes to the "else" section where for all the restaurants and cafes it outputs the opening and closing hours and also tells us if it is opened on weekends. It also outputs the "specials" link beside the restaurants.

``` HTML

{% if error %}
   {{ error }}

{% else %}
<center>
   <h3>Restaurants</h3>
   {% if restaurants %}
      {% for r in restaurants %}
         <li>{{ r.name}}, {{r.location}} 
         <b> Opening hours: </b> {{ r.opening_hours}} - {{r.closing_hours}} 
         {% if r.is_staff_only %} (staff only!) {% endif %}
         {% if r.is_open_wknd%} (open on weekends: {{ r.opening_hours_wknd}} - {{ r.closing_hours_wknd}})
         {% else%}
         (closed on weekends)
         {% endif%}
    <a href="{% url 'eatatdcu:specials' restaurant=r.name %}">Specials</a>
         </li>
      {% endfor %}
   {% else %}
      No restaurants found
   {% endif %}

   <h3>Cafes</h3>
   {% if cafes %}
      {% for c in cafes %}
         <li>{{ c.name}}, {{c.location}} 
         <b> Opening hours: </b> {{c.opening_hours}} - {{c.closing_hours}} 
         {% if c.is_staff_only %} (staff only!) {% endif %}
         {% if c.is_open_wknd%}
         (open on weekends: {{ c.opening_hours_wknd}}) - {{ c.closing_hours_wknd}})
         {%else%}
         (closed on weekends)
         {%endif%}
         </li>
      {% endfor %}
   {% else %}
      No cafes found
   {% endif %}
{% endif %}
```

#### Motivation

This is a University project Developed in CA377 module. This is created to let the users know when are the opening and closing times.

#### Installation

When installing the code firstly clone the repository. Once cloned CD to the folder src/ca377. Run "python3 manage.py runserver" in the terminal. If the code is running without errors go to the link provided in the terminal and add "/eatatdcu" at the end.
If the code is not running and you got an error go back to the code and fix any errors in where the terminal highlighted them.

#### Deploying to Pythonanywhere

In order to upload to [Pythonanywhere](https://www.pythonanywhere.com) you need to create an account.

1. Once your account is created.

1. You must edit the "Settings.py" file at the end of the file find ALLOWED_HOSTS on line 28.

1. You must edit this to "ALLOWED_HOSTS = ['127.0.0.1', 'example.pythonanywhere.com']" replace "example" to your own name.

1. In your terminal create a zip/tar.gz file of src and data folder.

1. Upload the zipped files to the pythonanywhere account on the "Files" tab.

1. Navigate to the console tab and create a console. Once youre there extract the zipped files.

1. Make a virtualenv to run Django and install required libraries.

 ```Bash
 $ mkvirtualenv --python=/usr/bin/python3.5 eatatdcu-virtualenv
(mysite-virtualenv)$ pip install django==1.11
(mysite-virtualenv)$ pip install requests
```

8. Create the webapp from the "Web" tab.

1. Choose the manual configuration and select Python3.5

1. Edit the source code and working directory values. "/home/yourusername/src/ca377"

1. Add your virtualenv and the path.

1. Edit the WSGI configuration and remove everything except whats on the image below.

[WSGI PHOTO](https://gitlab.computing.dcu.ie/jfoster/2019-ca377-EatAtDCU/wikis/uploads/a63ee3cdeb11649995bbdfcc0a47bb4a/image.png)

13. Set your database in the bash console.

```Bash
(mysite-virtualenv) $ ./manage.py makemigrations
(mysite-virtualenv) $ ./manage.py migrate
(mysite-virtualenv) $ ./manage.py shell
>>>import load_db_data
```

14. Once thats done Reload the webappp from the Web tab.

1. To make sure that the web site works go to the URL on the Web Tab.


#### Tests

The website has been tested on different web browsers such as Google Chrome, Firefox , Opera and IE. Further testing on different mobiles showed that on most mobile screens the responsive layout works fine. Running test cases can be ran by typing "python3 manage.py test eatatdcu" in the terminal.
 **Note** you have to be in the src/ca377 directory

#### Contributors

[Boostrap 4:](https://getbootstrap.com/)

[Theme:](https://codepen.io/adamabundis/pen/BWyEEZ)

[Explore DCU slideshow 1:](https://www.youtube.com/watch?v=KkzVFB3Ba_o)

[Explore DCU slideshow 2:](https://www.youtube.com/watch?v=7ZO2RTMNSAY)

[Explore DCU slideshow 3:](https://www.youtube.com/watch?v=nJWq74MHplc)

[Contact page:](https://codepen.io/stephanrusu/pen/QwKLJX)

[Contacr page 2:](https://www.youtube.com/watch?v=Iv93yjdvkWI)
