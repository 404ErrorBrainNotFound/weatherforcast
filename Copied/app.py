from flask import Flask, render_template, request, redirect, url_for
from weather import Weather, WeatherException

app = Flask(__name__)
app.config.from_pyfile('config/config.cfg')
w = Weather(app.config)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/result', methods=['POST', 'GET'])
def result_page():
    if request.method == 'POST':
        location = request.form
       
        w.set_location(location.get('location'))
        names=['Today','Tommorrow','Day 3','Day 4','Day 5','Day 6','Day 7','Day 8','Day 9','Day 10','Day 11','Day 12','Day 13','Day 14','Day 15']
        try:
            data=w.get_forecast_data()
            combined_data = list(zip(names, data))
            return render_template('result.html', combined_data=combined_data)
        except WeatherException:
            app.log_exception(WeatherException)
            return render_template('error.html')
    else:
        return redirect(url_for('homepage'))

@app.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
 #<<<<<<< HEAD
    app.run(host='0.0.0.0', port=8080)
 #=======
  #  app.run(host='0.0.0.0', port=80)
 #>>>>>>> 947b935549ca986524074f1c56ee16103ba4edaf
