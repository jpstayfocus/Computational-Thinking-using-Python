
# Author : Jephté Piere
# Date : March 13, 2023
#
# Program that verifies that  pi = 4/1 - 4/3 + 4/5 - 4/7 + ....
# converges to pi.


error=5e-6       # variable corresponding to the error sought by your program
approx=4/1       # first value of the approximation
approx_two=approx - 4/3  # the second value of the approximation
expo=2                   # expo will be used for changing the alternate signs
power_ten=10             # verify if the the numbers of terms is power of ten

# find the terms untill the tolerable error

print('at 1 term the sum is equal to ',approx) # print the first term's sum
while abs(math.pi - approx_two)>error:
    approx=approx_two
    approx_two=approx_two + ((-1)**expo)*4/(2*expo+1) # calculates pi
    
    if expo == power_ten:   # verify if the numbers of terms are: power of ten
        print('at',expo, 'term the sum is equal to', approx)
        power_ten=power_ten * 10
    expo=expo+1
    
    ## will displayed in case the sum does not converge quickly enough
    if abs(math.pi - approx_two)<error: 
        print('the sum hasn\'t reached the tol.err of',error,'at',expo)

# Print how many terms there are in the sum and the value
# of the sum if the error is more than the "error"

print('Sum reaches the tol.err of ',error,' at ',expo,' terms')
print('Sum is equal to ',approx_two)
        
        
