import os
import openai
import requests
from pprint import pprint
import dotenv

dotenv.load_dotenv()
bing_search_api_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
bing_search_endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] + "/v7.0/search"


def search(query):
    # Construct a request
    mkt = 'en-US'
    params = {'q': query, 'mkt': mkt}
    headers = {'Ocp-Apim-Subscription-Key': bing_search_api_key}

    # Call the API
    try:
        response = requests.get(bing_search_endpoint,
                                headers=headers, params=params)
        response.raise_for_status() 
        json = response.json()
        results = json["webPages"]["value"]
        results_prompts = [
            f"Source:\nTitle: {result['name']}\nURL: {result['url']}\nContent: {result['snippet']}" for result in results
        ]
        return results_prompts

        # print("\nJSON Response:\n")
        # pprint(response.json())
    except Exception as ex:
        raise ex


# Prompt the user for a question
# question = input("What is your question? ")

# # Send a query to the Bing search engine and retrieve the results
# results = search(question)
# print(results)



