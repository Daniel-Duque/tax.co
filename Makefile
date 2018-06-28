SHELL := bash
.PHONY: raw subsamples vat_subsamples                         \
  vat_1 vat_10 vat_100 vat_1000                               \
  vat_pics_1 vat_pics_10                                      \
  vat_pics_households_1 vat_pics_households_10                \
  vat_pics_income-households_1 vat_pics_income-households_10  \
  vat_pics_people_1 vat_pics_people_10                        \
  vat_pics_purchases_1 vat_pics_purchases_10

##=##=##=##=##=##=##=## Variables

python_from_here = PYTHONPATH='.' python3

enph_files = coicop              \
  factores_ciclo19               \
  hogares_tot_completos          \
  st2_sea_enc_gcar_csv           \
  st2_sea_enc_gcau_csv           \
  st2_sea_enc_gcfhr_ce_csv       \
  st2_sea_enc_gcfhr_csv          \
  st2_sea_enc_gcfhu_diarios_csv  \
  st2_sea_enc_gcfhup_diarios_csv \
  st2_sea_enc_gdr_csv            \
  st2_sea_enc_gdrj1_csv          \
  st2_sea_enc_gdsr_mer_csv       \
  st2_sea_enc_gdsu_mer_csv       \
  st2_sea_enc_gmf_csv            \
  st2_sea_enc_gmf_transpuesta    \
  st2_sea_enc_gsdp_dia_csv       \
  st2_sea_enc_gsdp_diarios_csv   \
  st2_sea_enc_gsdu_dia_csv       \
  st2_sea_enc_gsdu_diarios_csv   \
  st2_sea_enc_hogc3_csv          \
  st2_sea_enc_hog_csv            \
  st2_sea_enc_per_csv

enig_files = Ig_gsdp_dias_sem    \
  Ig_gsdp_gas_dia                \
  Ig_gsdp_perceptores            \
  Ig_gsdu_caract_alim            \
  Ig_gsdu_dias_sem               \
  Ig_gsdu_gas_dia                \
  Ig_gsdu_gasto_alimentos_cap_c  \
  Ig_gsdu_mercado                \
  Ig_gs_hogar                    \
  Ig_gsmf_compra                 \
  Ig_gsmf_forma_adqui            \
  Ig_gsmf_serv_pub               \
  Ig_gssr_caract_alim            \
  Ig_gssr_gas_sem                \
  Ig_gssr_gasto_alimentos_cap_c  \
  Ig_gssr_mercado                \
  Ig_gs_vivienda                 \
  Ig_ml_desocupado               \
  Ig_ml_hogar                    \
  Ig_ml_inactivo                 \
  Ig_ml_ocupado                  \
  Ig_ml_pblcion_edad_trbjar      \
  Ig_ml_persona                  \
  Ig_ml_vivienda

enig_orig = $(addsuffix .txt, $(addprefix data/enig-2007/orig-txt/, $(enig_files)))
enph_orig = $(addsuffix .dta, $(addprefix data/enph-2017/orig-dta/, $(enph_files)))
subsamples = $(addsuffix .csv, $(addprefix data/enph-2017/recip-1/, $(enph_files)))      \
             $(addsuffix .csv, $(addprefix data/enig-2007/recip-1/, $(enig_files)))      \
             $(addsuffix .csv, $(addprefix data/enph-2017/recip-10/, $(enph_files)))     \
             $(addsuffix .csv, $(addprefix data/enig-2007/recip-10/, $(enig_files)))     \
             $(addsuffix .csv, $(addprefix data/enph-2017/recip-100/, $(enph_files)))    \
             $(addsuffix .csv, $(addprefix data/enig-2007/recip-100/, $(enig_files)))    \
             $(addsuffix .csv, $(addprefix data/enph-2017/recip-1000/, $(enph_files)))   \
             $(addsuffix .csv, $(addprefix data/enig-2007/recip-1000/, $(enig_files)))

vat_pics_rootless =                      \
  $(vat_pics_households_rootless)        \
  $(vat_pics_income-households_rootless) \
  $(vat_pics_people_rootless)            \
  $(vat_pics_purchases_rootless)         
vat_pics_households_rootless = households/oldest.png       \
  households/transactions-per-month.png                    \
  households/youngest.png                                  \
  households/size.png                                      \
  households/max-edu.png                                   \
  households/VAT-over-consumption,-by-income-decile.png    \
  households/income.png
vat_pics_income-households_rootless =                      \
  income-households/VAT-over-income,-by-has-elderly.png    \
  income-households/VAT-over-income,-by-has-child.png      \
  income-households/spending-over-income.png               \
  income-households/VAT-over-income,-by-income-decile.png
