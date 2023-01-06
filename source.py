from flask import Flask, render_template, request
import openai

# Set the API key for the OpenAI API
openai.api_key = "YOUR_API_KEY"

app = Flask(__name__)

@app.route("/")
def home():
    # Set the model to use for text generation
    model_engine = "text-davinci-002"

    # Render the home page template
    return render_template("home.html", model_engine=model_engine)

@app.route("/generate", methods=["POST"])
def generate_cover_letter():
    # Get the input fields
    job_url = request.form["job_url"]
    name = request.form["name"]
    contact_info = request.form["contact_info"]
    work_experience = request.form["work_experience"]
    education = request.form["education"]
    skills = request.form["skills"]

    # Set the prompt for the model
    prompt = f"Please write a cover letter for the following job posting:\n{job_url}\n\nHere is my personal information:\nName: {name}\nContact Information: {contact_info}\nWork Experience:\n{work_experience}\nEducation:\n{education}\nSkills:\n{skills}"

    # Generate text using the GPT-3 model
    generated_text = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, temperature=0.5)

    # Render the generated text in the result page template
    return render_template("result.html", generated_text=generated_text.text)
