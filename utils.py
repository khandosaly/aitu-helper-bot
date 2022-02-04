# Проверка на число
def isnumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Починка после перезапуска
def reboot_fix(idd, state):
    if idd in state:
        pass
    else:
        state[idd] = 'MENU'
    return state


def get_pov_final(terms_mid):
    mid_total = round(terms_mid * 0.3, 2)
    pov_total = 90 - mid_total
    pov_final = round(pov_total / 0.4, 2)
    return pov_final


def get_ret_final(terms_mid):
    mid_total = round(terms_mid * 0.3, 2)
    ret_total = 50 - mid_total
    ret_final = round(ret_total / 0.4, 2)
    if ret_final < 50:
        ret_final = 50
    return ret_final


def get_sch_final(terms_mid):
    mid_total = round(terms_mid * 0.3, 2)
    sch_total = 70 - mid_total
    sch_final = round(sch_total / 0.4, 2)
    if sch_final < 50:
        sch_final = 50
    return sch_final


