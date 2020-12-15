import numpy as np
import pandas as pd

 def builddf(self):
        df = pd.read_csv('Flowers.csv')
        subset = df[['x', 'y']]
        flowers = [tuple(x) for x in subset.to_numpy()]
        f = flowers
        genome = deepcopy(f)
        np.random.shuffle(genome)
        return genome