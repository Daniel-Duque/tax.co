
if True:
  import sys
  import pandas as pd
  #
  import python.common.util as util
  import python.build.output_io as oio
  import python.common.common as c


if True: # old: merging purchase sums into people
  purchase_sums = oio.readStage( c.subsample, "purchase_sums." + c.strategy_suffix )

  if True: # merge purchase sums into people
    people = pd.merge( people, purchase_sums
                     , how = "left"
                     , on=["household", "household-member"] )
    for s in ["min", "max"]:
      people.loc[ people["region-1"] == "SAN ANDRÉS", "vat paid, " + s ] = 0

  if True: # create a few more variables
    people["vat/value, min" ] = people["vat paid, min"] / people["value" ]
    people["vat/value, max" ] = people["vat paid, max"] / people["value" ]
    people["vat/income, min"] = people["vat paid, min"] / people["income"]
    people["vat/income, max"] = people["vat paid, max"] / people["income"]
    people["value/income"   ] = people["value"]         / people["income"]

if True: # old in households.py
  households["vat/value, min"]  = households["vat paid, min"]/households["value"]
  households["vat/value, max"]  = households["vat paid, max"]/households["value"]
  households["vat/income, min"] = households["vat paid, min"]/households["income"]
  households["vat/income, max"] = households["vat paid, max"]/households["income"]
  households["value/income"]    = households["value"]/households["income"]

if True: # old test for people_3
  # see people_3_purchases_test for how to use new_cols
  new_cols = [ "vat/value, min",
               "vat/value, max",
               "vat/income, min",
               "vat/income, max",
               "value/income" ]

  if True: # some places should be San Andrés, and they should have no IVA.
    assert (p3["region-1"] == "SAN ANDRÉS").any()
    assert p3[ p3["region-1"] == "SAN ANDRÉS" ]["vat paid, min"].max() == 0
    assert p3[ p3["region-1"] == "SAN ANDRÉS" ]["vat paid, max"].max() == 0

  per_cell_spec = {
      # see people_3_purchases_test for how to use this
      "vat/value, min"  : { cl.IsNull(), cl.InRange( 0, 0.3 ) },
      "vat/value, max"  : { cl.IsNull(), cl.InRange( 0, 0.3 ) },
      "vat/income, min" : { cl.IsNull(), cl.InRange( 0, np.inf ) },
      "vat/income, max" : { cl.IsNull(), cl.InRange( 0, np.inf ) },
      "value/income"    : { cl.IsNull(), cl.InRange( 0, np.inf ) },

  per_column_spec = {
      # see people_3_purchases_test for how to use this
      "vat/value, min"  : cl.CoversRange( 0,      0.15   ),
      "vat/value, max"  : cl.CoversRange( 0,      0.15   ),
      "vat/income, min" : cl.CoversRange( 0,      np.inf ),
      "vat/income, max" : cl.CoversRange( 0,      np.inf ),
      "value/income"    : cl.CoversRange( 0.01,   np.inf ),

  assert ( len( p3    .columns ) ==
           len( p2cols.columns ) +
           len( prCols.columns ) - 2 + # omit the 2 keys we merged on
           len( new_cols ) )
