# This function estimates the square root of a given number using the bisection method.
# The bisection method works by iteratively narrowing the search range until an 
# approximation is found within a given tolerance.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Handle the case where the input is negative, since the square root of a negative number 
    # is not defined in real numbers.
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # Handle special cases where the square root is trivial.
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Define the lower and upper bounds for the bisection search.
        # If the target number is less than 1, we use [0,1] as the range;
        # otherwise, we use [0, square_target] as the range.
        low = 0
        high = max(1, square_target)
        root = None  # Initialize root as None, to be updated once convergence is achieved.

        # Iterate up to max_iterations times to approximate the square root.
        for _ in range(max_iterations):
            mid = (low + high) / 2  # Find the midpoint of the current range.
            square_mid = mid**2  # Compute the square of the midpoint.

            # If the square of the midpoint is close enough to the target (within tolerance),
            # we consider it as the square root and break out of the loop.
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            # If the square of mid is less than the target, we adjust the lower bound.
            elif square_mid < square_target:
                low = mid
            # Otherwise, adjust the upper bound.
            else:
                high = mid

        # If the loop finishes without finding a suitable root, print a failure message.
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")

        # If a valid root is found, print the result.
        else:   
            print(f'The square root of {square_target} is approximately {root}')

    # Return the computed square root value.
    return root

# Define a large number N to test the function.
N = 2000000000
square_root_bisection(N)  # Call the function to compute and print the square root.