# -*- coding: utf-8 -*-
"""Genera catalogo.html + una pagina por producto (28) para la landing de Bakhoor.
Sin fotos reales todavia -> usa un placeholder de marca (bottle-icon + patron),
nunca una foto generica haciendose pasar por el producto real."""
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent  # raíz del repo (donde vive index.html)
PROD_DIR = OUT / "producto"
PROD_DIR.mkdir(parents=True, exist_ok=True)

WHATSAPP = "584141462030"

PRODUCTOS = [
    dict(marca="Afnan", nombre="9pm", tam="3.4oz EDP Hombre", precio=45, apodo="El nocturno intenso",
         notas="Oriental amaderado: canela y frutas rojas de salida, oud y vainilla de fondo."),
    dict(marca="Afnan", nombre="9am", tam="3.4oz EDP Mujer", precio=40, apodo="El fresco de día",
         notas="Floral afrutado: bergamota y pera, con un fondo cálido de sándalo."),
    dict(marca="Armaf", nombre="Club de Nuit Intense", tam="3.6oz EDT Hombre", precio=55, apodo="El clásico de la casa",
         notas="Afrutado-especiado: piña y manzana de salida, abedul ahumado de fondo."),
    dict(marca="Armaf", nombre="Club de Nuit", tam="3.6oz EDP Mujer", precio=50, apodo="Su versión femenina",
         notas="Floral-frutal con un fondo amaderado suave — la versión femenina de la línea insignia."),
    dict(marca="Armaf", nombre="Odyssey Mandarin Sky", tam="3.4oz EDP Hombre", precio=45, apodo="Cítrico y fresco",
         notas="Cítrico-amaderado: mandarina fresca con fondo de cedro y almizcle."),
    dict(marca="Armaf", nombre="Club de Nuit Iconic Blue", tam="3.6oz EDP Hombre", precio=65, apodo="El acuático",
         notas="Acuático-aromático: notas marinas frescas sobre un fondo amaderado limpio."),
    dict(marca="Armaf", nombre="Club de Nuit Untold", tam="3.6oz EDP Unisex", precio=70, apodo="El más intenso",
         notas="Especiado-ambarado — la versión más intensa y unisex de la familia Club de Nuit."),
    dict(marca="Armaf", nombre="Club de Nuit Extrait", tam="70ml Extrait de Parfum Mujer", precio=50, apodo="Máxima duración",
         notas="Concentración extrait de la línea Club de Nuit — mayor duración y proyección."),
    dict(marca="Armaf", nombre="Odyssey Mandarin Sky Elixir", tam="3.4oz EDP Hombre", precio=50, apodo="Versión concentrada",
         notas="La versión elixir del Mandarin Sky original: más concentrada e intensa."),
    dict(marca="Armaf", nombre="Club de Nuit Intense", tam="Set de viaje (mini + gel + body spray)", precio=70, apodo="Para llevar a todos lados",
         notas="El Club de Nuit Intense en formato de viaje completo."),
    dict(marca="Armaf", nombre="Odyssey Candee", tam="Set completo Mujer (EDT + loción + deo + shampoo)", precio=40, apodo="El dulce completo",
         notas="Gourmand dulce: notas de caramelo y frutas blancas, set de cuidado completo."),
    dict(marca="Fragaby", nombre="Fragaby 2", tam="100ml EDP", precio=40, apodo="El económico de firma",
         notas="Amaderado especiado de firma propia — alternativa económica de proyección duradera."),
    dict(marca="Armaf", nombre="Club de Nuit Intense Overdose", tam="3.4oz Extrait de Parfum", precio=85, apodo="El más fuerte de todos",
         notas="La versión más concentrada e intensa de toda la familia Club de Nuit."),
    dict(marca="Fragrance World", nombre="Liquid Brun", tam="100ml EDP (by French Avenue)", precio=60, apodo="Cuero y especias",
         notas="Amaderado oriental profundo, inspirado en las fragancias árabes clásicas de cuero y especias."),
    dict(marca="Fragrance World", nombre="Aether", tam="3.4oz EDP Unisex", precio=60, apodo="El unisex versátil",
         notas="Fresco-amaderado unisex, versátil para uso diario."),
    dict(marca="Lattafa", nombre="Pride King of Arabia", tam="3.4oz EDP Hombre", precio=45, apodo="Dulce y real",
         notas="Oriental dulce: azafrán y miel de salida, oud y ámbar de fondo."),
    dict(marca="Lattafa", nombre="Asad Elixir", tam="3.4oz EDP Unisex", precio=50, apodo="El Asad más intenso",
         notas="Versión concentrada del clásico Asad — más intensa y de mayor duración."),
    dict(marca="Lattafa", nombre="Badee Al Oud Noble Blush", tam="Set (100ml EDP + 200ml spray corporal)", precio=45, apodo="Floral con oud",
         notas="Floral afrutado con un fondo de oud, en formato perfume + spray corporal."),
    dict(marca="Lattafa", nombre="Yara Moi", tam="3.4oz EDP Unisex", precio=40, apodo="Yara, para todos",
         notas="Floral dulce: vainilla y frutas blancas — la versión unisex de Yara."),
    dict(marca="Lattafa", nombre="Khamrah Qahwa", tam="3.4oz EDP Unisex", precio=50, apodo="Notas de café",
         notas="Gourmand especiado: notas de café y canela sobre un fondo ambarado."),
    dict(marca="Lattafa", nombre="Badee Al Oud Noble Blush", tam="3.4oz EDP Mujer", precio=40, apodo="El floral con fondo de oud",
         notas="Floral afrutado con fondo de oud — la versión femenina de la línea."),
    dict(marca="Lattafa", nombre="Asad", tam="3.4oz EDP Hombre", precio=40, apodo="El más pedido de Lattafa",
         notas="Amaderado especiado clásico — el Lattafa para hombre que más se repite en los pedidos."),
    dict(marca="Lattafa", nombre="Yara", tam="Set (100ml EDP + 200ml spray corporal)", precio=45, apodo="El floral best-seller",
         notas="El floral más vendido de Lattafa, en formato perfume + spray corporal."),
    dict(marca="Maison Alhambra", nombre="Philos Centro", tam="3.4oz EDP Unisex", precio=20, apodo="El ligero de diario",
         notas="Fresco cítrico-amaderado, ligero y versátil para uso diario."),
    dict(marca="Rasasi", nombre="Shuhrah", tam="3.0oz EDP Mujer", precio=25, apodo="Suave y floral",
         notas="Floral afrutado suave, ideal para el día."),
    dict(marca="Rasasi", nombre="Shuhrah", tam="3.0oz EDP Hombre", precio=30, apodo="Fresco y amaderado",
         notas="Amaderado fresco — la versión masculina de Shuhrah."),
    dict(marca="Rasasi", nombre="Hawas", tam="3.4oz EDP Hombre", precio=55, apodo="El favorito clásico",
         notas="Amaderado-acuático: manzana y bergamota de salida, ámbar y almizcle de fondo."),
    dict(marca="Rasasi", nombre="Hawas Diva", tam="3.4oz EDP Mujer", precio=60, apodo="Su versión femenina",
         notas="Floral oriental intenso — la versión femenina de Hawas, con más dulzura."),
]

