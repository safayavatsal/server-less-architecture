import json
import boto3

def lambda_handler(event, context):
    # Extract the review text from the incoming event
    review = event['review']
    
    # Initialize the Boto3 Comprehend client
    comprehend = boto3.client('comprehend')
    
    # Analyze sentiment using Comprehend
    sentiment_response = comprehend.detect_sentiment(Text=review, LanguageCode='en')
    
    # Extract sentiment from response
    sentiment = sentiment_response['Sentiment']
    
    # Log the sentiment analysis result
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    
    # Return the sentiment result
    return {
        'statusCode': 200,
        'body': json.dumps({'Sentiment': sentiment})
    }
