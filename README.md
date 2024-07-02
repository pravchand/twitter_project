# Twitter Search

The repository contains the code for searching users on Twitter based on a given type of account, searches for tweets relating to the type, gets the users, tweets, and then if needed, increases the number of users by collecting all the lists that the users are a part of. We call this latter process, 'snowballing'.  The script can be run with or without the snowballing component.

The processing and filtering scripts geo-locate the users, classify them based on relevance using a zero-shot model.


## How to Use

For the extraction part:

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

5. Execute the project from the command line:

```bash
python3 twitter_search location(str) industry_type(str) list_needed(bool) --num_interations (int)
```


For example:

```bash
python3 twitter_search "Kolkata" "media" "False" --num_iterations 1
```

gets users from Kolkata in the media industry, where lists(snowballing) is not needed (note that you do not need to use the quotation marks). The optional argument number of iterations tells the script how many snowballing iterations are needed. Each iteration fetches lists, gets all users from the lists and filters the users based on location and content relevance.

6. The project will search Twitter based on the specified query and location, collecting user data and saving it in the raw data directory.

7. If you want, it is also possible to generate csv files for a particular location. The command for generating Kolkata's csv files  would be:

```bash
python3 twitter_search/etl/generate_csv_files.py "Kolkata"
```

8. Concatenate all .csv files

There is another command we can use to concatenate all of the .csv files in the `cleaned_data` directory into a single file. This command is:

```bash
python3 twitter_search/etl/concat_csv_files.py
```

### For a given location, get all the account types at once

If you want to get all the account types for a given location, you can use the following command:

```bash
python3 twitter_search "Kolkata" "all" "False"
```
Which will output all the account types for the given location (in this case, Kolkata). This will also generate the corresponding csv file for "Kolkata".


## For all locations, get all the account types at once

If you want to get all the account types for all locations, you can use the following command:

```bash
python3 twitter_search "all" "all" "False"
```

Which will output all the account types for all locations. Additionally, this will also generate the corresponding csv files for each location.

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