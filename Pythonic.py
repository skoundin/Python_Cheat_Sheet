'''
filter
'''

friends=['Rolf','Jose','Randy','Anna','Mary']
starts_with_r=filter(lambda x:x.startswith('R'),friends)

print(list(starts_with_r))




'''
map  All three below are correct
'''
friends=['Rolf','Jose','Randy','Anna','Mary']
friends_lower_1= map(lambda x:x.lower(), friends)  # applies the lamda function to the whole list of iterables
friends_lower_2= [f.lower() for f in friends]
friends_lower_3=(friend.lower() for friend in friends)

'''
enumerate- When we need acces to the index 
'''
