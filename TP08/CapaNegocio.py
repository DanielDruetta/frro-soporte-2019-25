from CapaDatos import  DatosChampions
from datetime import datetime

class NoSeEstanJugando(Exception):
    pass

class HoyNoHay(Exception):
    pass

class NoHayRegistroTemporada(Exception):
    pass

class NoHayPartidosPendientes(Exception):
    pass

class FaseDeGrupoSinJugarse(Exception):
    pass

class NoHayEnfrentamientos(Exception):
    pass

class PartidoNegocio:

    def __init__(self, ronda, grupo, fecha, hora, local, visitante, golesL, golesV,tiempo):
        self.ronda=ronda
        self.grupo=grupo
        self.fecha=fecha
        self.hora=hora
        self.equipoLocal=local
        self.equipoVisitante=visitante
        self.golesLocal=golesL
        self.golesVisitante=golesV
        self.tiempo=tiempo

class JugadorNegocio:

    def __init__(self, nombre, nacionalidad, equipo, posicion, goles):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.equipo = equipo
        self.posicion = posicion
        self.goles = goles

class PosicionNegocio:

    def __init__(self, nro, escudo, equipo, jugados, ganados, empatados, perdidos, gf, gc, dg, pts):
        self.nro=nro
        self.escudo=escudo
        self.equipo=equipo
        self.jugados=jugados
        self.ganados=ganados
        self.empatados=empatados
        self.perdidos=perdidos
        self.gf=gf
        self.gc=gc
        self.dg=dg
        self.pts=pts