vat_pics_people_rootless =                                 \
  people/transactions-per-month.png                        \
  people/spending-per-month.png                            \
  people/age.png                                           \
  people/education.png                                     \
  people/income.png
vat_pics_purchases_rootless = purchases/value.png          \
  purchases/frequency.png                                  \
  purchases/quantity.png                                   \
  purchases/frequency-cdf.png                              \
  purchases/vat-in-pesos.png

vat_pics_households_1    = $(addprefix output/vat-pics/recip-1/,    $(vat_pics_households_rootless))
vat_pics_households_10   = $(addprefix output/vat-pics/recip-10/,   $(vat_pics_households_rootless))
vat_pics_households_100  = $(addprefix output/vat-pics/recip-100/,  $(vat_pics_households_rootless))
vat_pics_households_1000 = $(addprefix output/vat-pics/recip-1000/, $(vat_pics_households_rootless))

vat_pics_income-households_1    = $(addprefix output/vat-pics/recip-1/,    $(vat_pics_income-households_rootless))
vat_pics_income-households_10   = $(addprefix output/vat-pics/recip-10/,   $(vat_pics_income-households_rootless))
vat_pics_income-households_100  = $(addprefix output/vat-pics/recip-100/,  $(vat_pics_income-households_rootless))
vat_pics_income-households_1000 = $(addprefix output/vat-pics/recip-1000/, $(vat_pics_income-households_rootless))

vat_pics_people_1    = $(addprefix output/vat-pics/recip-1/,    $(vat_pics_people_rootless))
vat_pics_people_10   = $(addprefix output/vat-pics/recip-10/,   $(vat_pics_people_rootless))
vat_pics_people_100  = $(addprefix output/vat-pics/recip-100/,  $(vat_pics_people_rootless))
vat_pics_people_1000 = $(addprefix output/vat-pics/recip-1000/, $(vat_pics_people_rootless))

vat_pics_purchases_1    = $(addprefix output/vat-pics/recip-1/,    $(vat_pics_purchases_rootless))
vat_pics_purchases_10   = $(addprefix output/vat-pics/recip-10/,   $(vat_pics_purchases_rootless))
vat_pics_purchases_100  = $(addprefix output/vat-pics/recip-100/,  $(vat_pics_purchases_rootless))
vat_pics_purchases_1000 = $(addprefix output/vat-pics/recip-1000/, $(vat_pics_purchases_rootless))

vat_pics_1 = $(vat_pics_households_1) $(vat_pics_income-households_1) $(vat_pics_people_1) $(vat_pics_purchases_1)
vat_pics_10 = $(vat_pics_households_10) $(vat_pics_income-households_10) $(vat_pics_people_10) $(vat_pics_purchases_10)

# The VAT data build is divided into two stages:
  # "early" (big, slow, hopefully infrequent) and "late"

vat_files = $(vat_files_early) $(vat_files_late)
vat_files_early = 1.purchases.csv                \
  2.purchases,prices,taxes.csv
vat_files_late = 3.person-level-expenditures.csv \
  4.demog.csv                                    \
  5.person-demog-expenditures.csv                \
  6.households.csv				 \
  7.households_w_income.csv			 \
  8.households_w_income_decile_summary.csv	 \
  9.households_decile_summary.csv

vat_subsamples = $(vat_1) $(vat_10) $(vat_100) $(vat_1000)
vat_1    = $(addprefix output/vat-data/recip-1/,    $(vat_files))
vat_10   = $(addprefix output/vat-data/recip-10/,   $(vat_files))
vat_100  = $(addprefix output/vat-data/recip-100/,  $(vat_files))
vat_1000 = $(addprefix output/vat-data/recip-1000/, $(vat_files))

vat_1_early    = $(addprefix output/vat-data/recip-1/,    $(vat_files_early))
vat_10_early   = $(addprefix output/vat-data/recip-10/,   $(vat_files_early))
vat_100_early  = $(addprefix output/vat-data/recip-100/,  $(vat_files_early))
vat_1000_early = $(addprefix output/vat-data/recip-1000/, $(vat_files_early))

vat_1_late    = $(addprefix output/vat-data/recip-1/,    $(vat_files_late))
vat_10_late   = $(addprefix output/vat-data/recip-10/,   $(vat_files_late))
vat_100_late  = $(addprefix output/vat-data/recip-100/,  $(vat_files_late))
vat_1000_late = $(addprefix output/vat-data/recip-1000/, $(vat_files_late))


##=##=##=##=##=##=##=## Recipes

##=## Draw pictures for the VAT analysis

