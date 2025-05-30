from logueo import *
from actividades import *

driver, _ = login_siebel('rpaajustes2.service', '6yckCF6GjhyxjJSU/')
resultados = aplicacionAjuste(driver, '2025-05-28', '-', '40755273', '-', 'CARGO POR PAGO EXTEMPORANEO', '-', '2025-05-28T16:28:00','','')