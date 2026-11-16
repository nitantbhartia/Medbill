"""Spanish guides on bills and billing rights. Machine-drafted translations: need native review.

Each guide translates one English guide (en_slug) and adds no new facts.
"""

ITEMIZED = {
    "slug": "como-obtener-factura-detallada-hospital",
    "en_slug": "how-to-get-itemized-hospital-bill",
    "title": "Cómo obtener su factura detallada del hospital",
    "description": "Usted tiene derecho a pedir una factura detallada (itemized bill) del hospital. Aprenda cómo pedirla, qué errores buscar y cómo comparar los cargos con Medicare.",
    "answer": "Llame a la oficina de facturación del hospital y pida una factura detallada (itemized bill) con todos los cargos, incluyendo el código CPT o el código de ingresos (revenue code) de cada línea. Los hospitales que participan en Medicare deben dárselo si usted lo pide.",
    "body": """
<p class="lead">Es probable que el hospital le haya enviado solo un resumen: una página con un total de $18,400, $52,000 o la cantidad que sea. Ese resumen casi no sirve para encontrar errores. El documento que usted necesita es la factura detallada (itemized bill), que muestra cada cargo, línea por línea, con sus códigos. Aquí le explicamos cómo obtenerla y qué hacer con ella.</p>

<div class="key-takeaway"><strong>Para ahorrar tiempo:</strong> nuestra <a href="/itemized-bill" lang="en">herramienta para pedir la factura detallada</a> escribe la solicitud con la dirección de facturación del hospital. Es gratis, pero está en inglés.</div>

<nav class="toc">
    <h2>En esta guía</h2>
    <ol>
        <li><a href="#derecho">Su derecho a una factura detallada</a></li>
        <li><a href="#como-pedirla">Cómo pedirla</a></li>
        <li><a href="#que-buscar">Qué debe tener cada línea</a></li>
        <li><a href="#errores">Errores comunes en las facturas</a></li>
        <li><a href="#medicare">Cómo comparar los cargos con Medicare</a></li>
        <li><a href="#error-encontrado">Qué hacer si encuentra un error</a></li>
    </ol>
</nav>

<h2 id="derecho">Su derecho a una factura detallada</h2>
<p>La ley federal exige que los hospitales que participan en Medicare, que son prácticamente todos los hospitales de Estados Unidos, den una factura detallada de los cargos cuando el paciente la pide. Este requisito está en las Condiciones de Participación de Medicare (Medicare Conditions of Participation, 42 CFR §482.13), que los hospitales deben cumplir para recibir pagos de Medicare y Medicaid.</p>
<p>Además, muchos estados tienen sus propias leyes sobre facturas detalladas. California, Nueva York, Texas y Florida, entre otros, tienen leyes de derechos del paciente que incluyen una factura detallada. Algunos estados exigen que el hospital la entregue sin que el paciente la pida.</p>
<p>La regla de transparencia de precios de hospitales (Hospital Price Transparency Rule, vigente desde enero de 2021 y reforzada en 2024) exige que los hospitales publiquen sus precios estándar. Esto quiere decir que usted puede comparar su factura detallada con los precios publicados por el propio hospital (el chargemaster).</p>

<h2 id="como-pedirla">Cómo pedirla</h2>
<p>Lo más rápido es una llamada seguida de una solicitud por escrito. Estos son los pasos:</p>
<ol>
    <li><strong>Llame a la oficina de facturación (billing department).</strong> El número está en su factura o en el sitio web del hospital. Llame a facturación, no a la línea de servicios al paciente.</li>
    <li><strong>Use esta frase.</strong> Como el personal del hospital habla inglés, esta es la frase original: <em lang="en">“I am requesting a complete itemized statement of all charges for my visit on [date], including the CPT code or revenue code for every line item.”</em> En español sería: “Pido un estado de cuenta detallado de todos los cargos de mi visita del [fecha], con el código CPT o el código de ingresos de cada línea.”</li>
    <li><strong>Pídala por escrito,</strong> por correo o por correo electrónico. Un PDF es mejor porque se puede buscar dentro del documento.</li>
    <li><strong>Anote el nombre de la persona con quien habló y la fecha.</strong> Si la factura no llega en dos semanas, vuelva a llamar y mencione su solicitud anterior.</li>
    <li><strong>Pida también su expediente médico</strong> (o por lo menos el resumen de alta y las notas de enfermería). Los usará para comprobar que los cargos corresponden a la atención que recibió.</li>
</ol>
<p>Si facturación no responde, pida hablar con el defensor del paciente (patient financial advocate o patient ombudsman). La mayoría de los hospitales tienen uno. Si sigue sin respuesta, puede presentar una queja ante la agencia estatal que da licencia a los hospitales o ante los Centros de Servicios de Medicare y Medicaid (CMS).</p>
<p><strong>En general, no pague la factura mientras espera la versión detallada.</strong> Pida que pongan la cuenta en espera (billing hold) mientras revisa los cargos. Muchos hospitales aceptan esperar de 30 a 60 días si usted lo pide.</p>

<h2 id="que-buscar">Qué debe tener cada línea</h2>
<p>Una factura detallada debe mostrar, para cada cargo:</p>
<ul>
    <li><strong>Fecha del servicio:</strong> el día en que se prestó el servicio</li>
    <li><strong>Código de ingresos (revenue code):</strong> un código de 3 o 4 dígitos que indica el tipo de cargo (por ejemplo, 0250 = farmacia, 0360 = quirófano)</li>
    <li><strong>Código CPT o HCPCS:</strong> el código del procedimiento clínico</li>
    <li><strong>Descripción:</strong> el nombre del servicio o del suministro</li>
    <li><strong>Cantidad:</strong> cuántas unidades se cobraron</li>
    <li><strong>Precio por unidad</strong></li>
    <li><strong>Cargo total:</strong> el precio por unidad multiplicado por la cantidad</li>
</ul>
<p>Al revisar cada línea, pregúntese: ¿Estaba yo en el hospital en esa fecha? ¿Recibí este servicio o este medicamento? ¿La cantidad parece correcta? Si le pusieron anestesia para una cirugía, no puede comprobar cada suministro usado en el quirófano. Pero sí puede comprobar sus fechas de ingreso y alta, los medicamentos que le dieron en su cuarto y los procedimientos que aparecen.</p>

<h2 id="errores">Errores comunes en las facturas</h2>
<p>Estudios de la Oficina de Responsabilidad del Gobierno (GAO), de organizaciones que ayudan con facturas médicas y de auditorías de aseguradoras encuentran errores con frecuencia en las facturas de hospital. Estos son los más comunes:</p>
<h3>Cargos duplicados (duplicate charges)</h3>
<p>El mismo servicio, suministro o procedimiento cobrado dos veces en la misma fecha o en fechas seguidas. Es el error más común. Busque dos líneas iguales con la misma descripción y fecha. También fíjese si el mismo medicamento aparece con dos códigos de ingresos distintos.</p>
<h3>Código de nivel más alto (upcoding)</h3>
<p>Cobrar un servicio más caro que el que se prestó. En la sala de emergencias, por ejemplo, es cobrar la visita con el nivel más alto (CPT 99285) cuando la visita fue sencilla y debió ser 99283 o 99284. La diferencia puede ser de $400 a $800 por visita. Pida su expediente médico y compare el nivel de complejidad documentado con el código cobrado.</p>
<h3>Cargos separados que deberían ir juntos (unbundling)</h3>
<p>Cobrar por separado procedimientos que deberían facturarse con un solo código. Por ejemplo, cobrar por separado las partes de una cirugía que tiene un código CPT único e integral aumenta el total sin razón. La Iniciativa Nacional de Codificación Correcta de Medicare (National Correct Coding Initiative, NCCI) define qué códigos deben ir juntos.</p>
<h3>Servicios que no se prestaron</h3>
<p>Artículos cobrados que usted no recibió. Por ejemplo, sesiones de terapia física que no ocurrieron, consultas con especialistas que nunca conoció o suministros de un paquete estándar que no se abrieron durante su atención.</p>
<h3>Información equivocada del paciente</h3>
<p>Su factura tiene el diagnóstico, la fecha de ingreso o los datos del seguro de otra persona por un error al escribir los datos. Esto puede hacer que rechacen su reclamo o que aparezcan cargos de otro paciente. Verifique su nombre, fecha de nacimiento, número de seguro y fechas de ingreso y alta en cada página.</p>
<h3>Cargos altos en farmacia</h3>
<p>Medicamentos cobrados a precio de venta al público o más, cuando el hospital los compró con un descuento grande. Por ejemplo, bolsas de solución salina que le cuestan al hospital de $1 a $3 y se cobran de $30 a $80. Los cargos de farmacia están entre los más inflados en la mayoría de las facturas de hospital.</p>

<h2 id="medicare">Cómo comparar los cargos con Medicare</h2>
<p>Las tarifas de Medicare son un buen punto de comparación para ver si los cargos del hospital son razonables. Medicare paga a los hospitales con el Sistema de Pago Prospectivo para Pacientes Hospitalizados (IPPS) y con el Sistema de Pago Prospectivo para Pacientes Ambulatorios (OPPS). Para los servicios de médicos que aparecen en su factura se usa la Lista de Tarifas de Médicos de Medicare (Medicare Physician Fee Schedule).</p>
<p>Para procedimientos ambulatorios y servicios de médicos, cada código CPT tiene una tarifa de Medicare que usted puede buscar. Como regla general, cargos de 2 a 3 veces la tarifa de Medicare están dentro del rango típico de la facturación hospitalaria para pacientes con seguro comercial. Cargos de 5, 8 o 10 veces la tarifa de Medicare son muy altos y se pueden negociar, sobre todo si usted no tiene seguro o su seguro cubre poco.</p>
<p>Cuando hable con facturación, cite la tarifa de Medicare. Por ejemplo, en inglés: <em lang="en">“Medicare pays $142 for CPT 99283. You billed $780. I’d like to understand the basis for that charge.”</em></p>
<p>Para hospitalizaciones, pregunte a qué grupo relacionado por diagnóstico (DRG, Diagnosis-Related Group) se asignó su estadía y busque el pago de Medicare para ese DRG. Si el hospital cobró $85,000 y Medicare pagaría $18,000 por el mismo DRG, usted tiene un punto de comparación concreto.</p>

<h2 id="error-encontrado">Qué hacer si encuentra un error</h2>
<p>Encontrar un error es solo el comienzo. Para actuar con eficacia:</p>
<ol>
    <li><strong>Anote cada error por escrito.</strong> Haga una lista sencilla: línea, cargo, código CPT, su duda y la evidencia (expediente médico, tarifa de Medicare).</li>
    <li><strong>Pida una revisión de la factura (billing review).</strong> Llame a facturación y pida una revisión formal de líneas específicas. Sea concreto: “La línea 47 de mi factura detallada muestra un cargo de $380 por CPT 99285 el 12 de marzo. Mi expediente médico indica que fue una visita de nivel 3, que debería ser 99283 a $142. Pido que lo corrijan.”</li>
    <li><strong>Dé seguimiento por escrito.</strong> Después de la llamada, envíe un correo electrónico o una carta certificada que resuma lo que hablaron y lo que pidió. Así deja un registro.</li>
    <li><strong>Escale el caso si es necesario.</strong> Si facturación no corrige errores claros, pida hablar con el defensor del paciente, con el director del ciclo de ingresos (revenue cycle director) o con el departamento de cumplimiento (compliance). Puede decir que está dispuesto a presentar una queja ante CMS y ante el comisionado de seguros de su estado.</li>
    <li><strong>Hable con su aseguradora.</strong> Si el error afectó cómo la aseguradora procesó el reclamo, presente también una apelación a la aseguradora con la información corregida.</li>
</ol>
<div class="key-takeaway">
    <strong>BillKarma puede ayudarle con esta revisión.</strong> Suba su factura detallada y marcamos cargos duplicados, comparamos cada código CPT con las tarifas de Medicare y señalamos posibles códigos de nivel más alto. <a href="/es/escanear/">Vea cómo funciona</a>. La herramienta está en inglés.
</div>
""",
    "faqs": [
        ("¿El hospital tiene que darme una factura detallada?", "Sí. Según la ley federal y los reglamentos de todos los estados, usted tiene derecho a pedir un estado de cuenta detallado de todos los cargos. Los hospitales que participan en Medicare, que son casi todos, deben darlo si se lo piden. Pídalo por escrito a facturación; deben responder en un plazo razonable, que normalmente es de 30 días. Algunos estados exigen que el hospital entregue la factura detallada sin que usted la pida."),
        ("¿Cuál es la diferencia entre una factura resumida y una detallada?", "Una factura resumida agrupa los cargos en categorías amplias, como “habitación y comida”, “farmacia” o “suministros médicos”, con una sola cantidad cada una. Una factura detallada enumera cada servicio, suministro y procedimiento en su propia línea, con fecha, cantidad, precio por unidad, código CPT o de ingresos y cargo total. No se puede buscar errores en una factura resumida. Necesita la versión detallada."),
        ("¿Cómo comparo los cargos del hospital con las tarifas de Medicare?", "Cada línea de su factura detallada debe tener un código CPT (para procedimientos) o un código de ingresos (para habitación y suministros). Busque cada código CPT en la Lista de Tarifas de Médicos de Medicare de CMS o use la herramienta de costos de BillKarma. Las tarifas de Medicare son datos públicos. Si el hospital cobra de 5 a 10 veces la tarifa de Medicare por un procedimiento, es un punto para negociar: cítelo específicamente cuando hable con facturación."),
    ],
    "sources": [
        ("CMS Medicare Conditions of Participation: Patient Rights (42 CFR §482.13)", "https://www.cms.gov/medicare/provider-enrollment-and-certification/certificationandcomplianc/downloads/usersguide.pdf"),
        ("CMS Hospital Price Transparency Requirements", "https://www.cms.gov/hospital-price-transparency"),
        ("GAO: Hospital Billing Practices and Price Transparency", "https://www.gao.gov/products/gao-22-104622"),
        ("KFF: Patient Rights and Hospital Billing", "https://www.kff.org/health-costs/issue-brief/surprise-medical-bills-new-protections-for-consumers-take-effect-in-2022/"),
        ("CMS National Correct Coding Initiative (NCCI) Edits", "https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci"),
    ],
}

