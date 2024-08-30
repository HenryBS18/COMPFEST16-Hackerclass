# Get the password input from the user
pw = input('Enter THE password: ')

# Check if the password is alphanumeric
if pw.isalnum():
  # Check if the password is of correct length (not too long or too short)
  if len(pw) > 9:
    print('Password is too long!')
    exit()
  elif len(pw) < 9:
    print('Password is too short!')
    exit()

  # Initialize an empty list and fill it with the ordinal values of the password characters
  x = [0] * 9

  for i in range(9):
    x[len(x) - i - 1] = ord(pw[i])

  # Print the list (optional, possibly for debugging purposes)
  print(x)

  # Validate the password based on certain criteria
  if (x[7] + 69 == 120 and
    x[3] ^ 1337 == 1355 and
    x[0] // 22 == 5 and
    x[4] - 16 == 35 and
    x[8] << 3 == 832 and
    x[1] ** 2 == 9409 and
    x[6] * 7 == 693 and
    ~x[2] == -110 and
    x[5] == 107):
    
    # If the criteria are met, print the flag
    print("Correct! Here's your flag: ")
    print(open('flag.txt').read())
    exit()

  if x[0] // 22 == 5:
    print('x0 correct')
  if x[1] ** 2 == 9409:
    print('x1 correct')
  if ~x[2] == -110:
    print('x2 correct')
  if x[3] ^ 1337 == 1355:
    print('x3 correct')
  if x[4] - 16 == 35:
    print('x4 correct')
  if x[5] == 107:
    print('x5 correct')
  if x[6] * 7 == 693:
    print('x6 correct')
  if x[7] + 69 == 120:
    print('x7 correct')
  if x[8] << 3 == 832:
    print('x8 correct')
else:
  # If the password is not alphanumeric, print an error message
  print('Password format is not valid!')
  exit()

# If the password does not meet the criteria, print an error message
print('Wrong password.')
