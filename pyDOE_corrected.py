"""
This code was originally published by the following individuals for use with
Scilab:
    Copyright (C) 2012 - 2013 - Michael Baudin
    Copyright (C) 2012 - Maria Christopoulou
    Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
    Copyright (C) 2009 - Yann Collette
    Copyright (C) 2009 - CEA - Jean-Marc Martinez
    
    website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

Much thanks goes to these individuals. It has been converted to Python by 
Abraham Lee.
"""

import re
import numpy as np

#__all__ = ['np', 'fullfact_corrected', 'ff2n', 'fracfact']

def fullfact_corrected(levels):
    """
    Create a general full-factorial design
    
    Parameters
    ----------
    levels : array-like
        An array of integers that indicate the number of levels of each input
        design factor.
    
    Returns
    -------
    mat : 2d-array
        The design matrix with coded levels 0 to k-1 for a k-level factor
    
    Example
    -------
    ::
    
        >>> fullfact([2, 4, 3])
        array([[ 0.,  0.,  0.],
               [ 1.,  0.,  0.],
               [ 0.,  1.,  0.],
               [ 1.,  1.,  0.],
               [ 0.,  2.,  0.],
               [ 1.,  2.,  0.],
               [ 0.,  3.,  0.],
               [ 1.,  3.,  0.],
               [ 0.,  0.,  1.],
               [ 1.,  0.,  1.],
               [ 0.,  1.,  1.],
               [ 1.,  1.,  1.],
               [ 0.,  2.,  1.],
               [ 1.,  2.,  1.],
               [ 0.,  3.,  1.],
               [ 1.,  3.,  1.],
               [ 0.,  0.,  2.],
               [ 1.,  0.,  2.],
               [ 0.,  1.,  2.],
               [ 1.,  1.,  2.],
               [ 0.,  2.,  2.],
               [ 1.,  2.,  2.],
               [ 0.,  3.,  2.],
               [ 1.,  3.,  2.]])
               
    """
    n = len(levels)  # number of factors
    nb_lines = np.prod(levels)  # number of trial conditions
    H = np.zeros((nb_lines, n))
    
    level_repeat = 1
    range_repeat = np.prod(levels)
    for i in range(n):
        range_repeat //= levels[i]
        lvl = []
        for j in range(levels[i]):
            lvl += [j]*level_repeat
        rng = lvl*range_repeat
        level_repeat *= levels[i]
        H[:, i] = rng
     
    return H
    
################################################################################

def ff2n(n):
    """
    Create a 2-Level full-factorial design
    
    Parameters
    ----------
    n : int
        The number of factors in the design.
    
    Returns
    -------
    mat : 2d-array
        The design matrix with coded levels -1 and 1
    
    Example
    -------
    ::
    
        >>> ff2n(3)
        array([[-1., -1., -1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1., -1.],
               [-1., -1.,  1.],
               [ 1., -1.,  1.],
               [-1.,  1.,  1.],
               [ 1.,  1.,  1.]])
       
    """
    return 2*fullfact_corrected([2]*n) - 1

################################################################################

