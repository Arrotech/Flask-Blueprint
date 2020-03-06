# What a Flask Blueprint Looks Like


Flask Blueprints encapsulate functionality, such as views, templates, and other resources. To get a taste for how a Flask Blueprint would work, you can refactor the previous application by moving the index view into a Flask Blueprint. To do so, you have to create a Flask Blueprint that contains the index view and then use it in the application.

This is what the file structure looks like for this new application:

    app/
    |
    ├── app.py
    └── example_blueprint.py

example_blueprint.py will contain the Flask Blueprint implementation. You’ll then modify app.py to use it.

The following code block shows how you can implement this Flask Blueprint in example_blueprint.py. It contains a view at the route / that returns the text This is an example app:

    from flask import Blueprint

    example_blueprint = Blueprint('example_blueprint', __name__)

    @example_blueprint.route('/')
    def index():
        return "This is an example app"

In the above code, you can see the steps common to most Flask Blueprint definitions:

Create a Blueprint object called example_blueprint.

Add views to example_blueprint using the route decorator.

The following code block shows how your application imports and uses the Flask Blueprint:

    from flask import Flask
    from example_blueprint import example_blueprint

    app = Flask(__name__)
    app.register_blueprint(example_blueprint)

To use any Flask Blueprint, you have to import it and then register it in the application using register_blueprint(). When a Flask Blueprint is registered, the application is extended with its contents.

You can run the application with the following command:

    $ flask run
    
While the application is running, go to http://localhost:5000 using your web browser. You’ll see a page showing the message, This is an example app.


## How Flask Blueprints Work


In this section, you’ll learn in detail how a Flask Blueprint is implemented and used. Each Flask Blueprint is an object that works very similarly to a Flask application. They both can have resources, such as static files, templates, and views that are associated with routes.

However, a Flask Blueprint is not actually an application. It needs to be registered in an application before you can run it. When you register a Flask Blueprint in an application, you’re actually extending the application with the contents of the Blueprint.

This is the key concept behind any Flask Blueprint. They record operations to be executed later when you register them on an application. For example, when you associate a view to a route in a Flask Blueprint, it records this association to be made later in the application when the Blueprint is registered.


### Making a Flask Blueprint


Let’s revisit the Flask Blueprint definition that you’ve seen previously and review it in detail. The following code shows the Blueprint object creation:

    from flask import Blueprint

    example_blueprint = Blueprint('example_blueprint', __name__)

Note that in the above code, some arguments are specified when creating the Blueprint object. The first argument, "example_blueprint", is the Blueprint’s name, which is used by Flask’s routing mechanism. The second argument, __name__, is the Blueprint’s import name, which Flask uses to locate the Blueprint’s resources.

There are other optional arguments that you can provide to alter the Blueprint’s behavior:

-**static_folder:** the folder where the Blueprint’s static files can be found

-**static_url_path:** the URL to serve static files from

-**template_folder:** the folder containing the Blueprint’s templates

-**url_prefix:** the path to prepend to all of the Blueprint’s URLs

-**subdomain:** the subdomain that this Blueprint’s routes will match on by default

-**url_defaults:** a dictionary of default values that this Blueprint’s views will receive

-**root_path:** the Blueprint’s root directory path, whose default value is obtained from the Blueprint’s import name

Note that all paths, except root_path, are relative to the Blueprint’s directory.

The Blueprint object example_blueprint has methods and decorators that allow you to record operations to be executed when registering the Flask Blueprint in an application to extend it. One of the most used decorators is route. It allows you to associate a view function to a URL route. The following code block shows how this decorator is used:

    @example_blueprint.route('/')
    def index():
        return "This is an example app"

You decorate index() using example_blueprint.route and associate the function to the URL /.

Blueprint objects also provide other methods that you may find useful:

-**.errorhandler()** to register an error handler function
-**.before_request()** to execute an action before every request
-**.after_request()** to execute an action after every request
-**.app_template_filter()** to register a template filter at the application level

You can learn more about using Blueprints and the Blueprint class in the Flask Blueprints Documentation.


### Registering the Blueprint in Your Application


Recall that a Flask Blueprint is not actually an application. When you register the Flask Blueprint in an application, you extend the application with its contents. The following code shows how you can register the previously-created Flask Blueprint in an application:

    from flask import Flask
    from example_blueprint import example_blueprint

    app = Flask(__name__)
    app.register_blueprint(example_blueprint)

When you call .register_blueprint(), you apply all operations recorded in the Flask Blueprint example_blueprint to app. Now, requests to the app for the URL / will be served using .index() from the Flask Blueprint.

You can customize how the Flask Blueprint extends the application by providing some parameters to register_blueprint:

-**url_prefix** is an optional prefix for all the Blueprint’s routes.
-**subdomain** is a subdomain that Blueprint routes will match.
-**url_defaults** is a dictionary with default values for view arguments.

Being able to do some customization at registration time, instead of at creation time, is particularly useful when you’re sharing the same Flask Blueprint in different projects.