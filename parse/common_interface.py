
type_id_dic = {0: 'Undefined', 1: 'M_SP_NA_1', 2: 'M_SP_TA_1', 3: 'M_DP_NA_1', 4: 'M_DP_TA_1', 5: 'M_ST_NA_1', \
               6: 'M_ST_TA_1', 7: 'M_BO_NA_1', 8: 'M_BO_TA_1', 9: 'M_ME_NA_1', 10: 'M_ME_TA_1', 11: 'M_ME_NB_1', \
               12: 'M_ME_TB_1', 13: 'M_ME_NC_1', 14: 'M_ME_TC_1', 15: 'M_IT_NA_1', 16: 'M_IT_TA_1', 17: 'M_EP_TA_1', \
               18: 'M_EP_TB_1', 19: 'M_EP_TC_1', 20: 'M_PS_NA_1', 21: 'M_ME_ND_1', 30: 'M_SP_TB_1', 31: 'M_DP_TB_1', \
               32: 'M_ST_TB_1', 33: 'M_BO_TB_1', 34: 'M_ME_TD_1', 35: 'M_ME_TE_1', 36: 'M_ME_TF_1', 37: 'M_IT_TB_1', \
               38: 'M_EP_TD_1', 39: 'M_EP_TE_1', 40: 'M_EP_TF_1', 45: 'C_SC_NA_1', 46: 'C_DC_NA_1', 47: 'C_RC_NA_1', \
               48: 'C_SE_NA_1', 49: 'C_SE_NB_1', 50: 'C_SE_NC_1', 51: 'C_BO_NA_1', 70: 'M_EI_NA_1', 100: 'C_IC_NA_1', \
               101: 'C_CI_NA_1', 102: 'C_RD_NA_1', 103: 'C_CS_NA_1', 104: 'C_TS_NA_1', 105: 'C_RP_NA_1', 106: 'C_CD_NA_1', \
               110: 'P_ME_NA_1', 111: 'P_ME_NB_1', 112: 'P_ME_NC_1', 113: 'P_AC_NA_1', 120: 'F_FR_NA_1', 121: 'F_SR_NA_1', \
               122: 'F_SC_NA_1', 123: 'F_LS_NA_1', 124: 'F_AF_NA_1', 125: 'F_SG_NA_1', 126: 'F_DR_TA_1'}

cot_dic = {0: 'Undefined', 1: 'per or cyc', 2: 'back', 3: 'spont', 4: 'init', 5: 'req', 6: 'act', 7: 'actcon', \
           8: 'deact', 9: 'deactcon', 10: 'actterm', 11: 'retrem', 12: 'retloc', 13: 'file', 14: 'reserve', 15: 'reserve', \
           16: 'reserve', 17: 'reserve', 18: 'reserve', 19: 'reserve', 20: 'introgen', 21: 'inro1', 22: 'inro2', 23: 'inro3', \
           24: 'inro4', 25: 'inro5', 26: 'inro6', 27: 'inro7', 28: 'inro8', 29: 'inro9', 30: 'inro10', 31: 'inro11', \
           32: 'inro12', 33: 'inro13', 34: 'inro14', 35: 'inro15', 36: 'inro16', 37: 'reqcogen', 38: 'reqco1', 39: 'reqco2', \
           40: 'reqco3', 41: 'reqco4', 42: 'reserve', 43: 'reserve', 44: 'UnknowTypeID', 45: 'UnknowCOT', 46: 'UnknowPubAddr', \
           47: 'UnknowInfoAddr'}

def HexStrToHexArray(hexstr):
    hexarray = []
    offset = 0
    tmp_data = 0
    for c in hexstr:
        if offset % 2 == 0:
            tmp_data = 16 * int(c, 16)
        else:
            tmp_data += int(c, 16)
            hexarray.append(tmp_data)
        offset += 1
    return hexarray

