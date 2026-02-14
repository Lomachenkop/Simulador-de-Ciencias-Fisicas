import streamlit as st
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Simulador Física", layout="wide")

st.title("🎢 Simulador de Física: Movimiento y Vectores")
st.markdown("Basado en la secuencia didáctica de Conceptos del Movimiento.")

# Selección de actividad
actividad = st.sidebar.selectbox(
    "Selecciona la Actividad",
    ["Actividad 2: Rosario", "Actividad 3 y 4: Recorrido A-B-FIN"]
)

if actividad == "Actividad 2: Rosario":
    st.header("🚶 Actividad 2: El camino de Rosario")
    st.write("Rosario camina 500 m desde el colmado hasta su casa[cite: 182].")
    
    # Sistema de Coordenadas (SC) [cite: 211]
    direccion = st.selectbox("Sentido del movimiento:", ["Norte", "Sur", "Este", "Oeste"])
    
    x_f, y_f = 0, 0
    if direccion == "Norte": y_f = 500
    elif direccion == "Sur": y_f = -500
    elif direccion == "Este": x_f = 500
    elif direccion == "Oeste": x_f = -500

    fig = go.Figure()
    # Vector posición r (Naranja según el documento) [cite: 265]
    fig.add_annotation(x=x_f, y=y_f, ax=0, ay=0, xref="x", yref="y", axref="x", ayref="y",
                       showarrow=True, arrowhead=3, arrowcolor="orange", text="Vector r")
    
    fig.update_layout(xaxis_range=[-600, 600], yaxis_range=[-600, 600], title="SC: Origen en Colmado")
    st.plotly_chart(fig)
    
    st.info(f"Tiempo estimado: 500 segundos[cite: 199].")

elif actividad == "Actividad 3 y 4: Recorrido A-B-FIN":
    st.header("📍 Trayectoria y Desplazamiento")
    
    # Datos del problema [cite: 318]
    coords = {'INICIO': [0,0], 'A': [0,2.6], 'B': [4,2.6], 'FIN': [7.5, 6.5]}
    
    # Corregir índices para evitar el error de tu imagen
    x_tray = [coords['INICIO'][0], coords['A'][0], coords['B'][0], coords['FIN'][0]]
    y_tray = [coords['INICIO'][1], coords['A'][1], coords['B'][1], coords['FIN'][1]]
    
    fig = go.Figure()
    
    # Trayectoria (Azul) [cite: 273]
    fig.add_trace(go.Scatter(x=x_tray, y=y_tray, mode='lines+markers', name='Trayectoria (Δs)'))
    
    # Vectores rA y rB (Mismo color) [cite: 296, 317]
    for p in ['A', 'B']:
        fig.add_annotation(x=coords[p][0], y=coords[p][1], ax=0, ay=0, 
                           xref="x", yref="y", axref="x", ayref="y",
                           showarrow=True, arrowhead=2, arrowcolor="darkblue", text=f"r{p}")
    
    # Desplazamiento Total (Verde) [cite: 299]
    fig.add_annotation(x=coords['FIN'][0], y=coords['FIN'][1], ax=0, ay=0, 
                       xref="x", yref="y", axref="x", ayref="y",
                       showarrow=True, arrowhead=3, arrowcolor="green", text="Δr Total")
    
    st.plotly_chart(fig)
    
    dist_total = 2.6 + 4.0 + 5.2 # [cite: 318]
    st.success(f"Distancia Total (Δs): {dist_total} km. El desplazamiento (Δr) es el vector verde[cite: 318, 319].")