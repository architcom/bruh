secret_number= 9
number_of_count=0
total_number_of_counts_possible=3

while number_of_count < total_number_of_counts_possible:
    guess=int(input('Guess the number '))
    number_of_count=number_of_count+1
    if secret_number == guess:
        print('you won')
        break

else:
    print('u lost')