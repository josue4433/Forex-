Currency Converter
This is a small currency converter web application built with Flask and forex-python. It allows users to convert an amount from one currency to another using real-time exchange rates.

Installation
Clone this repository to your local machine.
Create a virtual environment for the project: python -m venv venv.
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Install the required dependencies: pip install -r requirements.txt.
Usage
Run the Flask application: python app.py.
Open your web browser and navigate to http://localhost:5000.
Enter the three-letter currency code to convert from (e.g., USD, EUR, JPY) in the "From Currency" input field.
Enter the three-letter currency code to convert to in the "To Currency" input field.
Enter the amount you want to convert in the "Amount" input field.
Click the "Convert" button to see the converted amount.
Testing
To run the tests for Flask routes and other functions, use the following command:

bash
Copy code
python -m unittest test_app.py
Please note that the tests for the currency conversion logic will not verify actual exchange rates due to their dynamic nature. Instead, these tests will ensure the correct functionality of the Flask app.

Refactoring
If you wish to refactor the code and move certain functions to separate files, consider the following files:

utils.py: Contains utility functions like is_valid_currency_code and convert_currency.
app.py: Contains the main Flask application code and routes.
You can further extend this project by adding more features, such as selecting currencies from a dropdown list or implementing user authentication.

Credits
This project uses the forex-python library for currency conversion. (Link to library documentation)
The Flask web framework is used for creating the web application. (Link to Flask documentation)
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.




