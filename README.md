# Twitter Search

The repository contains the code for searching users on Twitter based on a given type of account and location. The process searches for tweets related to the account type and location, extracts the users, and filters them based on relevance by using a zero-shot model.

## Setting up the repository

1. Clone the repository

```
git clone https://github.com/Energy-Lab-Pollution/twitter_search.git
```

2. Navigate to the repository

```
cd ./twitter_search
```


3. Download Poetry, which allows the user to run the application in a virtual environment, [following these instructions](https://python-poetry.org/docs/). Then install poetry.

```
poetry install
```

4. Activate the virtual environment in poetry.

```
poetry shell
```
**Note:**  Receive the secret keys from the authors, go to twitter_search/config_utils, and create a file called config.py. You then need to paste all of the access keys there.

## Extracting and classificating users

As of now, we can extract users from Twitter in two ways:

1. Use (Twitter's)[https://docs.x.com/x-api/introduction] official API.
2. Use the (Twikit)[https://github.com/d60/twikit] library for scraping.

We are keeping both options open in case Twikit stops working or Twitter's API becomes more restrictive.

If you use twitter's API, you can execute the project from the command line:

```bash
python3 twitter_search location(str) account_type(str)
```

If you use Twikit, you can execute the project from the command line:

```bash
python3 twitter_search/run_twikit.py location(str) account_type(str)
```

For example, if you want to get users from Kolkata in the "media" category with Twitter's official API, you can use the following command:

```bash
python3 twitter_search "kolkata" "media"
```


The project will search Twitter based on the specified query and location, collecting user data and saving it in the raw data directory.

If you want, it is also possible to generate csv files for a particular location. The command for generating Kolkata's csv files  would be:

```bash
python3 twitter_search/etl/generate_csv_files.py "kolkata"
```

#### Concatenate all .csv files (WIP: adapt method to work with Twikit)

There is another command we can use to concatenate all of the .csv files in the `cleaned_data` directory into a single file. This command is:

```bash
python3 twitter_search/etl/concat_csv_files.py
```

#### For a given location, get all the account types at once

If you want to get all the account types for a given location, you can use the following command:

```bash
python3 twitter_search "kolkata" "all"
```

Which will output all the account types for the given location (in this case, Kolkata). This will also generate the corresponding csv file for "Kolkata".


### For a given location, get all the account types at once, but skip _media_ account type.

During the project, we found that the _media_ account type outputs the most number of accounts, but it also captures a lot of irrelevant users. Therefore, to save resources and Twitter API calls, we added a skip_media parameter.

If you want to get all the account types for a given location, but skip the _media_ account type, you can use the following command:

```bash
python3 twitter_search "Kolkata" "all" --skip_media "True"
```

Which will output all the account types for the given location (in this case, Kolkata), but skip the _media_ account type. This will also generate the corresponding csv file for "Kolkata".


## For all locations, get all the account types at once (not advisable since it will consume lots of tokens)

If you want to get all the account types for all locations, you can use the following command:

```bash
python3 twitter_search "all" "all"
```
Note that you can also use the `--skip_media` parameter for this command.

```bash
python3 twitter_search "all" "all" --skip_media "True"
```

## Get more users by using list expansion (WIP: create Twikit methods)

```bash
python3 twitter_search/list_expansion.py "bangalore" "researcher"
```

This will analyze the filtered users from bangalore that belong to the 'researcher' query (you must have already run the default script for the location and account type). It will then get all the lists that the users are a part of, filter the lists based on keywords, and then get all the users from the fitered lists.

TODO: The script will then filter the users based on location and content relevance.

Additionally, you can use the "all" parameter for the location to get all the account types for all locations. For example:

```bash
python3 twitter_search/list_expansion.py "all" "all"
```

You can also get all the account types for a given location by using the "all" parameter for the account type. For example:

```bash
python3 twitter_search/list_expansion.py "bangalore" "all"
```


## Make Commands and addtional information

Note that, to add code to the repository, you will need to install pre-commit. This will ensure that the code is formatted correctly and that the tests pass before you commit. To install pre-commit, run the following command:

```bash
pip install pre-commit
```

You can then use the Makefile to format the code:

```bash
make lint
```


## Constants

Several constants are used in the code.

- Queries and account types: The available types of accounts, along with the queries used to search for the twitter users, are in the `config_utils/queries.py` file.

- Locations of interest: The locations of interest are in the `config_utils/cities.py` file. The `run.py` script iterates over these locations to search for users when the `all` argument is passed for the location.

- Access: The access keys are in the `config_utils/config.py` file. This tokens are used to access the Twitter API and the Google Maps API; you need to ask for this file from the authors.

- Other constants: Other constants are in the `config_utils/constants.py` file. These constants include paths, the number of users to fetch, capitals, the zero-shot threshold score and others.

- Constants for the `twitter_filtering code`: There are also some other constants in the `twitter_filtering/util/constants.py` file. These constants include paths, mostly.
