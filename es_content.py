"""Spanish copy for the /es/ home page and the /es/escanear/ page. Machine-drafted: needs native review."""

HOME = {
    "title": "BillKarma en español: revise su factura de hospital",
    "description": "Guías en español sobre cómo pedir su factura detallada, disputar cobros y buscar ayuda financiera. Revisamos su factura con lo que paga Medicare.",
    "h1": "Revise su factura de hospital. Entienda qué puede hacer.",
    "lede": "BillKarma compara cada cargo de su factura de hospital con lo que paga Medicare por el mismo código y marca cargos duplicados y otros puntos que vale la pena preguntar. Revisar su factura es gratis.",
    "cta_text": "Cómo revisar mi factura",
    "cta_url": "/es/escanear/",
    "body": """
<h2>Qué hacemos</h2>
<ol>
    <li><strong>Revisamos su factura (gratis).</strong> Cada línea con un código de facturación se compara con la tarifa de Medicare para ese código. Marcamos cargos duplicados, pruebas cobradas dos veces y niveles de visita altos.</li>
    <li><strong>Le ayudamos a pedir información al hospital primero.</strong> Puede pedir su factura detallada (itemized bill) y preguntar por la asistencia financiera (financial assistance, también llamada charity care) del hospital.</li>
    <li><strong>Si usted lo decide, enviamos una disputa por escrito</strong> a la oficina de facturación del hospital y le damos seguimiento. Esto tiene una tarifa fija, y el precio se muestra antes de pagar.</li>
</ol>

<h2>Lo que no hacemos</h2>
<ul>
    <li>No negociamos por teléfono y no podemos garantizar que el hospital reduzca su factura. El resultado depende del hospital.</li>
    <li>No somos un bufete de abogados y no damos asesoría legal. Si necesita ayuda legal, consulte a un abogado de consumidores o a una organización de asistencia legal.</li>
</ul>

<h2>Importante: la herramienta está en inglés</h2>
<p>Las guías de esta sección están en español. La revisión de la factura, los resultados y las cartas de disputa todavía están <strong>solo en inglés</strong>, y los hospitales también usan palabras en inglés. Por eso, en las guías le damos el término en inglés entre paréntesis la primera vez que aparece.</p>
""",
}

SCAN = {
    "title": "Revisar mi factura de hospital gratis | BillKarma",
    "description": "Cómo funciona la revisión gratuita de BillKarma: comparamos cada cargo de su factura con lo que paga Medicare. La herramienta está en inglés.",
    "h1": "Revise su factura de hospital con lo que paga Medicare",
    "lede": "Suba una foto o un PDF de su factura detallada y vea cada cargo junto a la tarifa de Medicare para el mismo código. Es gratis y no necesita cuenta.",
    "cta_text": "Ir a la revisión (en inglés)",
    "cta_url": "/scan",
    "body": """
<div class="key-takeaway"><strong>Aviso:</strong> la página de la revisión (<a href="/scan" lang="en">/scan</a>) y sus resultados están en inglés. Esta página le explica cómo funciona para que pueda usarla con confianza. Si lo necesita, pida ayuda a un familiar o amigo que lea inglés.</div>

<h2>Cómo funciona</h2>
<ol>
    <li><strong>Suba su factura detallada.</strong> Puede ser una foto o un PDF. Si solo tiene un resumen, pida la versión detallada primero: lea <a href="/es/guias/como-obtener-factura-detallada-hospital/">cómo obtener su factura detallada (itemized bill)</a>. Nuestra herramienta para escribir esa solicitud (<a href="/itemized-bill" lang="en">/itemized-bill</a>) también está en inglés.</li>
    <li><strong>Vea qué parece incorrecto.</strong> Cada línea con un código de facturación se compara con la tarifa de Medicare para ese código. Marcamos cargos duplicados, pruebas que se traslapan y niveles de visita altos.</li>
    <li><strong>Decida qué hacer.</strong> Con los resultados puede hablar con la oficina de facturación del hospital. Si quiere, también puede pedirnos que enviemos una disputa por escrito. Eso es opcional y tiene una tarifa fija que se muestra antes de pagar.</li>
</ol>

<h2>Qué significan los resultados</h2>
<ul>
    <li>Un cargo marcado no quiere decir que el hospital se equivocó. Quiere decir que vale la pena preguntar por él.</li>
    <li>La tarifa de Medicare es un punto de comparación basado en datos públicos de CMS (los Centros de Servicios de Medicare y Medicaid). No es el precio que el hospital tiene que cobrarle.</li>
    <li>No podemos garantizar que el hospital reduzca su factura. El resultado depende del hospital.</li>
    <li>BillKarma no es un bufete de abogados. Nada de esto es asesoría legal ni financiera.</li>
</ul>

<h2>Antes de pagar</h2>
<p>Si su factura le preocupa por el monto, lea también estas guías: <a href="/es/guias/asistencia-financiera-hospital/">asistencia financiera del hospital</a> y <a href="/es/guias/no-puedo-pagar-factura-medica/">qué hacer si no puede pagar una factura médica</a>.</p>
""",
}

REASON_LABELS_ES = {
    "duplicate_charge": "Cobrado más de una vez",
    "price_markup": "Muy por encima de lo que paga Medicare",
    "upcoding": "El nivel de la visita puede ser más alto que la atención recibida",
    "unbundling": "Cobrado por separado de una prueba que ya lo incluye",
    "quantity_flag": "La cantidad parece incorrecta",
    "benchmark_outlier": "Por encima del cargo típico en su región",
    "eob_mismatch": "No coincide con el estado de cuenta de su seguro (EOB)",
    "insurer_rate": "Por encima de la tarifa contratada de su seguro",
    "quantity_question": "Cantidad que vale la pena preguntar",
    "price_info": "Precio de lista alto, ya con el descuento de su seguro",
    "no_surprises_act": "Puede estar protegido por la Ley No Surprises (No Surprises Act)",
}
