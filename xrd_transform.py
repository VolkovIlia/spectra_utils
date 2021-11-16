import numpy as np
import math

def xrd_transform(double_theta_1, lambda1, lambda2):
    """
    lambda1 and lambda2 must be in the same units
    parameter
    ---------
    double_theta_1 : numpy.array
        array of 2theta in degrees
    lambda1 : float
        wavelength of x-rays which was used to gain pattern
    lambda2 : float
        wavelength of x-rays to convert data to

    return
    ------
    double_theta_2 : numpy.array
        array of 2theta in degrees after conversion
    """
    theta1 = double_theta_1 * math.pi / 180 / 2
    theta2 = np.arcsin(lambda2 * np.sin(theta1) / lambda1)
    double_theta_2 = theta2 * 180 * 2 / math.pi
    return double_theta_2
