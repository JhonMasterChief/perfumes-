# Bakhoor — Landing page: SEO, frontend y backend

## Qué es esto
`entregables/bakhoor/landing-page/index.html` es una landing page **estática** (un solo archivo HTML con su CSS adentro, sin dependencias externas más que las fuentes de Google Fonts) — pensada como la página "de presentación" de la marca: la que pones en la bio de Instagram/Facebook o le mandas a alguien que pregunta "¿tienen página web?".

## Frontend
- Un solo archivo, responsive (se ve bien en celular y escritorio — probado en ambos tamaños).
- Paleta y tipografía tomadas de `entregables/bakhoor/branding/identidad_marca.md` — cualquier cambio de color/fuente de marca se hace ahí primero y se refleja aquí.
- Secciones: hero con CTA, marcas que se trabajan, cómo comprar (3 pasos), destacados (3 productos de ejemplo con precio ya sacado de `entregables/bakhoor/catalogo/estrategia_precios.md`), zonas de entrega (Caracas y Punto Fijo), CTA final, footer.
- El botón "Escríbenos por WhatsApp" es un link `https://wa.me/<numero>?text=...` — no hace falta backend ni formulario para que funcione: abre WhatsApp directo con un mensaje pre-escrito.

## Backend — no hay, y no hace falta uno todavía
Esta landing **no tiene backend** (no hay servidor, base de datos, ni carrito de compra) — la "conversión" completa pasa por WhatsApp, igual que toda la operación de AutoVzla. Esto es intencional para arrancar rápido: no hay nada que mantener, hostear con backend, ni que se pueda caer.

Si más adelante el negocio crece y se necesita algo más (formulario de pedido, catálogo con filtros, pasarela de pago), eso sí sería un proyecto de desarrollo aparte — avisar cuando se llegue a ese punto para dimensionarlo bien, no hace falta ahora.

## SEO ya aplicado
- `<title>` y `<meta name="description">` con las palabras clave reales del negocio (perfumes árabes, marcas, ciudades).
- Open Graph (`og:title`, `og:description`, `og:image`) para que se vea bien cuando se comparta el link en WhatsApp/Facebook/Instagram.
- Datos estructurados (`schema.org/Store`) con `areaServed` en Caracas y Punto Fijo — ayuda a que buscadores entiendan que el negocio sirve a esas dos ciudades específicamente.
- `rel="canonical"` ya está en el HTML, pero apunta a `https://bakhoor.ve/` como **placeholder** — no es un dominio real todavía. Hay que reemplazarlo por el dominio real en cuanto se compre uno (o quitarlo si la página solo va a vivir en Facebook/Instagram y no en un dominio propio).

## Pendiente para publicar esto de verdad
1. **Dominio real** (opcional): si se quiere una URL propia tipo `bakhoor.ve` o `bakhoor.com`, hay que comprarlo — no está incluido en este entregable. Sin dominio propio, esta misma página se puede publicar gratis en un subdominio (Vercel/Netlify), como se hizo con la vista previa de El Códice (`vista-previa-vercel.vercel.app`).
2. **Confirmar el número de WhatsApp** — ahora mismo el link usa el número de la factura de Shoppex como placeholder (ver `identidad_marca.md`).
3. **Reemplazar los 3 "destacados" de ejemplo** por los que el usuario quiera resaltar, y sumar fotos reales cuando estén disponibles.
4. **`og:image`** apunta a una ruta que no existe todavía (`/assets/bakhoor_logo.png`) — hay que subir el logo (`assets/bakhoor/logo/bakhoor_logo.png`) al hosting final con esa ruta, o ajustar la ruta según donde quede publicada la página.
