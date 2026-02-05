import streamlit as st

st.title("🧬 Simulador de Estabilidad Térmica del ADN")
st.write("Calcula la energía necesaria para separar las hebras según su composición física.")

# Entrada de datos
secuencia = st.text_input("Introduce una secuencia de ADN (ej. ATGC):", "ATGC").upper()

# Lógica física básica: 
# Los pares G-C tienen 3 puentes de hidrógeno (más fuertes)
# Los pares A-T tienen 2 puentes de hidrógeno (más débiles)
n_at = secuencia.count('A') + secuencia.count('T')
n_gc = secuencia.count('G') + secuencia.count('C')

# Fórmula simplificada de Wallace para la temperatura de fusión (Tm)
tm = (2 * n_at) + (4 * n_gc)

# Interfaz interactiva
st.subheader("Resultados del Análisis:")
col1, col2 = st.columns(2)
col1.metric("Puentes de H (A-T)", f"{n_at * 2}")
col2.metric("Puentes de H (G-C)", f"{n_gc * 3}")

st.info(f"La temperatura estimada de separación es de: **{tm} °C**")

# Explicación pedagógica
st.write("---")
st.markdown("""
### ¿Qué estamos viendo desde la física?
* **Energía de Enlace:** El par G-C es más estable porque tiene más puentes de hidrógeno. 
* **Termodinámica:** A mayor temperatura, aumentamos la energía cinética de las moléculas hasta vencer la energía de enlace.
""")
st.balloons