class NegocioChampions:

    def __init__(self):
        self.datos = DatosChampions()

    def obtenerPartidosRonda1(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosRonda1(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidosRonda2(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosRonda2(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidosRonda3(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosRonda3(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidosPlayOffs(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosPlayOffs(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidosFaseDeGrupos(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosFaseDeGrupos(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidosOctavos(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosOctavos(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidosCuartos(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosCuartos(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidosSemi(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidosSemi(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def obtenerPartidoFinal(self, temporada):
        if (int(temporada) < 2017):
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            partidos=self.datos.obtenerPartidoFinal(temporada)
            if partidos is False:
                return False
            else:
                return partidos

    def partidosPorJugarse(self):
        partidos=self.datos.partidosPorJugarse()
        if partidos is False:
            raise NoHayPartidosPendientes("No hay partidos pendientes para la competencia")
        else:
            pendientes=[]
            for i in partidos['matches']:
                ronda = i['stage']
                grupo = i['group']
                fechahora = (i['utcDate'])
                fecha = fechahora[0:10]
                hora = str(eval(fechahora[11:13]+'-3')) + fechahora[13:16]
                local = i['homeTeam']['name']
                visitante = i['awayTeam']['name']
                golesLocal = None
                golesVisitante = None
                tiempo = None
                pendientes.append(PartidoNegocio(ronda, grupo, fecha, hora, local, visitante, golesLocal, golesVisitante, tiempo))
            return pendientes


    def obtenerPartidosDeHoy(self):
        partidos=self.datos.obtenerPartidosDeHoy()
        if partidos is False:
            raise HoyNoHay('Hoy no hay partidos por jugar')
        else:
            jugando=[]
            for i in partidos['matches']:
                ronda = i['stage']
                grupo = i['group']
                fechahora = (i['utcDate'])
                fecha = fechahora[0:10]
                hora = str(eval(fechahora[11:13]+'-3')) + fechahora[13:16]
                local = i['homeTeam']['name']
                visitante = i['awayTeam']['name']
                golesLocal = i['score']['fullTime']['homeTeam']
                golesVisitante = i['score']['fullTime']['awayTeam']
                tiempo=''
                jugando.append(PartidoNegocio(ronda, grupo, fecha, hora, local, visitante, golesLocal, golesVisitante, tiempo))
            return jugando

    def partidosQueSeEstanJugando(self):
        partidos=self.datos.partidosQueSeEstanJugando()
        if partidos is False:
            raise NoSeEstanJugando('No se está jugando ningún partido en este momento')
        else:
            jugando=[]
            for i in partidos['matches']:
                ronda = i['stage']
                grupo = i['group']
                if grupo is None:
                    grupo=' - '
                fechahora = (i['utcDate'])
                fecha = datetime.strptime(fechahora[0:10], '%Y-%m-%d')
                hora = str(eval(fechahora[11:13]+'-3')) + fechahora[13:16]
                local = i['homeTeam']['name']
                visitante = i['awayTeam']['name']
                golesLocal = i['score']['fullTime']['homeTeam']
                golesVisitante = i['score']['fullTime']['awayTeam']
                tiempo=''
                jugando.append(PartidoNegocio(ronda, grupo, fecha, hora, local, visitante, golesLocal, golesVisitante, tiempo))
            return jugando

    def partidosEquipo(self, equipo):
        partidosEquipo=self.datos.partidosEquipo(equipo)
        if partidosEquipo is False:
            return False
        else:
            return partidosEquipo

    def tablaGoleadoresTemporada(self, temporada):
        goleadores=self.datos.tablaGoleadoresTemporada(temporada)
        if int(temporada) < 2017:
            raise NoHayRegistroTemporada('Sólo hay registros desde la temporada 2017 de la UCL')
        else:
            goleadoresTemporada=[]
            for i in goleadores['scorers']:
                nombre = i['player']['name']
                nacionalidad = i['player']['nationality']
                equipo = i['team']['name']
                posicion = i['player']['position']
                goles = i['numberOfGoals']
                goleadoresTemporada.append(JugadorNegocio(nombre, nacionalidad, equipo, posicion, goles))
            return goleadoresTemporada

    def listaDeCampeones(self):
        campeones = self.datos.listaDeCampeones()
        return campeones

    def diferenciaPartidosEquipos(self, equipo1, equipo2):
        equipo1=equipo1.upper()
        equipo2=equipo2.upper()
        partidos = self.datos.partidosEntreEquipos(equipo1, equipo2)
        if partidos is False:
            raise NoHayEnfrentamientos('Los equipos no se enfrentaron nunca')
        else:
            cantidadEnfrentamientos = self.cantidadEnfrentamientos(partidos)
            victoriasEquipo1 = self.victoriasEquipo(partidos, equipo1)
            victoriasEquipo2 = self.victoriasEquipo(partidos, equipo2)
            cantidadEmpates = cantidadEnfrentamientos - (victoriasEquipo1 + victoriasEquipo2)
            enfrentamientos = [equipo1, equipo2, cantidadEnfrentamientos, victoriasEquipo1, victoriasEquipo2, cantidadEmpates]
            return enfrentamientos

    def cantidadEnfrentamientos(self, partidos):
        cantidad = len(partidos)
        return cantidad

    def victoriasEquipo(self, partidos, equipo):
        victorias=0
        for i in partidos:
            if  equipo in i.equipoLocal:
                if (i.golesLocal > i.golesVisitante):
                    victorias = victorias + 1
            elif equipo in i.equipoVisitante:
                if (i.golesLocal < i.golesVisitante):
                    victorias = victorias + 1
        return victorias

#Escudops

    def posicionesTemporada(self, temporada):
        grupoA=[]
        grupoB=[]
        grupoC=[]
        grupoD=[]
        grupoE=[]
        grupoF=[]
        grupoG=[]
        grupoH=[]
        posiciones=self.datos.posicionesTemporada(temporada)
        if posiciones is False:
            raise FaseDeGrupoSinJugarse('La fase de grupo aún no se jugó')
        else:
            for p in posiciones:
                if p['group']=='GROUP_A':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoA.append(posicion)
                elif p['group']=='GROUP_B':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoB.append(posicion)
                elif p['group']=='GROUP_C':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoC.append(posicion)
                elif p['group']=='GROUP_D':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoD.append(posicion)
                elif p['group']=='GROUP_E':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoE.append(posicion)
                elif p['group']=='GROUP_F':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoF.append(posicion)
                elif p['group']=='GROUP_G':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoG.append(posicion)
                elif p['group']=='GROUP_H':
                    for t in p['table']:
                        nro=t['position']
                        escudo=t['team']['crestUrl']
                        if t['team']['name'] == 'FC Internazionale Milano':
                            escudo='https://1.bp.blogspot.com/-5he2E1pMpIE/WX_0DvXNEAI/AAAAAAAABfQ/b4qdHXH4EEgNST-_CYys6IHVC0lVq1T2wCLcBGAs/s400/internazionale256.png'
                        elif t['team']['name'] == 'Paris Saint-Germain FC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/49.png'
                        elif t['team']['name'] == 'RSC Anderlecht':
                            escudo='http://1.bp.blogspot.com/-u99JRU42LkI/UjzhVrSP-0I/AAAAAAAAPFY/dbUvKZedezA/s1600/186.png'
                        elif t['team']['name'] == 'PFC CSKA Moskva':
                            escudo='http://1.bp.blogspot.com/-jIRKPgzCFbY/UhzSLHoLhPI/AAAAAAAAAEk/rq-kAAdLAgE/s1600/escudo.png'
                        elif t['team']['name'] == 'Sport Lisboa e Benfica':
                            escudo='https://seeklogo.com/images/S/sport-lisboa-e-benfica-logo-149703CDAB-seeklogo.com.png'
                        elif t['team']['name'] == 'Club Brugge KV':
                            escudo='https://upload.wikimedia.org/wikipedia/el/f/fd/Club_Brugge_KV.svg'
                        elif t['team']['name'] == 'AS Monaco FC':
                            escudo='http://4.bp.blogspot.com/-FsxgtE36OT4/U9K_hi7wF1I/AAAAAAAAS6o/tqcjuZbC-kY/s1600/826.png'
                        elif t['team']['name'] == 'FK Crvena Zvezda':
                            escudo='http://3.bp.blogspot.com/-FCWB6wF8e4A/UJc6p7wfbBI/AAAAAAAAJBM/a3RwHLnVRHo/s1600/800px-Gazprom-Logo_svg.png'
                        elif t['team']['name'] == 'Qarabağ Ağdam FK':
                            escudo='http://i.imgur.com/giNRGO5.png'
                        elif t['team']['name'] == 'Sporting Clube de Portugal':
                            escudo='http://3.bp.blogspot.com/-1Wf0t1RfO5k/UDq33HnTM_I/AAAAAAAABeM/5peX-zpHvbY/s1600/563404_325318857557645_1557008623_n.png'
                        elif t['team']['name'] == 'FK Spartak Moskva':
                            escudo='http://2.bp.blogspot.com/-_R2WhIk1hDA/UIieGWaPr-I/AAAAAAAAFOQ/uk6FiI7C4nA/s1600/Spartak-Moscow.png'
                        elif t['team']['name'] == 'NK Maribor':
                            escudo='http://2.bp.blogspot.com/-B4sZBJrocyQ/UE3_bfMxrnI/AAAAAAAACKI/hKlDFgaepUY/s1600/maribor.png'
                        elif t['team']['name'] == 'FK Shakhtar Donetsk':
                            escudo='http://2.bp.blogspot.com/-21Sm4RNBYro/Ujo9wBMLarI/AAAAAAAAADQ/7Z-aneABWfg/s1600/EscudoShakhtarDonetsk.png'
                        elif t['team']['name'] == 'Beşiktaş JK':
                            escudo='http://4.bp.blogspot.com/-R9s5QLjXMdE/UDlNGxfOo_I/AAAAAAAABR0/lqvBkXN9jSs/s1600/Besiktas.png'
                        elif t['team']['name'] == 'APOEL FC':
                            escudo='http://4.bp.blogspot.com/-w6w8eBX1FKA/UjzjIV4cY7I/AAAAAAAAPFw/T9VCg2Ah2M4/s1600/451.png'
                        elif t['team']['name'] == 'FK Lokomotiv Moskva':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/561.png'
                        elif t['team']['name'] == 'PAE AEK':
                            escudo='http://1.bp.blogspot.com/-PORXmfV5Uf8/UPs-BopC9fI/AAAAAAAAEl8/itrKlZ1pg1Q/s1600/aek-emblem-transparent.png'
                        elif t['team']['name'] == 'Olympique Lyonnais':
                            escudo='http://1.bp.blogspot.com/--Zh5GOb25ec/UcMsbfjDoQI/AAAAAAAAOgo/AtrRhcXL5VQ/s1600/Lyon.png'
                        elif t['team']['name'] == 'FC Viktoria Plzeň':
                            escudo='http://2.bp.blogspot.com/-0XE9LfeuNIw/UjzkQUvJrdI/AAAAAAAAPGE/R-rv5glKcxQ/s1600/477.png'
                        elif t['team']['name'] == 'BSC Young Boys':
                            escudo='https://pronosticos.futbol/images/teams/young-boys-YOB-CH.png?v=1509560237'
                        elif t['team']['name'] == 'FC Red Bull Salzburg':
                            escudo='https://3.bp.blogspot.com/-WUsK0vLOIDk/WVmHVEC3_1I/AAAAAAABLWE/PwCxEXV0v3A8ORVFO6NgZh9cmvaJXGd7ACLcBGAs/s1600/FC%2BRed%2BBull%2BSalzburg.png'
                        elif t['team']['name'] == 'KRC Genk':
                            escudo='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KRC_Genk_Logo_2016.svg/1200px-KRC_Genk_Logo_2016.svg.png'
                        elif t['team']['name'] == 'SK Slavia Praha':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/914.png'
                        elif t['team']['name'] == 'Lille OSC':
                            escudo='http://as00.epimg.net/img/comunes/fotos/fichas/equipos/large/124.png'
                        equipo=t['team']['name']
                        judados=t['playedGames']
                        ganados=t['won']
                        empatados=t['draw']
                        perdidos=t['lost']
                        gf=t['goalsFor']
                        gc=t['goalsAgainst']
                        dg=t['goalDifference']
                        pts=t['points']
                        posicion=PosicionNegocio(nro, escudo, equipo, judados, ganados, empatados, perdidos, gf, gc, dg, pts)
                        grupoH.append(posicion)
            return {'A':grupoA, 'B':grupoB, 'C':grupoC, 'D':grupoD, 'E':grupoE, 'F':grupoF, 'G':grupoG, 'H':grupoH}
