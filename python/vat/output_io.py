import pandas as pd
import os


def saveStage(subsample,data,name):
  path = 'output/vat-data/recip-' + str(subsample)
  if not os.path.exists(path): os.makedirs(path)
  data.to_csv( path + '/' + name + ".csv" )

def readStage(subsample,name): # to skip rebuilding something
  path = 'output/vat-data/recip-' + str(subsample)
  return pd.read_csv( path + '/' + name + ".csv" )


if False:
  # Commonly used (copy, paste) commands to read into Python's working memory the data generated by build.py

  subsample = 1

  # intermediate data sets
    # purchasesEarly = ooio.readStage( subsample, '/1.purchases') # memory hog
    # demog = ooio.readStage( subsample, '/4.demog')

  purchases = ooio.readStage( subsample, '/2.purchases,prices,taxes') # memory hog
  people = ooio.readStage( subsample, '/5.person-demog-expenditures')
  households = ooio.readStage( subsample, '/6.households')
