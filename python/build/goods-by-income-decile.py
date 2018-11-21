import pandas as pd
import python.build.output_io as oio
import python.build.common as common


# PITFALL: Always the detail vat strategy, because irrelevant.
hs = oio.readStage( common.subsample
                    , "households." + "detail_"
                  , usecols = ["household", "income-decile"]
)

ps = oio.readStage( common.subsample, 'purchases_1_5_no_origin'
                  , usecols = ["household", "value", "coicop"]  
)

ps = ps.merge( hs, on = "household" )

out = ps  . groupby( ["income-decile","coicop"]
  ) . agg( {"value":"sum"}
  ) . sort_values( "value"
                 , ascending = False
  ) . reset_index(
  ) . groupby( ["income-decile"]
  ) . head( 20
  ) . sort_values( ["income-decile","value"]
                 , ascending = [True,False]
)

out.to_csv( "output/vat/tables/recip-" + str(common.subsample) + "/goods_by_income_decile.csv" )