DISPUTE = {
    "slug": "como-disputar-factura-medica",
    "en_slug": "how-to-dispute-a-medical-bill",
    "title": "Cómo disputar una factura médica",
    "description": "Cómo disputar una factura médica paso a paso: qué reunir, qué incluir en la carta, cuándo escalar y qué esperar. Información general, no asesoría legal.",
    "answer": "Pida una factura detallada (itemized bill), compare cada cargo con la tarifa de Medicare y envíe una carta de disputa por escrito que cite el error específico. Muchos hospitales resuelven las disputas en 30 a 60 días. Si lo rechazan, puede escalar al comisionado de seguros de su estado.",
    "body": """
<p class="lead">Encontró un error en su factura médica. ¿Y ahora qué? Muchos pacientes nunca disputan porque no saben por dónde empezar. Esta guía le explica el proceso completo, desde la primera carta hasta cómo escalar el caso si el hospital no cambia su respuesta.</p>

<div class="key-takeaway"><strong>Una nota sobre las cartas:</strong> la carta de ejemplo y el guion de llamada de nuestra guía en inglés están en inglés, porque el hospital las lee en inglés. Aquí le explicamos qué debe incluir cada una. Puede ver el modelo en <a href="/guides/how-to-dispute-a-medical-bill/" lang="en">la guía original</a>.</div>

<nav class="toc">
    <h2>En esta guía</h2>
    <ol>
        <li><a href="#evidencia">Antes de disputar: reúna su evidencia</a></li>
        <li><a href="#carta">Qué incluir en la carta de disputa</a></li>
        <li><a href="#llamada">La llamada a facturación</a></li>
        <li><a href="#vale-la-pena">Qué vale la pena disputar</a></li>
        <li><a href="#escalar">Cómo escalar si facturación dice que no</a></li>
        <li><a href="#tiempos">Tiempos de una disputa</a></li>
    </ol>
</nav>

<h2 id="evidencia">1. Antes de disputar: reúna su evidencia</h2>
<p>Una disputa sin evidencia es solo una queja. Antes de contactar al hospital, reúna estas cuatro cosas:</p>
<ol>
    <li><strong>Su factura detallada (itemized bill).</strong> No el resumen. Necesita el desglose línea por línea con códigos CPT, descripciones, cantidades y cargos. Si no la tiene, llame a facturación y pídala. Vea <a href="/es/guias/como-obtener-factura-detallada-hospital/">cómo obtenerla</a>.</li>
    <li><strong>Las tarifas de Medicare para cada código CPT.</strong> Son su punto de comparación. La <a href="/calculator" lang="en">calculadora de costos</a> (en inglés) muestra la tarifa de Medicare de cada servicio en su zona.</li>
    <li><strong>Su Explicación de Beneficios (EOB, Explanation of Benefits).</strong> Si tiene seguro, la EOB muestra lo que su aseguradora aprobó, lo que pagó y lo que cree que usted debe. Compárela con la factura del hospital; es común que no coincidan.</li>
    <li><strong>Sus papeles de alta (discharge paperwork).</strong> El resumen de alta enumera los servicios que realmente recibió. Es su prueba si la factura incluye servicios que no recibió o cantidades que no coinciden.</li>
</ol>
<div class="key-takeaway">
    <strong>Regla clave:</strong> no llame a facturación sin su evidencia lista. Necesita cifras concretas, no quejas generales. “Mi factura parece muy alta” no lleva a nada. “El CPT 71046 está cobrado a $940 pero Medicare paga $127, es 7.4 veces más” es mucho más claro.
</div>

<h2 id="carta">2. Qué incluir en la carta de disputa</h2>
<p>Una carta crea un registro por escrito. Envíe una carta aunque también llame. Incluya:</p>
<ul>
    <li>Su nombre, número de cuenta y fecha del servicio</li>
    <li>Las líneas específicas que disputa (código CPT, descripción y cantidad cobrada)</li>
    <li>La razón por la que cada cargo parece incorrecto (duplicado, cargos separados que deberían ir juntos, por encima de la tarifa de Medicare, etc.)</li>
    <li>La tarifa de Medicare para cada servicio disputado</li>
    <li>Lo que pide: que quiten el cargo, que lo reduzcan a una cantidad específica o que lo revisen</li>
</ul>
<p>Al final, pida una factura corregida en 30 días y diga que con gusto pagará pronto la parte que no disputa.</p>
<p><strong>Cómo enviarla:</strong> use el portal del paciente del hospital si tiene uno, porque deja un registro con fecha y hora. Si no, envíela por correo certificado con acuse de recibo. Guarde una copia de todo.</p>

<h2 id="llamada">3. La llamada a facturación</h2>
<p>A veces una llamada resuelve las cosas más rápido que una carta. Antes de llamar, tenga a la mano su número de cuenta, la fecha del servicio y la lista de cargos que quiere preguntar, cada uno con su código CPT y la tarifa de Medicare. Explique cada punto con calma y pregunte cuáles son los siguientes pasos para revisar esos cargos. Mencione que también envió una disputa por escrito. Anote el nombre de la persona y la fecha de la llamada.</p>
<p>Si desea saber cuánto podría reducir cada cargo, compárelo con la tarifa de Medicare antes de llamar. Eso le da un estimado, no una garantía.</p>

<h2 id="vale-la-pena">4. Qué vale la pena disputar</h2>
<p>No todos los cargos valen el esfuerzo. Concéntrese en lo que más importa:</p>
<table>
    <thead><tr><th>Vale la pena disputar</th><th>Dificultad</th></tr></thead>
    <tbody>
        <tr><td>Cargos duplicados</td><td>Fácil: es un error claro</td></tr>
        <tr><td>Cargos separados que deberían ir juntos (unbundling)</td><td>Fácil: cite las reglas NCCI</td></tr>
        <tr><td>Visita de emergencias con nivel demasiado alto (upcoding)</td><td>Moderada: puede necesitar las notas clínicas</td></tr>
        <tr><td>Cargos de más de 5 veces la tarifa de Medicare</td><td>Moderada: requiere negociar</td></tr>
        <tr><td>Servicios que no recibió</td><td>Fácil: compare con el resumen de alta</td></tr>
    </tbody>
</table>
<table>
    <thead><tr><th>Normalmente no vale la pena disputar</th><th>Por qué</th></tr></thead>
    <tbody>
        <tr><td>Cargos de menos de $50</td><td>El tiempo que toma supera lo que podría ahorrar</td></tr>
        <tr><td>Cargos de 1 a 2 veces la tarifa de Medicare</td><td>Están dentro del rango normal de precios comerciales</td></tr>
        <tr><td>Cargos de instalación (facility fees) que usted aceptó</td><td>El consentimiento firmado normalmente los cubre</td></tr>
    </tbody>
</table>

<h2 id="escalar">5. Cómo escalar si facturación dice que no</h2>
<p>Si facturación rechaza su disputa o deja de responder, siga esta escalera:</p>
<ol>
    <li><strong>Supervisor de facturación.</strong> Pida hablar con un supervisor o gerente. El personal de primera línea a veces no puede aprobar ajustes por encima de cierta cantidad.</li>
    <li><strong>Defensor del paciente (patient advocate).</strong> La mayoría de los hospitales tienen uno. Su trabajo es resolver quejas de pacientes. Pida a la operadora del hospital que lo comunique.</li>
    <li><strong>Su aseguradora.</strong> Si tiene seguro, llame al número de servicio a miembros y pida que revisen los cargos. Las aseguradoras tienen más influencia que un paciente solo.</li>
    <li><strong>Comisionado de seguros de su estado.</strong> Cada estado tiene un Departamento de Seguros que acepta quejas sobre facturación médica. Presentar una queja suele provocar una respuesta del hospital en unas semanas.</li>
    <li><strong>Fiscal general del estado.</strong> Si hay un patrón de cobros excesivos, la división de protección al consumidor de la oficina del fiscal general (attorney general) de su estado puede investigar.</li>
    <li><strong>Defensor de facturación médica (medical billing advocate).</strong> En disputas complejas, con más de $5,000 de ahorro posible, un defensor profesional cobra del 25% al 35% de lo que se ahorra y conoce bien el sistema.</li>
</ol>
<div class="key-takeaway">
    <strong>Importante:</strong> en cada paso, mencione sus comunicaciones anteriores: “Envié una carta de disputa el [fecha] y hablé con [nombre] el [fecha]. Estos son los números de caso.” La documentación convierte una queja en una disputa creíble.
</div>

<h2 id="tiempos">6. Tiempos de una disputa</h2>
<table>
    <thead><tr><th>Etapa</th><th>Plazo</th><th>Qué pasa</th></tr></thead>
    <tbody>
        <tr><td>Envía la carta</td><td>Día 1</td><td>Empieza el plazo. El hospital debería confirmar el recibo en 5 a 7 días hábiles.</td></tr>
        <tr><td>Revisión del hospital</td><td>Días 7 a 30</td><td>Facturación investiga. Puede pedir más información.</td></tr>
        <tr><td>Primera respuesta</td><td>Días 14 a 45</td><td>El hospital envía una factura ajustada o un rechazo con explicación.</td></tr>
        <tr><td>Escalar (si hace falta)</td><td>Días 30 a 60</td><td>Contacte al defensor del paciente o presente una queja estatal.</td></tr>
        <tr><td>Resolución</td><td>Días 30 a 90</td><td>Muchas disputas se resuelven en 90 días. Los casos complejos pueden tardar más.</td></tr>
    </tbody>
</table>
<p><strong>Durante la disputa:</strong> pague a tiempo la parte de la factura que no disputa. Pida por escrito que la cantidad en disputa no se envíe a cobros (collections) mientras dure la revisión. Muchos hospitales aceptan.</p>
<div class="key-takeaway">
    <strong>¿Quiere ver qué podría estar mal en su factura antes de disputar?</strong> <a href="/es/escanear/">Vea cómo funciona la revisión gratuita de BillKarma</a>. La herramienta marca duplicados, cargos que deberían ir juntos y cargos altos. Está en inglés.
</div>
""",
    "faqs": [
        ("¿Cuánto tiempo tengo para disputar una factura médica?", "Muchos hospitales permiten disputas dentro de los 120 a 180 días de la fecha de la factura. Aun así, conviene actuar rápido. Cuando una factura pasa a cobros (normalmente después de 90 a 120 días sin pago), es más difícil disputarla. Para mejores resultados, contacte a facturación dentro de los 30 días de recibir la factura."),
        ("¿Puedo disputar una factura que ya pasó a cobros?", "Sí. Según la Ley de Prácticas Justas de Cobro de Deudas (FDCPA, Fair Debt Collection Practices Act), usted tiene 30 días desde el primer aviso de cobro para pedir la validación de la deuda (debt validation). El cobrador debe dar pruebas de que la deuda es correcta y de que tiene derecho a cobrarla. Si la factura tiene errores, el departamento de facturación del hospital original todavía puede corregirlos."),
        ("¿Disputar una factura afecta mi puntaje de crédito?", "No. Disputar una factura no afecta su puntaje de crédito. Desde 2023, las tres agencias principales de crédito (Experian, TransUnion y Equifax) ya no incluyen en los informes de crédito la deuda médica menor de $500. Las cuentas médicas en cobros que ya se pagaron también se eliminan. La deuda médica sin pagar de más de $500 solo puede aparecer después de 12 meses, lo que le da tiempo para resolver disputas."),
        ("¿Qué hago si el hospital no quiere ajustar mi factura?", "Escale en este orden: (1) pida hablar con un supervisor de facturación, (2) contacte al defensor del paciente del hospital, (3) presente una queja ante el comisionado de seguros de su estado, (4) si tiene seguro, pida a su aseguradora que revise los cargos, (5) para casos complejos, consulte a un defensor de facturación médica."),
        ("¿Necesito un abogado para disputar una factura médica?", "En la mayoría de los casos, no. Casi todos los errores de facturación se pueden resolver contactando directamente a facturación del hospital con documentación del error. Un abogado solo hace falta si la disputa tiene temas legales, como cobros indebidos (balance billing) bajo la ley No Surprises Act, o si la factura ya está en cobros y el caso llegó a la corte. En esos casos, consulte a un abogado de consumidores o a una organización de asistencia legal."),
        ("¿Debo pagar mi factura médica mientras la disputo?", "Debe pagar la parte que no disputa, para mostrar buena fe. Para la cantidad en disputa, envíe una carta por escrito que explique qué cargos cuestiona. Pida que el hospital no envíe esa parte a cobros mientras la disputa siga activa. Muchos hospitales ponen una pausa (hold) sobre la cantidad en disputa."),
    ],
    "sources": [
        ("CMS Medicare Physician Fee Schedule (2026)", "https://www.cms.gov/medicare/payment/fee-schedules/physician"),
        ("CMS National Correct Coding Initiative (NCCI) Edits", "https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-edits"),
        ("CFPB: Your Rights When Dealing With Debt Collectors", "https://www.consumerfinance.gov/ask-cfpb/what-are-my-rights-when-dealing-with-debt-collectors-en-1403/"),
        ("CFPB: Medical Debt and Credit Reporting Changes", "https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/"),
        ("No Surprises Act, CMS", "https://www.cms.gov/nosurprises"),
        ("NAIC: State Insurance Commissioner Directory", "https://www.naic.org/state_web_map.htm"),
    ],
}