def fracfact(gen):
    """
    Create a 2-level fractional-factorial design with a generator string.
    
    Parameters
    ----------
    gen : str
        A string, consisting of lowercase, uppercase letters or operators "-"
        and "+", indicating the factors of the experiment
    
    Returns
    -------
    H : 2d-array
        A m-by-n matrix, the fractional factorial design. m is 2^k, where k
        is the number of letters in ``gen``, and n is the total number of
        entries in ``gen``.
    
    Notes
    -----
    In ``gen`` we define the main factors of the experiment and the factors
    whose levels are the products of the main factors. For example, if
    
        gen = "a b ab"
    
    then "a" and "b" are the main factors, while the 3rd factor is the product
    of the first two. If we input uppercase letters in ``gen``, we get the same
    result. We can also use the operators "+" and "-" in ``gen``.
    
    For example, if
    
        gen = "a b -ab"
    
    then the 3rd factor is the opposite of the product of "a" and "b".
    
    The output matrix includes the two level full factorial design, built by
    the main factors of ``gen``, and the products of the main factors. The
    columns of ``H`` follow the sequence of ``gen``.
    
    For example, if
    
        gen = "a b ab c"
    
    then columns H[:, 0], H[:, 1], and H[:, 3] include the two level full
    factorial design and H[:, 2] includes the products of the main factors.
    
    Examples
    --------
    ::
    
        >>> fracfact("a b ab")
        array([[-1., -1.,  1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1.,  1.]])
       
        >>> fracfact("A B AB")
        array([[-1., -1.,  1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1.,  1.]])
        
        >>> fracfact("a b -ab c +abc")
        array([[-1., -1., -1., -1., -1.],
               [ 1., -1.,  1., -1.,  1.],
               [-1.,  1.,  1., -1.,  1.],
               [ 1.,  1., -1., -1., -1.],
               [-1., -1., -1.,  1.,  1.],
               [ 1., -1.,  1.,  1., -1.],
               [-1.,  1.,  1.,  1., -1.],
               [ 1.,  1., -1.,  1.,  1.]])
       
    """
    # Recognize letters and combinations
    A = [item for item in re.split('\-?\s?\+?', gen) if item]  # remove empty strings
    C = [len(item) for item in A]
    
    # Indices of single letters (main factors)
    I = [i for i, item in enumerate(C) if item==1]
    
    # Indices of letter combinations (we need them to fill out H2 properly).
    J = [i for i, item in enumerate(C) if item!=1]
    
    # Check if there are "-" or "+" operators in gen
    U = [item for item in gen.split(' ') if item]  # remove empty strings
    
    # If R1 is either None or not, the result is not changed, since it is a
    # multiplication of 1.
    R1 = _grep(U, '+')
    R2 = _grep(U, '-')
    
    # Fill in design with two level factorial design
    H1 = ff2n(len(I))
    H = np.zeros((H1.shape[0], len(C)))
    H[:, I] = H1
    
    # Recognize combinations and fill in the rest of matrix H2 with the proper
    # products
    for k in J:
        # For lowercase letters
        xx = np.array([ord(c) for c in A[k]]) - 97
        
        # For uppercase letters
        if np.any(xx<0):
            xx = np.array([ord(c) for c in A[k]]) - 65
        
        H[:, k] = np.prod(H1[:, xx], axis=1)
    
    # Update design if gen includes "-" operator
    if R2:
        H[:, R2] *= -1
        
    # Return the fractional factorial design
    return H
    
def _grep(haystack, needle):
    try:
        haystack[0]
    except (TypeError, AttributeError):
        return [0] if needle in haystack else []
    else:
        locs = []
        for idx, item in enumerate(haystack):
            if needle in item:
                locs += [idx]
        return locs


#__all__ = ['bbdesign_corrected']

def bbdesign_corrected(n, center=None):
    """
    Create a Box-Behnken design
    
    Parameters
    ----------
    n : int
        The number of factors in the design
    
    Optional
    --------
    center : int
        The number of center points to include (default = 1).
    
    Returns
    -------
    mat : 2d-array
        The design matrix
    
    Example
    -------
    ::
    
        >>> bbdesign(3)
        array([[-1., -1.,  0.],
               [ 1., -1.,  0.],
               [-1.,  1.,  0.],
               [ 1.,  1.,  0.],
               [-1.,  0., -1.],
               [ 1.,  0., -1.],
               [-1.,  0.,  1.],
               [ 1.,  0.,  1.],
               [ 0., -1., -1.],
               [ 0.,  1., -1.],
               [ 0., -1.,  1.],
               [ 0.,  1.,  1.],
               [ 0.,  0.,  0.],
               [ 0.,  0.,  0.],
               [ 0.,  0.,  0.]])
        
    """
    assert n>=3, 'Number of variables must be at least 3'
    
    # First, compute a factorial DOE with 2 parameters
    H_fact = ff2n(2)
    # Now we populate the real DOE with this DOE
    
    # We made a factorial design on each pair of dimensions
    # - So, we created a factorial design with two factors
    # - Make two loops
    Index = 0
    nb_lines = int((0.5*n*(n-1))*H_fact.shape[0])
    H = repeat_center(n, nb_lines)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            Index = Index + 1
            H[max([0, (Index - 1)*H_fact.shape[0]]):Index*H_fact.shape[0], i] = H_fact[:, 0]
            H[max([0, (Index - 1)*H_fact.shape[0]]):Index*H_fact.shape[0], j] = H_fact[:, 1]

    if center is None:
        if n<=16:
            points= [0, 0, 0, 3, 3, 6, 6, 6, 8, 9, 10, 12, 12, 13, 14, 15, 16]
            center = points[n]
        else:
            center = n
        
    H = np.c_[H.T, repeat_center(n, center).T].T
    
    return H

def repeat_center(n, repeat):
    """
    Create the center-point portion of a design matrix
    
    Parameters
    ----------
    n : int
        The number of factors in the original design
    repeat : int
        The number of center points to repeat
    
    Returns
    -------
    mat : 2d-array
        The center-point portion of a design matrix (elements all zero).
    
    Example
    -------
    ::
    
        >>> repeat_center(3, 2)
        array([[ 0.,  0.,  0.],
               [ 0.,  0.,  0.]])
       
    """
    return np.zeros((repeat, n))
