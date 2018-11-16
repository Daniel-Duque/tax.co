import sys
import pandas as pd
import numpy as np

import python.util as util
import python.build.output_io as oio
from python.build.people.files import edu_key
import python.build.common as common


people = oio.readStage( common.subsample, "people_4_ss." + common.vat_strategy_suffix )

people["education"] = util.interpretCategorical( people["education"]
                                               , edu_key.values() )

if True: # compute five columns for top five member incomes
  people["income, rank 1"] = (
    people["income"] * (people["member-by-income"] == 1) )
  people["income, rank 2"] = (
    people["income"] * (people["member-by-income"] == 2) )
  people["income, rank 3"] = (
    people["income"] * (people["member-by-income"] == 3) )
  people["income, rank 4"] = (
    people["income"] * (people["member-by-income"] == 4) )
  people["income, rank 5"] = (
    people["income"] * (people["member-by-income"] == 5) )

  people["income, labor, rank 1"] = (
    people["income, labor"] * (people["member-by-income"] == 1) )
  people["income, labor, rank 2"] = (
    people["income, labor"] * (people["member-by-income"] == 2) )
  people["income, labor, rank 3"] = (
    people["income, labor"] * (people["member-by-income"] == 3) )
  people["income, labor, rank 4"] = (
    people["income, labor"] * (people["member-by-income"] == 4) )
  people["income, labor, rank 5"] = (
    people["income, labor"] * (people["member-by-income"] == 5) )


if True: # aggregate from household members to households
  people["members"] = 1
  h_first = people.groupby( ['household']
    ) ['region-1','region-2','estrato', 'weight' # these are constant within household
    ] . agg('first')
  h_sum = people.groupby(
      ['household']
    ) [  'value'
       ,'vat paid, min','vat paid, max'
       , "income, rank 1"
       , "income, rank 2"
       , "income, rank 3"
       , "income, rank 4"
       , "income, rank 5"
       , "income, labor, rank 1"
       , "income, labor, rank 2"
       , "income, labor, rank 3"
       , "income, labor, rank 4"
       , "income, labor, rank 5"
       , "pension", "salud", "solidaridad"
       , 'transactions','income','members'
       , 'income, pension'
       , 'income, cesantia'
       , 'income, capital, dividends'
       , 'income, capital w/o dividends'
       , 'income, infrequent'
       , 'income, govt'
       , 'income, private'
       , 'income, labor'
    ] . agg('sum')
  h_min = people.groupby(
      ['household']
    ) ['age','female'
    ] . agg('min'
    ) . rename( columns = {'age' : 'age-min',
                           'female' : 'has-male',
    } )
  h_min["has-male"] = 1 - h_min["has-male"]
    # if female is ever 0, then its min = 0, i.e. there is a male
  h_max = people.groupby(
      ['household']
    ) ['age','literate','student','female','female head','education',
       'race, indig', 'race, git|rom', 'race, raizal', 'race, palenq', 'race, whi|mest'
    ] . agg('max'
    ) . rename( columns = {'age' : 'age-max',
                           'literate' : 'has-lit',
                           'student' : 'has-student',
                           'education' : 'edu-max',
                           'female' : 'has-female',
                           'race, indig' : 'has-indig',
                           'race, git|rom' : 'has-git|rom',
                           'race, raizal' : 'has-raizal',
                           'race, palenq' : 'has-palenq',
                           'race, whi|mest' : 'has-whi|mest'
    } )
  households = pd.concat( [h_first,h_sum,h_min,h_max]
                        , axis=1 )

  households["vat/value, min"] = households["vat paid, min"]/households["value"]
  households["vat/value, max"] = households["vat paid, max"]/households["value"]
  households["vat/income, min"] = households["vat paid, min"]/households["income"]
  households["vat/income, max"] = households["vat paid, max"]/households["income"]
  households["value/income"] = households["value"]/households["income"]

  households["household"] = households.index
    # when there are multiple indices, reset_index is the way to do that

  households["has-child"] = households["age-min"] < 18
  households["has-elderly"] = households["age-max"] > 65

  households["income-decile"] = pd.qcut( # PITFALL: there's a different such variable at the person level
    households["income"], 10, labels = False, duplicates='drop')

  households["income-percentile"] = pd.qcut( # PITFALL: there's a different such variable at the person level
    households["income"], 100, labels = False, duplicates='drop')

  households["one"] = 1


if True: # data sets derived from households
  if True: # households with income
    households_w_income = households[ households["income"] > 0 ].copy()
      # Without the copy (even if I use .loc(), as suggested by the error)
      # this causes an error about modifying a view.
    households_w_income["income-decile"] = pd.qcut(
      households_w_income["income"], 10, labels = False, duplicates='drop')

  if True: # summaries of the income deciles in two data sets
    households_w_income_decile_summary = \
      util.summarizeQuantiles("income-decile", households_w_income)

    households_decile_summary = \
      util.summarizeQuantiles("income-decile", households)


if True: # save
  oio.saveStage( common.subsample, households
                        , 'households.' + common.vat_strategy_suffix )
  oio.saveStage( common.subsample, households_w_income
                        , 'households_w_income.' + common.vat_strategy_suffix )
  oio.saveStage( common.subsample, households_w_income_decile_summary
                        , 'households_w_income_decile_summary.' + common.vat_strategy_suffix )
  oio.saveStage( common.subsample, households_decile_summary
                       , 'households_decile_summary.' + common.vat_strategy_suffix )