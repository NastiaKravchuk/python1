import data_pr as pr
import logger as log

def dataView():
    data=pr.InputDate()
    log.add_data(data)
    return data