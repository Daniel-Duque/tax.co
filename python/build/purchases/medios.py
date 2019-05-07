# This file would be relevant, because it records house purchases,
# but the VAT is charged only on sales of new homes,
# and newness is not reported in the ENPH.

import pandas as pd
from numpy import nan
import python.build.classes as classes
import python.common.misc as c


files = [
  classes.File( "medios"
    , "Gastos_menos_frecuentes_-_Medio_de_pago.csv"
    , { **c.variables
      , "P10305"   : "new-or-old-house"
      , "P10305S1" : "value"
    }, [ classes.Correction.Create_Constant_Column( "quantity", 1 )
       , classes.Correction.Create_Constant_Column( "how-got", 1 )
       , classes.Correction.Create_Constant_Column( "coicop", nan ) ]
      + c.corrections
        # TODO (#safe) : "where-got"
        # TODO (#safe) : "freq" = in the last year
) ]
