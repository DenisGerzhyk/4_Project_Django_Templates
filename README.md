# 4_Project_Django_Templates

This is a Python code for a simple web application using the Django framework. It consists of three files: views.py, models.py, and forms.py.

The views.py file defines two functions: index() and display(). The index() function processes the form data submitted through HTTP POST method and saves the data to the database using a Django form. It then redirects the user to the display() function. The display() function retrieves all the saved data from the database and performs arithmetic operations based on the sign field (either +, -, *, or /) to calculate the result field. Finally, it renders the display.html template file with the processed data.

The models.py file defines a Django model Calculates which represents the database table schema. It has three fields: x, y, and sign, which are integers and a string, respectively. It also defines a method __str__() which returns a formatted string representing the instance.

The forms.py file defines a Django form CalculatesForm that inherits from forms.ModelForm. It specifies the model and the fields to include in the form.

Lastly, there are two HTML templates: index.html and display.html. The index.html template renders a form with three input fields: x, y, and sign, and a submit button. The display.html template iterates over the saved data and displays each instance's x, y, sign, and the calculated result field based on the sign.