NO_SURPRISES = {
    "slug": "ley-no-surprises-facturas-sorpresa",
    "en_slug": "no-surprises-act-explained",
    "title": "La ley No Surprises Act: qué cubre y qué no cubre",
    "description": "La ley No Surprises Act prohíbe la mayoría de las facturas médicas sorpresa, pero tiene límites. Vea qué cubre, qué no cubre y qué hacer si le cobran de más.",
    "answer": "La ley No Surprises Act (vigente desde enero de 2022) prohíbe el cobro de la diferencia (balance billing) en emergencias y cuando un proveedor fuera de la red atiende en un centro de la red. Tiene límites importantes: ambulancia terrestre, centros fuera de la red que usted eligió y ciertos tipos de planes no están cubiertos.",
    "body": """
<p class="lead">Antes de 2022, recibir atención de emergencia en un hospital fuera de la red, o incluso elegir un hospital de la red y recibir sin saberlo atención de un anestesiólogo fuera de la red, podía terminar en una factura sorpresa de miles de dólares. La ley No Surprises Act cambió eso en muchas situaciones. Pero tiene límites importantes, y saber qué está protegido y qué no puede ahorrarle mucho dinero.</p>

<nav class="toc">
    <h2>En esta guía</h2>
    <ol>
        <li><a href="#que-cubre">Qué cubre la ley</a></li>
        <li><a href="#que-no-cubre">Qué NO cubre</a></li>
        <li><a href="#costos">Cómo se calcula lo que usted paga</a></li>
        <li><a href="#idr">El proceso de resolución independiente de disputas (IDR)</a></li>
        <li><a href="#estimado">Estimado de buena fe para pacientes sin seguro</a></li>
        <li><a href="#cobro-indebido">Qué hacer si le cobran de más</a></li>
    </ol>
</nav>

<h2 id="que-cubre">Qué cubre la ley</h2>
<p>La ley se aplica a los servicios de emergencia y a los servicios que no son de emergencia cuando un proveedor fuera de la red lo atiende en un centro de la red. Estos son los casos protegidos:</p>
<h3>Atención de emergencia en cualquier centro</h3>
<p>Si recibe atención de emergencia en la sala de emergencias de cualquier hospital, esté o no en la red de su seguro, no le pueden cobrar más que lo que pagaría dentro de la red (deducible, copago y coseguro) por los servicios de emergencia. Esto aplica aunque:</p>
<ul>
    <li>lo hayan llevado al hospital más cercano y ese hospital estuviera fuera de la red,</li>
    <li>lo hayan estabilizado en un centro fuera de la red antes de trasladarlo,</li>
    <li>haya recibido atención posterior a la estabilización como paciente hospitalizado después de una admisión de emergencia.</li>
</ul>
<p>Cuando usted está estabilizado y se le puede trasladar con seguridad, se aplican las reglas de atención posterior a la estabilización: el proveedor debe avisarle que está fuera de la red y darle la opción de trasladarse a un centro de la red. Si usted acepta por escrito quedarse en el centro fuera de la red para seguir su atención, la protección contra el cobro de la diferencia termina para esa parte de su estadía.</p>
<h3>Proveedores fuera de la red en centros de la red</h3>
<p>Cuando programa un procedimiento en un hospital o centro de cirugía de la red, no siempre puede controlar qué proveedores lo atienden. La ley lo protege de facturas sorpresa de:</p>
<ul>
    <li><strong>Anestesiólogos</strong> que usted no eligió y que no pudo evitar razonablemente</li>
    <li><strong>Radiólogos</strong> que leen sus estudios de imágenes</li>
    <li><strong>Patólogos</strong> que analizan sus muestras de laboratorio</li>
    <li><strong>Hospitalistas</strong> o médicos consultores que su médico llamó</li>
    <li><strong>Neonatólogos</strong> que atendieron al recién nacido durante el parto</li>
    <li><strong>Cirujanos asistentes</strong> asignados por el centro y no elegidos por usted</li>
</ul>
<p>Con todos ellos, usted paga solo su parte dentro de la red. El proveedor y su aseguradora resuelven entre sí la diferencia de pago, sin que usted participe en esa diferencia.</p>
<h3>Ambulancia aérea</h3>
<p>La ambulancia aérea (helicóptero y avión) está totalmente protegida. Esté o no la empresa en la red de su seguro, usted paga solo su parte dentro de la red. Esta protección aplica a todos los planes grupales e individuales que no son “grandfathered” (planes anteriores a la ley ACA que no han cambiado de forma importante).</p>

<h2 id="que-no-cubre">Qué NO cubre la ley</h2>
<p>Conocer los límites es tan importante como conocer lo que cubre. En estas situaciones todavía puede recibir facturas sorpresa:</p>
<h3>Ambulancia terrestre</h3>
<p>La ambulancia terrestre quedó fuera de la ley original. El Congreso pidió a un comité asesor federal que estudiara por separado el cobro de la diferencia en ambulancias terrestres. CMS publicó reglas propuestas en 2024, pero hasta 2026 no se ha emitido la regla final. Si recibe una factura de ambulancia terrestre con un saldo mayor que su parte de costos, la ley federal no lo protege automáticamente, a menos que su estado tenga su propia ley sobre este cobro. Consulte el sitio web del comisionado de seguros de su estado.</p>
<h3>Centros fuera de la red que usted eligió voluntariamente</h3>
<p>Si eligió un hospital o centro fuera de la red para un procedimiento que no era de emergencia, y recibió y firmó un formulario de consentimiento adecuado que reconoce que está fuera de la red por lo menos 72 horas antes del servicio, la ley no lo protege del cobro de la diferencia por parte de ese centro. Los proveedores individuales fuera de la red en ese centro todavía pueden estar protegidos si usted no los eligió específicamente.</p>
<h3>Proveedores fuera de la red cuando usted sí tenía opción</h3>
<p>Si el centro le ofreció un proveedor de la red y usted eligió voluntariamente uno fuera de la red, le pueden cobrar la diferencia por los servicios de ese proveedor. La pregunta clave es si recibió y firmó un consentimiento válido por escrito por lo menos 72 horas antes del servicio. Un proveedor que no obtiene ese consentimiento por escrito no puede cobrarle la diferencia.</p>
<h3>Planes solo dentales o solo de la vista</h3>
<p>Los planes dentales o de la vista que se venden por separado no están sujetos a la ley. Los servicios de salud conductual tienen reglas más complejas que dependen de su tipo de plan.</p>
<h3>Planes de corto plazo y planes “grandfathered”</h3>
<p>Los planes de salud de duración limitada a corto plazo (short-term) y los planes “grandfathered” generalmente están exentos de la ley. Si tiene uno de estos planes, revise los documentos de su plan o consulte al comisionado de seguros de su estado para saber qué protecciones tiene.</p>

<h2 id="costos">Cómo se calcula lo que usted paga</h2>
<p>Cuando la ley aplica, su parte se calcula como si el proveedor fuera de la red estuviera dentro de la red. En la práctica:</p>
<ul>
    <li>El cargo cuenta para su <strong>deducible dentro de la red</strong>, no para el deducible más alto de fuera de la red</li>
    <li>Usted paga su <strong>coseguro o copago dentro de la red</strong></li>
    <li>Los cargos cuentan para su <strong>máximo de gastos de bolsillo dentro de la red</strong></li>
</ul>
<p>Si su aseguradora procesa el reclamo con tarifas de fuera de la red y le cobra más que su parte dentro de la red, eso no cumple con la ley. Primero presente una apelación interna ante su aseguradora, porque muchas veces es un error de procesamiento que se puede corregir. Si no lo corrigen, presente una queja ante el comisionado de seguros de su estado o ante el centro de ayuda federal (No Surprises Help Desk).</p>

<h2 id="idr">El proceso de resolución independiente de disputas (IDR)</h2>
<p>Cuando un proveedor fuera de la red y una aseguradora no se ponen de acuerdo sobre el pago, pueden llevar la disputa a la Resolución Independiente de Disputas federal (Independent Dispute Resolution, IDR):</p>
<ol>
    <li><strong>Negociación abierta (30 días).</strong> Después de que la aseguradora paga, el proveedor tiene 30 días para negociar directamente con ella. Usted no participa en esas negociaciones.</li>
    <li><strong>Inicio del IDR.</strong> Si la negociación falla, cualquiera de las partes puede iniciar el IDR federal dentro de los 4 días siguientes al fin del plazo de negociación. Las partes eligen una entidad independiente certificada o se les asigna una.</li>
    <li><strong>Arbitraje de “béisbol”.</strong> Cada parte presenta una sola cantidad de pago. La entidad debe elegir una de las dos; no puede dividir la diferencia. Debe dar un peso sustancial a la Cantidad Calificada de Pago (Qualifying Payment Amount, QPA), que es la tarifa mediana contratada dentro de la red que usa la aseguradora para ese servicio en esa zona.</li>
    <li><strong>Decisión final.</strong> La parte que pierde paga la tarifa administrativa del IDR (normalmente de $350 a $600 por disputa). El resultado es final y obligatorio.</li>
</ol>
<p><strong>Qué significa para usted como paciente:</strong> usted no es parte del IDR. Sea cual sea el resultado entre el proveedor y la aseguradora, usted paga solo su parte dentro de la red.</p>

<h2 id="estimado">Estimado de buena fe para pacientes sin seguro</h2>
<p>La ley creó una protección aparte para pacientes sin seguro o que pagan por su cuenta (self-pay): el Estimado de Buena Fe (Good Faith Estimate, GFE). Todo proveedor que programe un servicio que no es de emergencia para un paciente sin seguro o que paga por su cuenta debe dar un GFE por escrito por lo menos un día hábil antes del servicio. El GFE debe incluir:</p>
<ul>
    <li>Los cargos esperados por el servicio principal y por todos los servicios adicionales previstos (laboratorios, anestesia, cirujanos asistentes)</li>
    <li>Los códigos de diagnóstico, los códigos de servicio y el cargo esperado de cada artículo</li>
    <li>El nombre, el NPI y el número de identificación fiscal de cada proveedor incluido</li>
</ul>
<p>Si su factura final supera el GFE por más de $400, usted puede iniciar la Resolución de Disputas entre Paciente y Proveedor (Patient-Provider Dispute Resolution, PPDR) dentro de los 120 días de recibir la factura. La tarifa de presentación es de $25. Si la decisión es a su favor, el proveedor le devuelve la tarifa y debe aceptar un pago igual o cercano al GFE.</p>
<p>Las protecciones contra el cobro de la diferencia se aplican principalmente a pacientes con seguro.</p>

<h2 id="cobro-indebido">Qué hacer si le cobran de más</h2>
<p>Si recibe una factura que cree que no cumple con la ley No Surprises Act, siga estos pasos en orden:</p>
<ol>
    <li><strong>Revise su EOB.</strong> Verifique que su aseguradora procesó el reclamo con tarifas de dentro de la red. Muchos casos parecidos son en realidad errores de procesamiento. Llame primero a su aseguradora y pida que vuelvan a procesar el reclamo según la ley.</li>
    <li><strong>Escriba al proveedor.</strong> Diga que el servicio está sujeto a la ley No Surprises Act, que su parte debe calcularse con tarifas de dentro de la red y pida una factura corregida. Envíela por correo certificado y guarde el número de rastreo.</li>
    <li><strong>Presente una queja federal.</strong> Llame al No Surprises Help Desk al <strong>1-800-985-3059</strong> o presente la queja en línea en <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener" lang="en">cms.gov/nosurprises</a>. CMS y el Departamento de Trabajo comparten la responsabilidad de hacer cumplir la ley. Los proveedores que no la cumplen pueden recibir multas civiles de hasta $10,000 por violación.</li>
    <li><strong>Presente una queja estatal.</strong> El comisionado de seguros de su estado puede tener autoridad al mismo tiempo. Muchos estados tienen procesos rápidos para quejas sobre facturas sorpresa.</li>
    <li><strong>No pague el saldo en disputa mientras la queja siga abierta.</strong> Pida al proveedor que ponga la cuenta en espera (billing hold). Pagar el saldo no le quita sus derechos, pero complica el reembolso.</li>
</ol>
<p>Guarde la factura, la EOB de su aseguradora y todas sus comunicaciones con el proveedor.</p>
<div class="key-takeaway">
    <strong>¿No está seguro de si su factura cumple con la ley?</strong> <a href="/es/escanear/">Vea cómo funciona la revisión de BillKarma</a>. Esta guía es información general, no asesoría legal. Si necesita ayuda legal, consulte a un abogado de consumidores o a una organización de asistencia legal.
</div>
""",
    "faqs": [
        ("¿La ley No Surprises Act cubre las facturas de ambulancia terrestre?", "No, todavía no. La ambulancia terrestre quedó fuera de la ley original mientras un comité asesor federal estudiaba el tema. Hasta 2026, CMS ha propuesto reglas para extender las protecciones a la ambulancia terrestre, pero no se ha emitido la regla final. La ambulancia aérea (helicóptero y avión) sí está totalmente protegida. Revise el sitio web del comisionado de seguros de su estado para ver si hay protecciones estatales contra el cobro de la diferencia en ambulancias terrestres."),
        ("¿Qué hago si un proveedor me cobra la diferencia y creo que no cumple con la ley?", "Presente una queja de inmediato. Puede llamar al No Surprises Help Desk federal al 1-800-985-3059 o presentarla en línea en CMS.gov. También puede presentarla ante el comisionado de seguros de su estado. Los proveedores que no cumplen con la ley pueden recibir multas civiles de hasta $10,000 por violación. Guarde la factura, la EOB de su aseguradora y todas las comunicaciones con el proveedor."),
        ("¿La ley No Surprises Act aplica a pacientes que pagan por su cuenta?", "Las protecciones contra el cobro de la diferencia se aplican principalmente a pacientes con seguro. Pero la ley también creó el requisito del Estimado de Buena Fe: los proveedores deben dar a los pacientes sin seguro o que pagan por su cuenta un estimado de costos por escrito antes de los servicios programados. Si su factura final supera el estimado por más de $400, usted tiene derecho a disputarla mediante el proceso de resolución de disputas entre paciente y proveedor."),
    ],
    "sources": [
        ("CMS: No Surprises Act Resources and Consumer Tools", "https://www.cms.gov/nosurprises"),
        ("HHS: No Surprises Act Consumer Protections Fact Sheet", "https://www.hhs.gov/sites/default/files/surprise-billing-consumer-protections.pdf"),
        ("KFF: No Surprises Act Implementation and Consumer Impact (2024)", "https://www.kff.org/health-costs/issue-brief/no-surprises-act-implementation/"),
        ("DOL: No Surprises Act, Group Health Plan Requirements", "https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/no-surprises-act"),
        ("CMS: Independent Dispute Resolution Process Overview", "https://www.cms.gov/files/document/idr-process-overview.pdf"),
    ],
}

GUIDES = [ITEMIZED, DISPUTE, NO_SURPRISES]
