from CapaDatos import Partido, DatosChampions, Campeon
from datetime import datetime, timedelta
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': 'd4187688c1b24d6fbbb6630380d7f0c1'}
datos=DatosChampions()

def crear_tablaPartidos():
    datos.crear_tablaPartidos()

def crear_tablaCampeones():
    datos.crear_tablaCampeones()

def borrar_tablaPartidos():
    datos.borrar_tablaPartidos()

def borrar_tablaCampeones():
    datos.borrar_tablaCampeones()

def altaPartidos(temporada):
        connection.request('GET', '/v2/competitions/CL/matches?season='+temporada, None, headers)
        partidos = json.loads(connection.getresponse().read().decode())
        for i in (partidos['matches']):
            ronda = i['stage']
            grupo = i['group']
            if grupo is None:
                grupo = '-'
            fechahora = (i['utcDate'])
            fecha = datetime.strptime(fechahora[0:10], '%Y-%m-%d')
            hora = str(eval(fechahora[11:13]+'-3')) + fechahora[13:16]
            local = i['homeTeam']['name']
            visitante = i['awayTeam']['name']
            golesLocal = i['score']['fullTime']['homeTeam']
            if golesLocal is None:
                golesLocal = '-'
            golesVisitante = i['score']['fullTime']['awayTeam']
            if golesVisitante is None:
                golesVisitante='-'
            golesLocalExtra = i['score']['extraTime']['homeTeam']
            if golesLocalExtra is None:
                golesLocalExtra = '-'
            golesVisitanteExtra = i['score']['extraTime']['awayTeam']
            if golesVisitanteExtra is None:
                golesVisitanteExtra = '-'
            penalesLocal = i['score']['penalties']['homeTeam']
            if penalesLocal is None:
                penalesLocal = '-'
            penalesVisitante = i['score']['penalties']['awayTeam']
            if penalesVisitante is None:
                penalesVisitante = '-'
            datos.altaPartido(Partido(temporada=temporada, ronda=ronda, grupo=grupo, fecha=fecha, hora=hora, equipoLocal=local.upper(),
                                      equipoVisitante=visitante.upper(), golesLocal=golesLocal, golesVisitante=golesVisitante,
                                      golesLocalExtra=golesLocalExtra, golesVisitanteExtra=golesVisitanteExtra, penalesLocal=penalesLocal, penalesVisitante=penalesVisitante))

def actualizarPartidosBD():
    datos.bajaPartidosSinActualizar()
    temporada=str(datetime.now().year)
    dateFrom=datetime.strftime(datos.obtenerFechaUltimo()+timedelta(days=1), '%Y-%m-%d')
    dateTo=datetime.strftime(datetime(2019, 12, 31), '%Y-%m-%d')
    connection.request('GET', '/v2/competitions/CL/matches?season='+temporada+'&dateFrom='+dateFrom+'&dateTo='+dateTo, None, headers)
    partidos = json.loads(connection.getresponse().read().decode())
    for i in (partidos['matches']):
            ronda = i['stage']
            grupo = i['group']
            if grupo is None:
                grupo = '-'
            fechahora = (i['utcDate'])
            fecha = datetime.strptime(fechahora[0:10], '%Y-%m-%d')
            hora = str(eval(fechahora[11:13]+'-3')) + fechahora[13:16]
            local = i['homeTeam']['name']
            visitante = i['awayTeam']['name']
            golesLocal = i['score']['fullTime']['homeTeam']
            if golesLocal is None:
                golesLocal = '-'
            golesVisitante = i['score']['fullTime']['awayTeam']
            if golesVisitante is None:
                golesVisitante='-'
            golesLocalExtra = i['score']['extraTime']['homeTeam']
            if golesLocalExtra is None:
                golesLocalExtra = '-'
            golesVisitanteExtra = i['score']['extraTime']['awayTeam']
            if golesVisitanteExtra is None:
                golesVisitanteExtra = '-'
            penalesLocal = i['score']['penalties']['homeTeam']
            if penalesLocal is None:
                penalesLocal = '-'
            penalesVisitante = i['score']['penalties']['awayTeam']
            if penalesVisitante is None:
                penalesVisitante = '-'
            datos.altaPartido(Partido(temporada=temporada, ronda=ronda, grupo=grupo, fecha=fecha, hora=hora, equipoLocal=local.upper(),
                                      equipoVisitante=visitante.upper(), golesLocal=golesLocal, golesVisitante=golesVisitante,
                                      golesLocalExtra=golesLocalExtra, golesVisitanteExtra=golesVisitanteExtra, penalesLocal=penalesLocal, penalesVisitante=penalesVisitante))


