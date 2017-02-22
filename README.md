# checkMnetions
a script to scrap twitter and get the total # of mentions for another users, from a list of users.
the script take one command line argument as file name, in my case it is a csv of list of twitter username.
Then iterate over the list, in a nested way, that check the total mentions from every users in every other users.
the output is user1, user2, total mentions. This format is made to be used in Gephi, which require the format of source,
target,weight.
