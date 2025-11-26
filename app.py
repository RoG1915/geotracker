"""
GeoTracker - Sistema de Geolocalización con Mapa Interactivo
Versión sin pandas - Compatible con Python 3.13
"""

from flask import Flask, render_template, request, jsonify
import openpyxl
import os
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Crear carpeta de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def parse_coordinates(coord_string):
    """
    Parsea diferentes formatos de coordenadas:
    - "-6.7749, -79.8408"
    - "-6.7749,-79.8408"
    - "-6.7749 -79.8408"
    """
    if coord_string is None:
        return None, None
    
    coord_string = str(coord_string).strip()
    
    # Intentar formato decimal simple (lat, lon)
    decimal_pattern = r'(-?\d+\.?\d*)[,\s]+(-?\d+\.?\d*)'
    match = re.search(decimal_pattern, coord_string)
    
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))
        return lat, lon
    
    return None, None

def process_excel(file_path):
    """Procesa el archivo Excel y extrae las ubicaciones usando openpyxl"""
    try:
        # Cargar el archivo Excel
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        
        # Obtener encabezados (primera fila)
        headers = []
        for cell in sheet[1]:
            if cell.value:
                headers.append(str(cell.value).strip().lower())
            else:
                headers.append('')
        
        # Buscar columnas de descripción y coordenadas
        desc_col = None
        coord_col = None
        
        for idx, header in enumerate(headers):
            if 'desc' in header or 'nombre' in header or 'lugar' in header:
                desc_col = idx
            if 'coord' in header or 'latitud' in header or 'gps' in header:
                coord_col = idx
        
        # Si no encuentra, usar las dos primeras columnas
        if desc_col is None:
            desc_col = 0
        if coord_col is None:
            coord_col = 1 if len(headers) > 1 else 0
        
        locations = []
        
        # Iterar filas (desde la 2 para saltar encabezados)
        for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
            if row and len(row) > max(desc_col, coord_col):
                descripcion = str(row[desc_col]).strip() if row[desc_col] else "Sin descripción"
                coord_raw = row[coord_col]
                
                lat, lon = parse_coordinates(coord_raw)
                
                if lat is not None and lon is not None:
                    locations.append({
                        'descripcion': descripcion,
                        'lat': lat,
                        'lon': lon,
                        'coordenadas_raw': str(coord_raw)
                    })
        
        workbook.close()
        return locations, None
    
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    """Página principal con el mapa"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint para subir el archivo Excel"""
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró archivo'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó archivo'}), 400
    
    if not file.filename.endswith(('.xlsx', '.xls')):
        return jsonify({'error': 'El archivo debe ser Excel (.xlsx o .xls)'}), 400
    
    # Guardar archivo
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_locations.xlsx')
    file.save(filepath)
    
    # Procesar archivo
    locations, error = process_excel(filepath)
    
    # Limpiar archivo temporal
    try:
        os.remove(filepath)
    except:
        pass
    
    if error:
        return jsonify({'error': f'Error procesando archivo: {error}'}), 400
    
    if not locations:
        return jsonify({'error': 'No se encontraron ubicaciones válidas en el archivo'}), 400
    
    return jsonify({
        'success': True,
        'locations': locations,
        'count': len(locations)
    })

@app.route('/demo')
def demo_data():
    """Devuelve datos de demostración para Chongoyape"""
    demo_locations = [
        {
            'descripcion': 'Mi Casa - Chongoyape',
            'lat': -6.6414,
            'lon': -79.3894,
            'coordenadas_raw': '-6.6414, -79.3894'
        },
        {
            'descripcion': 'IESTP Chongoyape',
            'lat': -6.6389,
            'lon': -79.3867,
            'coordenadas_raw': '-6.6389, -79.3867'
        },
        {
            'descripcion': 'Plaza de Armas Chongoyape',
            'lat': -6.6397,
            'lon': -79.3881,
            'coordenadas_raw': '-6.6397, -79.3881'
        },
        {
            'descripcion': 'Reservorio de Tinajones',
            'lat': -6.6833,
            'lon': -79.4167,
            'coordenadas_raw': '-6.6833, -79.4167'
        },
        {
            'descripcion': 'Casa de mi Amigo',
            'lat': -6.6420,
            'lon': -79.3850,
            'coordenadas_raw': '-6.6420, -79.3850'
        }
    ]
    return jsonify({
        'success': True,
        'locations': demo_locations,
        'count': len(demo_locations)
    })

# Para desarrollo local
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
