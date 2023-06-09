from django.db import models
class CabepedidoBack(models.Model):
    mov_compro = models.CharField(db_column='MOV_COMPRO', max_length=11)  # Field name made lowercase.
    mov_fecha = models.DateTimeField(db_column='MOV_FECHA')  # Field name made lowercase.
    mov_glosa = models.CharField(db_column='MOV_GLOSA', max_length=100)  # Field name made lowercase.
    pla_cuenta = models.CharField(db_column='PLA_CUENTA', max_length=25)  # Field name made lowercase.
    mov_codaux = models.CharField(db_column='MOV_CODAUX', max_length=13)  # Field name made lowercase.
    doc_codigo = models.CharField(db_column='DOC_CODIGO', max_length=2)  # Field name made lowercase.
    doc_serie = models.CharField(db_column='DOC_SERIE', max_length=5)  # Field name made lowercase.
    mov_docum = models.CharField(db_column='MOV_DOCUM', max_length=25)  # Field name made lowercase.
    mov_moneda = models.CharField(db_column='MOV_MONEDA', max_length=3)  # Field name made lowercase.
    mov_d = models.DecimalField(db_column='MOV_D', max_digits=16, decimal_places=2)  # Field name made lowercase.
    mov_h = models.DecimalField(db_column='MOV_H', max_digits=16, decimal_places=2)  # Field name made lowercase.
    mov_d_d = models.DecimalField(db_column='MOV_D_D', max_digits=16, decimal_places=2)  # Field name made lowercase.
    mov_h_d = models.DecimalField(db_column='MOV_H_D', max_digits=16, decimal_places=2)  # Field name made lowercase.
    mov_t_c = models.DecimalField(db_column='MOV_T_C', max_digits=12, decimal_places=5)  # Field name made lowercase.
    mov_glosa1 = models.CharField(db_column='MOV_GLOSA1', max_length=100)  # Field name made lowercase.
    mov_linea = models.DecimalField(db_column='MOV_LINEA', max_digits=6, decimal_places=0)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=8)  # Field name made lowercase.
    fechausu = models.DateTimeField(db_column='FECHAUSU')  # Field name made lowercase.
    mov_concil = models.CharField(db_column='MOV_CONCIL', max_length=1)  # Field name made lowercase.
    mov_fechac = models.DateTimeField()
    mov_fvenc = models.DateTimeField()
    mov_docum2 = models.CharField(max_length=20)
    caj_codigo = models.CharField(max_length=2)
    #identi = models.AutoField(db_column='IDENTI')  # Field name made lowercase.
    rou_anula = models.DecimalField(db_column='ROU_ANULA', max_digits=1, decimal_places=0)  # Field name made lowercase.
    rou_subtot = models.DecimalField(db_column='ROU_SUBTOT', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rou_inafec = models.DecimalField(db_column='ROU_INAFEC', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rou_bruto = models.DecimalField(db_column='ROU_BRUTO', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rou_pigv = models.DecimalField(db_column='ROU_PIGV', max_digits=6, decimal_places=2)  # Field name made lowercase.
    rou_igv = models.DecimalField(db_column='ROU_IGV', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rou_tventa = models.DecimalField(db_column='ROU_TVENTA', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rou_export = models.DecimalField(max_digits=1, decimal_places=0)
    mom_d_int = models.CharField(max_length=15)
    gui_tipotr = models.DecimalField(max_digits=1, decimal_places=0)
    gui_certif = models.CharField(max_length=50)
    gui_licenc = models.CharField(max_length=50)
    gui_chofer = models.CharField(db_column='GUI_CHOFER', max_length=50)  # Field name made lowercase.
    gui_placa = models.CharField(max_length=10)
    gui_marca = models.CharField(max_length=20)
    tra_codigo = models.CharField(max_length=4)
    gui_motivo = models.DecimalField(max_digits=2, decimal_places=0)
    fac_serie = models.CharField(max_length=5)
    fac_docum = models.CharField(max_length=10)
    mov_pedido = models.CharField(max_length=25)
    doc_cod2 = models.CharField(max_length=2)
    ubi_codigo = models.CharField(max_length=2)
    gui_exp001 = models.TextField()  # This field type is a guess.
    gui_exp002 = models.TextField()  # This field type is a guess.
    pag_codigo = models.CharField(max_length=3)
    fac_interc = models.DecimalField(max_digits=2, decimal_places=0)
    fac_impre = models.DecimalField(max_digits=2, decimal_places=0)
    gui_exactu = models.DecimalField(max_digits=2, decimal_places=0)
    modifica = models.DecimalField(max_digits=1, decimal_places=0)
    elimini = models.DecimalField(max_digits=1, decimal_places=0)
    inc_codigo = models.CharField(max_length=4)
    mom_d_int2 = models.CharField(max_length=15)
    gui_otros = models.CharField(max_length=50)
    gui_direc = models.CharField(max_length=200)
    doc_codori = models.CharField(max_length=2)
    fac_serori = models.CharField(max_length=5)
    fac_docori = models.CharField(max_length=10)
    fac_fecori = models.DateTimeField()
    gui_exp003 = models.TextField()  # This field type is a guess.
    gui_exp004 = models.CharField(max_length=150)
    gui_exp005 = models.CharField(max_length=150)
    gui_tienda = models.CharField(max_length=30)
    anu_codigo = models.CharField(max_length=2)
    anu_observ = models.TextField()  # This field type is a guess.
    anu_fecha = models.DateTimeField()
    anu_usu = models.CharField(max_length=8)
    gui_perufa = models.DecimalField(max_digits=1, decimal_places=0)
    lis_codigo = models.CharField(max_length=2)
    lis_dscto = models.DecimalField(max_digits=9, decimal_places=2)
    ven_codigo = models.CharField(max_length=3)
    ped_status = models.DecimalField(max_digits=1, decimal_places=0)
    ped_fecapr = models.DateTimeField(blank=True, null=True)
    ped_rechaz = models.TextField()  # This field type is a guess.
    ped_usuapr = models.CharField(max_length=8, blank=True, null=True)
    gui_tiedir = models.CharField(max_length=120)
    gui_ordenc = models.CharField(max_length=25)
    rou_submon = models.DecimalField(max_digits=18, decimal_places=2)
    rou_dscto = models.DecimalField(max_digits=18, decimal_places=2)
    ped_statu2 = models.DecimalField(max_digits=1, decimal_places=0)
    ped_fecap2 = models.DateTimeField()
    ped_recha2 = models.TextField()  # This field type is a guess.
    ped_usuap2 = models.CharField(max_length=8)
    ope_codigo = models.CharField(max_length=4)
    ped_tiedir = models.CharField(max_length=120)
    ped_dscto = models.DecimalField(max_digits=9, decimal_places=2)
    ped_fecdes = models.DateTimeField()
    ped_marca = models.DecimalField(max_digits=1, decimal_places=0)
    ped_rutas = models.CharField(max_length=3)
    ped_letra = models.CharField(max_length=8)
    ped_letgir = models.DateTimeField()
    ped_letusu = models.CharField(max_length=8)
    ped_flag = models.DecimalField(max_digits=1, decimal_places=0)
    ped_numgui = models.CharField(max_length=11)
    ped_docgui = models.CharField(max_length=2)
    ubi_codig2 = models.CharField(max_length=2)
    ped_cierre = models.DecimalField(max_digits=1, decimal_places=0)
    tra_codig2 = models.CharField(max_length=4)
    aux_nuevo = models.CharField(max_length=150)
    aux_contac = models.CharField(max_length=150)
    gui_ruc = models.CharField(max_length=11)
    gui_inclu = models.DecimalField(max_digits=1, decimal_places=0)
    gui_aprot1 = models.DecimalField(max_digits=1, decimal_places=0)
    gui_aprot2 = models.DecimalField(max_digits=1, decimal_places=0)
    gui_aprot3 = models.DecimalField(max_digits=1, decimal_places=0)
    gui_aprov1 = models.DecimalField(max_digits=1, decimal_places=0)
    gui_aprov2 = models.DecimalField(max_digits=1, decimal_places=0)
    gui_aproc1 = models.DecimalField(max_digits=1, decimal_places=0)
    ped_exoner = models.DecimalField(max_digits=1, decimal_places=0)
    alm_codigo = models.CharField(max_length=2)
    agr_codigo = models.CharField(max_length=3)
    mov_cotiza = models.CharField(max_length=25)
    ped_tipven = models.DecimalField(max_digits=1, decimal_places=0)
    gui_pormay = models.DecimalField(max_digits=1, decimal_places=0)
    gui_titgra = models.DecimalField(max_digits=1, decimal_places=0)
    rou_pper = models.DecimalField(max_digits=6, decimal_places=2)
    rou_percep = models.DecimalField(max_digits=18, decimal_places=2)
    rou_tveper = models.DecimalField(max_digits=18, decimal_places=2)
    gui_percep = models.DecimalField(max_digits=1, decimal_places=0)
    cco_codigo = models.CharField(max_length=15)
    est_codigo = models.CharField(max_length=20)
    est_numero = models.CharField(max_length=11)
    est_nombre = models.CharField(max_length=100)
    tob_codigo = models.CharField(max_length=3)
    gui_exp006 = models.TextField()  # This field type is a guess.
    ped_recep1 = models.CharField(max_length=120)
    ped_recep2 = models.CharField(max_length=120)
    gui_albara = models.CharField(max_length=180)
    rou_icbper = models.DecimalField(max_digits=8, decimal_places=2)
    gui_oferta = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'cabepedido_back'


class Movipedido(models.Model):
    alm_codigo = models.CharField(db_column='ALM_CODIGO', max_length=2)  # Field name made lowercase.
    mom_mes = models.CharField(db_column='MOM_MES', max_length=4)  # Field name made lowercase.
    mov_compro = models.CharField(max_length=11)
    doc_codigo = models.CharField(max_length=2)
    mom_fecha = models.DateTimeField(db_column='MOM_FECHA')  # Field name made lowercase.
    art_codigo = models.CharField(db_column='ART_CODIGO', max_length=20)  # Field name made lowercase.
    art_codadi = models.CharField(max_length=30)
    mom_tipmov = models.CharField(db_column='MOM_TIPMOV', max_length=1)  # Field name made lowercase.
    ope_codigo = models.CharField(db_column='OPE_CODIGO', max_length=4)  # Field name made lowercase.
    ubi_cod = models.CharField(db_column='UBI_COD', max_length=4)  # Field name made lowercase.
    ubi_cod1 = models.CharField(db_column='UBI_COD1', max_length=4)  # Field name made lowercase.
    mom_bruto = models.DecimalField(db_column='MOM_BRUTO', max_digits=16, decimal_places=3)  # Field name made lowercase.
    mom_b_p_r = models.DecimalField(db_column='MOM_B_P_R', max_digits=16, decimal_places=0)  # Field name made lowercase.
    mom_conos = models.DecimalField(db_column='MOM_CONOS', max_digits=16, decimal_places=0)  # Field name made lowercase.
    mom_tara = models.DecimalField(db_column='MOM_TARA', max_digits=16, decimal_places=3)  # Field name made lowercase.
    mom_cant = models.DecimalField(db_column='MOM_CANT', max_digits=16, decimal_places=3)  # Field name made lowercase.
    mom_valor = models.DecimalField(max_digits=16, decimal_places=3)
    mom_moneda = models.CharField(db_column='MOM_MONEDA', max_length=1)  # Field name made lowercase.
    mom_t_c = models.DecimalField(db_column='MOM_T_C', max_digits=8, decimal_places=4)  # Field name made lowercase.
    mom_valors = models.DecimalField(max_digits=16, decimal_places=3)
    mom_punit = models.DecimalField(db_column='MOM_PUNIT', max_digits=18, decimal_places=7)  # Field name made lowercase.
    mom_lote = models.CharField(db_column='MOM_LOTE', max_length=10)  # Field name made lowercase.
    ord_numero = models.CharField(db_column='ORD_NUMERO', max_length=15)  # Field name made lowercase.
    doc_cod1 = models.CharField(max_length=5)
    mom_d_int = models.CharField(db_column='MOM_D_INT', max_length=15)  # Field name made lowercase.
    mom_glosa = models.CharField(db_column='MOM_GLOSA', max_length=100)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=8)  # Field name made lowercase.
    fechausu = models.DateTimeField(db_column='FECHAUSU')  # Field name made lowercase.
    mom_numero = models.CharField(max_length=30)
    #identi = models.AutoField(db_column='IDENTI')  # Field name made lowercase.
    modifica = models.DecimalField(db_column='MODIFICA', max_digits=1, decimal_places=0)  # Field name made lowercase.
    elimini = models.DecimalField(db_column='ELIMINI', max_digits=1, decimal_places=0)  # Field name made lowercase.
    mom_inicia = models.CharField(max_length=3)
    mom_chkfor = models.DecimalField(max_digits=1, decimal_places=0)
    cam_codigo = models.CharField(db_column='CAM_CODIGO', max_length=4)  # Field name made lowercase.
    mom_d_ints = models.CharField(db_column='MOM_D_INTS', max_length=1)  # Field name made lowercase.
    mom_dscto1 = models.DecimalField(max_digits=18, decimal_places=7)
    mom_dscto2 = models.DecimalField(max_digits=9, decimal_places=2)
    ped_lista2 = models.CharField(max_length=2)
    art_afecto = models.CharField(max_length=1)
    ped_observ = models.TextField()  # This field type is a guess.
    ped_nomtem = models.CharField(max_length=120)
    col_codigo = models.CharField(max_length=3)
    tal_codigo = models.CharField(max_length=3)
    ped_separa = models.DecimalField(max_digits=9, decimal_places=3)
    ped_colnom = models.CharField(max_length=120)
    gui_inclu = models.DecimalField(max_digits=1, decimal_places=0)
    mom_pcosdo = models.DecimalField(max_digits=18, decimal_places=4)
    mom_pcosso = models.DecimalField(max_digits=18, decimal_places=4)
    mom_bonifi = models.CharField(max_length=1)
    mom_punit2 = models.DecimalField(max_digits=16, decimal_places=2)
    mom_conpre = models.CharField(max_length=1)
    mom_peso = models.DecimalField(max_digits=16, decimal_places=2)
    gui_factor = models.DecimalField(max_digits=12, decimal_places=2)
    ped_kilome = models.DecimalField(max_digits=16, decimal_places=2)
    ped_horome = models.DecimalField(max_digits=16, decimal_places=2)
    aut_codigo = models.CharField(max_length=7)
    cco_codigo = models.CharField(max_length=15)
    ped_oferta = models.DecimalField(max_digits=1, decimal_places=0)
    med_codigo = models.CharField(max_length=2)
    mom_factor = models.DecimalField(max_digits=16, decimal_places=4)
    mom_dscto3 = models.DecimalField(max_digits=9, decimal_places=2)
    gui_percep = models.DecimalField(max_digits=1, decimal_places=0)
    est_codigo = models.CharField(max_length=20)
    ped_priori = models.CharField(max_length=20)
    gui_connum = models.CharField(max_length=10)
    art_codig2 = models.CharField(max_length=20)
    mom_eans = models.CharField(max_length=20)
    mom_pdscto = models.DecimalField(max_digits=9, decimal_places=2)
    gui_icbper = models.DecimalField(max_digits=1, decimal_places=0)
    mom_linea = models.DecimalField(db_column='MOM_LINEA', max_digits=16, decimal_places=0)  # Field name made lowercase.
    mom_conpro = models.DecimalField(max_digits=1, decimal_places=0)
    mom_conreg = models.DecimalField(max_digits=1, decimal_places=0)
    mom_confle = models.DecimalField(max_digits=1, decimal_places=0)
    mom_cofleg = models.DecimalField(max_digits=1, decimal_places=0)
    mom_concom = models.DecimalField(max_digits=1, decimal_places=0)
    mom_concoa = models.DecimalField(max_digits=1, decimal_places=0)
    mom_cofle2 = models.DecimalField(max_digits=1, decimal_places=0)
    mom_conpr2 = models.DecimalField(max_digits=1, decimal_places=0)
    lis_mindes = models.DecimalField(max_digits=8, decimal_places=2)
    lis_maxdes = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'movipedido'


class TArticulo(models.Model):
    art_codigo = models.CharField(db_column='ART_CODIGO', primary_key=True, max_length=20)  # Field name made lowercase.
    art_nombre = models.CharField(db_column='ART_NOMBRE', max_length=120)  # Field name made lowercase.
    pa1_codigo = models.CharField(db_column='PA1_CODIGO', max_length=9)  # Field name made lowercase.
    pa2_codigo = models.CharField(db_column='PA2_CODIGO', max_length=9)  # Field name made lowercase.
    pa3_codigo = models.CharField(db_column='PA3_CODIGO', max_length=9)  # Field name made lowercase.
    pa4_codigo = models.CharField(db_column='PA4_CODIGO', max_length=9)  # Field name made lowercase.
    art_corre = models.CharField(max_length=20)
    lin_codigo = models.CharField(db_column='LIN_CODIGO', max_length=4)  # Field name made lowercase.
    fam_codigo = models.CharField(db_column='FAM_CODIGO', max_length=5)  # Field name made lowercase.
    sub_codigo = models.CharField(db_column='SUB_CODIGO', max_length=5)  # Field name made lowercase.
    ume_codigo = models.CharField(db_column='UME_CODIGO', max_length=3)  # Field name made lowercase.
    ume_abrev = models.CharField(max_length=5)
    alm_codigo = models.CharField(db_column='ALM_CODIGO', max_length=50)  # Field name made lowercase.
    art_stock = models.DecimalField(db_column='ART_STOCK', max_digits=18, decimal_places=0)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=8)  # Field name made lowercase.
    fechausu = models.DateTimeField(db_column='FECHAUSU')  # Field name made lowercase.
    #identi = models.AutoField(db_column='IDENTI')  # Field name made lowercase.
    modifica = models.DecimalField(db_column='MODIFICA', max_digits=1, decimal_places=0)  # Field name made lowercase.
    elimini = models.DecimalField(db_column='ELIMINI', max_digits=1, decimal_places=0)  # Field name made lowercase.
    art_conver = models.DecimalField(max_digits=7, decimal_places=3)
    art_ubica = models.CharField(max_length=20)
    art_parte = models.CharField(max_length=30)
    art_catalo = models.CharField(max_length=30)
    art_provee = models.CharField(max_length=30)
    pla_almain = models.CharField(max_length=8)
    art_nompro = models.CharField(max_length=120)
    art_activo = models.DecimalField(max_digits=1, decimal_places=0)
    art_nomexp = models.CharField(max_length=120)
    art_ctaexa = models.CharField(max_length=25)
    art_cenexa = models.CharField(max_length=8)
    art_refexa = models.CharField(max_length=40)
    art_tipo = models.CharField(max_length=40)
    ume_precod = models.CharField(max_length=3)
    ume_preabr = models.CharField(max_length=5)
    art_afecto = models.CharField(max_length=1)
    pla_almai2 = models.CharField(max_length=8)
    art_hicoss = models.DecimalField(max_digits=18, decimal_places=4)
    art_hicosd = models.DecimalField(max_digits=18, decimal_places=4)
    art_mansto = models.DecimalField(max_digits=1, decimal_places=0)
    art_hueso = models.DecimalField(max_digits=1, decimal_places=0)
    art_noauto = models.DecimalField(max_digits=1, decimal_places=0)
    art_feccre = models.DateTimeField()
    tip_codigo = models.CharField(max_length=15)
    art_partes = models.DecimalField(max_digits=1, decimal_places=0)
    tem_codigo = models.CharField(max_length=20)
    gen_codigo = models.CharField(max_length=11)
    pla_almre1 = models.CharField(max_length=8)
    pla_almre2 = models.CharField(max_length=8)
    art_peso = models.DecimalField(max_digits=18, decimal_places=6)
    art_serie = models.CharField(max_length=20)
    agr_codigo = models.CharField(max_length=3)
    pa5_codigo = models.CharField(max_length=5)
    pa6_codigo = models.CharField(max_length=5)
    art_factor = models.DecimalField(max_digits=18, decimal_places=4)
    pla_almace = models.CharField(max_length=10)
    pla_consum = models.CharField(max_length=10)
    pla_ajuste = models.CharField(max_length=10)
    art_combo = models.DecimalField(max_digits=1, decimal_places=0)
    art_anter = models.CharField(max_length=20)
    art_expor = models.CharField(max_length=120)
    det_codigo = models.CharField(max_length=3)
    art_eanmul = models.DecimalField(max_digits=1, decimal_places=0)
    art_gramo = models.DecimalField(max_digits=18, decimal_places=4)
    art_percep = models.DecimalField(max_digits=1, decimal_places=0)
    art_uempaq = models.CharField(max_length=20)
    art_observ = models.TextField()  # This field type is a guess.
    pla_almai3 = models.CharField(max_length=8)
    pai_codigo = models.CharField(max_length=8)
    art_unipal = models.DecimalField(max_digits=18, decimal_places=2)
    pla_compra = models.CharField(max_length=8)
    art_punven = models.DecimalField(max_digits=1, decimal_places=0)
    art_posven = models.DecimalField(max_digits=10, decimal_places=0)
    art_punve2 = models.DecimalField(max_digits=1, decimal_places=0)
    art_posve2 = models.DecimalField(max_digits=10, decimal_places=0)
    art_punve3 = models.DecimalField(max_digits=1, decimal_places=0)
    art_posve3 = models.DecimalField(max_digits=10, decimal_places=0)
    li_codigo = models.CharField(max_length=4)
    sl_codigo = models.CharField(max_length=4)
    art_comvti = models.DecimalField(max_digits=8, decimal_places=2)
    art_comvex = models.DecimalField(max_digits=8, decimal_places=2)
    art_volume = models.DecimalField(max_digits=12, decimal_places=4)
    cco_codigo = models.CharField(max_length=15)
    art_marca = models.CharField(max_length=100)
    art_regsan = models.CharField(max_length=200)
    art_antici = models.DecimalField(max_digits=1, decimal_places=0)
    art_rs_ini = models.DateTimeField()
    art_rs_fin = models.DateTimeField()
    art_rs_nro = models.CharField(max_length=30)
    art_as_ini = models.DateTimeField()
    art_as_fin = models.DateTimeField()
    art_as_nro = models.CharField(max_length=12)
    art_ha_ini = models.DateTimeField()
    art_ha_fin = models.DateTimeField()
    art_ha_nro = models.CharField(max_length=12)
    art_ft_ini = models.DateTimeField()
    art_ft_fin = models.DateTimeField()
    art_ft_nro = models.CharField(max_length=12)
    art_c_p_d = models.DecimalField(max_digits=16, decimal_places=2)
    art_t_r_p = models.DecimalField(max_digits=3, decimal_places=0)
    cod_sunat = models.CharField(max_length=20)
    art_noapds = models.DecimalField(max_digits=1, decimal_places=0)
    art_obsequ = models.DecimalField(max_digits=1, decimal_places=0)
    art_icbper = models.DecimalField(max_digits=1, decimal_places=0)
    art_ivap = models.DecimalField(max_digits=1, decimal_places=0)
    art_preesp = models.DecimalField(max_digits=1, decimal_places=0)
    art_diaven = models.DecimalField(max_digits=16, decimal_places=3)
    art_repeca = models.DecimalField(max_digits=1, decimal_places=0)
    col_codigo = models.CharField(max_length=6)
    art_facyde = models.DateTimeField()
    pre_scta = models.CharField(max_length=10)
    art_flegra = models.DecimalField(max_digits=1, decimal_places=0)
    art_codpro = models.CharField(max_length=20)
    art_prefij = models.CharField(max_length=10)
    art_entero = models.DecimalField(max_digits=1, decimal_places=0)
    ven_codigo = models.CharField(max_length=3)
    art_peso2 = models.DecimalField(max_digits=16, decimal_places=2)
    art_ean14 = models.CharField(max_length=14)
    art_rema = models.DecimalField(max_digits=1, decimal_places=0)
    art_pesocj = models.DecimalField(max_digits=8, decimal_places=2)
    art_pesobl = models.DecimalField(max_digits=8, decimal_places=2)
    art_link = models.CharField(max_length=200)
    art_noprom = models.DecimalField(max_digits=1, decimal_places=0)
    art_norega = models.DecimalField(max_digits=1, decimal_places=0)
    cla_codigo = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 't_articulo'


class TAuxiliar(models.Model):
    maa_codigo = models.CharField(db_column='MAA_CODIGO', max_length=2)  # Field name made lowercase.
    aux_codigo = models.CharField(db_column='AUX_CODIGO', max_length=11)  # Field name made lowercase.
    aux_clave = models.CharField(db_column='AUX_CLAVE', unique=True, max_length=13)  # Field name made lowercase.
    aux_nombre = models.CharField(db_column='AUX_NOMBRE', max_length=130)  # Field name made lowercase.
    aux_razon = models.CharField(db_column='AUX_RAZON', max_length=130)  # Field name made lowercase.
    ven_codigo = models.CharField(db_column='VEN_CODIGO', max_length=3)  # Field name made lowercase.
    pag_codigo = models.CharField(db_column='PAG_CODIGO', max_length=3)  # Field name made lowercase.
    ubi_codigo = models.CharField(db_column='UBI_CODIGO', max_length=13)  # Field name made lowercase.
    pla_ctacom = models.CharField(db_column='PLA_CTACOM', max_length=8)  # Field name made lowercase.
    pla_ctavta = models.CharField(db_column='PLA_CTAVTA', max_length=8)  # Field name made lowercase.
    maa_nombre = models.CharField(db_column='MAA_NOMBRE', max_length=30)  # Field name made lowercase.
    aux_direcc = models.CharField(db_column='AUX_DIRECC', max_length=150)  # Field name made lowercase.
    aux_direc2 = models.CharField(max_length=70)
    pai_codigo = models.CharField(db_column='PAI_CODIGO', max_length=6)  # Field name made lowercase.
    dep_codigo = models.CharField(db_column='DEP_CODIGO', max_length=30)  # Field name made lowercase.
    pro_codigo = models.CharField(db_column='PRO_CODIGO', max_length=40)  # Field name made lowercase.
    dis_codigo = models.CharField(db_column='DIS_CODIGO', max_length=40)  # Field name made lowercase.
    aux_tipope = models.DecimalField(db_column='AUX_TIPOPE', max_digits=3, decimal_places=0)  # Field name made lowercase.
    aux_docum = models.CharField(db_column='AUX_DOCUM', max_length=11)  # Field name made lowercase.
    aux_docadi = models.CharField(db_column='AUX_DOCADI', max_length=30)  # Field name made lowercase.
    aux_telef = models.CharField(db_column='AUX_TELEF', max_length=100)  # Field name made lowercase.
    aux_fax = models.CharField(db_column='AUX_FAX', max_length=100)  # Field name made lowercase.
    aux_creado = models.DateTimeField(db_column='AUX_CREADO')  # Field name made lowercase.
    aux_email = models.CharField(db_column='AUX_EMAIL', max_length=100)  # Field name made lowercase.
    aux_cont1 = models.CharField(db_column='AUX_CONT1', max_length=40)  # Field name made lowercase.
    aux_cargo1 = models.CharField(db_column='AUX_CARGO1', max_length=40)  # Field name made lowercase.
    aux_telef1 = models.CharField(db_column='AUX_TELEF1', max_length=40)  # Field name made lowercase.
    aux_email1 = models.CharField(db_column='AUX_EMAIL1', max_length=80)  # Field name made lowercase.
    aux_cont2 = models.CharField(db_column='AUX_CONT2', max_length=40)  # Field name made lowercase.
    aux_cargo2 = models.CharField(db_column='AUX_CARGO2', max_length=40)  # Field name made lowercase.
    aux_telef2 = models.CharField(db_column='AUX_TELEF2', max_length=40)  # Field name made lowercase.
    aux_email2 = models.CharField(db_column='AUX_EMAIL2', max_length=80)  # Field name made lowercase.
    aux_user_i = models.CharField(db_column='AUX_USER_I', max_length=8)  # Field name made lowercase.
    aux_pass_i = models.CharField(db_column='AUX_PASS_I', max_length=8)  # Field name made lowercase.
    aux_userci = models.CharField(max_length=8)
    aux_passci = models.CharField(max_length=8)
    aux_credit = models.DecimalField(db_column='AUX_CREDIT', max_digits=4, decimal_places=0)  # Field name made lowercase.
    aux_limite = models.DecimalField(db_column='AUX_LIMITE', max_digits=18, decimal_places=2)  # Field name made lowercase.
    aux_activo = models.DecimalField(db_column='AUX_ACTIVO', max_digits=1, decimal_places=0)  # Field name made lowercase.
    aux_edi = models.CharField(db_column='AUX_EDI', max_length=20)  # Field name made lowercase.
    aux_com20i = models.DecimalField(db_column='AUX_COM20I', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_com40i = models.DecimalField(db_column='AUX_COM40I', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_combli = models.DecimalField(db_column='AUX_COMBLI', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_comcni = models.DecimalField(db_column='AUX_COMCNI', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_com20e = models.DecimalField(db_column='AUX_COM20E', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_com40e = models.DecimalField(db_column='AUX_COM40E', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_comble = models.DecimalField(db_column='AUX_COMBLE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_comcne = models.DecimalField(db_column='AUX_COMCNE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_comta1 = models.DecimalField(db_column='AUX_COMTA1', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_comta2 = models.DecimalField(db_column='AUX_COMTA2', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_comta3 = models.DecimalField(db_column='AUX_COMTA3', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_comta4 = models.DecimalField(db_column='AUX_COMTA4', max_digits=10, decimal_places=2)  # Field name made lowercase.
    aux_observ = models.TextField()  # This field type is a guess.
    usuario = models.CharField(db_column='USUARIO', max_length=3)  # Field name made lowercase.
    fechausu = models.CharField(db_column='FECHAUSU', max_length=3)  # Field name made lowercase.
    elimini = models.CharField(db_column='ELIMINI', max_length=3)  # Field name made lowercase.
    modifica = models.CharField(db_column='MODIFICA', max_length=3)  # Field name made lowercase.
    #identi = models.AutoField(db_column='IDENTI')  # Field name made lowercase.
    aux_sobrrf = models.DecimalField(max_digits=3, decimal_places=0)
    aux_sobrot = models.DecimalField(max_digits=3, decimal_places=0)
    aux_diaalm = models.DecimalField(max_digits=3, decimal_places=0)
    aux_comoth = models.CharField(max_length=50)
    aux_almata = models.DecimalField(db_column='AUX_ALMATA', max_digits=18, decimal_places=0)  # Field name made lowercase.
    aux_banco = models.CharField(max_length=50)
    aux_ctabco = models.CharField(max_length=50)
    zon_codigo = models.CharField(max_length=4)
    rut_codigo = models.CharField(max_length=4)
    cat_codigo = models.CharField(max_length=5)
    abc_codigo = models.CharField(max_length=1)
    can_codigo = models.CharField(max_length=3)
    aux_cobert = models.DecimalField(max_digits=5, decimal_places=0)
    aux_linea = models.CharField(max_length=250)
    tcl_codigo = models.CharField(max_length=3)
    aux_dialun = models.DecimalField(max_digits=1, decimal_places=0)
    aux_diamar = models.DecimalField(max_digits=1, decimal_places=0)
    aux_diamie = models.DecimalField(max_digits=1, decimal_places=0)
    aux_diajue = models.DecimalField(max_digits=1, decimal_places=0)
    aux_diavie = models.DecimalField(max_digits=1, decimal_places=0)
    aux_diasab = models.DecimalField(max_digits=1, decimal_places=0)
    aux_diadom = models.DecimalField(max_digits=1, decimal_places=0)
    ter_codigo = models.CharField(max_length=4)
    aux_cuenta = models.CharField(max_length=10)
    aux_cuentd = models.CharField(max_length=10)
    cco_codigo = models.CharField(max_length=15)
    aux_detrac = models.DecimalField(max_digits=6, decimal_places=2)
    det_ctacte = models.CharField(max_length=30)
    aux_tipdoc = models.DecimalField(max_digits=1, decimal_places=0)
    aux_reten = models.DecimalField(max_digits=1, decimal_places=0)
    aux_pagfle = models.DecimalField(max_digits=1, decimal_places=0)
    aux_porret = models.DecimalField(max_digits=5, decimal_places=2)
    aux_desac = models.DecimalField(max_digits=1, decimal_places=0)
    aux_percep = models.DecimalField(max_digits=1, decimal_places=0)
    aux_manean = models.DecimalField(max_digits=1, decimal_places=0)
    aux_buenco = models.DecimalField(max_digits=1, decimal_places=0)
    aux_imone = models.CharField(max_length=1)
    aux_ictabe = models.CharField(max_length=35)
    aux_irazbe = models.CharField(max_length=60)
    aux_idirbe = models.CharField(max_length=60)
    aux_ipaibe = models.CharField(max_length=30)
    aux_ibcobe = models.CharField(max_length=30)
    aux_iciube = models.CharField(max_length=30)
    aux_ipabbe = models.CharField(max_length=30)
    aux_itipbe = models.CharField(max_length=30)
    aux_iswfbe = models.CharField(max_length=30)
    aux_ibcoin = models.CharField(max_length=30)
    aux_iciuin = models.CharField(max_length=30)
    aux_ipabin = models.CharField(max_length=30)
    aux_itipin = models.CharField(max_length=30)
    aux_iswfin = models.CharField(max_length=30)
    aux_iaobin = models.CharField(max_length=30)
    compufecha = models.DateTimeField()
    bk_usuario = models.CharField(max_length=8)
    bk_fecha = models.DateTimeField()
    bk_observ = models.TextField()  # This field type is a guess.
    compu = models.CharField(max_length=30)
    aux_facpes = models.DecimalField(max_digits=1, decimal_places=0)
    aux_girado = models.CharField(max_length=50)
    aux_moneda = models.CharField(max_length=1)
    aux_sucur = models.DecimalField(max_digits=1, decimal_places=0)
    aux_rechon = models.DecimalField(max_digits=1, decimal_places=0)
    aux_recho2 = models.DecimalField(max_digits=1, decimal_places=0)
    aux_condic = models.CharField(max_length=120)
    aux_facdet = models.DecimalField(max_digits=1, decimal_places=0)
    aux_sinpen = models.DecimalField(max_digits=1, decimal_places=0)
    aux_cuegas = models.CharField(max_length=10)
    aux_bcpago = models.DecimalField(max_digits=1, decimal_places=0)
    aux_insur = models.DecimalField(max_digits=1, decimal_places=0)
    t25_codigo = models.CharField(max_length=2)
    reg_codigo = models.CharField(max_length=4)
    ofi_codigo = models.CharField(max_length=4)
    pl_codigo = models.CharField(max_length=4)
    aux_despro = models.DecimalField(max_digits=6, decimal_places=2)
    aux_anter = models.CharField(max_length=15)
    aux_nemail = models.DecimalField(max_digits=1, decimal_places=0)
    lis_codigo = models.CharField(max_length=2)
    aux_infoco = models.DecimalField(max_digits=1, decimal_places=0)
    aux_preesp = models.DecimalField(max_digits=1, decimal_places=0)
    aux_banco2 = models.CharField(max_length=50)
    aux_ctabc2 = models.CharField(max_length=50)
    aux_venlot = models.DecimalField(max_digits=4, decimal_places=0)
    aux_cci = models.CharField(max_length=50)
    aux_cci2 = models.CharField(max_length=50)
    aux_apraut = models.DecimalField(max_digits=1, decimal_places=0)
    aux_feccum = models.DateTimeField()
    aux_dircor = models.CharField(max_length=120)
    aux_pagweb = models.CharField(max_length=120)
    ban_codigo = models.CharField(max_length=4)
    ban_codig2 = models.CharField(max_length=4)
    aux_repleg = models.CharField(max_length=120)
    aux_gnegoc = models.CharField(max_length=120)
    aux_fecing = models.DateTimeField()
    aux_autdet = models.DecimalField(max_digits=1, decimal_places=0)
    aux_enlote = models.DecimalField(max_digits=1, decimal_places=0)
    aux_estado = models.CharField(max_length=120)
    aux_fecoru = models.DateTimeField()
    aux_facdoc = models.CharField(max_length=2)
    aux_facser = models.CharField(max_length=5)
    aux_facnum = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_auxiliar'

class TUsuario(models.Model):
    usu_codigo = models.CharField(db_column='USU_CODIGO', primary_key=True, max_length=3)  # Field name made lowercase.
    usu_nombre = models.CharField(db_column='USU_NOMBRE', max_length=50)  # Field name made lowercase.
    usu_abrev = models.CharField(db_column='USU_ABREV', max_length=8)  # Field name made lowercase.
    usu_login = models.CharField(db_column='USU_LOGIN', max_length=8)  # Field name made lowercase.
    usu_nivel = models.CharField(db_column='USU_NIVEL', max_length=2)  # Field name made lowercase.
    usu_clave = models.CharField(db_column='USU_CLAVE', max_length=8)  # Field name made lowercase.
    usu_grupo = models.CharField(db_column='USU_GRUPO', max_length=3)  # Field name made lowercase.
    usu_email = models.CharField(db_column='USU_EMAIL', max_length=100)  # Field name made lowercase.
    usu_idioma = models.DecimalField(db_column='USU_IDIOMA', max_digits=1, decimal_places=0)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=8)  # Field name made lowercase.
    fechausu = models.DateTimeField(db_column='FECHAUSU')  # Field name made lowercase.
    elimini = models.CharField(db_column='ELIMINI', max_length=1)  # Field name made lowercase.
    modifica = models.CharField(db_column='MODIFICA', max_length=1)  # Field name made lowercase.
    #identi = models.AutoField()
    usu_area = models.CharField(max_length=30)
    usu_cargo = models.CharField(max_length=30)
    usu_inicia = models.CharField(max_length=4)
    usu_admin = models.DecimalField(max_digits=1, decimal_places=0)
    usu_mensa = models.DecimalField(max_digits=1, decimal_places=0)
    logistica = models.CharField(max_length=3)
    usu_autor1 = models.CharField(max_length=8)
    usu_autor2 = models.CharField(max_length=8)
    usu_autor3 = models.CharField(max_length=8)
    usu_autor4 = models.CharField(max_length=15)
    usu_repo = models.DecimalField(max_digits=1, decimal_places=0)
    usu_guia = models.CharField(max_length=5)
    usu_fact = models.CharField(max_length=5)
    usu_bole = models.CharField(max_length=5)
    usu_tick = models.CharField(max_length=5)
    caj_codigo = models.CharField(max_length=3)
    ven_codigo = models.CharField(max_length=3)
    usu_telef = models.CharField(max_length=200)
    usu_nexcel = models.CharField(max_length=200)
    firma = models.BinaryField()
    usu_docgui = models.CharField(max_length=2)
    usu_docfac = models.CharField(max_length=2)
    usu_docbol = models.CharField(max_length=2)
    usu_doctic = models.CharField(max_length=2)
    usu_aprob1 = models.DecimalField(max_digits=1, decimal_places=0)
    usu_aprob2 = models.DecimalField(max_digits=1, decimal_places=0)
    usu_aprob3 = models.DecimalField(max_digits=1, decimal_places=0)
    usu_aprob4 = models.DecimalField(max_digits=1, decimal_places=0)
    usu_doccre = models.CharField(max_length=2)
    usu_cred = models.CharField(max_length=5)
    usu_docdeb = models.CharField(max_length=2)
    usu_debi = models.CharField(max_length=5)
    usu_visser = models.DecimalField(max_digits=1, decimal_places=0)
    usu_docalm = models.CharField(max_length=2)
    usu_alma = models.CharField(max_length=5)
    usu_docost = models.CharField(max_length=2)
    usu_ost = models.CharField(max_length=5)
    ubi_codigo = models.CharField(max_length=2)
    usu_docal2 = models.CharField(max_length=2)
    usu_alma2 = models.CharField(max_length=5)
    usu_doctib = models.CharField(max_length=2)
    usu_tickbo = models.CharField(max_length=5)
    usu_docit = models.CharField(max_length=2)
    usu_it = models.CharField(max_length=5)
    usu_vallin = models.DecimalField(max_digits=1, decimal_places=0)
    usu_alerta = models.DecimalField(max_digits=1, decimal_places=0)
    usu_perped = models.DecimalField(max_digits=1, decimal_places=0)
    ori_codigo = models.CharField(max_length=2)
    usu_oculta = models.DecimalField(max_digits=1, decimal_places=0)
    usu_doctom = models.CharField(max_length=2)
    usu_toma = models.CharField(max_length=5)
    usu_docal3 = models.CharField(max_length=2)
    usu_alma3 = models.CharField(max_length=5)
    usu_docal4 = models.CharField(max_length=2)
    usu_alma4 = models.CharField(max_length=5)
    usu_docpla = models.CharField(max_length=2)
    usu_plani = models.CharField(max_length=5)
    ori_caja = models.CharField(max_length=2)
    usu_perpla = models.DecimalField(max_digits=1, decimal_places=0)
    usu_docimp = models.CharField(max_length=2)
    usu_impor = models.CharField(max_length=5)
    usu_seralm = models.DecimalField(max_digits=1, decimal_places=0)
    usu_serpla = models.DecimalField(max_digits=1, decimal_places=0)
    fecha_valida = models.CharField(max_length=8)
    usu_verotr = models.DecimalField(max_digits=1, decimal_places=0)
    usu_docper = models.CharField(max_length=2)
    usu_percep = models.CharField(max_length=5)
    usu_docpre = models.CharField(max_length=2)
    usu_prevta = models.CharField(max_length=5)
    usu_docfic = models.CharField(max_length=2)
    usu_ficha = models.CharField(max_length=5)
    ori_caja2 = models.CharField(max_length=2)
    usu_bloqro = models.DecimalField(max_digits=1, decimal_places=0)
    usu_2aprob = models.DecimalField(max_digits=1, decimal_places=0)
    usu_observ = models.TextField()  # This field type is a guess.
    usu_doceqp = models.CharField(max_length=2)
    usu_equipo = models.CharField(max_length=5)
    lin_guia = models.DecimalField(max_digits=9, decimal_places=0)
    lin_fact = models.DecimalField(max_digits=9, decimal_places=0)
    lin_bole = models.DecimalField(max_digits=9, decimal_places=0)
    lin_ncre = models.DecimalField(max_digits=9, decimal_places=0)
    lin_ndeb = models.DecimalField(max_digits=9, decimal_places=0)
    usu_pernsa = models.DecimalField(max_digits=1, decimal_places=0)
    prefijo = models.CharField(max_length=3)
    usu_modped = models.DecimalField(max_digits=1, decimal_places=0)
    usu_alecon = models.DecimalField(max_digits=1, decimal_places=0)
    usu_notc = models.DecimalField(max_digits=1, decimal_places=0)
    usu_novalo = models.DecimalField(max_digits=1, decimal_places=0)
    usu_modicc = models.DecimalField(max_digits=1, decimal_places=0)
    usu_almace = models.CharField(max_length=2)
    usu_manpta = models.DecimalField(max_digits=1, decimal_places=0)
    usu_skype = models.CharField(max_length=50)
    usu_visbot = models.DecimalField(max_digits=1, decimal_places=0)
    usu_modpes = models.DecimalField(max_digits=1, decimal_places=0)
    usu_passwo = models.CharField(max_length=30)
    usu_cemail = models.CharField(max_length=150)
    usu_alogi1 = models.DecimalField(max_digits=1, decimal_places=0)
    usu_alogi2 = models.DecimalField(max_digits=1, decimal_places=0)
    usu_alogi3 = models.DecimalField(max_digits=1, decimal_places=0)
    usu_rangde = models.DecimalField(max_digits=16, decimal_places=2)
    usu_rangha = models.DecimalField(max_digits=16, decimal_places=2)
    usu_modpef = models.DecimalField(max_digits=1, decimal_places=0)
    usu_moddes = models.DecimalField(max_digits=1, decimal_places=0)
    ori_cajegr = models.CharField(max_length=2)
    usu_calida = models.DecimalField(max_digits=1, decimal_places=0)
    usu_dococ = models.CharField(max_length=2)
    usu_ordenc = models.CharField(max_length=5)
    usu_ciemes = models.DecimalField(max_digits=1, decimal_places=0)
    usu_docop = models.CharField(max_length=2)
    usu_ordenp = models.CharField(max_length=5)
    usu_docreb = models.CharField(max_length=2)
    usu_credbo = models.CharField(max_length=5)
    lin_ncrebo = models.DecimalField(max_digits=9, decimal_places=0)
    usu_apraut = models.DecimalField(max_digits=1, decimal_places=0)
    usu_dodebb = models.CharField(max_length=2)
    usu_debibo = models.CharField(max_length=5)
    lin_ndebbo = models.DecimalField(max_digits=9, decimal_places=0)
    usu_modulo = models.DecimalField(max_digits=2, decimal_places=0)
    enca_jefe = models.DecimalField(max_digits=1, decimal_places=0)
    usu_nocpag = models.DecimalField(max_digits=1, decimal_places=0)
    usu_nomven = models.DecimalField(max_digits=1, decimal_places=0)
    usu_mpedid = models.DecimalField(max_digits=1, decimal_places=0)
    usu_ocospe = models.DecimalField(max_digits=1, decimal_places=0)
    usu_bconpa = models.DecimalField(max_digits=1, decimal_places=0)
    usu_aprobc = models.DecimalField(max_digits=1, decimal_places=0)
    usu_bbtape = models.DecimalField(max_digits=1, decimal_places=0)
    usu_bcnmst = models.DecimalField(max_digits=1, decimal_places=0)
    usu_apnaut = models.DecimalField(max_digits=1, decimal_places=0)
    usu_hcajle = models.DecimalField(max_digits=1, decimal_places=0)
    usu_tipomi = models.DecimalField(max_digits=1, decimal_places=0)
    usu_nimpap = models.DecimalField(max_digits=1, decimal_places=0)
    usu_modpro = models.CharField(max_length=2)
    usu_hacoar = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        managed = False
        db_table = 't_usuario'
        unique_together = (('usu_codigo', 'usu_nombre'),)

