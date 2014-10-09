'''constants.py

A collection of physical constants for the atmosphere and ocean.

Code developed by Brian Rose, University at Albany
brose@albany.edu
in support of the class ATM/ENV 415: Climate Laboratory
'''

import numpy as np

a = 6.373E6      #  Radius of Earth, in m
Lhvap = 2.5E6    #  Latent heat of vaporization, in J / kg
Lhsub = 2.834E6   # Latent heat of sublimation, in J / kg
Lhfus = Lhsub - Lhvap  #  Latent heat of fusion, in J / kg
cp = 1004.        #  specific heat at constant pressure for dry air, in J / kg / K
Rd = 287.         #  gas constant for dry air, in J / kg / K
kappa = Rd / cp
Rv = 461.5       #  gas constant for water vapor, in J / kg / K
cpv = 1875.       # specific heat at constant pressure for water vapor, in J / kg / K
Omega = 2 * np.math.pi / 24. /3600.  # Earth's rotation rate, in s**(-1)
g = 9.8          #  gravitational acceleration, in m / s**2
sigma = 5.67E-8  #  Stefan-Boltzmann constant for blackbody radiation, W / m**2 / K**4
kBoltzmann = 1.38E-23  #  J / K, the Boltzmann constant

S0 = 1365.2       #  solar constant, W / m**2 
# value is consistent with Trenberth and Fasullo, Surveys of Geophysics 2012

ps = 1000.       #  approximate surface pressure, mb or hPa

rho_w = 1000.    #  density of water, kg / m**3
cw = 4181.3      #  specific heat of liquid water, J / kg / K

tempCtoK = 273.15   # 0degC in kelvin
tempKtoC = -tempCtoK  # 0 K in degC
mb_to_Pa = 100.  # conversion factor from mb to Pa

#  Some useful time conversion factors
seconds_per_minute = 60.
seconds_per_hour = 60. * seconds_per_minute
seconds_per_day = 24. * seconds_per_hour
seconds_per_month = 30. * seconds_per_day  # approximate, for 30-day month.
days_per_year = 365.2422  # the length of the "tropical year" -- time between vernal equinoxes
seconds_per_year = seconds_per_day * days_per_year

area_earth = 4 * np.math.pi * a**2

