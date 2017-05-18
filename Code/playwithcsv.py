#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:47:00 2017

@author: carla.agurto
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
data = pd.read_csv('../data/oecd-countries.csv')


data.set_index('Country', inplace=True)
data['EducationalAttainment'].plot.bar()
plt.title('EducationalAttainment by country')
plt.savefig('EducationalAttainment.png')
plt.figure()
data.plot()
plt.title('All information')