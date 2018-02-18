def folder(year):
  if year == 2007: "data/enig-2007"
  elif year == 2017: "data/enig-2017"
  else: error (year + " is not one of the survey years.")

files = {2017:
         [ "coicop"
           , "factores_ciclo19"
           , "hogares_tot_completos"
           , "st2_sea_enc_gcar_csv"
           , "st2_sea_enc_gcau_csv"
           , "st2_sea_enc_gcfhr_ce_csv"
           , "st2_sea_enc_gcfhr_csv"
           , "st2_sea_enc_gcfhu_diarios_csv"
           , "st2_sea_enc_gcfhup_diarios_csv"
           , "st2_sea_enc_gdr_csv"
           , "st2_sea_enc_gdrj1_csv"
           , "st2_sea_enc_gdsr_mer_csv"
           , "st2_sea_enc_gdsu_mer_csv"
           , "st2_sea_enc_gmf_csv"
           , "st2_sea_enc_gmf_transpuesta"
           , "st2_sea_enc_gsdp_dia_csv"
           , "st2_sea_enc_gsdp_diarios_csv"
           , "st2_sea_enc_gsdu_dia_csv"
           , "st2_sea_enc_gsdu_diarios_csv" # the biggest, 1.5GB; if this goes through, everything does
           , "st2_sea_enc_hogc3_csv"
           , "st2_sea_enc_hog_csv"
           , "st2_sea_enc_per_csv"
         ],

         2007: [ "Ig_gsdp_dias_sem"
                 , "Ig_gsdp_gas_dia"
                 , "Ig_gsdp_perceptores"
                 , "Ig_gsdu_caract_alim"
                 , "Ig_gsdu_dias_sem"
                 , "Ig_gsdu_gas_dia"
                 , "Ig_gsdu_gasto_alimentos_cap_c"
                 , "Ig_gsdu_mercado"
                 , "Ig_gs_hogar"
                 , "Ig_gsmf_compra"
                 , "Ig_gsmf_forma_adqui"
                 , "Ig_gsmf_serv_pub"
                 , "Ig_gssr_caract_alim"
                 , "Ig_gssr_gas_sem"
                 , "Ig_gssr_gasto_alimentos_cap_c"
                 , "Ig_gssr_mercado"
                 , "Ig_gs_vivienda"
                 , "Ig_ml_desocupado"
                 , "Ig_ml_hogar"
                 , "Ig_ml_inactivo"
                 , "Ig_ml_ocupado"
                 , "Ig_ml_pblcion_edad_trbjar"
                 , "Ig_ml_persona"
                 , "Ig_ml_vivienda"
         ] }
