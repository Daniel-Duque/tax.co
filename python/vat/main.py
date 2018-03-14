# The value-added tax.

import numpy as np
import pandas as pd
import python.util as util
import python.datafiles as datafiles
import python.vat.files as vatfiles
import os


subsample = 1 # The reciprocal of the subsample size. Valid values include 1, 10, 100 and 1000.
purchases = pd.DataFrame() # accumulator: begins empty, accumulates across files
files = list( vatfiles.purchase_file_legends.keys() )

def saveStage(data,name):
  path = 'output/vat-data/recip-' + str(subsample)
  if not os.path.exists(path): os.makedirs(path)
  data.to_csv( path + '/' + name + ".csv" )

def readStage(name): # to skip rebuilding something
  path = 'output/vat-data/recip-' + str(subsample)
  return pd.read_csv( path + '/' + name + ".csv" )


if True: # build the purchase data
  for file in files:
    legend = vatfiles.purchase_file_legends[file]
    shuttle = pd.read_csv( datafiles.yearSubsampleSurveyFolder(2017,subsample) + file + '.csv'
                        , usecols = list( legend.keys() )
    )
    shuttle = shuttle.rename(columns=legend) # homogenize column names across files
    shuttle["file-origin"] = file
  
    if False: # print summary stats for `shuttle`, before merging with `purchases`
      print( "\n\nFILE: " + file + "\n" )
      for colname in shuttle.columns.values:
        col = shuttle[colname]
        print("\ncolumn: " + colname)
        print("missing: " + str(len(col.index)-col.count())
              + " / "  + str(len(col.index)))
        print( col.describe() )

    purchases = purchases.append(shuttle)
  del(shuttle)
  saveStage(purchases, '/1.purchases')

if True: # merge coicop, construct some money-valued variables
  # TODO ? sort both frames on coicop before merging, for speed
  coicop_vat = pd.read_csv( "data/vat/coicop-vat.csv", sep=';' )
  purchases = purchases.merge( coicop_vat, on="coicop" )
  purchases["price"] = purchases["value"] / purchases["quantity"]
  purchases["vat-paid"] = purchases["value"] * purchases["vat-rate"]
  saveStage(purchases, '/2.purchases,prices,taxes')
  purchases["transactions"] = 1

if True: # build the person expenditure data
  people = purchases.groupby(
    ['household', 'household-member'])['value','vat-paid',"transactions"].agg('sum')
  people = people.reset_index(level = ['household', 'household-member'])
    # https://stackoverflow.com/questions/20461165/how-to-convert-pandas-index-in-a-dataframe-to-a-column
  saveStage(people, '/3.person-level-expenditures')

if True: # merge demographic statistics
  # PITFALL: Even if using a subsample of purchases, use the complete demographic data sample
  demog = pd.read_csv( datafiles.yearSubsampleSurveyFolder(2017,1) + 'st2_sea_enc_per_csv.csv'
                    , usecols = list( vatfiles.person_file_legend.keys() )
  )
  demog = demog.rename(columns=vatfiles.person_file_legend) # homogenize column names across files
  saveStage(demog, '/4.demog')
  people = pd.merge( people, demog, on=["household","household-member"] )
  del(demog)

saveStage(people, '/5.person-demog-expenditures')
