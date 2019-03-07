import numpy                     as np
import pandas                    as pd

import python.build.output_io    as oio
import python.common.misc        as c
import python.common.cl_fake     as cl


people = oio.readStage( cl.subsample
                      , 'people_4_income_taxish.' + cl.vat_strategy_suffix )

ppl = people.rename( columns = {
    "relative, child" : "child"
  , "relative, non-child" : "rel"
  , "dependent" : "dep"
  , "disabled" : "disab"
  , "income, labor" : "labor" } )

# These should all have a mean of 1
ppl["dep"][
  (ppl["student"] == 1) & (ppl["age"] < 24) ].mean()

ppl["dep"][
  (ppl["child"] == 1) & (ppl["age"] < 19) ].mean()

ppl["dep"][
  ((ppl["rel"]==1) & (ppl["labor"] < (260*c.uvt) ) ) ].mean()

ppl["dep"][
  ((ppl["child"]==1) & (ppl["disab"]==1)) ].mean()

# and this, a mean of 0
ppl["dep"] [ ~(
    ((ppl["student"] == 1) & (ppl["age"] < 24))
  | ((ppl["child"] == 1)   & (ppl["age"] < 19))
  | ((ppl["rel"]==1)       & (ppl["labor"] < (260*c.uvt) ) )
  | ((ppl["child"]==1)     & (ppl["disab"]==1)) ) ].mean()
