import numpy as np

def dist(x, y, z):
    '''
    Get the magnitude of a vector with three components (x, y, z).

    Parameters:
    ----------
        x : float | int 
            The x component of the vector.
        y : float | int 
            The y component of the vector.
        z : float | int 
            The z component of the vector.

    Returns
    -------
        The magnitude of the vector.
    '''

    result = np.sqrt(np.square(x) + np.square(y) + np.square(z))
    return result
