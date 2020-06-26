import seaborn as sn
import numpy as np
import pandas as pd

dataFrame = pd.DataFrame(np.random.random(7,7))

sn.heatmap(dataFrame)