if True:
  import datetime
  import pandas as pd
  #
  import python.build.people_4_income_taxish_functions as f4
  from   python.common.util import near
  import python.build.output_io as oio
  import python.common.common   as com


def test_insert_has_dependent_column():
  d = pd.DataFrame(
      { "household"        : [1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4] ,
        "dependent"        : [0,0,1,1,1, 0,0,0,1,1, 0,0,0,0,1, 0,0] ,
        "dependents"       : [3,3,3,3,3, 2,2,2,2,2, 1,1,1,1,1, 0,0] ,
        "member-by-income" : [1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2] ,
        "has dependent"    : list( map( bool,
                             [1,1,1,0,0, # PITFALL: The 3rd 1 here is absurd.
                                         1,1,0,0,0, 1,0,0,0,0, 0,0] ) ) } )
  def rei( df: pd.DataFrame ) -> pd.DataFrame():
      return df . reindex( sorted(df.columns), axis=1) 
  d_input  =          rei( d.drop( columns = [ "dependents",
                                               "has dependent"] ) )
  d_intended_putput = rei( d.drop( columns = [ "dependent"] ) )
  d_output =          rei( f4.insert_has_dependent_column( d_input ) )
  return (d_input, d_intended_putput, d_output)
#  assert d_intended_putput . equals( d_output )

if True:
  log = str( datetime.datetime.now() )
  test_insert_has_dependent_column()
  oio.test_write( com.subsample
                , "people_4_income_taxish"
                , log )
