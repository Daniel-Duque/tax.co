import sys
import pandas                    as pd

import python.build.ss_functions as ss
import python.build.output_io    as oio
import python.common.util               as util
import python.common.misc as c
import python.common.cl_args as cl


# The frequent division by 12 below is because income is measured monthly,
# whereas deductions and exemptions are in UVTs per year.

ppl = oio.readStage( cl.subsample
                      , "people_3_purchases." + cl.vat_strategy_suffix )

m = 1/12 # to convert from yearly to monthly income
         # (multiplication is faster than division)
muvt = c.uvt / 12

ppl["tax, gmf"] = (0.004 * ( ppl["income, cash"] - 11.6e6)
                  ).apply( lambda x: max(0,x) )

ppl["tax, ganancia ocasional"] = ppl["income, ganancia ocasional"] * 0.1
ppl["tax, indemnizacion"]      = ppl["income, indemnizacion"]      * 0.2
ppl["tax, donacion"]           = ppl["income, donacion"].apply(
  lambda x: (x - min( x*0.2, 2290*muvt)) * 0.1 )

for (goal,function) in [
      ("tax, pension"               , ss.mk_pension)
    , ("tax, pension, employer"     , ss.mk_pension_employer)
    , ("tax, salud"                 , ss.mk_salud)
    , ("tax, salud, employer"       , ss.mk_salud_employer)
    , ("tax, solidaridad"           , ss.mk_solidaridad)
    , ("tax, parafiscales"          , ss.mk_parafiscales_employer)
    , ("tax, cajas de compensacion" , ss.mk_cajas_de_compensacion_employer)
    , ("cesantias + primas"         , ss.mk_cesantias_y_primas_employer) ]:
  ppl[goal] = ppl.apply(
      lambda row: function( row["independiente"], row["income, labor, cash"] )
    , axis = "columns" )

if True: # income taxes
  ppl["taxable income, labor + pension"] = (
    (ppl["income, pension"] + ppl["income, labor"]).apply(
      lambda x: x - min( 0.325 * x, 5040 * muvt) )
    )
  ppl["tax, income, labor + pension"] = (
    ppl["taxable income, labor + pension"].apply( lambda x:
                    0                          if x < (1090*muvt)
      else (   (x - 1090*muvt)*0.19            if x < (1700*muvt)
        else ( (x - 1700*muvt)*0.28 + 116*muvt if x < (4100*muvt)
          else (x - 4100*muvt)*0.33 + 788*muvt ) ) ) )

  ppl["taxable income, capital w/o dividends"] = (
    ppl["income, capital w/o dividends"].apply(
      lambda x: x - min( 0.1 * x, 1000*muvt)
    ) )
  ppl["tax, income, capital w/o dividends"] = (
    ppl["taxable income, capital w/o dividends"].apply( lambda x:
                   0                               if x < ( 600*muvt)
      else (       (x - 600*muvt) *0.1             if x < (1000*muvt)
        else (     (x - 1000*muvt)*0.2  + 40*muvt  if x < (2000*muvt)
          else (   (x - 2000*muvt)*0.3  + 240*muvt if x < (3000*muvt)
            else ( (x - 3000*muvt)*0.35 + 540*muvt if x < (4000*muvt)
              else (x - 4000*muvt)*0.4  + 870*muvt ) ) ) ) ) )

  ppl["tax, dividends"] = (
    ppl["income, capital, dividends"].apply( lambda x:
             0                      if x < ( 600*muvt)
      else ( (x -  600*muvt) * 0.05 if x < (1000*muvt)
        else (x - 1000*muvt) * 0.1 + 20*muvt ) ) )

if True: # determine dependents, for income tax
  hh = ( ppl[["household","dependent"]]
         . groupby( "household" )
         . agg( 'sum' )
         . rename( columns = {"dependent":"dependents"} )
         . reset_index() )
  ppl = ( ppl.merge( hh, how='inner', on='household' )
          . drop( columns = "dependent" ) )
  ppl["has dependent"] = (
    ppl["member-by-income"] <= ppl["dependents"] )
  del(hh)

oio.saveStage( cl.subsample
             , ppl
             , 'people_4_income_taxish.' + cl.vat_strategy_suffix
)
