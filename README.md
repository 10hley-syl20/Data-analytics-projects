# Data Science Portfolio

Soy Dishley, ingeniero industrial y trabajo como planificador de producción y
analista de datos en una embotelladora de Coca-Cola. Estoy haciendo una maestría
en Ciencia de Datos e IA. En el día a día uso datos para tomar decisiones:
pronósticos, tableros y automatización de reportes.

Aquí voy subiendo proyectos donde practico o aplico lo que voy aprendiendo.

## Proyectos

**pronostico-turistas-2026**
Pronóstico de cuántos turistas va a recibir República Dominicana por mes y por
nacionalidad para 2026, usando 4 años de datos del Ministerio de Turismo (132
países). Regresión con tendencia y estacionalidad sobre el total nacional,
probada contra un baseline naive (WAPE 5.4% vs. 4.5%) antes de confiar en el
R², y repartida por nacionalidad según la participación histórica de cada país.

**demand-forecasting**
Pronóstico de ventas semanales. Comparo dos modelos, Holt-Winters y una regresión,
y escojo el que mejor funciona en cada producto midiendo el error con WAPE. Es el
mismo enfoque que uso en el trabajo, aquí sobre datos públicos.

**insurance-cost-analysis**
Miro qué hace que suba el costo de un seguro médico usando un dataset público.
Lo interesante sale de una interacción bmi x smoker: el IMC casi no afecta el
costo en no fumadores, pero en fumadores cada punto de IMC agrega casi 100
veces más al costo. R² de 0.827.

**crime analysis**
Práctica de SQL. Cruzo datos de crimen, censo y escuelas de Chicago con joins y
subconsultas para responder algunas preguntas.

**stock-revenue-dashboard**
Saco el precio de la acción de Tesla y GameStop con yfinance y los ingresos con
web scraping, y armo un gráfico para comparar los dos.

**Hurricane analysis**
Análisis de huracanes del Atlántico con Python.

## Herramientas
Python (pandas, numpy, scikit-learn, statsmodels, matplotlib), SQL, Power BI y Excel.
