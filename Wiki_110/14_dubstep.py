'''
Write a function to decode a dubstep string to its original form.The string
may begin and end with one or more "WUB"s and there will be at least one (and
possibly more) "WUB"s between each word.
The input consists of a single non-empty string, consisting only of uppercase
English letters.

Examples:
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
# should return "WE ARE THE CHAMPIONS MY FRIEND"

'''
def song_decoder(strng):
    return strng.replace('WUB', ' ')

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
# should return "WE ARE THE CHAMPIONS MY FRIEND"