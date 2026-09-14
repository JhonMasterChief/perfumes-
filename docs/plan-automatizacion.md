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
- **El repo ya está conectado a Vercel: un `git push` a `main` = deploy automático a producción.** Confirmar con el usuario ANTES de cada `git push` a este repo (ya no después) — no hay un paso de deploy separado que confirmar. Crear/borrar un proyecto de Vercel o aprovisionar Supabase también requiere confirmación explícita — son acciones sobre cuentas reales, no gratis de deshacer.
- **Nunca** cambiar paleta, tipografía o tono de marca sin que el usuario lo pida expresamente.

## Estado verificado del entorno (actualizado 13/09/2026, misma noche)
- El repo de GitHub **`JhonMasterChief/perfumes-`** (privado) ya tiene el contenido de la landing (`index.html`, `docs/`, `assets/`, favicon, robots.txt, sitemap.xml) — poblado y con push hecho.
- Vercel: proyecto **`bakhoor`** creado bajo `jhonmasterchiefs-projects`, **conectado directo al repo de GitHub** (`vercel link` lo detectó y conectó solo). Ya está desplegado y en vivo: **https://bakhoor-ruby.vercel.app**
- **Importante — esto cambia el guardrail de despliegue:** al estar conectado el repo a Vercel, **cualquier `git push` a `main` dispara un deploy automático a producción**. Ya no hay un paso separado de "confirmar el deploy" — el punto de confirmación ahora es **antes del `git push`**, no después.
- `gh` (GitHub CLI) sigue sin estar instalado — el push se hizo por HTTPS con las credenciales de git ya cacheadas en esta máquina, sin necesitarlo.
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
1. [x] Username de GitHub confirmado: `JhonMasterChief`. Repo privado ya existente: `perfumes-`.
2. [x] Repo poblado (`index.html`, `docs/`, `assets/`, favicon, robots.txt, sitemap.xml) + push a `main`.
3. [x] Proyecto Vercel `bakhoor` creado y conectado al repo — **en vivo:** https://bakhoor-ruby.vercel.app
4. [x] Rediseño de la landing (hero asimétrico con medallón geométrico, sección de historia, tarjetas estilo catálogo) — ver detalle en `seo_y_arquitectura.md`.
5. [ ] (Cuando haga falta) Aprovisionar Supabase vía Vercel Marketplace para catálogo/leads.
6. [ ] Confirmar número de WhatsApp real y actualizarlo en `index.html` (sigue siendo el de la factura de Shoppex).
7. [ ] Sumar fotos reales de producto en cuanto lleguen.
8. [ ] Dominio propio (opcional) — hoy vive en `bakhoor-ruby.vercel.app`, el `canonical`/`og:image` del HTML todavía apuntan al placeholder `bakhoor.ve`.
