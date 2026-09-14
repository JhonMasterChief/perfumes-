# Bakhoor — Plan técnico y de automatización

Este documento es el contexto que debe leer cualquier automatización de Claude Code (la que el usuario ya configuró) antes de tocar la landing page o generar contenido nuevo de Bakhoor. Objetivo de la automatización: **mejorar la landing page y seguir generando contenido**, dentro del marco de marca ya definido — nunca "en el aire".

## Fuentes de verdad (leer siempre primero, en este orden)
1. `entregables/bakhoor/branding/identidad_marca.md` — paleta, tipografía, tono, reglas de la marca.
2. `entregables/bakhoor/catalogo/estrategia_precios.md` — catálogo de 28 referencias con precio vigente.
3. `entregables/bakhoor/plan-contenido/guia_contenido.md` — pilares de contenido y calendario.
4. `entregables/bakhoor/landing-page/index.html` + `seo_y_arquitectura.md` — estado actual de la landing.
5. `CLAUDE.md` (raíz del proyecto) — reglas generales del portafolio (El Códice / AutoVzla / Bakhoor).

## Guardrails — no negociables
- **Nunca** subir a un repo (público o privado) documentos con datos personales/financieros reales (facturas, números de teléfono personales, direcciones) — hoy no hay ninguno en esta carpeta, pero si en algún momento se guarda uno acá, debe ir al `.gitignore`.
- **Nunca** inventar fotos de producto — mientras no haya fotos reales de las botellas, la landing y los posts se quedan en texto/diseño (ver regla ya existente en `identidad_marca.md`).
- **Nunca** hacer `git push`, crear/borrar un proyecto de Vercel, o aprovisionar Supabase sin confirmación explícita del usuario en esa sesión — son acciones sobre cuentas reales, no gratis de deshacer.
- **Nunca** cambiar paleta, tipografía o tono de marca sin que el usuario lo pida expresamente.

## Estado verificado del entorno (13/09/2026)
- Esta carpeta **no es un repositorio git todavía**.
- `gh` (GitHub CLI) **no está instalado** en esta máquina.
- `vercel` CLI sí está instalado y con sesión iniciada como **`jhonmasterchief`** — 4 proyectos ya existentes en esa cuenta: `romary`, `vista-previa-vercel`, `landing-vita-frut`, `marketing-os`. Ninguno es de Bakhoor todavía.
- `supabase` CLI no está instalado (se puede usar sin CLI, vía integración de Vercel Marketplace).

## Stack objetivo

### 1. GitHub — control de versiones
Plan de ejecución:
1. `git init` local + `.gitignore` (node_modules, `.vercel`, cualquier documento personal/financiero).
2. Primer commit con el estado actual de `entregables/bakhoor/`, `assets/bakhoor/` y la skill.
3. Crear el repositorio remoto en GitHub con el usuario del usuario — **pendiente: username de GitHub y si el repo debe ser público o privado**.
4. `git remote add origin` + push.

`gh` no está instalado; alternativas: `winget install --id GitHub.cli` y autenticar con `gh auth login`, o crear el repo manualmente en github.com y conectar por HTTPS con un token.

### 2. Vercel — despliegue
Ya hay cuenta lista (`jhonmasterchief`). Crear un proyecto nuevo (ej. `bakhoor` o `bakhoor-landing`) y desplegar `entregables/bakhoor/landing-page/` con la skill `deploy` ya disponible en este entorno — mismo patrón que se usó para `vista-previa-vercel` (El Códice). Requiere confirmación del usuario antes de ejecutar el deploy real (no es destructivo, pero sí crea un recurso nuevo en su cuenta).

### 3. Supabase — para qué serviría (no es indispensable hoy)
La landing no necesita backend ahora mismo (cierre 100% por WhatsApp). Casos donde sí aportaría:
- Mover el catálogo (hoy en `estrategia_precios.md` y quemado en el HTML) a una tabla real — permite actualizar precio/stock sin tocar código.
- Un formulario "avísame cuando llegue" que guarde leads (nombre, ciudad, producto) para hacer seguimiento, más confiable que depender solo de WhatsApp suelto.

Se aprovisiona sin salir de la terminal usando la skill `marketplace` (integraciones de Vercel Marketplace) una vez exista el proyecto de Vercel — no hace falta instalar el CLI de Supabase por separado.

## Herramientas web externas — uso manual (no hay automatización de navegador en este entorno)
Ya se estableció con Google Flow que no hay capacidad de controlar un navegador desde aquí. El rol en estas herramientas es preparar el prompt/contexto exacto para que el usuario lo pegue manualmente:
- **Google Stitch** (labs.google — genera UI a partir de un prompt de texto): sirve para explorar variantes visuales de la landing más allá del HTML ya construido. Si se quiere, se prepara un prompt de diseño con la identidad de marca (paleta, tono, secciones) para pegar ahí.
- **Magnific** (upscaler/enhancer de imágenes con IA): útil en cuanto existan fotos reales de las botellas, para mejorar nitidez/resolución antes de publicarlas — nunca para generar una foto de producto que no existe.
- **Manus** (agente de IA autónomo de propósito general): útil para tareas de investigación más profundas que no dependen de este repo (ej. mapear competencia de perfumería árabe en Venezuela/Punto Fijo). Se prepara el brief de la tarea para que el usuario lo ejecute ahí.

## Ampliar agentes/skills de Claude Code
Ya hay agentes relevantes instalados en este entorno (`seo-specialist`, `ui-designer`, `content-marketer`, entre otros) — revisar si ya cubren la necesidad antes de instalar algo nuevo. Si hace falta algo puntual, usar el agente `agent-installer` (ya disponible) para buscarlo e instalarlo desde el repo público `awesome-claude-code-subagents`.

## Qué puede hacer la automatización sola vs. qué necesita del usuario

**Puede hacer sola** (con el contexto de este documento + `identidad_marca.md`):
- Iterar el HTML/CSS de la landing (nuevos destacados, ajustes de copy, mejoras de SEO on-page).
- Generar más contenido (posts/Reels) siguiendo `guia_contenido.md`.
- Actualizar `estrategia_precios.md` si llegan nuevos costos/inventario.

**Necesita al usuario cada vez:**
- Confirmar antes de `git push`, deploy a Vercel, o cualquier cambio de infraestructura real.
- Fotos reales de producto.
- Número de WhatsApp real (pendiente desde la sesión anterior — hoy la landing usa el número de la factura de Shoppex como placeholder).
- Username y visibilidad (público/privado) del repo de GitHub.

## Checklist de próximos pasos, en orden
1. [ ] Confirmar username de GitHub y visibilidad del repo (público/privado).
2. [ ] `git init` + `.gitignore` + primer commit.
3. [ ] Crear repo remoto en GitHub + push.
4. [ ] Crear proyecto Vercel para Bakhoor + desplegar la landing.
5. [ ] (Cuando haga falta) Aprovisionar Supabase vía Vercel Marketplace para catálogo/leads.
6. [ ] Confirmar número de WhatsApp real y actualizarlo en `index.html`.
7. [ ] Sumar fotos reales de producto en cuanto lleguen.
