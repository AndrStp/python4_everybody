t = []

while True:
    user_inp = input('Enter a number: ').lower()
    if user_inp == 'done':
        break
    try:
        user_inp = int(user_inp)
        t.append(user_inp)
    except:
        print('Please enter a number')
    

print(t)
print(min(t))
print(max(t))

