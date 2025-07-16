# Twitter Sentiment Analysis Using Website

A web application for analyzing the sentiment of tweets using machine learning, built with Flask and TextBlob. The app allows users to input a tweet or upload a CSV file of tweets and visualize the overall sentiment—positive, neutral, or negative—through interactive charts.

---

## Features

- **Analyze single tweet or bulk tweets (CSV upload)**
- **Visualize sentiment distribution** with Pie, Bar, and Doughnut charts
- **Displays sample tweets** and their detected sentiment
- **User-friendly web interface** powered by Flask

---

## Screenshots

### Home Page - Analyze Tweets
Upload a CSV or enter a tweet to analyze:

<img width="1907" height="979" alt="image" src="https://github.com/user-attachments/assets/d2206d9c-2f91-41e6-859a-120621a78a2a" />


---

### Sentiment Analysis Results

#### Doughnut Chart View

<img width="1895" height="977" alt="image" src="https://github.com/user-attachments/assets/153d9362-f036-412b-b1dc-463babf06ba5" />


#### Bar Chart View (with sample tweets)

<img width="1899" height="978" alt="image" src="https://github.com/user-attachments/assets/c365c40c-88ce-46d5-adc0-ccbb70417143" />


#### Pie Chart View

<img width="1900" height="974" alt="image" src="https://github.com/user-attachments/assets/4404dddd-0d5f-48e5-b0aa-e502b38160ea" />


---

## How It Works

1. **Input**: Enter a tweet manually or upload a CSV file containing tweets.
2. **Processing**: The app uses TextBlob to analyze the sentiment of each tweet.
3. **Visualization**: Results are shown in interactive charts:
   - **Positive**: Green
   - **Neutral**: Yellow
   - **Negative**: Red
4. **Sample Results**: View sample tweets and their sentiment label.

---

## Sentiment Analysis Output

- **Overall Sentiment**: Shows whether the general sentiment is positive, neutral, or negative.
- **Sentiment Counts**: Number of tweets in each sentiment category.
- **Charts**: Switch between Pie, Bar, and Doughnut charts for different visual perspectives.

---

## Technologies Used

- **Python**
- **Flask** (Backend Web Framework)
- **TextBlob** (Sentiment Analysis)
- **HTML/CSS/JavaScript** (Frontend)
- **Chart.js** (Interactive Charts)

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dharaneesh0205/Twitter-sentiment-analysis-using-website.git
   cd Twitter-sentiment-analysis-using-website
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m venv venv
   venv\Scripts\activate
   pip install flask pandas textblob
   python -m textblob.download_corpora
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Open your browser** and go to `http://localhost:5000`.

---

## Usage

- **Analyze a single tweet**: Type in the textbox and click "Analyze Sentiment".
- **Analyze multiple tweets**: Upload a CSV file with tweets.
- **Switch chart views**: Use the Pie, Bar, and Doughnut chart buttons.
- **View sample tweets**: Check the table below the charts for sample results.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [TextBlob](https://textblob.readthedocs.io/)
- [Chart.js](https://www.chartjs.org/)

---