def altaCampeon(temporada, escudo, nombre, pais):
    datos.altaCampeon(Campeon(temporada=temporada, escudo=escudo, nombre=nombre, pais=pais))

def bajaCampeon(temporada):
    datos.bajaCampeonTemporada(temporada)

def bajaPartidosTemporada(temporada):
    datos.bajaPartidosTemporada(temporada)

#crear_tablaPartidos()
#crear_tablaCampeones()
#borrar_tablaPartidos()
#borrar_tablaCampeones()
#bajaPartidosTemporada(2019)
#altaPartidos('2019')
actualizarPartidosBD()

'''
altaCampeon('1956', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('1957', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('1958', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('1959', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('1960', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('1961', 'http://1.bp.blogspot.com/-kbVpvktIDyY/UGevjJt6COI/AAAAAAAACBU/2mtC4PaxL_0/s1600/BENFICA.png', 'Benfica', 'Portugal')
altaCampeon('1962', 'http://1.bp.blogspot.com/-kbVpvktIDyY/UGevjJt6COI/AAAAAAAACBU/2mtC4PaxL_0/s1600/BENFICA.png', 'Benfica', 'Portugal')
altaCampeon('1963', 'http://4.bp.blogspot.com/-UztIC5pFmaE/UfiATSd7Q8I/AAAAAAAACOk/s9QuS0YhSeQ/s400/escudo-milan-sin-fondo.png', 'Milan', 'Italia')
altaCampeon('1964', 'https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png', 'Inter', 'Italia')
altaCampeon('1965', 'https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png', 'Inter', 'Italia')
altaCampeon('1966', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('1967', 'http://1.bp.blogspot.com/-FM_8NtYnt0I/UF_gGEhayWI/AAAAAAAABJU/LUSsX16ygg4/s1600/CELTIC.png', 'Celtic', 'Escocia')
altaCampeon('1968', 'http://4.bp.blogspot.com/-9s9OU6jqnuE/UkR9uCR2zEI/AAAAAAAAAA0/NopXGf7J8xU/s1600/Manchester+United+1.png', 'Manchester United', 'Inglaterra')
altaCampeon('1969', 'http://4.bp.blogspot.com/-UztIC5pFmaE/UfiATSd7Q8I/AAAAAAAACOk/s9QuS0YhSeQ/s400/escudo-milan-sin-fondo.png', 'Milan', 'Italia')
altaCampeon('1970', 'http://www.boutiquemaillotfootpascher.fr/images/img/Feyenoord.png', 'Feyenoord', 'Holanda')
altaCampeon('1971', 'http://3.bp.blogspot.com/-NtPddMii_dE/UC_3CTETeBI/AAAAAAAAB3k/z_MlCMq1nYM/s1600/992.png', 'Ajax', 'Holanda')
altaCampeon('1972', 'http://3.bp.blogspot.com/-NtPddMii_dE/UC_3CTETeBI/AAAAAAAAB3k/z_MlCMq1nYM/s1600/992.png', 'Ajax', 'Holanda')
altaCampeon('1973', 'http://3.bp.blogspot.com/-NtPddMii_dE/UC_3CTETeBI/AAAAAAAAB3k/z_MlCMq1nYM/s1600/992.png', 'Ajax', 'Holanda')
altaCampeon('1974', 'http://4.bp.blogspot.com/-5nJ5NgA5BgM/Vc4jB3RTO4I/AAAAAAAABCE/L-BqsbDlaao/s1600/bayern-munich.png', 'Bayern Múnich', 'Alemania')
altaCampeon('1975', 'http://4.bp.blogspot.com/-5nJ5NgA5BgM/Vc4jB3RTO4I/AAAAAAAABCE/L-BqsbDlaao/s1600/bayern-munich.png', 'Bayern Múnich', 'Alemania')
altaCampeon('1976', 'http://4.bp.blogspot.com/-5nJ5NgA5BgM/Vc4jB3RTO4I/AAAAAAAABCE/L-BqsbDlaao/s1600/bayern-munich.png', 'Bayern Múnich', 'Alemania')
altaCampeon('1977', 'http://2.bp.blogspot.com/-M9842_a3KpQ/UASXH-WuxuI/AAAAAAAAAIo/M6f827rKuvE/s1600/escudo+inedito+del+liverpool.png', 'Liverpool', 'Inglaterra')
altaCampeon('1978', 'http://2.bp.blogspot.com/-M9842_a3KpQ/UASXH-WuxuI/AAAAAAAAAIo/M6f827rKuvE/s1600/escudo+inedito+del+liverpool.png', 'Liverpool', 'Inglaterra')
altaCampeon('1979', 'http://4.bp.blogspot.com/-m9R-yvkL6-4/USo9Ljp0TRI/AAAAAAAAE1E/jjYohRqWo9U/s1600/escudo+del+nottingham+f.png', 'Nottingham F.', 'Inglaterra')
altaCampeon('1980', 'http://4.bp.blogspot.com/-m9R-yvkL6-4/USo9Ljp0TRI/AAAAAAAAE1E/jjYohRqWo9U/s1600/escudo+del+nottingham+f.png', 'Nottingham F.', 'Inglaterra')
altaCampeon('1981', 'http://2.bp.blogspot.com/-M9842_a3KpQ/UASXH-WuxuI/AAAAAAAAAIo/M6f827rKuvE/s1600/escudo+inedito+del+liverpool.png', 'Liverpool', 'Inglaterra')
altaCampeon('1982', 'http://3.bp.blogspot.com/-BWbdJeM3QEc/U-1uJEMrO1I/AAAAAAAAKew/TAEixQUJdHw/s1600/603.png', 'Aston Villa', 'Inglaterra')
altaCampeon('1983', 'https://uefaclubs.com/images/Hamburger-SV%402.-other-logo.png', 'Hamburgo', 'Alemania')
altaCampeon('1984', 'http://2.bp.blogspot.com/-M9842_a3KpQ/UASXH-WuxuI/AAAAAAAAAIo/M6f827rKuvE/s1600/escudo+inedito+del+liverpool.png', 'Liverpool', 'Inglaterra')
altaCampeon('1985', 'http://2.bp.blogspot.com/-FIP91uaGywc/UKmnoJ0SxgI/AAAAAAAACNc/pfN_S7jXrWA/s1600/Juventus1.png', 'Juventus', 'Italia')
altaCampeon('1986', 'http://1.bp.blogspot.com/-FoPDqDsVN4Y/UOBnZ_MopkI/AAAAAAAANSY/fv_RVk2Nrn8/s1600/steaua+bucuresti.png', 'Steaua Bucarest', 'Rumania')
altaCampeon('1987', 'http://2.bp.blogspot.com/-_UAxaGH0cZM/UL-Lfggl-DI/AAAAAAAAAjM/VgP_ToUufyQ/s1600/escudo+inedito+del+porto.png', 'Porto', 'Portugal')
altaCampeon('1988', 'http://1.bp.blogspot.com/-6QhxWseaozw/UVJiGl_3XfI/AAAAAAAAFB8/_FdtjAPLM8o/s1600/Preview.png', 'PSV', 'Holanda')
altaCampeon('1989', 'http://4.bp.blogspot.com/-UztIC5pFmaE/UfiATSd7Q8I/AAAAAAAACOk/s9QuS0YhSeQ/s400/escudo-milan-sin-fondo.png', 'Milan', 'Italia')
altaCampeon('1990', 'http://4.bp.blogspot.com/-UztIC5pFmaE/UfiATSd7Q8I/AAAAAAAACOk/s9QuS0YhSeQ/s400/escudo-milan-sin-fondo.png', 'Milan', 'Italia')
altaCampeon('1991', 'http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png', 'Estrella Roja', 'Serbia')
altaCampeon('1992', 'http://www.logospng.com/images/21/renders-f-218tbol-2013-fc-barcelona-21025.png', 'Barcelona', 'España')
altaCampeon('1993', 'http://4.bp.blogspot.com/-6BBwXzathq4/Uhl95oUOSXI/AAAAAAAAQRc/IpGOuMcxPLc/s1600/866.png', 'Marsella', 'Francia')
altaCampeon('1994', 'http://4.bp.blogspot.com/-UztIC5pFmaE/UfiATSd7Q8I/AAAAAAAACOk/s9QuS0YhSeQ/s400/escudo-milan-sin-fondo.png', 'Milan', 'Italia')
altaCampeon('1995', 'http://3.bp.blogspot.com/-NtPddMii_dE/UC_3CTETeBI/AAAAAAAAB3k/z_MlCMq1nYM/s1600/992.png', 'Ajax', 'Holanda')
altaCampeon('1996', 'http://2.bp.blogspot.com/-FIP91uaGywc/UKmnoJ0SxgI/AAAAAAAACNc/pfN_S7jXrWA/s1600/Juventus1.png', 'Juventus', 'Italia')
altaCampeon('1997', 'http://3.bp.blogspot.com/-MtoQz8P6TnY/U83JbLHdG3I/AAAAAAAASrA/zPMKkNyGEg4/s1600/Inedito+Local.png', 'Borussia Dortmund', 'Alemania')
altaCampeon('1998', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('1999', 'http://4.bp.blogspot.com/-9s9OU6jqnuE/UkR9uCR2zEI/AAAAAAAAAA0/NopXGf7J8xU/s1600/Manchester+United+1.png', 'Manchester United', 'Inglaterra')
altaCampeon('2000', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('2001', 'http://4.bp.blogspot.com/-5nJ5NgA5BgM/Vc4jB3RTO4I/AAAAAAAABCE/L-BqsbDlaao/s1600/bayern-munich.png', 'Bayern Múnich', 'Alemania')
altaCampeon('2002', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('2003', 'http://4.bp.blogspot.com/-UztIC5pFmaE/UfiATSd7Q8I/AAAAAAAACOk/s9QuS0YhSeQ/s400/escudo-milan-sin-fondo.png', 'Milan', 'Italia')
altaCampeon('2004', 'http://2.bp.blogspot.com/-_UAxaGH0cZM/UL-Lfggl-DI/AAAAAAAAAjM/VgP_ToUufyQ/s1600/escudo+inedito+del+porto.png', 'Porto', 'Portugal')
altaCampeon('2005', 'http://2.bp.blogspot.com/-M9842_a3KpQ/UASXH-WuxuI/AAAAAAAAAIo/M6f827rKuvE/s1600/escudo+inedito+del+liverpool.png', 'Liverpool', 'Inglaterra')
altaCampeon('2006', 'http://www.logospng.com/images/21/renders-f-218tbol-2013-fc-barcelona-21025.png', 'Barcelona', 'España')
altaCampeon('2007', 'http://4.bp.blogspot.com/-UztIC5pFmaE/UfiATSd7Q8I/AAAAAAAACOk/s9QuS0YhSeQ/s400/escudo-milan-sin-fondo.png', 'Milan', 'Italia')
altaCampeon('2008', 'http://4.bp.blogspot.com/-9s9OU6jqnuE/UkR9uCR2zEI/AAAAAAAAAA0/NopXGf7J8xU/s1600/Manchester+United+1.png', 'Manchester United', 'Inglaterra')
altaCampeon('2009', 'http://www.logospng.com/images/21/renders-f-218tbol-2013-fc-barcelona-21025.png', 'Barcelona', 'España')
altaCampeon('2010', 'https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png', 'Inter', 'Italia')
altaCampeon('2011', 'http://www.logospng.com/images/21/renders-f-218tbol-2013-fc-barcelona-21025.png', 'Barcelona', 'España')
altaCampeon('2012', 'http://4.bp.blogspot.com/-0iKROE0pbt8/UGiD1eLyP5I/AAAAAAAACHc/op_oDMRpqDg/s1600/Chelsea+inedito.png', 'Chelsea', 'Inglaterra')
altaCampeon('2013', 'http://4.bp.blogspot.com/-5nJ5NgA5BgM/Vc4jB3RTO4I/AAAAAAAABCE/L-BqsbDlaao/s1600/bayern-munich.png', 'Bayern Múnich', 'Alemania')
altaCampeon('2014', 'http://www.logospng.com/images/57/real-madrid-logo-wallpapers-hd-2017-wallpaper-cave-57286.png', 'Real Madrid', 'España')
altaCampeon('2015', 'http://www.logospng.com/images/21/renders-f-218tbol-2013-fc-barcelona-21025.png', 'Barcelona', 'España')
altaCampeon('2016', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('2017', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('2018', 'https://upload.wikimedia.org/wikipedia/commons/9/98/Escudo_real_madrid_1941.png', 'Real Madrid', 'España')
altaCampeon('2019', 'http://2.bp.blogspot.com/-M9842_a3KpQ/UASXH-WuxuI/AAAAAAAAAIo/M6f827rKuvE/s1600/escudo+inedito+del+liverpool.png', 'Liverpool', 'Inglaterra')
'''







