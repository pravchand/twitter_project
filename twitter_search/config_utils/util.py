import json
import os
import googlemaps
import pandas as pd
import tweepy
from config_utils import config


def load_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data


LIST_FIELDS = ["id", "name", "description"]
USER_FIELDS = [
    "created_at",
    "description",
    "entities",
    "id",
    "location",
    "most_recent_tweet_id",
    "name",
    "pinned_tweet_id",
    "profile_image_url",
    "protected",
    "public_metrics",
    "url",
    "username",
]


def list_filter_keywords(all_lists, location):
    filtered_lists = set()
    keywords = {
        f"{keyword.lower()} {location.lower()}"
        for keyword in [
            "journalists",
            "journalism",
            "news",
            "politics",
            "ngo",
            "pollution",
            "air",
            "health",
            "swatchh",
            "clean",
            "climate",
            "energy",
            "environment",
            "activist",
        ]
    } | {
        keyword.lower()
        for keyword in [
            "journalists",
            "journalism",
            "news",
            "politics",
            "ngo",
            "pollution",
            "air",
            "health",
            "swatchh",
            "clean",
            "climate",
            "energy",
            "environment",
            "activist",
        ]
    }

    for lst in all_lists:
        list_name_lower = lst["name"].lower()
        list_description_lower = lst.get(
            "description", ""
        ).lower()  # Handle missing descriptions

        # Check if any keyword intersects with the lowercase name/description
        if any(
            keyword in list_name_lower or keyword in list_description_lower
            for keyword in keywords
        ):
            filtered_lists.add(lst["list_id"])

    return list(filtered_lists)


def tweet_dictmaker(tweet_list):
    """
    This function takes a list of tweet objects and
    transforms it into a list of dictionaries

    Parameters
    ----------
    tweet_list : list
        List of tweet objects

    Returns
    -------
    dict_list: list
        List of dictionaries with tweet data
    """
    dict_list = []
    for tweet in tweet_list:
        values = {
            "tweet_id": tweet.id,
            "text": tweet.text,
            "author_id": tweet.author_id,
            "created_at": tweet.created_at.isoformat(),  # Convert datetime to ISO format string
            "conversation_id": tweet.conversation_id,
            "geo": tweet.geo,
            "lang": tweet.lang,
            "possibly_sensitive": tweet.possibly_sensitive,
            "reply_settings": tweet.reply_settings,
            "source": tweet.source,
            "attachments": tweet.attachments,
            "context_annotations": tweet.context_annotations,
            "entities": tweet.entities,
            "public_metrics": tweet.public_metrics,
            "non_public_metrics": tweet.non_public_metrics,
            "organic_metrics": tweet.organic_metrics,
            "promoted_metrics": tweet.promoted_metrics,
            "withheld": tweet.withheld,
            "in_reply_to_user_id": tweet.in_reply_to_user_id,
        }
        dict_list.append(values)
    return dict_list


def user_dictmaker(user_list):
    """
    This function takes a list of user objects and
    transformis it into a list of dictionaries

    Parameters
    ----------
    user_list : list
        List of user objects

    Returns
    -------
    dict_list: list
        List of dictionaries with user data
    """
    dict_list = []
    for user in user_list:
        values = {
            "user_id": user["id"],
            "username": user["username"],
            "description": user["description"],
            "location": user["location"],
            "name": user["name"],
            "url": user["url"],
            "tweets": [],
            "geo_code": [],
        }
        values.update(user["public_metrics"])
        dict_list.append(values)
    return dict_list


def list_dictmaker(incoming_datastruct):
    """
    - Function description -

    Parameters
    ----------
    incoming_datastruct : _type_
        _description_

    Returns
    -------
    dict_list: list
    """
    dict_list = []
    for userid, lsts in incoming_datastruct.items():
        for lst in lsts:
            values = {
                "user_id": userid,
                "list_id": lst["id"],
                "name": lst["name"],
                "created_at": lst["created_at"],
                "description": lst["description"],
                "follower_count": lst["follower_count"],
                "member_count": lst["member_count"],
                "private": lst["private"],
                "owner_id": lst["owner_id"],
            }
            dict_list.append(values)
    return dict_list


def gmaps_client():
    """
    Creates google maps client
    """
    return googlemaps.Client(key=config.SECRET_KEY)


def client_creator():
    """
    Creates a wrapper for the Twitter API client.
    """
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret
    bearer_token = config.bearer_token

    return tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )


def flatten_and_remove_empty(input_list):
    """
    Flatten a list of lists into a single list and remove any empty lists within it.

    Args:
        input_list (list): The list of lists to be flattened and cleaned.

    Returns:
        list: The flattened list with empty lists removed.
    """
    return [item for sublist in input_list for item in sublist if sublist]


def json_maker(file_path, data_to_append):
    """
    Create a JSON file with the data provided, the
    JSON is saved in the file path provided.

    Parameters
    ----------
    file_path : str
        The path where the JSON file will be saved.

    data_to_append : dict
        The data to be saved in the JSON file.
    """
    try:
        with open(file_path, "r") as f:
            existing_data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        existing_data = []

    # Append the new data to the existing list
    existing_data.append(data_to_append)

    # Check if the file path exists
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
        print("Created directory:", os.path.dirname(file_path))

    # Write the updated list of dictionaries back to the file
    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=1)


def excel_maker(dict_list, file_path):
    """
    Creates an Excel file with the data provided,
    and it is saved on a given path.

    Parameters
    ----------
    dict_list : list
        List of dictionaries with the data to be saved.

    file_path : str
        The path where the Excel file will be saved.
    """
    df = pd.DataFrame(dict_list)
    new_df = df.drop_duplicates()
    new_df.to_excel(file_path, index=False)
