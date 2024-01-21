import pandas

# Read CSV file and fix column names.
csvRead = pandas.read_csv("Remi.csv")
csvRead = csvRead.rename(columns=lambda name: name.strip())
for column in csvRead.columns:
    csvRead[column] = csvRead[column].apply(lambda name: name.strip() if isinstance(name, str) else name)

# Check if data needs to be cleaned or not.
if "MATCHMAKING_OUTCOME" in csvRead.columns:
    # Remove tuples with unsuccessful queue time.
    csvRead = csvRead[csvRead["MATCHMAKING_OUTCOME"] == "success"]

    # Drop unnecessary columns.
    csvRead = csvRead.drop(columns=["MATCH_ID","CHARACTER_NAME","MATCHMAKING_OUTCOME"], axis = 1)

    # Rearrange dataframe.
    csvRead = csvRead.reindex(columns=["MATCHMAKING_ATTEMPT_START_TIME_UTC","MATCHMAKING_DAY_OF_WEEK",
                                    "PLAYER_ROLE","PARTY_SIZE","SERVER_NAME","PLATFORM",
                                    "MMR_GROUP_DECILE","QUEUE_DURATION_IN_SECS"])

# Print resulting dataframe.
print(csvRead)