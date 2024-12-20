from src.pipline.prediction_pipline import CustomData, PredictPipeline
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # Collecting data from the form
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        
        # Convert the collected data into a DataFrame
        final_data = data.get_data_as_dataframe()
        
        # Create a prediction pipeline instance
        predict_pipeline = PredictPipeline()
        
        # Make a prediction
        pred = predict_pipeline.predict(final_data)
        
        # Round the prediction result
        result = round(pred[0], 2)
        
        # Render the result in the result.html template
        return render_template("result.html", final_result=result)

# Execution begins
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)