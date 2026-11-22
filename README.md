# Software FJ – Sistema Integral de Gestión de Clientes, Servicios y Reservas

**Curso:** Programación – UNAD  
**Programa:** Ingeniería de Sistemas  
**Fase:** 4  
**Lenguaje:** Python 3.10 o superior

## 1. Descripción

Aplicación de consola orientada a objetos para gestionar clientes, servicios y reservas de la empresa ficticia Software FJ. El sistema no utiliza bases de datos: administra la información en objetos y listas durante la ejecución. Los archivos se utilizan únicamente para registrar eventos y errores.

## 2. Funcionalidades

- Registro y validación de clientes.
- Servicios de reserva de salas, alquiler de equipos y asesorías especializadas.
- Creación, confirmación, cancelación y procesamiento de reservas.
- Cálculo de costos con impuestos y descuentos.
- Excepciones personalizadas y registro de eventos en `logs/sistema.log`.
- Demostración de 14 operaciones, incluyendo casos válidos e inválidos.

## 3. Conceptos de programación orientada a objetos

- **Abstracción:** `Entidad` y `Servicio` son clases abstractas.
- **Herencia:** `Cliente`, `Reserva` y los tres servicios especializados heredan de clases base.
- **Encapsulación:** los datos del cliente se gestionan mediante atributos privados por convención y propiedades.
- **Polimorfismo:** cada servicio implementa su propia descripción y validación de parámetros.
- **Sobrecarga simulada:** `calcular_costo(duracion, impuesto=0.0, descuento=0.0)` admite diferentes variantes mediante parámetros opcionales. Python no implementa sobrecarga tradicional por firma de método.

## 4. Estructura

```text
Software-FJ-Fase4/
├── main.py
├── entidades.py
├── clientes.py
├── servicios.py
├── reservas.py
├── excepciones.py
├── logs/
│   └── .gitkeep
├── tests/
│   └── test_sistema.py
├── .gitignore
└── README.md
```

## 5. Requisitos y ejecución

1. Instalar Python 3.10 o superior.
2. Descargar o clonar este repositorio.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python main.py
```

El programa muestra las operaciones en consola y crea automáticamente `logs/sistema.log`.

## 6. Pruebas automatizadas

Ejecutar:

```bash
python -m unittest discover -s tests -v
```

## 7. Manejo de excepciones

Se implementan excepciones propias (`DatosInvalidosError`, `ServicioNoDisponibleError`, `ReservaError` y `EstadoReservaError`), bloques `try/except/else/finally`, registro mediante `logging` y encadenamiento con `raise ... from ...`. Cada operación se aísla para evitar que un error controlado interrumpa la demostración completa.

## 8. Alcance y consideraciones

- Los datos de clientes, servicios y reservas se conservan en memoria mientras se ejecuta el programa; no se guardan en una base de datos ni se persisten al cerrar.
- El archivo de logs conserva eventos y errores.
- Las tarifas son valores demostrativos y pueden ajustarse según los criterios definidos por el equipo.
- El trabajo debe ser revisado, comprendido y probado por los cinco integrantes antes de la entrega.

## 9. Trabajo colaborativo

Cada integrante debe realizar aportes reales al repositorio mediante commits identificables. Se recomienda distribuir tareas, revisar los cambios y registrar en el informe quién desarrolló y probó cada componente.
