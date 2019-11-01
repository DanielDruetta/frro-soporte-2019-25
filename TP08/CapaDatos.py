from sqlalchemy.ext.declarative import declarative_base as db
from sqlalchemy import Column, Integer, Date, String, create_engine, or_, and_
from sqlalchemy.orm import sessionmaker
import http.client
import json
from datetime import datetime

connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': 'd4187688c1b24d6fbbb6630380d7f0c1'}
Base= db()

class Partido(Base):
    __tablename__='partidos'
    idPartido = Column(Integer, primary_key=True, autoincrement=True)
    temporada = Column(String)
    ronda = Column(String)
    grupo = Column(String)
    fecha = Column(Date)
    hora = Column(String)
    equipoLocal = Column(String)
    equipoVisitante = Column(String)
    golesLocal = Column(Integer)
    golesVisitante = Column(Integer)
    golesLocalExtra = Column(Integer)
    golesVisitanteExtra = Column(Integer)
    penalesLocal = Column(Integer)
    penalesVisitante = Column(Integer)

class Campeon(Base):
    __tablename__='campeones'
    temporada = Column(String, primary_key=True)
    escudo = Column(String)
    nombre=Column(String)
    pais=Column(String)


class DatosChampions(object):

    def __init__(self):
        engine=create_engine('sqlite:///tpi.db')
        Base.metadata.bind=engine
        db_session=sessionmaker()
        db_session.bind=engine
        self.session=db_session()

    def crear_tablaPartidos(self):
        Partido.__table__.create()

    def borrar_tablaPartidos(self):
        Partido.__table__.drop()

    def crear_tablaCampeones(self):
        Campeon.__table__.create()

    def borrar_tablaCampeones(self):
        Campeon.__table__.drop()

    def altaPartido(self,partido):
        self.session.add(partido)
        self.session.commit()
        return partido

    def altaCampeon(self, campeon):
        self.session.add(campeon)
        self.session.commit()
        return campeon

    def bajaPartidosTemporada(self, temporada):
        partidosTemp=self.session.query(Partido).filter(Partido.temporada == temporada).all()
        if partidosTemp == []:
            return False
        else:
            for i in partidosTemp:
                self.session.delete(i)
                self.session.commit()
        return True

    def bajaPartidosSinActualizar(self):
        partidoNull = self.session.query(Partido).filter(Partido.golesLocal == '-').all()
        if partidoNull == []:
            return False
        else:
            for i in partidoNull:
                self.session.delete(i)
                self.session.commit()

    def bajaCampeonTemporada(self, temporada):
        campeon=self.session.query(Campeon).filter(Campeon.temporada == temporada).first()
        if campeon is None:
            return False
        else:
            self.session.delete(campeon)
            self.session.commit()
            return True

    def obtenerFechaUltimo(self):
        ultimo = self.session.query(Partido).order_by(Partido.idPartido.desc()).first()
        if ultimo is None:
            return False
        else:
            return ultimo.fecha

    def obtenerPartidosRonda1(self, temporada):
        partidosRonda1=self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda=='1ST_QUALIFYING_ROUND').all()
        if partidosRonda1 == []:
            return False
        else:
            return partidosRonda1

    def obtenerPartidosRonda2(self, temporada):
        partidosRonda2=self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda=='2ND_QUALIFYING_ROUND').all()
        if partidosRonda2 == []:
            return False
        else:
            return partidosRonda2

    def obtenerPartidosRonda3(self, temporada):
        partidosRonda3=self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda=='3RD_QUALIFYING_ROUND').all()
        if partidosRonda3 == []:
            return False
        else:
            return partidosRonda3

    def obtenerPartidosPlayOffs(self, temporada):
        partidosPlayOffs=self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda=='PLAY_OFF_ROUND').all()
        if partidosPlayOffs == []:
            return False
        else:
            return partidosPlayOffs

    def obtenerPartidosFaseDeGrupos(self, temporada):
        partidosGrupos=self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda=='GROUP_STAGE').all()
        if partidosGrupos == []:
            return False
        else:
            return partidosGrupos

    def obtenerPartidosOctavos(self, temporada):
        partidosOctavos=self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda=='ROUND_OF_16').all()
        if partidosOctavos==[]:
            return False
        else:
            return partidosOctavos

    def obtenerPartidosCuartos(self, temporada):
        partidosCuartos=self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda=='QUARTER_FINALS').all()
        if partidosCuartos==[]:
            return False
        else:
            return partidosCuartos

    def obtenerPartidosSemi(self, temporada):
        partidosSemi = self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda == 'SEMI_FINALS').all()
        if partidosSemi == []:
            return False
        else:
            return partidosSemi

    def obtenerPartidoFinal(self, temporada):
        final = self.session.query(Partido).filter(Partido.temporada == temporada, Partido.ronda == 'FINAL').all()
        if final == []:
            return False
        else:
            return final

    def partidosPorJugarse(self):
        connection.request('GET', '/v2/competitions/CL/matches?status=SCHEDULED', None, headers)
        partidos = json.loads(connection.getresponse().read().decode())
        if partidos['count'] == 0:
            return False
        else:
            return partidos

    def obtenerPartidosDeHoy(self):
        hoy = datetime.strftime(datetime.today(), '%Y-%m-%d')
        connection.request('GET', '/v2/competitions/CL/matches?dateFrom='+hoy+'&dateTo='+hoy, None, headers)
        partidos = json.loads(connection.getresponse().read().decode())
        if partidos['count'] == 0:
            return False
        else:
            return partidos

    def partidosQueSeEstanJugando(self):
        connection.request('GET', '/v2/competitions/CL/matches?status=LIVE', None, headers)
        partidosJugando = json.loads(connection.getresponse().read().decode())
        if partidosJugando['count'] == 0:
            return False
        else:
            return partidosJugando

    def partidosEquipo(self, equipo):
        equipo=equipo.upper()
        partidosEquipo=self.session.query(Partido).filter(or_(Partido.equipoLocal.ilike('%'+equipo+'%'), Partido.equipoVisitante.ilike('%'+equipo+'%'))).all()
        if partidosEquipo is None:
            return False
        else:
            return partidosEquipo

    def tablaGoleadoresTemporada(self, temporada):
        if int(temporada) > 2016:
            connection.request('GET', '/v2/competitions/CL/scorers?season='+temporada, None, headers)
            goleadores = json.loads(connection.getresponse().read().decode())
            return goleadores
        else:
            return False

    def listaDeCampeones(self):
        campeones=self.session.query(Campeon).filter().all()
        return campeones

    def posicionesTemporada(self, temporada):
        posicionesDevolver=[]
        if int(temporada) > 2016:
            connection.request('GET', '/v2/competitions/CL/standings?season='+temporada, None, headers)
            posiciones = json.loads(connection.getresponse().read().decode())
            posiciones=posiciones['standings']
            if posiciones==[]:
                return False
            else:
                for p in posiciones:
                    if p['type']=='TOTAL':
                        posicionesDevolver.append(p)
                return posicionesDevolver
        else:
            return False

    def partidosEntreEquipos(self, equipo1, equipo2):
        partidos=self.session.query(Partido).filter(or_(and_(Partido.equipoLocal.ilike('%'+equipo1+'%'), Partido.equipoVisitante.ilike('%'+equipo2+'%')),and_(Partido.equipoLocal.ilike('%'+equipo2+'%'), Partido.equipoVisitante.ilike('%'+equipo1+'%')))).all()
        if partidos == []:
            return False
        else:
            return partidos
