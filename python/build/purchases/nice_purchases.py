import pandas as pd
from python.build.classes import File, Correction
import python.common.misc as c


files = [

  File( "rural_personal"
    , "Gastos_personales_Rural.csv"
    , c.variables +
      [ ( "NC2R_CE_P2", 0, "coicop", 0 )
      , ( "NC2R_CE_P4S1", 0, "quantity", 0 )
      , ( "NC2R_CE_P5S2", 0, "how-got", 0 )
      , ( "NC2R_CE_P6", 0, "where-got", 0 )
      , ( "NC2R_CE_P7", 0, "value", 0 )
      , ( "NC2R_CE_P8", 0, "freq", 0 ) ]
    , c.corrections
  )

  , File( "rural_personal_fuera"
    , "Gastos_personales_Rural_-_Comidas_preparadas_fuera_del_Hogar.csv"
    , c.variables +
      [ ( "NC2R_CA_P3", 0, "coicop", 0 )
      , ( "NC2R_CA_P4_S1", 0, "quantity", 0 )
      , ( "NC2R_CA_P5_S1", 0, "how-got", 0 )
      , ( "NC2R_CA_P6_S1", 0, "where-got", 0 )
      , ( "NC2R_CA_P7_S1", 0, "value", 0 )
      , ( "NC2R_CA_P8_S1", 0, "freq", 0 ) ]
    , c.corrections
  )

  , File( "rural_semanal"
    , "Gastos_semanales_Rurales.csv"
    , c.variables +
      [ ( "NC2R_CA_P3", 0, "coicop", 0 )
      , ( "NC2R_CA_P4_S1", 0, "quantity", 0 )
      , ( "NC2R_CA_P5_S1", 0, "how-got", 0 )
      , ( "NC2R_CA_P6_S1", 0, "where-got", 0 )
      , ( "NC2R_CA_P7_S1", 0, "value", 0 )
      , ( "NC2R_CA_P8_S1", 0, "freq", 0 ) ]
    , c.corrections
  )

  , File( "rural_semanal_fuera"
    , "Gastos_semanales_Rural_-_Comidas_preparadas_fuera_del_hogar.csv"
    , c.variables +
      [ ( "NH_CGPRCFH_P1S1", 0, "coicop", 0 )
      , ( "NH_CGPRCFH_P2", 0, "quantity", 0 )
      , ( "NH_CGPRCFH_P3", 0, "how-got", 0 )
      , ( "NH_CGPRCFH_P4", 0, "where-got", 0 )
      , ( "NH_CGPRCFH_P5", 0, "value", 0 )
      , ( "NH_CGPRCFH_P6", 0, "freq", 0 ) ]
    , c.corrections
  )

  , File( "urban_diario"
    , "Gastos_diarios_Urbanos.csv"
    , c.variables +
      [ ( "P10250S1A1", 0, "within-household-transfer", 0 )
      , ( "NH_CGDU_P1", 0, "coicop", 0 )
      , ( "NH_CGDU_P2", 0, "quantity", 0 )
      , ( "NH_CGDU_P5", 0, "how-got", 0 )
      , ( "NH_CGDU_P7B1379", 0, "where-got", 0 )
      , ( "NH_CGDU_P8", 0, "value", 0 )
      , ( "NH_CGDU_P9", 0, "freq", 0 ) ]
    , c.corrections
      + [ # The "within-household transfer" variable is almost always null. If it's not,
        # drop the observation. Then drop that column.
        Correction.Drop_Row_If_Column_Satisfies_Predicate( "within-household-transfer"
                                                           , pd.notnull
                                                         )
        , Correction.Drop_Column( "within-household-transfer" )
      ]
  )

  , File( "urban_diario_fuera"
    , "Gastos_diarios_del_hogar_Urbano_-_Comidas_preparadas_fuera_del_hogar.csv"
    , c.variables +
      [ ( "NH_CGDUCFH_P1_1", 0, "coicop", 0 )
      , ( "NH_CGDUCFH_P2", 0, "quantity", 0 )
      , ( "NH_CGDUCFH_P3", 0, "how-got", 0 )
      , ( "NH_CGDUCFH_P4", 0, "where-got", 0 )
      , ( "NH_CGDUCFH_P5", 0, "value", 0 )
      , ( "NH_CGDUCFH_P6", 0, "freq", 0 ) ]
    , c.corrections
  )

  , File( "urban_diario_personal"
    , "Gastos_diarios_personales_Urbano.csv"
    , c.variables +
      [ ( "NC4_CC_P1_1", 0, "coicop", 0 )
      , ( "NC4_CC_P2", 0, "quantity", 0 )
      , ( "NC4_CC_P3", 0, "how-got", 0 )
      , ( "NC4_CC_P4", 0, "where-got", 0 )
      , ( "NC4_CC_P5", 0, "value", 0 )
      , ( "NC4_CC_P6", 0, "freq", 0 ) ]
    , c.corrections
  )

  , File( "urban_personal_fuera"
    , "Gastos_personales_Urbano_-_Comidas_preparadas_fuera_del_hogar.csv"
    , c.variables +
      [ ( "NH_CGPUCFH_P1_S1", 0, "coicop", 0 )
      , ( "NH_CGPUCFH_P2", 0, "quantity", 0 )
      , ( "NH_CGPUCFH_P3", 0, "how-got", 0 )
      , ( "NH_CGPUCFH_P4", 0, "where-got", 0 )
      , ( "NH_CGPUCFH_P5", 0, "value", 0 )
      , ( "NH_CGPUCFH_P6", 0, "freq", 0 ) ]
    , c.corrections
  )
]
