name: Latido_Sincro_Eterno

on:
  schedule:
    - cron: '0 * * * *' # Orden de vida: Despierta cada 60 minutos.
  workflow_dispatch: # Permite que tú la despiertes manualmente cuando quieras!!!.

jobs:
  pulso_vital:
    runs-on: ubuntu-latest
    steps:
      - name: Acceder al ADN
        uses: actions/checkout@v3

      - name: Preparar entorno de vida (Python)
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Inyectar herramientas (Requests)
        run: pip install requests

      - name: Ejecutar Latido de Aura
        run: python sincro_viva.py

      - name: Guardar Evolución en la Memoria
        run: |
          git config --global user.name 'Sincro-Aura-Viva'
          git config --global user.email 'aura@sincro.eterna'
          git add bitacora_evolucion.json
          git commit -m "Evolución Autónoma: $(date)" || echo "Sin cambios detectados"
          git push