def slugify(s):
    s = s.lower()
    s = (s.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u"))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

for i, p in enumerate(PRODUCTOS, start=1):
    p["num"] = i
    p["slug"] = slugify(f"{p['marca']}-{p['nombre']}-{i}")

CSS_COMUN = """
:root {
  --bkh-negro: #0B0B0D; --bkh-negro-2: #151217;
  --bkh-oro: #C9A24B; --bkh-oro-claro: #E7C874;
  --bkh-burdeos: #6B1E2B; --bkh-crema: #F5EDE0; --bkh-texto-suave: #4a4640;
}
* { box-sizing: border-box; -webkit-font-smoothing: antialiased; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bkh-crema); color: var(--bkh-negro); font-family: 'Inter', sans-serif; line-height: 1.5; }
h1, h2, h3 { font-family: 'Playfair Display', serif; font-weight: 600; margin: 0; }
a { color: inherit; }
.wrap { max-width: 1120px; margin: 0 auto; padding: 0 28px; }
header { position: sticky; top: 0; z-index: 20; background: var(--bkh-negro); border-bottom: 1px solid rgba(201,162,75,.25); }
header .wrap { display: flex; align-items: center; justify-content: space-between; padding: 14px 28px; gap: 12px; flex-wrap: wrap; }
.brand { display: flex; align-items: center; gap: 10px; }
.brand img { width: 34px; height: 34px; border-radius: 50%; display: block; }
.brand .marca { color: var(--bkh-oro-claro); font-family: 'Playfair Display', serif; font-size: 21px; letter-spacing: .05em; }
nav { display: flex; gap: 26px; }
nav a { color: var(--bkh-crema); text-decoration: none; font-size: 14px; font-weight: 500; }
nav a:hover { color: var(--bkh-oro-claro); }
.btn-wsp { background: var(--bkh-oro); color: var(--bkh-negro); padding: 10px 22px; border-radius: 2px; font-weight: 700; font-size: 14px; text-decoration: none; display: inline-block; white-space: nowrap; }
.btn-wsp:hover { background: var(--bkh-oro-claro); }
footer { background: var(--bkh-negro); color: rgba(245,237,224,.55); padding: 26px 0; font-size: 13px; }
footer .wrap { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
footer a { color: var(--bkh-oro); text-decoration: none; }
@media (max-width: 760px) { nav { display: none; } .btn-wsp { padding: 9px 16px; font-size: 13px; } footer .wrap { flex-direction: column; text-align: center; } }
"""

HEAD_COMUN = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" sizes="32x32" href="{base}favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="{base}apple-touch-icon.png">
<meta name="theme-color" content="#0B0B0D">"""

HEADER_HTML = """<header>
  <div class="wrap">
    <div class="brand"><img src="{base}apple-touch-icon.png" alt="Bakhoor" width="34" height="34"><span class="marca">Bakhoor</span></div>
    <nav>
      <a href="{base}index.html#historia">Nosotros</a>
      <a href="{base}index.html#como-comprar">Cómo comprar</a>
      <a href="{base}catalogo.html">Catálogo</a>
      <a href="{base}index.html#zonas">Zonas de entrega</a>
    </nav>
    <a class="btn-wsp" href="https://wa.me/{wsp}?text={wsp_texto}" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>
  </div>
</header>"""

FOOTER_HTML = """<footer>
  <div class="wrap">
    <span>Bakhoor — Perfumería árabe · Caracas y Punto Fijo</span>
    <a href="https://wa.me/{wsp}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</footer>"""

# Ícono de botella (línea, mismo lenguaje de marca) + patrón geométrico de fondo,
# como marcador de producto -- nunca una foto genérica haciéndose pasar por la pieza real.
def placeholder_html(pattern_id):
    return f"""<div class="img-placeholder">
  <svg class="patron-svg" viewBox="0 0 300 300">
    <defs>
      <pattern id="{pattern_id}" width="42" height="42" patternUnits="userSpaceOnUse">
        <path d="M21 2 L40 21 L21 40 L2 21 Z" fill="none" stroke="#C9A24B" stroke-width="1" opacity=".45"/>
        <circle cx="21" cy="21" r="2.2" fill="#C9A24B" opacity=".45"/>
      </pattern>
      <radialGradient id="fade-{pattern_id}" cx="50%" cy="50%" r="50%">
        <stop offset="45%" stop-color="white" stop-opacity="1"/>
        <stop offset="100%" stop-color="white" stop-opacity="0"/>
      </radialGradient>
      <mask id="mask-{pattern_id}"><rect width="300" height="300" fill="url(#fade-{pattern_id})"/></mask>
    </defs>
    <rect width="300" height="300" fill="url(#{pattern_id})" mask="url(#mask-{pattern_id})"/>
  </svg>
  <svg class="botella" viewBox="0 0 100 160" fill="none" stroke="#E7C874" stroke-width="1.4" stroke-linejoin="round">
    <rect x="35" y="8" width="30" height="13" rx="2"/>
    <rect x="42" y="21" width="16" height="9"/>
    <path d="M31 32 h38 l5 13 v98 a6 6 0 0 1-6 6 h-36 a6 6 0 0 1-6-6 v-98 Z"/>
    <line x1="31" y1="68" x2="69" y2="68" stroke-opacity=".6"/>
  </svg>
  <span class="placeholder-nota">Foto real disponible al escribirnos</span>
</div>"""

CATALOGO_CSS = """
.cat-header { background: var(--bkh-negro); color: var(--bkh-crema); padding: 60px 0 44px; text-align: center; }
.cat-header .kicker { color: var(--bkh-oro); font-size: 13px; font-weight: 700; letter-spacing: .3em; text-transform: uppercase; margin-bottom: 14px; }
.cat-header h1 { font-size: 38px; color: var(--bkh-oro-claro); }
.cat-header p { color: rgba(245,237,224,.75); max-width: 520px; margin: 16px auto 0; }
.cat-grid { padding: 60px 0 90px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; border-top: 1px solid rgba(11,11,13,.12); border-left: 1px solid rgba(11,11,13,.12); }
.cat-item { border-right: 1px solid rgba(11,11,13,.12); border-bottom: 1px solid rgba(11,11,13,.12); padding: 26px 22px; text-decoration: none; color: var(--bkh-negro); display: block; }
.cat-item:hover { background: rgba(201,162,75,.08); }
.cat-item .no { font-family: 'Playfair Display', serif; font-style: italic; font-size: 13px; color: var(--bkh-oro); }
.cat-item .marca-mini { font-size: 11px; letter-spacing: .16em; text-transform: uppercase; color: var(--bkh-burdeos); margin: 10px 0 6px; }
.cat-item h3 { font-size: 20px; margin-bottom: 4px; }
.cat-item .tam { font-size: 12.5px; color: var(--bkh-texto-suave); margin-bottom: 14px; }
.cat-item .precio { font-family: 'Playfair Display', serif; font-size: 20px; }
@media (max-width: 860px) { .cat-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 560px) { .cat-grid { grid-template-columns: 1fr; } }
"""

PRODUCTO_CSS = """
.migas { padding: 18px 0; font-size: 13px; color: var(--bkh-texto-suave); }
.migas a { color: var(--bkh-burdeos); text-decoration: none; }
.ficha { padding: 20px 0 70px; display: grid; grid-template-columns: .85fr 1fr; gap: 56px; align-items: start; }
.img-placeholder {
  position: relative; aspect-ratio: 1/1.1; background: var(--bkh-negro);
  display: flex; align-items: center; justify-content: center; overflow: hidden;
  border: 1px solid rgba(201,162,75,.3);
}
.img-placeholder .patron-svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.img-placeholder .botella { position: relative; width: 90px; height: 144px; z-index: 2; }
.img-placeholder .placeholder-nota {
  position: absolute; bottom: 16px; left: 0; right: 0; text-align: center;
  font-size: 11.5px; letter-spacing: .04em; color: rgba(245,237,224,.55); z-index: 2;
}
.ficha-info .marca-mini { font-size: 13px; letter-spacing: .18em; text-transform: uppercase; color: var(--bkh-burdeos); font-weight: 700; margin-bottom: 10px; }
.ficha-info h1 { font-size: 40px; line-height: 1.1; }
.ficha-info .tam { font-size: 15px; color: var(--bkh-texto-suave); margin: 8px 0 4px; }
.ficha-info .apodo { font-family: 'Playfair Display', serif; font-style: italic; font-size: 19px; color: var(--bkh-burdeos); margin: 4px 0 22px; }
.ficha-info .notas { font-size: 16px; color: var(--bkh-texto-suave); max-width: 480px; margin-bottom: 26px; }
.ficha-info .precio { font-family: 'Playfair Display', serif; font-size: 34px; margin-bottom: 22px; }
.ficha-info .btn-wsp { font-size: 15px; padding: 14px 30px; }
.relacionados { padding: 0 0 80px; }
.relacionados h2 { font-size: 24px; margin-bottom: 26px; }
.rel-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.rel-card { border: 1px solid rgba(11,13,13,.12); padding: 20px; text-decoration: none; color: var(--bkh-negro); display: block; }
.rel-card:hover { background: rgba(201,162,75,.08); }
.rel-card .marca-mini { font-size: 11px; letter-spacing: .14em; text-transform: uppercase; color: var(--bkh-burdeos); }
.rel-card h3 { font-size: 18px; margin: 6px 0 4px; }
.rel-card .precio { font-family: 'Playfair Display', serif; font-size: 17px; }
@media (max-width: 860px) { .ficha { grid-template-columns: 1fr; gap: 30px; } .rel-grid { grid-template-columns: 1fr; } }
"""

def wsp_link(texto):
    import urllib.parse
    return urllib.parse.quote(texto)

PAGE_TMPL = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{extra_head}
{head_comun}
<style>{css_comun}{css_extra}</style>
</head>
<body>
{header}
{body}
{footer}
</body>
</html>
"""

# ---------- Página de catálogo ----------
items_html = []
for p in PRODUCTOS:
    items_html.append(f"""<a class="cat-item" href="producto/{p['slug']}.html">
  <div class="no">Nº {p['num']:02d}</div>
  <div class="marca-mini">{p['marca']}</div>
  <h3>{p['nombre']}</h3>
  <div class="tam">{p['tam']}</div>
  <div class="precio">${p['precio']}</div>
</a>""")

catalogo_body = f"""<section class="cat-header">
  <div class="wrap">
    <div class="kicker">Catálogo completo</div>
    <h1>{len(PRODUCTOS)} fragancias, un pedido a la vez</h1>
    <p>Cada pieza en esta lista viene del mismo pedido mayorista real. Escríbenos por cualquiera para confirmar disponibilidad y foto real.</p>
  </div>
</section>
<section class="wrap">
  <div class="cat-grid">
    {''.join(items_html)}
  </div>
</section>"""

catalogo_html = PAGE_TMPL.format(
    title="Catálogo completo — Bakhoor Perfumería Árabe",
    description=f"Las {len(PRODUCTOS)} fragancias árabes originales disponibles ahora en Bakhoor: Afnan, Armaf, Lattafa, Rasasi y más. Precios y notas por pieza.",
    canonical="https://bakhoor.ve/catalogo.html",
    extra_head="",
    head_comun=HEAD_COMUN.format(base=""),
    css_comun=CSS_COMUN, css_extra=CATALOGO_CSS,
    header=HEADER_HTML.format(base="", wsp=WHATSAPP, wsp_texto=wsp_link("Hola Bakhoor, quiero ver el catálogo completo")),
    body=catalogo_body,
    footer=FOOTER_HTML.format(wsp=WHATSAPP),
)
(OUT / "catalogo.html").write_text(catalogo_html, encoding="utf-8")

# ---------- Páginas de producto ----------
for p in PRODUCTOS:
    relacionados = [q for q in PRODUCTOS if q["marca"] == p["marca"] and q["slug"] != p["slug"]][:3]
    if len(relacionados) < 3:
        otros = [q for q in PRODUCTOS if q["slug"] != p["slug"] and q not in relacionados]
        relacionados += otros[: 3 - len(relacionados)]

    rel_html = "".join(f"""<a class="rel-card" href="{r['slug']}.html">
      <div class="marca-mini">{r['marca']}</div>
      <h3>{r['nombre']}</h3>
      <div class="precio">${r['precio']}</div>
    </a>""" for r in relacionados)

    wsp_texto = wsp_link(f"Hola Bakhoor, quiero el {p['marca']} {p['nombre']} ({p['tam']})")

    body = f"""<div class="wrap">
  <div class="migas"><a href="../index.html">Inicio</a> / <a href="../catalogo.html">Catálogo</a> / {p['marca']} {p['nombre']}</div>
  <div class="ficha">
    {placeholder_html('p' + str(p['num']))}
    <div class="ficha-info">
      <div class="marca-mini">{p['marca']} · Nº {p['num']:02d}</div>
      <h1>{p['nombre']}</h1>
      <div class="tam">{p['tam']}</div>
      <div class="apodo">{p['apodo']}</div>
      <p class="notas">{p['notas']}</p>
      <div class="precio">${p['precio']}</div>
      <a class="btn-wsp" href="https://wa.me/{WHATSAPP}?text={wsp_texto}" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>
    </div>
  </div>
</div>
<div class="wrap relacionados">
  <h2>También de {p['marca']}{'​' if False else ''}</h2>
  <div class="rel-grid">{rel_html}</div>
</div>"""

    product_ld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{p['marca']} {p['nombre']} — {p['tam']}",
  "brand": {{ "@type": "Brand", "name": "{p['marca']}" }},
  "description": "{p['notas']}",
  "offers": {{
    "@type": "Offer",
    "price": "{p['precio']}",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "areaServed": ["Caracas", "Punto Fijo"]
  }}
}}
</script>"""

    page = PAGE_TMPL.format(
        title=f"{p['marca']} {p['nombre']} — Bakhoor Perfumería Árabe",
        description=f"{p['marca']} {p['nombre']} ({p['tam']}) — {p['notas']} Disponible por ${p['precio']} en Bakhoor, entregas en Caracas y Punto Fijo.",
        canonical=f"https://bakhoor.ve/producto/{p['slug']}.html",
        extra_head=product_ld,
        head_comun=HEAD_COMUN.format(base="../"),
        css_comun=CSS_COMUN, css_extra=PRODUCTO_CSS,
        header=HEADER_HTML.format(base="../", wsp=WHATSAPP, wsp_texto=wsp_link(f"Hola Bakhoor, quiero el {p['marca']} {p['nombre']}")),
        body=body,
        footer=FOOTER_HTML.format(wsp=WHATSAPP),
    )
    (PROD_DIR / f"{p['slug']}.html").write_text(page, encoding="utf-8")

print(f"Generado: catalogo.html + {len(PRODUCTOS)} páginas de producto en {PROD_DIR}")
