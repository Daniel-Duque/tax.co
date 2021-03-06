# These functions use the schedules encoded at
# `python/build/ss_schedules.py` to compute someone's
# "generalized income taxes" (a term I am inventing,
# which include things like social security contributions,
# which is not technically a tax).

if True:
  import pandas                    as pd
  #
  import python.build.ss_schedules as ss
  import python.common.util        as util


def mk_pension( independiente, income ):
  if independiente:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contrib_schedule_for_contractor["pension"] )
    return compute_base( income ) * rate
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contrib_schedule_for_employee["pension"] )
    return compute_base( income ) * rate

def mk_pension_employer( independiente, income ):
  if independiente: return 0
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contribs_by_employer["pension"] )
    return compute_base( income ) * rate

def mk_salud( independiente, income ):
  if independiente:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contrib_schedule_for_contractor["salud"] )
    return compute_base( income ) * rate
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contrib_schedule_for_employee["salud"] )
    return compute_base( income ) * rate

def mk_salud_employer( independiente, income ):
  if independiente: return 0
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contribs_by_employer["salud"] )
    return compute_base( income ) * rate

def mk_solidaridad( independiente, income ):
  if independiente:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contrib_schedule_for_contractor["solidaridad"] )
    return compute_base( income ) * rate
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contrib_schedule_for_employee["solidaridad"] )
    return compute_base( income ) * rate

def mk_parafiscales_employer( independiente, income ):
  if independiente: return 0
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contribs_by_employer["parafiscales"] )
    return compute_base( income ) * rate

def mk_cajas_de_compensacion_employer( independiente, income ):
  if independiente: return 0
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contribs_by_employer["cajas de compensacion"] )
    return compute_base( income ) * rate

def mk_cesantias_y_primas_employer( independiente, income ):
  if independiente: return 0
  else:
    (_, compute_base, rate) = util.tuple_by_threshold(
        income, ss.ss_contribs_by_employer["cesantias + primas"] )
    return compute_base( income ) * rate

def mk_ss_contribs( ppl : pd.DataFrame ) -> pd.DataFrame:
  """PITFALL: Destructive."""
  for (goal,function) in [
      ( "tax, ss, pension",
        mk_pension)
    , ( "tax, ss, pension, employer",
        mk_pension_employer)
    , ( "tax, ss, salud",
        mk_salud)
    , ( "tax, ss, salud, employer",
        mk_salud_employer)
    , ( "tax, ss, solidaridad",
        mk_solidaridad)
    , ( "tax, ss, parafiscales",
        mk_parafiscales_employer)
    , ( "tax, ss, cajas de compensacion",
        mk_cajas_de_compensacion_employer)
    , ( "cesantias + primas",
        mk_cesantias_y_primas_employer) ]:

    ppl[goal] = ppl.apply(
        lambda row: function(
            row["independiente"],
            row["income, labor, cash"] )
      , axis = "columns" )

  ppl["tax, ss, total employee contribs"] = (
    ppl["tax, ss, pension"] +
    ppl["tax, ss, salud"] +
    ppl["tax, ss, solidaridad"] )

  return ppl
