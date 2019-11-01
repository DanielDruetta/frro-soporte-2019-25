from flask import Flask, request, render_template
from CapaNegocio import NegocioChampions

app=Flask(__name__)

@app.route('/')
def index():
    try:
        partidos=NegocioChampions().partidosPorJugarse()
        return render_template('index.html', partidos=partidos)
    except:
        return render_template('index.html')

@app.route('/partidosDeHoy')
def partidosDeHoy():
    try:
        partidos=NegocioChampions().obtenerPartidosDeHoy()
        return render_template('partidosDeHoy.html', partidos=partidos)
    except:
        return render_template('partidosDeHoy2.html')

@app.route('/resultadosEnVivo')
def resultadosEnVivo():
    try:
        partidos=NegocioChampions().partidosQueSeEstanJugando()
        return render_template('enVivo.html', partidos=partidos)
    except:
        return render_template('enVivo2.html')

@app.route('/partidosEquipo', methods=['GET'])
def partidosEquipo():
    try:
        equipo=request.args.get("equipo")
        partidos=NegocioChampions().partidosEquipo(equipo)
        return render_template('partidosEquipo.html', partidos=partidos)
    except:
        return render_template('partidosEquipo2.html')

@app.route('/partidosRondaTemporada', methods = ['GET'])
def partidosPorFase():
    try:
        temporada=request.args.get("temporada")
        ronda=request.args.get("ronda")
        ronda=ronda.upper()
        if ronda == 'RONDA1':
            partidos=NegocioChampions().obtenerPartidosRonda1(temporada)
        elif ronda == "RONDA2":
            partidos=NegocioChampions().obtenerPartidosRonda2(temporada)
        elif ronda == "RONDA2":
            partidos=NegocioChampions().obtenerPartidosRonda2(temporada)
        elif ronda == "RONDA3":
            partidos=NegocioChampions().obtenerPartidosRonda3(temporada)
        elif ronda == "PLAY-OFFS":
            partidos=NegocioChampions().obtenerPartidosPlayOffs(temporada)
        elif ronda == "FASE DE GRUPOS":
            partidos=NegocioChampions().obtenerPartidosFaseDeGrupos(temporada)
        elif ronda == "OCTAVOS":
            partidos=NegocioChampions().obtenerPartidosOctavos(temporada)
        elif ronda == "CUARTOS":
            partidos=NegocioChampions().obtenerPartidosCuartos(temporada)
        elif ronda == "SEMIFINAL":
            partidos=NegocioChampions().obtenerPartidosSemi(temporada)
        elif ronda == "FINAL":
            partidos=NegocioChampions().obtenerPartidoFinal(temporada)
        return render_template('partidosRondaTemporada.html', partidos=partidos)
    except:
        return render_template('partidosRondaTemporada2.html')

@app.route('/goleadores', methods=['GET'])
def goleadores():
    try:
        temporada=request.args.get("temporada")
        goleadores=NegocioChampions().tablaGoleadoresTemporada(temporada)
        return render_template('goleadores.html', goleadores=goleadores)
    except:
        return render_template('goleadores2.html')

@app.route('/campeones')
def campeones():
    try:
        campeones=NegocioChampions().listaDeCampeones()
        return render_template('campeones.html', campeones=campeones)
    except:
        return render_template('campeones.html')

@app.route('/posicionesGrupos', methods=['GET'])
def posicionesTemporada():
    try:
        temporada=request.args.get("temporada")
        posiciones=NegocioChampions().posicionesTemporada(temporada)
        return render_template('posiciones.html', grupoA=posiciones['A'], grupoB=posiciones['B'], grupoC=posiciones['C'], grupoD=posiciones['D'], grupoE=posiciones['E'], grupoF=posiciones['F'], grupoG=posiciones['G'], grupoH=posiciones['H'])
    except:
        return render_template('posiciones2.html')

@app.route('/fotos')
def fotos():
    return render_template('fotos.html')

@app.route('/enfrentamientos', methods=['GET'])
def enfrentamientos():
    if (request.args.get("equipo1") is None and request.args.get("equipo2") is None) or (request.args.get("equipo1") == '' and request.args.get("equipo2") == ''):
        return render_template('enfrentamientos2.html')
    else:
        try:
            equipo1 = request.args.get("equipo1")
            equipo2 = request.args.get("equipo2")
            enfrentamientos = NegocioChampions().diferenciaPartidosEquipos(equipo1, equipo2)
            return render_template('enfrentamientos.html', enfrentamientos=enfrentamientos)
        except:
            return render_template('enfrentamientos3.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

