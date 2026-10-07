# Contrato propuesto: evidencia pública

Propuesta conceptual V1 para Careertrackly. Versión de documento `0.1`; no es una API implementada ni un formato de exportación ya disponible.

[JSON Schema](../schemas/public-evidence.schema.json) · [Ejemplo ficticio](../examples/public-evidence.json)

## Modelo

Perfil → proyectos con contexto → evidencias con fuente y habilidades. El manifiesto limita campos a una selección deliberadamente pública. No admite campos de contacto ni evidencia marcada como privada. `verification: author_provided` expresa una afirmación del autor; `third_party_verified` requiere una revisión real fuera del schema y no puede inferirse por formato.

Las URLs requieren HTTPS y deben revisarse antes de compartirlas. `example.com` en el ejemplo es un dominio reservado para documentación; no es una prueba de trabajo real ni un destino que deba consultarse para validar el ejemplo.

## Validación local

Python 3.10+ y entorno virtual recomendado:

```sh
python -m venv .venv
# Activar el entorno según el sistema operativo.
python -m pip install -r requirements-validation.txt
python -m unittest discover -s tests -v
```

Las pruebas verifican Draft 2020-12, ejemplo válido, rechazo de evidencia privada, campos no previstos, URI inválida, contexto incompleto y habilidades duplicadas. CI ejecuta esas mismas pruebas además del checker de documentos.

## Límites y decisiones pendientes

- El schema comprueba estructura y formatos; no visita URLs ni verifica autoría, contenido o calidad.
- Un enlace público puede conducir a información sensible. La ausencia de campos privados no garantiza ausencia de datos privados en textos o fuentes.
- Unicidad global de IDs, revisión de afirmaciones, permisos para publicar, revocación y versiones requieren reglas de aplicación todavía por definir.
- Este ejemplo no contiene CV, certificados ni información de ninguna persona real.

[Contexto del producto](overview.md) · [Hoja de ruta](roadmap.md)
