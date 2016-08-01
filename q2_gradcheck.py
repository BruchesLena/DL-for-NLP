import numpy as np
import random

# First implement a gradient checker by filling in the following functions
def gradcheck_naive(f, x):
    """ 
    Gradient check for a function f 
    - f should be a function that takes a single argument and outputs the cost and its gradients
    - x is the point (numpy array) to check the gradient at
    """ 

    rndstate = random.getstate()
    random.setstate(rndstate)  
    fx, grad = f(x) # Evaluate function value at original point
    h = 1e-4

    # Iterate over all indexes in x
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index
        print ix

        ### try modifying x[ix] with h defined above to compute numerical gradients
        ### make sure you call random.setstate(rndstate) before calling f(x) each time, this will make it 
        ### possible to test cost functions with built in randomness later
        ### YOUR CODE HERE:
        #raise NotImplementedError

        # 1st variant
        min_value = x[ix] - h
        f_min = f(min_value)
        max_value = x[ix] + h
        f_max = f(max_value)
        grad[ix] = (f_max - f_min) / 2*h

        # 2nd variant
        old_value = x[ix] + h
        x[ix] = old_value - 2*h
        fxh = f(x)
        x[ix] = old_value
        grad[ix] = (fx - fxh) / 2*h
        ### END YOUR CODE

        # Compare gradients
        reldiff = abs(numgrad - grad[ix]) / max(1, abs(numgrad), abs(grad[ix]))
        if reldiff > 1e-5:
            print "Gradient check failed."
            print "First gradient error found at index %s" % str(ix)
            print "Your gradient: %f \t Numerical gradient: %f" % (grad[ix], numgrad)
            return
    
        it.iternext() # Step to next dimension

    print "Gradient check passed!"

def sanity_check():
    """
    Some basic sanity checks.
    """
    quad = lambda x: (np.sum(x ** 2), x * 2)

    print "Running sanity checks..."
    gradcheck_naive(quad, np.array(123.456))      # scalar test
    gradcheck_naive(quad, np.random.randn(3,))    # 1-D test
    gradcheck_naive(quad, np.random.randn(4,5))   # 2-D test
    print ""

def your_sanity_checks(): 
    """
    Use this space add any additional sanity checks by running:
        python q2_gradcheck.py 
    This function will not be called by the autograder, nor will
    your additional tests be graded.
    """
    print "Running your sanity checks..."
    ### YOUR CODE HERE
    raise NotImplementedError
    ### END YOUR CODE

if __name__ == "__main__":
    sanity_check()
    #your_sanity_checks()
    
    
1st variant console:
Running sanity checks...
()
Traceback (most recent call last):
  File "C:/Users/root/Downloads/assignment1(1)/assignment1/q2_gradcheck.py", line 81, in <module>
    sanity_check()
  File "C:/Users/root/Downloads/assignment1(1)/assignment1/q2_gradcheck.py", line 63, in sanity_check
    gradcheck_naive(quad, np.array(123.456))      # scalar test
  File "C:/Users/root/Downloads/assignment1(1)/assignment1/q2_gradcheck.py", line 34, in gradcheck_naive
    grad[ix] = (f_max - f_min) / 2*h
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'

2nd variant console:
Running sanity checks...
()
Traceback (most recent call last):
  File "D:\Python\PyCharm Community Edition 2016.1.4\helpers\pydev\pydevd.py", line 1531, in <module>
    globals = debugger.run(setup['file'], None, None, is_module)
  File "D:\Python\PyCharm Community Edition 2016.1.4\helpers\pydev\pydevd.py", line 938, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "C:/Users/root/Downloads/assignment1(1)/assignment1/q2_gradcheck.py", line 79, in <module>
    sanity_check()
  File "C:/Users/root/Downloads/assignment1(1)/assignment1/q2_gradcheck.py", line 61, in sanity_check
    gradcheck_naive(quad, np.array(123.456))      # scalar test
  File "C:/Users/root/Downloads/assignment1(1)/assignment1/q2_gradcheck.py", line 39, in gradcheck_naive
    grad[ix] = (fx - fxh) / 2*h
TypeError: 'numpy.float64' object does not support item assignment

Process finished with exit code -1
