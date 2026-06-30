# Curso de Python: Proyecto Integrador Final

Este repositorio contiene los desarrollos, desafíos y la entrega final oficial realizada durante el curso de Python. El proyecto consiste en un sistema interactivo completo respaldado por una base de datos relacional local.

## 📌 Estado del Proyecto
* **Pre-entrega:** 🟢 Completada y Aprobada
* **Entrega Final:** 🟢 Completada y Funcional (Versión Final)

---

## 🚀 Proyecto Final: Sistema de Gestión de Inventario con SQLite

### 📋 Descripción
Es una aplicación de línea de comandos (CLI) de nivel profesional diseñada para administrar el inventario de productos de un comercio o almacén. El sistema permite realizar el ciclo completo de gestión de datos (**CRUD**: Crear, Leer, Actualizar y Borrar) de forma persistente, garantizando la seguridad, estabilidad e integridad de la información mediante una base de datos relacional local.

### 🛠️ Características Técnicas y Funcionalidades
1. **Persistencia de Datos Eficiente:** Inicialización automática y modular de una base de datos SQLite (`inventario.db`) para asegurar que los datos no se pierdan al cerrar la aplicación.
2. **Ciclo CRUD Completo:**
   * **Registrar Producto:** Inserción segura con parámetros protegidos contra vulnerabilidades de inyección SQL.
   * **Visualización Avanzada:** Formateo y alineación de registros en forma de tabla limpia y legible directamente en la consola.
   * **Actualización Inteligente:** Permite modificar campos específicos de un producto por ID, conservando los valores existentes de forma automática si el usuario deja el campo en blanco.
   * **Eliminación con Confirmación:** Mecanismo de seguridad que solicita confirmación (`s/n`) previa antes de remover definitivamente un registro.
3. **Módulo de Consultas y Búsquedas:** Filtros dinámicos mediante operadores de coincidencia (`LIKE`) que permiten buscar productos de forma exacta o parcial por ID, Nombre o Categoría.
4. **Módulo de Reportes Críticos:** Generación de alertas en tiempo real para la toma de decisiones, listando productos con stock igual o inferior al umbral de alerta definido por el usuario.
5. **Experiencia de Usuario (UX) en Consola:** Integración de la librería `colorama` para codificación de colores según el contexto de la aplicación (Éxito en verde, Alertas informativas en amarillo, Errores/Salidas en rojo).

### 🗄️ Modelo de Datos (Esquema de Tabla)
El sistema gestiona una tabla relacional llamada `productos` con la siguiente estructura:
* `id`: Clave primaria autoincremental (`INTEGER PRIMARY KEY AUTOINCREMENT`)
* `nombre`: Nombre comercial del artículo (`TEXT NOT NULL`)
* `descripcion`: Detalles o especificaciones adicionales (`TEXT`)
* `cantidad`: Existencias físicas en stock (`INTEGER NOT NULL`)
* `precio`: Valor monetario unitario (`REAL NOT NULL`)
* `categoria`: Clasificación o rubro del producto (`TEXT`)

### 📦 Requisitos e Instalación
Para ejecutar este proyecto de forma local, clona el repositorio e instala la dependencia de interfaz visual:

```bash
# Instalar la librería requerida para los colores en consola
py -m pip install colorama
