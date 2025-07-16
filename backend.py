from flask import Flask, render_template, request
import pandas as pd
from textblob import TextBlob
import os
import io
import json

app = Flask(__name__)

# ...existing code...
def analyze_sentiment(text=None, df=None):
    try:
        if text:
            sentiment = TextBlob(str(text)).sentiment.polarity
            sentiment_label = 'Positive' if sentiment > 0 else ('Negative' if sentiment < 0 else 'Neutral')
            return sentiment_label, {sentiment_label: 1}, f"<p>{text}: {sentiment_label}</p>", None

        if df is None:
            path = os.path.join(os.path.dirname(__file__), 'vaccination_tweets.csv')
            df = pd.read_csv(path)
        # Try to find the text column
        text_col = None
        for col in df.columns:
            if col.lower() in ['text', 'tweet', 'tweet_text', 'content']:
                text_col = col
                break
        if not text_col:
            return "Error", {}, "<p>Error: CSV must have a column for tweet text (e.g., 'text', 'tweet').</p>", None

        df['Sentiment'] = df[text_col].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        df['Sentiment_Label'] = df['Sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
        sentiment_counts = df['Sentiment_Label'].value_counts().to_dict()
        most_common = max(sentiment_counts, key=sentiment_counts.get)
        table_html = df[[text_col, 'Sentiment_Label']].head(10).to_html(classes='table', index=False)
        chart_data = {
            'labels': list(sentiment_counts.keys()),
            'counts': list(sentiment_counts.values())
        }
        return most_common, sentiment_counts, table_html, chart_data
    except Exception as e:
        return "Error", {}, f"<p>Error: {str(e)}</p>", None
# ...existing code...

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    tweet = request.form.get('tweet', '').strip()
    csv_file = request.files.get('csv_file')
    df = None
    if csv_file and csv_file.filename:
        try:
            df = pd.read_csv(io.StringIO(csv_file.stream.read().decode("utf-8")))
        except Exception as e:
            return render_template('result.html', sentiment="Error", counts={}, table=f"<p>Error reading CSV: {str(e)}</p>", chart_data=None)
    result, counts, table, chart_data = analyze_sentiment(tweet if tweet else None, df)
    return render_template('result.html', sentiment=result, counts=counts, table=table, chart_data=json.dumps(chart_data) if chart_data else None)

if __name__ == '__main__':
    app.run(debug=True)