# TODO: this is awfully verbose
vat_pics_1: $(vat_pics_1)

vat_pics_households_1: $(vat_pics_households_1)
$(vat_pics_households_1): $(vat_1)     \
  python/draw/shell-load.py            \
  python/vat/report/main,households.py \
  python/vat/report/load.py            \
  python/vat/report/pics,households.py
	$(python_from_here) python/vat/report/main,households.py 1

vat_pics_income-households_1: $(vat_pics_income-households_1)
$(vat_pics_income-households_1): $(vat_1)     \
  python/draw/shell-load.py                   \
  python/vat/report/main,income-households.py \
  python/vat/report/load.py                   \
  python/vat/report/pics,income-households.py
	$(python_from_here) python/vat/report/main,income-households.py 1

vat_pics_people_1: $(vat_pics_people_1)
$(vat_pics_people_1): $(vat_1)         \
  python/draw/shell-load.py            \
  python/vat/report/main,people.py     \
  python/vat/report/load.py            \
  python/vat/report/pics,people.py
	$(python_from_here) python/vat/report/main,people.py 1

vat_pics_purchases_1: $(vat_pics_purchases_1)
$(vat_pics_purchases_1): $(vat_1)      \
  python/draw/shell-load.py            \
  python/vat/report/main,purchases.py  \
  python/vat/report/load.py            \
  python/vat/report/pics,purchases.py
	$(python_from_here) python/vat/report/main,purchases.py 1

vat_pics_10: $(vat_pics_10)

vat_pics_households_10: $(vat_pics_households_10)
$(vat_pics_households_10): $(vat_10)        \
  python/draw/shell-load.py                 \
  python/vat/report/main,households.py      \
  python/vat/report/load.py                 \
  python/vat/report/pics,households.py
	$(python_from_here) python/vat/report/main,households.py 10

vat_pics_income-households_10: $(vat_pics_income-households_10)
$(vat_pics_income-households_10): $(vat_10)       \
  python/draw/shell-load.py                       \
  python/vat/report/main,income-households.py     \
  python/vat/report/load.py                       \
  python/vat/report/pics,income-households.py
	$(python_from_here) python/vat/report/main,income-households.py 10

vat_pics_people_10: $(vat_pics_people_10)
$(vat_pics_people_10): $(vat_10)       \
  python/draw/shell-load.py            \
  python/vat/report/main,people.py     \
  python/vat/report/load.py            \
  python/vat/report/pics,people.py
	$(python_from_here) python/vat/report/main,people.py 10

vat_pics_purchases_10: $(vat_pics_purchases_10)
$(vat_pics_purchases_10): $(vat_10)      \
  python/draw/shell-load.py              \
  python/vat/report/main,purchases.py    \
  python/vat/report/load.py              \
  python/vat/report/pics,purchases.py
	$(python_from_here) python/vat/report/main,purchases.py 10


##=## Build the data for the VAT analysis

vat_subsamples: $(vat_1) $(vat_10) $(vat_100) $(vat_1000)
vat_1:    $(vat_1)
vat_10:   $(vat_10)
vat_100:  $(vat_100)
vat_1000: $(vat_1000)

$(vat_1_early): $(subsamples) python/vat/build_early.py
	$(python_from_here) python/vat/build_early.py 1
$(vat_10_early): $(subsamples) python/vat/build_early.py
	$(python_from_here) python/vat/build_early.py 10
$(vat_100_early): $(subsamples) python/vat/build_early.py
	$(python_from_here) python/vat/build_early.py 100
$(vat_1000_early): $(subsamples) python/vat/build_early.py
	$(python_from_here) python/vat/build_early.py 1000

$(vat_1_late): $(subsamples) python/vat/build_late.py
	$(python_from_here) python/vat/build_late.py 1
$(vat_10_late): $(subsamples) python/vat/build_late.py
	$(python_from_here) python/vat/build_late.py 10
$(vat_100_late): $(subsamples) python/vat/build_late.py
	$(python_from_here) python/vat/build_late.py 100
$(vat_1000_late): $(subsamples) python/vat/build_late.py
	$(python_from_here) python/vat/build_late.py 1000


##=##=##=## Build the ENPH, the ENIG, and subsamples of them

raw: $(enig_orig) $(enph_orig) $(subsamples)

subsamples: $(subsamples)

# TODO ? rather than build these monolithically, make the subsample size a parameter of subsample.py
  # would be faster if, e.g., you wanted to build only the 1/1000 subsample and not the others
$(subsamples) : $(enig_orig) $(enph_orig)
  # TODO ? add python/subsample.py to dependencies
	$(python_from_here) python/subsample.py
