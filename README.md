# 🌍 GeoTracker - Sistema de Geolocalización

Sistema de geolocalización que permite subir archivos Excel con ubicaciones y visualizarlas en un mapa interactivo estilo Google Earth.

---

## 📋 ÍNDICE

1. [Instalación Local](#-instalación-local-paso-a-paso)
2. [Subir a GitHub](#-subir-a-github)
3. [Desplegar en Render (Gratis)](#-desplegar-en-render-gratis)
4. [Formato del Excel](#-formato-del-archivo-excel)
5. [Uso de la Aplicación](#-uso-de-la-aplicación)

---

## 💻 INSTALACIÓN LOCAL (Paso a Paso)

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para control de versiones)

### Paso 1: Verificar Python
Abre una terminal (CMD en Windows) y ejecuta:
```bash
python --version
```

Si no tienes Python, descárgalo de: https://www.python.org/downloads/

**⚠️ IMPORTANTE para Windows:** Durante la instalación marca la opción "Add Python to PATH"

### Paso 2: Descargar el Proyecto
Descarga y descomprime el archivo ZIP en una carpeta, por ejemplo:
- Windows: `C:\Proyectos\geolocalizacion`
- Linux/Mac: `~/proyectos/geolocalizacion`

### Paso 3: Abrir Terminal en la Carpeta
**Windows (CMD):**
```bash
cd C:\Proyectos\geolocalizacion
```

**Windows (PowerShell):**
```powershell
cd C:\Proyectos\geolocalizacion
```

**Linux/Mac:**
```bash
cd ~/proyectos/geolocalizacion
```

### Paso 4: Crear Entorno Virtual
```bash
python -m venv venv
```

### Paso 5: Activar Entorno Virtual

**Windows CMD:**
```bash
venv\Scripts\activate.bat
```

**Windows PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

Verás que aparece `(venv)` al inicio de tu línea de comandos.

### Paso 6: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 7: Ejecutar la Aplicación
```bash
python app.py
```

Verás un mensaje similar a:
```
 * Running on http://127.0.0.1:5000
```

### Paso 8: Abrir en el Navegador
Abre tu navegador y visita: **http://localhost:5000**

### Paso 9: Detener la Aplicación
Presiona `Ctrl + C` en la terminal.

---

## 📤 SUBIR A GITHUB

### Paso 1: Crear Cuenta en GitHub
1. Ve a https://github.com
2. Crea una cuenta si no tienes una
3. Verifica tu correo electrónico

### Paso 2: Instalar Git
Descarga Git de: https://git-scm.com/downloads

### Paso 3: Configurar Git (solo la primera vez)
Abre una terminal y ejecuta:
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

### Paso 4: Crear Repositorio en GitHub
1. Inicia sesión en GitHub
2. Haz clic en el botón verde **"New"** o **"+"** → **"New repository"**
3. Nombre del repositorio: `geotracker`
4. Descripción: `Sistema de geolocalización con mapa interactivo`
5. Selecciona **"Public"**
6. **NO** marques "Add a README file"
7. Haz clic en **"Create repository"**

### Paso 5: Subir el Código
Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
# Inicializar repositorio Git
git init

# Agregar todos los archivos
git add .

# Crear primer commit
git commit -m "Primer commit - GeoTracker"

# Conectar con GitHub (reemplaza TU-USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU-USUARIO/geotracker.git

# Subir el código
git branch -M main
git push -u origin main
```

Te pedirá tu usuario y contraseña de GitHub (o token de acceso personal).

### Crear Token de Acceso Personal (si te lo pide)
1. Ve a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Genera un nuevo token con permisos de "repo"
3. Usa ese token como contraseña

---

## 🚀 DESPLEGAR EN RENDER (Gratis)

Render es una plataforma que te permite hospedar tu aplicación gratis.

### Paso 1: Crear Cuenta en Render
1. Ve a https://render.com
2. Crea una cuenta (puedes usar tu cuenta de GitHub)

### Paso 2: Crear Nuevo Web Service
1. En el Dashboard, haz clic en **"New +"** → **"Web Service"**
2. Selecciona **"Build and deploy from a Git repository"**
3. Conecta tu cuenta de GitHub si no lo has hecho
4. Busca y selecciona tu repositorio `geotracker`

### Paso 3: Configurar el Servicio
Completa los campos así:

| Campo | Valor |
|-------|-------|
| **Name** | `geotracker` |
| **Region** | `Oregon (US West)` o el más cercano |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | `Free` |

### Paso 4: Desplegar
1. Haz clic en **"Create Web Service"**
2. Espera unos minutos mientras se construye
3. Cuando termine, verás una URL como: `https://geotracker-xxxx.onrender.com`

### ¡Listo! 🎉
Tu aplicación estará disponible en esa URL para que cualquier persona la use.

**Nota:** En el plan gratuito, la aplicación se "duerme" después de 15 minutos de inactividad. La primera visita después de dormir tarda unos 30 segundos en cargar.

---

## 📊 FORMATO DEL ARCHIVO EXCEL

Tu archivo Excel debe tener esta estructura:

| descripcion | coordenadas |
|-------------|-------------|
| Mi Casa | -6.6414, -79.3894 |
| Instituto IESTP | -6.6389, -79.3867 |
| Casa de mi friend | -6.6420, -79.3850 |
| Plaza de Armas | -6.6397, -79.3881 |

### Formatos de Coordenadas Aceptados
```
-6.6414, -79.3894    ✅ (con coma y espacio)
-6.6414,-79.3894     ✅ (solo coma)
-6.6414 -79.3894     ✅ (solo espacio)
```

### Cómo Obtener Coordenadas

**Desde Google Maps (PC):**
1. Abre Google Maps
2. Haz clic derecho en la ubicación
3. Copia las coordenadas que aparecen

**Desde Google Maps (Celular):**
1. Abre Google Maps
2. Mantén presionado en la ubicación
3. Las coordenadas aparecen en la barra de búsqueda

---

## 🎮 USO DE LA APLICACIÓN

### Funciones Principales

| Botón | Función |
|-------|---------|
| 📁 Área de carga | Arrastra tu Excel aquí o haz clic para seleccionar |
| 🚀 Demo | Carga datos de ejemplo de Chongoyape |
| 🛰️ Satélite | Vista aérea estilo Google Earth |
| 🗺️ Calles | Mapa tradicional con nombres |
| ⛰️ Terreno | Vista con relieve topográfico |
| 🎯 Centrar | Ajusta el zoom para ver todas las ubicaciones |

### Navegación
- **Zoom:** Rueda del mouse o botones +/-
- **Mover:** Arrastra el mapa
- **Ver ubicación:** Haz clic en una tarjeta de la lista izquierda
- **Ver detalles:** Haz clic en un marcador del mapa

---

## 🛠️ SOLUCIÓN DE PROBLEMAS

### Error: "python no se reconoce como comando"
- Reinstala Python marcando "Add Python to PATH"
- O usa `python3` en lugar de `python`

### Error: "pip no se reconoce"
```bash
python -m pip install -r requirements.txt
```

### Error al activar entorno virtual en PowerShell
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### La página no carga después de subir Excel
- Verifica que el Excel tenga las columnas correctas
- Revisa que las coordenadas estén en formato decimal

---

## 📝 ESTRUCTURA DEL PROYECTO

```
geotracker/
├── app.py                 # Servidor Flask principal
├── requirements.txt       # Dependencias Python
├── Procfile              # Configuración para Render
├── .gitignore            # Archivos ignorados por Git
├── README.md             # Este archivo
├── templates/
│   └── index.html        # Interfaz web con mapa
└── uploads/              # Carpeta temporal para Excel
    └── .gitkeep
```

---

## 🤝 CRÉDITOS

- **Mapas:** Leaflet.js + Esri World Imagery
- **Backend:** Flask (Python)
- **Procesamiento Excel:** Pandas + OpenPyXL

---

Desarrollado con ❤️ por Roger - IESTP Chongoyape
