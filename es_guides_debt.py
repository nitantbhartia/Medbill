"""Spanish guides on financial help and medical debt. Machine-drafted translations: need native review.

Each guide translates one English guide (en_slug) and adds no new facts.
"""

FINANCIAL_ASSISTANCE = {
    "slug": "asistencia-financiera-hospital",
    "en_slug": "hospital-financial-assistance-charity-care",
    "title": "Asistencia financiera del hospital (charity care): ¿califica?",
    "description": "Los hospitales sin fines de lucro deben tener una política de asistencia financiera. Vea los límites de ingresos típicos, cómo solicitarla y qué hacer si la niegan.",
    "answer": "Los hospitales sin fines de lucro deben tener una política de asistencia financiera (financial assistance, también llamada charity care) que reduce o elimina la factura según sus ingresos. Puede solicitarla aunque ya haya recibido la factura y aunque tenga seguro.",
    "body": """
<p class="lead">Muchos hospitales sin fines de lucro de Estados Unidos ofrecen atención gratuita o con descuento, pero muchos pacientes no saben que pueden pedirla. Si sus ingresos son menores de $62,400 como persona sola, o de $128,800 para una familia de cuatro, es posible que califique para atención gratuita o con un descuento grande, incluso después de recibir la factura. Aquí le explicamos cómo solicitarla. No podemos garantizar que el hospital apruebe su solicitud.</p>

<nav class="toc">
    <h2>En esta guía</h2>
    <ol>
        <li><a href="#que-es">Qué es la asistencia financiera</a></li>
        <li><a href="#quien-califica">Quién califica</a></li>
        <li><a href="#su-hospital">Cómo saber si su hospital la ofrece</a></li>
        <li><a href="#como-solicitar">Cómo solicitarla, paso a paso</a></li>
        <li><a href="#importante">Cosas importantes que debe saber</a></li>
    </ol>
</nav>

<h2 id="que-es">1. Qué es la asistencia financiera</h2>
<p>La asistencia financiera de un hospital, también llamada <strong>charity care</strong> o atención para personas de bajos recursos (indigent care), es un programa que reduce o elimina la factura de pacientes que no pueden pagar. Son nombres distintos para lo mismo: un descuento o una cancelación de la deuda (write-off) según sus ingresos.</p>
<p>Según la <strong>Sección 501(r) del IRS</strong> (el servicio de impuestos de Estados Unidos), todo hospital sin fines de lucro debe tener por escrito una <strong>Política de Asistencia Financiera (Financial Assistance Policy, FAP)</strong>. Alrededor del 60% de los hospitales del país son sin fines de lucro, así que la mayoría debe ofrecer este programa. Es una condición para mantener su exención de impuestos.</p>
<p>La asistencia financiera normalmente cubre:</p>
<ul>
    <li><strong>Hospitalizaciones:</strong> cirugías, estadías de una noche o más, cuidados intensivos</li>
    <li><strong>Procedimientos ambulatorios:</strong> cirugías del mismo día, pruebas de diagnóstico, infusiones</li>
    <li><strong>Visitas a la sala de emergencias,</strong> sea que lo hayan hospitalizado o no</li>
    <li><strong>Honorarios de médicos:</strong> algunos hospitales incluyen los cobros de médicos que se facturan por medio del hospital (no siempre)</li>
</ul>
<p>La asistencia se puede aplicar <strong>de forma retroactiva</strong>. Es decir, puede solicitarla aunque ya haya recibido la factura, haya hecho pagos parciales o facturación ya se haya comunicado con usted. Muchos hospitales aceptan solicitudes hasta 240 días después del primer estado de cuenta.</p>

<h2 id="quien-califica">2. Quién califica</h2>
<p>La elegibilidad depende principalmente de los ingresos de su hogar en comparación con el <strong>Nivel Federal de Pobreza (Federal Poverty Level, FPL)</strong>. El FPL es una cifra que el gobierno fija cada año como referencia para varios programas de ayuda. Cada hospital decide sus propios límites, pero la mayoría sigue un patrón parecido:</p>
<table>
    <thead>
        <tr><th>Ingresos (% del FPL)</th><th>Persona sola (2026)</th><th>Familia de 4 (2026)</th><th>Ayuda típica</th></tr>
    </thead>
    <tbody>
        <tr><td>Menos de 200% del FPL</td><td>Menos de $31,200</td><td>Menos de $64,400</td><td>Atención gratuita: se cancela toda la factura</td></tr>
        <tr><td>200% a 300% del FPL</td><td>$31,200 a $46,800</td><td>$64,400 a $96,600</td><td>Descuento de 50% a 80%</td></tr>
        <tr><td>300% a 400% del FPL</td><td>$46,800 a $62,400</td><td>$96,600 a $128,800</td><td>Descuento de 25% a 50%</td></tr>
    </tbody>
</table>
<p><strong>Importante:</strong> estos son límites típicos. Algunos hospitales son más generosos. Grandes sistemas de salud como Kaiser Permanente, Providence y CommonSpirit ofrecen ayuda hasta 400% del FPL o más, y unos pocos hospitales dan descuentos parciales hasta 500% del FPL. Revise la política de su hospital.</p>
<p>Además de los ingresos, los hospitales pueden considerar:</p>
<ul>
    <li><strong>Bienes y ahorros (asset tests):</strong> algunos hospitales los revisan y muchos no. Si su hospital los cuenta, la vivienda principal y las cuentas de jubilación normalmente se excluyen.</li>
    <li><strong>Circunstancias especiales:</strong> perder el empleo, un divorcio, una nueva enfermedad grave, deudas médicas anteriores u otras dificultades pueden fortalecer su solicitud aunque sus ingresos estén un poco por encima del límite.</li>
    <li><strong>Carga de deuda médica:</strong> si sus facturas médicas superan cierto porcentaje de sus ingresos (a menudo de 10% a 25%), algunos hospitales lo aceptan aun con ingresos más altos.</li>
    <li><strong>Seguro:</strong> no es necesario estar sin seguro. Los pacientes con seguro pueden pedir ayuda con sus gastos de bolsillo (deducibles, coseguro y copagos).</li>
</ul>

<h2 id="su-hospital">3. Cómo saber si su hospital la ofrece</h2>
<p>Primero, averigüe si su hospital es sin fines de lucro. Alrededor del 60% de los hospitales de Estados Unidos lo son, incluidos la mayoría de los sistemas más grandes. Puede buscar su hospital en nuestro <a href="/hospitals/" lang="en">directorio de hospitales</a> (en inglés).</p>
<p>Todo hospital sin fines de lucro debe:</p>
<ul>
    <li>publicar su política de asistencia financiera (FAP) en su sitio web,</li>
    <li>dar un resumen de la política en lenguaje sencillo,</li>
    <li>tener copias en papel disponibles si usted las pide,</li>
    <li>informar a los pacientes sobre la política antes de tomar medidas de cobro.</li>
</ul>
<p>En la política busque: los criterios de elegibilidad (límites de ingresos como % del FPL y ajustes por tamaño de la familia), los servicios cubiertos, cómo se solicita y qué documentos se necesitan, si a los pacientes que califican se les cobra no más que las tarifas de Medicare u otras similares, y qué medidas de cobro no tomará el hospital contra ellos.</p>
<p><strong>Cómo encontrar la política:</strong></p>
<ol>
    <li><strong>Sitio web del hospital:</strong> busque “financial assistance”, “charity care” o “patient financial services”. A menudo está en la sección “Billing” o “Patients &amp; Visitors”.</li>
    <li><strong>Llame a facturación:</strong> pida la solicitud de asistencia financiera. Deben dársela.</li>
</ol>

<h2 id="como-solicitar">4. Cómo solicitarla, paso a paso</h2>
<h3>Paso 1: Consiga la solicitud</h3>
<p>Búsquela en el sitio web del hospital en “billing” o “patient financial services”. También puede llamar al número de su estado de cuenta y decir, en inglés: <em lang="en">“I’d like to apply for financial assistance. Can you send me the application?”</em> Muchos hospitales tienen consejeros financieros para pacientes que pueden guiarlo en persona.</p>
<h3>Paso 2: Reúna sus documentos</h3>
<p>La mayoría de las solicitudes piden:</p>
<ul>
    <li><strong>Comprobante de ingresos:</strong> dos o tres talones de pago recientes o su declaración de impuestos más reciente (Formulario 1040). Si está desempleado, una carta de su último empleador o un comprobante de beneficios de desempleo.</li>
    <li><strong>Declaración de impuestos:</strong> la declaración federal más reciente (Formulario 1040). Algunos hospitales aceptan solo las páginas 1 y 2.</li>
    <li><strong>Estados de cuenta bancarios:</strong> de uno a tres meses de cuentas de cheques y ahorros. No todos los hospitales los piden.</li>
    <li><strong>Prueba de dificultad económica</strong> (si aplica): aviso de despido, sentencia de divorcio, otras facturas médicas, carta de determinación de discapacidad o cualquier documento de un cambio financiero.</li>
    <li><strong>Información del hogar:</strong> cuántas personas viven en su hogar, porque los límites del FPL cambian según el tamaño de la familia.</li>
</ul>
<h3>Paso 3: Llene la solicitud</h3>
<p>Llene todos los campos. Las solicitudes incompletas son la causa más común de demoras y rechazos. Si una pregunta no aplica, escriba “N/A” en lugar de dejarla en blanco. Incluya una carta breve que explique su situación en una o dos frases, por ejemplo: “Solicito asistencia financiera para mi estadía en el hospital el [fecha]. Mis ingresos anuales del hogar son $[cantidad] para una familia de [número].”</p>
<h3>Paso 4: Envíela y dé seguimiento</h3>
<p>Envíela como indique el hospital: normalmente por correo, fax, correo electrónico o en persona en la oficina de servicios financieros al paciente. Guarde copias de todo. Llame para confirmar que la recibieron en un plazo de 5 días hábiles. Pida un número de referencia y el nombre de la persona que lleva su caso. Pida que pongan su cuenta en espera durante la revisión para que no pase a cobros.</p>
<h3>Paso 5: Si la niegan, apele</h3>
<ol>
    <li><strong>Pida la razón del rechazo por escrito.</strong> Las razones comunes son: solicitud incompleta, ingresos por encima del límite o documentos que faltan.</li>
    <li><strong>Corrija el problema y vuelva a enviarla.</strong> Si faltaban documentos, agréguelos. Si sus ingresos están cerca del límite, incluya pruebas de circunstancias especiales (otras deudas médicas, pérdida reciente de empleo, costos de tratamiento continuo).</li>
    <li><strong>Escale el caso si es necesario.</strong> Contacte al defensor del paciente del hospital. Si eso no funciona, presente una queja ante la división de protección al consumidor de la oficina del <strong>fiscal general de su estado (attorney general)</strong>, que investiga a hospitales que no cumplen con sus obligaciones de asistencia financiera.</li>
</ol>

<h2 id="importante">5. Cosas importantes que debe saber</h2>
<h3>Puede solicitarla después de recibir la factura</h3>
<p>Muchos pacientes creen que la asistencia financiera se arregla antes del tratamiento. No es así. Según las reglas del IRS, los hospitales deben aceptar solicitudes por lo menos 240 días después del primer estado de cuenta. Algunos las aceptan más tarde. Si recibió una factura hace semanas o meses, todavía puede solicitarla. Lo importante es hacerlo antes de que la factura pase a cobros.</p>
<h3>Puede solicitarla aunque tenga seguro</h3>
<p>La asistencia financiera no es solo para personas sin seguro. Si su seguro le dejó un deducible, coseguro o copago grande, puede pedir ayuda con la <strong>parte que le toca pagar a usted</strong>. Esto es muy útil para quienes tienen planes de deducible alto y gastos de bolsillo de $3,000 a $8,000.</p>
<h3>Algunos hospitales deben limitar el cobro a tarifas parecidas a Medicare</h3>
<p>Según la ley ACA (Affordable Care Act) y la Sección 501(r) del IRS, los hospitales sin fines de lucro no pueden cobrar a pacientes que califican más que los <strong>montos generalmente facturados (amounts generally billed, AGB)</strong> a pacientes con seguro. En la práctica, esto suele significar que a los pacientes que califican se les cobra cerca de las tarifas de Medicare, que pueden ser de 50% a 80% menos que el precio del chargemaster. Esto aplica aunque solo califique para un descuento parcial.</p>
<h3>Si el hospital no sigue su propia política</h3>
<p>La exención de impuestos de un hospital sin fines de lucro vale millones de dólares al año. Si el IRS encuentra que un hospital no cumple con los requisitos de la Sección 501(r), incluida la administración correcta de su programa de asistencia financiera, el hospital arriesga esa exención. Si cree que el hospital no sigue su política, puede presentar una queja ante el IRS o ante el fiscal general de su estado.</p>
<h3>Un rechazo no es la respuesta final</h3>
<p>Puede apelar con más documentos, escalar al defensor del paciente o presentar una queja ante el fiscal general de su estado. También puede <a href="/es/guias/como-disputar-factura-medica/">disputar cargos específicos</a> de la factura, por separado del proceso de asistencia financiera.</p>
<div class="key-takeaway">
    <strong>Antes de solicitarla,</strong> puede <a href="/es/escanear/">revisar su factura con lo que paga Medicare</a> para tener una lista de puntos que preguntar. La herramienta está en inglés.
</div>
""",
    "faqs": [
        ("¿Puedo solicitar asistencia financiera después de recibir la factura del hospital?", "Sí. La mayoría de los hospitales aceptan solicitudes hasta 240 días después del primer estado de cuenta posterior al alta. Algunos extienden ese plazo. Puede solicitarla aunque ya haya hecho pagos parciales o tenga un plan de pagos. Lo importante es hacerlo antes de que la factura pase a cobros. Llame a facturación y pida la solicitud: deben dársela."),
        ("¿La asistencia financiera afecta mi puntaje de crédito?", "No. Recibir asistencia financiera no aparece en su informe de crédito ni afecta su puntaje. No es un préstamo ni una línea de crédito: es un descuento o una cancelación que se aplica a su cuenta del hospital. Desde 2023, las tres agencias principales de crédito ya no incluyen en los informes la deuda médica menor de $500, y las cuentas médicas en cobros que ya se pagaron se eliminan."),
        ("¿Puedo recibir asistencia financiera si tengo seguro médico?", "Sí. Muchas políticas de asistencia financiera cubren la parte que le toca pagar a usted, incluidos deducibles, coseguro y copagos. Si su seguro le dejó un saldo grande de bolsillo y sus ingresos califican, puede pedir ayuda con la cantidad que debe después de que el seguro pagó su parte."),
        ("¿Y si mi hospital es con fines de lucro?", "Según la Sección 501(r) del IRS, los hospitales con fines de lucro no están obligados a ofrecer asistencia financiera, pero muchos tienen programas de dificultad económica o políticas de descuento. Llame a facturación y pregunte por descuentos para pacientes que pagan por su cuenta, programas de dificultad económica o planes de pago. También puede negociar directamente usando las tarifas de Medicare como punto de comparación."),
        ("¿Cuánto tarda el proceso de solicitud?", "La mayoría de los hospitales procesan las solicitudes en 30 a 45 días. Algunos dan una decisión preliminar en dos semanas. Durante la revisión, su cuenta debería estar en espera para que no pase a cobros. Si no recibe respuesta en 30 días, llame a servicios financieros al paciente para preguntar cómo va."),
        ("¿Qué pasa si me niegan la asistencia financiera?", "Tiene derecho a apelar. Pida la razón del rechazo por escrito y envíe documentos adicionales que respondan a esa razón. Las razones comunes son solicitudes incompletas o documentos que faltan. Si la apelación también se niega, puede escalar al defensor del paciente del hospital, contactar a la división de protección al consumidor del fiscal general de su estado o pedir un plan de pagos con la tarifa reducida que ofrece el hospital."),
    ],
    "sources": [
        ("IRS Section 501(r)(4): Financial Assistance Policy Requirements for Charitable Hospitals", "https://www.irs.gov/charities-non-profits/financial-assistance-policy-and-emergency-medical-care-policy-section-501r4"),
        ("CMS Medicare Physician Fee Schedule (2026)", "https://www.cms.gov/medicare/payment/fee-schedules/physician"),
        ("KFF: Charitable Hospital Financial Assistance and Community Benefits", "https://www.kff.org/health-costs/issue-brief/charitable-hospitals-financial-assistance-and-community-benefits/"),
        ("ASPE/HHS Federal Poverty Level Guidelines (2026)", "https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines"),
        ("CFPB: Medical Debt and Credit Reporting Changes", "https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/"),
    ],
}

CANT_AFFORD = {
    "slug": "no-puedo-pagar-factura-medica",
    "en_slug": "cant-afford-medical-bill",
    "title": "No puedo pagar mi factura médica: 7 opciones antes de que pase a cobros",
    "description": "Si no puede pagar una factura médica, tiene opciones: asistencia financiera, negociar, plan de pagos y más. Actúe antes de que pase a cobros. Información general.",
    "answer": "Antes de pagar, revise la factura por errores. Después solicite asistencia financiera (charity care), negocie el total y pida un plan de pagos sin intereses. Mientras más pronto actúe, más opciones tiene. Nadie puede garantizar el resultado: depende del hospital.",
    "body": """
<p class="lead">Una encuesta de KFF de 2024 encontró que <strong>41% de los adultos, unos 100 millones de personas, tienen algún tipo de deuda médica</strong>. Lo que mucha gente no sabe es que los hospitales prefieren llegar a un acuerdo con usted antes que enviar su factura a cobros (collections), donde recuperan solo de 4 a 7 centavos por cada dólar. Eso deja espacio para negociar.</p>

<nav class="toc">
    <h2>En esta guía</h2>
    <ol>
        <li><a href="#no-ignore">Por qué no debe ignorar una factura médica</a></li>
        <li><a href="#siete-opciones">7 opciones cuando no puede pagar</a></li>
        <li><a href="#cual-elegir">¿Cuál opción le conviene?</a></li>
        <li><a href="#que-decir">Qué decir cuando llame a facturación</a></li>
    </ol>
</nav>

<h2 id="no-ignore">1. Por qué no debe ignorar una factura médica</h2>
<p>Una factura que no puede pagar parece imposible, y muchas personas la dejan a un lado esperando que se resuelva sola. No se resuelve. Esto es lo que pasa si no hace nada:</p>
<table>
    <thead><tr><th>Tiempo</th><th>Qué pasa</th><th>Su margen de acción</th></tr></thead>
    <tbody>
        <tr><td>Días 1 a 30</td><td>El hospital envía la primera factura</td><td><strong>El más alto:</strong> todas las opciones están abiertas</td></tr>
        <tr><td>Días 30 a 90</td><td>Avisos de pago atrasado y llamadas de facturación</td><td><strong>Alto:</strong> todavía puede negociar y pedir ayuda</td></tr>
        <tr><td>Días 90 a 120</td><td>Cobros internos; pueden cobrar recargos</td><td><strong>Medio:</strong> las opciones se reducen</td></tr>
        <tr><td>Días 120 a 180</td><td>Pasa a una agencia de cobros externa</td><td><strong>Menor:</strong> ya trata con un tercero</td></tr>
        <tr><td>12 meses o más</td><td>Puede aparecer en su informe de crédito (si es de más de $500)</td><td><strong>El más bajo,</strong> pero no es cero</td></tr>
    </tbody>
</table>
<p>El mensaje es sencillo: <strong>mientras más pronto actúe, más puede ahorrar.</strong> Todas las opciones de abajo son más fáciles y eficaces antes de que la factura llegue a cobros.</p>

<h2 id="siete-opciones">2. 7 opciones cuando no puede pagar</h2>
<h3>Opción 1: Revise la factura por errores</h3>
<p>Antes de pagar nada, asegúrese de que la factura sea correcta. Los errores de facturación son comunes: cargos duplicados, pruebas de laboratorio cobradas por separado, servicios que no recibió o cargos que el seguro debió cubrir. Estos son hallazgos frecuentes:</p>
<ul>
    <li>Cargos duplicados (el mismo código cobrado dos veces)</li>
    <li>Pruebas de laboratorio cobradas por separado en lugar de como un panel (cuesta de 2 a 3 veces más)</li>
    <li>Seguro que no se aplicó (reclamos que nunca se enviaron o que se rechazaron por error)</li>
    <li>Visitas cobradas con un nivel más alto que el que ocurrió (upcoding)</li>
</ul>
<p>Pida su <a href="/es/guias/como-obtener-factura-detallada-hospital/">factura detallada</a> o <a href="/es/escanear/">vea cómo funciona la revisión de BillKarma</a> (en inglés).</p>

<h3>Opción 2: Solicite asistencia financiera del hospital (charity care)</h3>
<p>Si el hospital es sin fines de lucro (alrededor del 60% de los hospitales de Estados Unidos lo son), debe ofrecer asistencia financiera según la Sección 501(r) del IRS. Los límites de ingresos suelen ser más amplios de lo que la gente espera. Por ejemplo, con ingresos menores de 200% del Nivel Federal de Pobreza (FPL) (menos de $31,200 para una persona sola o menos de $64,400 para una familia de 4), la ayuda típica es atención gratuita. Con ingresos de 200% a 300% del FPL, el descuento típico es de 50% a 80%, y con 300% a 400%, de 25% a 50%. Puede solicitarla aunque ya tenga la factura: muchos hospitales aceptan solicitudes hasta 240 días después. Vea nuestra guía de <a href="/es/guias/asistencia-financiera-hospital/">asistencia financiera</a>.</p>

<h3>Opción 3: Negocie el total</h3>
<p>Llame a facturación y negocie. El precio de lista no es el precio final. Algunas estrategias:</p>
<ul>
    <li><strong>Pida el descuento para pacientes que pagan por su cuenta (self-pay discount).</strong> Muchos hospitales dan de 20% a 40% de descuento.</li>
    <li><strong>Mencione la tarifa de Medicare.</strong> Busque lo que paga Medicare por cada código CPT. Puede ofrecer pagar de 150% a 200% de la tarifa de Medicare, que sigue siendo mucho menos que lo que cobran muchos hospitales.</li>
    <li><strong>Ofrezca un pago único.</strong> “Puedo pagar $X hoy para resolver esto” funciona bien. Los hospitales prefieren un pago ahora que perseguirlo durante meses.</li>
</ul>

<h3>Opción 4: Pida un plan de pagos</h3>
<ul>
    <li>Los hospitales suelen ofrecer planes de pago, y casi siempre son <strong>sin intereses</strong>.</li>
    <li>La cuota mensual debe basarse en lo que usted realmente puede pagar, no en lo que sugiere el hospital.</li>
    <li>Pida el acuerdo del plan de pagos por escrito antes de hacer el primer pago.</li>
    <li><strong>En general, no conviene pagar facturas médicas con tarjeta de crédito:</strong> cambiaría el 0% de interés del hospital por un interés de 20% a 30% de la tarjeta.</li>
</ul>

<h3>Opción 5: Apele los rechazos de su seguro</h3>
<p>Si su seguro rechazó parte de la factura, tiene derecho a apelar. La tasa de éxito de la primera apelación va de 40% a 60% según el tipo de rechazo. Rechazos comunes que vale la pena apelar:</p>
<ul>
    <li>“No es médicamente necesario”: su médico puede dar documentación de apoyo</li>
    <li>“Fuera de la red”: la ley <a href="/es/guias/ley-no-surprises-facturas-sorpresa/">No Surprises Act</a> puede protegerlo</li>
    <li>“Se requería autorización previa” (prior authorization): si fue una emergencia, no se requiere autorización</li>
</ul>

<h3>Opción 6: Pregunte por la cobertura retroactiva de Medicaid</h3>
<p>En la mayoría de los estados, Medicaid puede cubrir facturas médicas hasta <strong>3 meses antes de la fecha de su solicitud</strong>. Si sus ingresos son lo bastante bajos para calificar ahora, puede cubrir facturas que ya recibió. Es uno de los programas que menos se usan.</p>

<h3>Opción 7: Busque programas de ayuda de su estado</h3>
<p>Muchos estados tienen programas más allá de los requisitos federales:</p>
<ul>
    <li><strong>California:</strong> la ley AB 1020 limita las facturas de hospital a lo que usted habría pagado con Medi-Cal si tiene ingresos menores de 400% del FPL</li>
    <li><strong>Nueva York:</strong> la Ley de Asistencia Financiera de Hospitales cubre a pacientes sin seguro con ingresos de hasta 300% del FPL</li>
    <li><strong>Illinois:</strong> la ley de descuentos para pacientes sin seguro (Hospital Uninsured Patient Discount Act) exige descuentos para pacientes con ingresos menores de 600% del FPL</li>
    <li><strong>Colorado:</strong> el programa Hospital Discounted Care tiene una escala móvil según los ingresos</li>
</ul>

<h2 id="cual-elegir">3. ¿Cuál opción le conviene?</h2>
<table>
    <thead><tr><th>Su situación</th><th>Mejor primer paso</th></tr></thead>
    <tbody>
        <tr><td>Ingresos menores de $64,400 (familia de 4)</td><td>Solicitar <a href="/es/guias/asistencia-financiera-hospital/">asistencia financiera</a> primero</td></tr>
        <tr><td>Sospecha que hay errores de facturación</td><td><a href="/es/guias/como-disputar-factura-medica/">Revisar y disputar</a> los cargos</td></tr>
        <tr><td>El seguro rechazó la cobertura</td><td>Apelar el rechazo ante la aseguradora</td></tr>
        <tr><td>Puede pagar algo, pero no el precio completo</td><td>Negociar usando las tarifas de Medicare</td></tr>
        <tr><td>No puede pagar nada por ahora</td><td>Pedir un plan de pagos sin intereses</td></tr>
        <tr><td>Ya está en cobros</td><td>Conocer sus derechos con los cobradores y negociar; consulte a un abogado de consumidores si recibe un aviso del tribunal</td></tr>
    </tbody>
</table>

<h2 id="que-decir">4. Qué decir cuando llame a facturación</h2>
<p>El personal de facturación suele hablar inglés. Aquí tiene tres ejemplos con la frase en inglés y su significado.</p>
<h3>Para pedir asistencia financiera</h3>
<p lang="en">“Hi, I received a bill for [amount] and I’m having difficulty paying it. I’d like to apply for your financial assistance program. Can you send me the application? My household income is [amount] and there are [number] people in my household.”</p>
<p>Significa: recibí una factura y me cuesta pagarla; quiero solicitar asistencia financiera; ¿pueden enviarme la solicitud? Mis ingresos del hogar son [cantidad] y somos [número] personas.</p>
<h3>Para negociar una cantidad menor</h3>
<p lang="en">“I’ve reviewed my bill and I’d like to discuss the charges. I looked up the Medicare rates for the procedures I received, and the total Medicare reimbursement would be about [amount]. I’d like to propose paying [150-200% of Medicare] to resolve this bill. I can pay that as a lump sum today.”</p>
<p>Significa: revisé mi factura y busqué las tarifas de Medicare; propongo pagar de 150% a 200% de esa tarifa en un solo pago hoy.</p>
<h3>Para pedir un plan de pagos</h3>
<p lang="en">“I want to pay this bill, but I can’t pay it all at once. I can afford [amount] per month. Can we set up a zero-interest payment plan? I’d like to get the agreement in writing before I start payments.”</p>
<p>Significa: quiero pagar, pero no todo a la vez; puedo pagar [cantidad] al mes; ¿podemos hacer un plan sin intereses? Quiero el acuerdo por escrito antes de empezar.</p>
<div class="key-takeaway">
    <strong>Esta guía es información general, no asesoría legal ni financiera.</strong> Para saber cuándo la deuda médica puede aparecer en su informe de crédito, lea <a href="/es/guias/deuda-medica-informe-de-credito/">la deuda médica y su informe de crédito</a>. Si le llega un aviso de un tribunal, consulte cuanto antes a un abogado de consumidores o a una organización de asistencia legal.
</div>
""",
    "faqs": [
        ("¿Qué pasa si no puedo pagar mi factura médica?", "Si no hace nada, el hospital enviará avisos de recordatorio durante 30 a 90 días, luego pasará la cuenta a cobros internos y, por último, a una agencia de cobros externa (normalmente después de 120 a 180 días). Antes de eso tiene varias opciones: solicitar asistencia financiera (charity care), negociar una cantidad menor, pedir un plan de pagos, revisar si hay errores o disputar cargos que su seguro debió cubrir. Mientras más pronto actúe, más opciones tiene."),
        ("¿Puedo negociar una factura médica que no puedo pagar?", "Sí. Los hospitales y los proveedores médicos negocian facturas con regularidad. Puede pedir un descuento para pacientes que pagan por su cuenta (normalmente de 20% a 40%), negociar un total menor usando las tarifas de Medicare o pedir un plan de pagos sin intereses. Lo importante es llamar a facturación antes de que la factura pase a cobros. Muchos hospitales prefieren aceptar una cantidad reducida antes que enviar la factura a un cobrador, donde recuperan solo de 4 a 7 centavos por dólar."),
        ("¿La deuda médica afecta mi puntaje de crédito?", "La deuda médica menor de $500 ya no aparece en los informes de crédito. Las cuentas médicas en cobros que ya se pagaron se eliminan. La deuda médica sin pagar de más de $500 no puede aparecer hasta después de un período de espera de 12 meses. Eso le da tiempo para resolver la factura con asistencia financiera, negociación o un plan de pagos antes de cualquier efecto en su crédito. Para los detalles y los cambios más recientes, lea nuestra guía sobre la deuda médica y su informe de crédito."),
        ("¿Puede el hospital llevarme a la corte si no puedo pagar?", "Los hospitales rara vez llevan a los pacientes a la corte directamente por deudas médicas. Es más probable que envíen la factura a cobros. Sin embargo, las agencias de cobro sí pueden presentar casos en la corte, sobre todo con saldos de más de $5,000. Cada estado tiene un plazo límite (statute of limitations) para la deuda médica, normalmente de 3 a 6 años. Para evitar llegar a ese punto, atienda la factura pronto con asistencia financiera, negociación o un plan de pagos. Si recibe un aviso de un tribunal, consulte a un abogado."),
        ("¿Cuál es la mejor forma de pagar una deuda médica?", "Empiece por revisar la factura por errores y por solicitar asistencia financiera (si el hospital es sin fines de lucro). Después negocie el saldo restante: pida un descuento para pacientes que pagan por su cuenta u ofrezca pagar una suma única reducida. Si no puede pagar todo, pida al hospital un plan de pagos sin intereses. Evite poner la deuda médica en tarjetas de crédito, que cobran intereses. Los planes de pago de hospitales casi siempre son sin intereses."),
    ],
    "sources": [
        ("KFF: Health Care Debt Survey (2024)", "https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/"),
        ("IRS Section 501(r): Nonprofit Hospital Financial Assistance Requirements", "https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3"),
        ("CFPB: Medical Debt and Credit Reporting Changes", "https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/"),
        ("CMS Medicare Physician Fee Schedule (2026)", "https://www.cms.gov/medicare/payment/fee-schedules/physician"),
        ("Commonwealth Fund: Medical Debt and Health Outcomes Survey (2023)", "https://www.commonwealthfund.org/publications/surveys/2023/oct/paying-for-it-costs-debt-americans-sicker-poorer"),
        ("Experian: Medical Debt Credit Reporting Changes (2023)", "https://www.experian.com/blogs/ask-experian/medical-debt-and-your-credit-score/"),
    ],
}

CREDIT_REPORT = {
    "slug": "deuda-medica-informe-de-credito",
    "en_slug": "medical-debt-credit-report-2026",
    "title": "La deuda médica y su informe de crédito en 2026",
    "description": "Las reglas sobre la deuda médica en los informes de crédito cambiaron en 2025 y 2026. Vea qué se reporta, qué protecciones hay por estado y cómo quitarla de su informe.",
    "answer": "Las agencias de crédito no incluyen la deuda médica pagada, la deuda menor de $500 ni la deuda médica de menos de 12 meses. La deuda médica sin pagar de más de $500 y de más de 12 meses todavía puede aparecer, a menos que su estado la proteja. Los datos de esta guía son de febrero de 2026.",
    "body": """
<p class="lead">Según investigaciones del CFPB (la Oficina para la Protección Financiera del Consumidor), la deuda médica en un informe de crédito baja el puntaje un promedio de 22 puntos. Las reglas cambiaron mucho en 2025 y 2026: un tribunal federal anuló una regla que habría eliminado $49 mil millones en deuda médica de los informes de crédito, pero las agencias de crédito quitaron voluntariamente miles de millones más y varios estados aprobaron leyes nuevas. Aquí le explicamos qué está protegido hoy y qué puede hacer si la deuda médica afecta su crédito.</p>

<nav class="toc">
    <h2>En esta guía</h2>
    <ol>
        <li><a href="#reglas">Las reglas actuales (febrero de 2026)</a></li>
        <li><a href="#regla-cfpb">La regla del CFPB que casi lo cambia todo</a></li>
        <li><a href="#estados">Protecciones por estado</a></li>
        <li><a href="#puntaje">Cómo afecta la deuda médica su puntaje</a></li>
        <li><a href="#revisar">Cómo revisar si la deuda médica está en su informe</a></li>
        <li><a href="#quitar">Cómo quitar la deuda médica de su informe</a></li>
        <li><a href="#prevenir">Cómo evitar que llegue a su crédito</a></li>
    </ol>
</nav>

<h2 id="reglas">1. Las reglas actuales (febrero de 2026)</h2>
<p>Las reglas sobre la deuda médica en los informes de crédito son una mezcla de políticas voluntarias de las agencias, una regla federal que fue anulada y leyes estatales. Esto es lo que hacen hoy las tres agencias principales: Equifax, Experian y TransUnion.</p>
<p>En marzo de 2023 las agencias anunciaron cambios voluntarios que quitaron de los informes una parte importante de la deuda médica. Siguen vigentes a febrero de 2026 y son la protección básica para todas las personas, sin importar el estado donde vivan:</p>
<table>
    <thead><tr><th>Tipo de deuda médica</th><th>¿Se reporta?</th><th>Por qué</th></tr></thead>
    <tbody>
        <tr><td>Cuentas médicas en cobros que ya se pagaron</td><td>No: se eliminan</td><td>Política voluntaria de las agencias desde julio de 2022</td></tr>
        <tr><td>Deuda médica sin pagar menor de $500</td><td>No: se elimina</td><td>Política voluntaria desde abril de 2023</td></tr>
        <tr><td>Deuda médica de menos de 12 meses</td><td>No: todavía no se puede reportar</td><td>Política voluntaria desde julio de 2022 (antes eran 180 días)</td></tr>
        <tr><td>Deuda médica sin pagar de más de $500 y de más de 12 meses</td><td>Sí: todavía se reporta</td><td>No hay protección federal ni voluntaria (a menos que se aplique una ley estatal)</td></tr>
    </tbody>
</table>
<div class="key-takeaway">
    <strong>Lo más importante:</strong> si en su informe aparece una cuenta médica en cobros de menos de $500, una ya pagada o una deuda de menos de 12 meses, no debería estar ahí. Pida sus informes en <a href="https://www.annualcreditreport.com" target="_blank" rel="noopener" lang="en">AnnualCreditReport.com</a> y dispute lo que no cumpla estas reglas. Antes de pagar a un cobrador, revise que la factura original sea correcta.
</div>

<h2 id="regla-cfpb">2. La regla del CFPB que casi lo cambia todo</h2>
<p>En enero de 2025, el CFPB aprobó su regla más ambiciosa sobre deuda médica: prohibir que la deuda médica aparezca en los informes de crédito. El CFPB calculó que la regla eliminaría <strong>$49 mil millones en deuda médica</strong> de los informes y mejoraría el puntaje de <strong>15 millones de personas</strong>.</p>
<p><strong>Lo que habría hecho la regla:</strong></p>
<ul>
    <li>Prohibir que las agencias de informes de crédito incluyeran cualquier deuda médica</li>
    <li>Prohibir que los prestamistas usaran información de deuda médica para decidir créditos</li>
    <li>Exigir que se eliminara toda la deuda médica ya reportada, sin importar la cantidad ni si estaba pagada</li>
    <li>Cerrar la brecha que dejan las reglas voluntarias (deuda sin pagar de más de $500 después de 12 meses)</li>
</ul>
<p><strong>Qué pasó:</strong> en julio de 2025, un tribunal federal anuló la regla en el caso <em>AHA v. CFPB</em>. La Asociación Americana de Hospitales (American Hospital Association) y la industria de informes de crédito dijeron que el CFPB se había pasado de su autoridad bajo la Ley de Informes Justos de Crédito (FCRA). El tribunal estuvo de acuerdo. El CFPB no apeló y argumentó que la decisión debía anular las protecciones estatales, un argumento que varios fiscales generales estatales han rechazado. A febrero de 2026, esa pregunta sigue sin resolverse en los tribunales y la regla no está en vigor.</p>

<h2 id="estados">3. Protecciones por estado</h2>
<p>Con la regla federal anulada, los estados se movieron rápido en 2025 y 2026. Al menos 10 estados tienen leyes que limitan el reporte de deuda médica más allá de la base voluntaria de las agencias:</p>
<ul>
    <li><strong>California, Nueva York, Washington y Minnesota:</strong> prohíben el reporte de deuda médica por completo</li>
    <li><strong>Colorado y Nevada:</strong> protegen las deudas menores de $2,500</li>
    <li><strong>Connecticut:</strong> protege las deudas menores de $1,000</li>
    <li><strong>Illinois y Oregón:</strong> protegen a los pacientes con ingresos menores de 400% del Nivel Federal de Pobreza</li>
    <li><strong>Maryland:</strong> restringe las medidas de cobro contra pacientes de menores ingresos</li>
</ul>
<p>Si vive en uno de estos estados, puede tener protecciones más fuertes. Si disputa un dato ante una agencia de crédito, cite la ley específica de su estado. Las leyes cambian; revise el texto vigente en su estado.</p>

<h2 id="puntaje">4. Cómo afecta la deuda médica su puntaje</h2>
<p>No todos los puntajes de crédito tratan la deuda médica igual. El modelo que usa su prestamista determina cuánto lo afecta una cuenta médica en cobros, y usted normalmente no elige el modelo.</p>
<table>
    <thead><tr><th>Modelo</th><th>Cuentas médicas pagadas</th><th>Cuentas médicas sin pagar</th></tr></thead>
    <tbody>
        <tr><td>FICO 8</td><td>Todavía cuentan (con menos peso que otras cuentas en cobros)</td><td>Efecto negativo completo</td></tr>
        <tr><td>FICO 9</td><td>Se ignoran por completo</td><td>Pesan menos que las cuentas en cobros no médicas</td></tr>
        <tr><td>FICO 10T</td><td>Se ignoran por completo</td><td>Menos peso; usa datos de tendencias</td></tr>
        <tr><td>VantageScore 4.0</td><td>Se ignoran por completo</td><td>Menos peso que otras cuentas en cobros</td></tr>
    </tbody>
</table>
<p><strong>El problema de las hipotecas:</strong> muchos prestamistas hipotecarios todavía usan FICO 8 u otros modelos más antiguos, que tratan las cuentas médicas casi igual que otras deudas. Fannie Mae y Freddie Mac ordenaron pasar a FICO 10T desde 2025, que es más indulgente con la deuda médica, pero la adopción es despareja.</p>
<p><strong>Los 22 puntos:</strong> el CFPB encontró que la deuda médica baja el puntaje un promedio de 22 puntos. Para alguien en el límite entre dos niveles de crédito (por ejemplo, 738 y 760), esos puntos pueden significar una tasa de interés hipotecaria 0.5% más alta, lo que podría costar de $20,000 a $40,000 en un préstamo de 30 años.</p>
<div class="key-takeaway">
    <strong>Lo más importante:</strong> pregunte a su prestamista qué versión de FICO usa <em>antes</em> de solicitar el préstamo.
</div>

<h2 id="revisar">5. Cómo revisar si la deuda médica está en su informe</h2>
<p><strong>Paso 1: Pida los tres informes.</strong> Vaya a <a href="https://www.annualcreditreport.com" target="_blank" rel="noopener" lang="en">AnnualCreditReport.com</a>, la única fuente autorizada por el gobierno federal para informes gratuitos. Tiene derecho a un informe gratis por agencia cada semana (esto se extendió hasta 2026). Pida los tres, porque la deuda médica puede aparecer en una agencia y en otra no.</p>
<p><strong>Paso 2: Busque cuentas médicas en cobros.</strong> Revise la sección de “Collections” o “Adverse Accounts” de cada informe. Las cuentas médicas normalmente muestran el nombre del proveedor original o la palabra “medical”. Anote el nombre del acreedor, el número de cuenta, el saldo, la fecha del primer atraso y la fecha del reporte de cada una.</p>
<p><strong>Paso 3: Compárelas con las reglas actuales.</strong> Para cada cuenta médica en cobros, pregunte:</p>
<ul>
    <li>¿La deuda está pagada? Si es así, no debería estar en su informe (política de 2022).</li>
    <li>¿El saldo es menor de $500? Si es así, no debería estar (política de 2023).</li>
    <li>¿Se reportó hace menos de 12 meses? Si es así, no debería estar (política de 2022).</li>
    <li>¿Su estado prohíbe reportar deuda médica? Si es así, no debería estar, sin importar la cantidad.</li>
</ul>
<p><strong>Paso 4: Guarde todo.</strong> Tome capturas de pantalla o guarde cada informe. Anote cuáles cuentas no cumplen las reglas. Necesitará esta documentación para disputar.</p>

<h2 id="quitar">6. Cómo quitar la deuda médica de su informe</h2>
<p>Hay cuatro métodos. Empiece por el primero; cada uno requiere más esfuerzo.</p>
<h3>Método 1: Verifique si se debe eliminar automáticamente</h3>
<p>Compruebe si la deuda ya debió eliminarse según las reglas voluntarias (pagada, menor de $500 o de menos de 12 meses). Si ya debería haber desaparecido, vaya directo a la disputa. Es la vía más rápida: no está negociando, está pidiendo que se cumpla una política existente.</p>
<h3>Método 2: Dispute los datos incorrectos ante las agencias</h3>
<p>Según la Ley de Informes Justos de Crédito (FCRA), usted tiene derecho a disputar cualquier información incorrecta. Presente la disputa por separado ante cada agencia que muestre el dato. Incluya:</p>
<ul>
    <li>Su nombre completo, dirección y número de Seguro Social</li>
    <li>La cuenta que disputa (número de cuenta y nombre del acreedor)</li>
    <li>Una explicación clara del error, por ejemplo: “Esta deuda médica de $380 es menor de $500 y no debería reportarse según las políticas actuales de las agencias de crédito”</li>
    <li>Documentos de apoyo (EOB, recibos de pago, factura detallada)</li>
</ul>
<p>Envíe la disputa por correo certificado con acuse de recibo. La agencia debe investigar en 30 días (45 días si usted envía más información). Si el cobrador no puede verificar la deuda o el dato no cumple las reglas de reporte, debe eliminarse.</p>
<h3>Método 3: Negocie un acuerdo de pago a cambio de eliminación (pay-for-delete)</h3>
<p>Si la deuda es válida y de más de $500, puede intentar una negociación de <em>pay-for-delete</em>: ofrece pagar una parte del saldo a cambio de que el cobrador acepte por escrito eliminar la cuenta de las tres agencias. Según las reglas de 2023, pagar una cuenta médica en cobros activa su eliminación de todas formas, así que aunque el cobrador no acepte eliminarla de forma expresa, pagar igual la quita de su informe.</p>
<p><strong>Antes de pagarle a un cobrador,</strong> verifique que la factura original sea correcta. Si la factura original tenía errores, la cantidad en cobros también está mal y puede que deba menos de lo que dicen.</p>
<h3>Método 4: Cite la ley de su estado</h3>
<p>Si su estado tiene una ley sobre el reporte de deuda médica, cite la ley específica en su carta de disputa. Las disputas con ley estatal pesan más porque una violación puede llevar a medidas de las autoridades contra la agencia.</p>

<h2 id="prevenir">7. Cómo evitar que la deuda médica llegue a su crédito</h2>
<p>Lo mejor es que la deuda médica no llegue a su informe. Tiene una ventana de 12 meses desde el primer atraso antes de que la deuda pueda siquiera aparecer. Úsela bien:</p>
<ol>
    <li><strong>Revise y dispute primero la factura original.</strong> Pida la factura detallada dentro de los 30 días de cualquier servicio médico y revise si hay cargos duplicados, códigos de nivel más alto, cargos separados que deberían ir juntos y servicios que no recibió. Vea <a href="/es/guias/como-disputar-factura-medica/">cómo disputar una factura médica</a>.</li>
    <li><strong>Solicite asistencia financiera antes de que pase a cobros.</strong> Los hospitales sin fines de lucro (60% de los hospitales de Estados Unidos) deben ofrecer estos programas. Si sus ingresos son menores de 200% del FPL ($31,200 para una persona sola en 2026), es probable que califique para la cancelación total. Vea la <a href="/es/guias/asistencia-financiera-hospital/">guía de asistencia financiera</a>.</li>
    <li><strong>Negocie antes de cobros.</strong> Llame a facturación y pida un plan de pagos o un descuento por pago en efectivo. La mayoría de los hospitales prefieren recibir $50 al mes directamente que vender la deuda a un cobrador por 4 a 7 centavos por dólar. Los planes de pago generalmente evitan que la cuenta pase a cobros.</li>
    <li><strong>Pida todo por escrito.</strong> Si hace un plan de pagos, disputa un cargo o le aprueban asistencia financiera, pida confirmación escrita. Si el hospital envía la cuenta a cobros a pesar del acuerdo, esos documentos son su evidencia.</li>
    <li><strong>Vigile su crédito.</strong> Use el monitoreo gratuito de su banco o de AnnualCreditReport.com. Si aparece una cuenta médica en cobros, actúe de inmediato: mientras más pronto disputa, menos daño hace.</li>
</ol>
<div class="key-takeaway">
    <strong>Lo más importante:</strong> tiene 12 meses antes de que la deuda médica sin pagar pueda aparecer en su informe de crédito. Use ese tiempo para disputar errores, solicitar asistencia financiera y negociar. Esta guía es información general, no asesoría legal ni financiera.
</div>
""",
    "faqs": [
        ("¿Todavía se reporta la deuda médica en los informes de crédito en 2026?", "Depende de la cantidad y del estado de la deuda. Las tres agencias principales de crédito excluyen voluntariamente las cuentas médicas en cobros pagadas, la deuda médica sin pagar menor de $500 y cualquier deuda médica de menos de 12 meses. La deuda sin pagar de más de $500 y de más de 12 meses todavía puede aparecer en su informe, a menos que su estado haya aprobado una ley que lo prohíba. La prohibición federal del CFPB fue anulada en julio de 2025, así que no hay una prohibición federal general."),
        ("¿Qué pasó con la regla del CFPB que prohibía la deuda médica en los informes de crédito?", "El CFPB aprobó la regla en enero de 2025, pero un tribunal federal la anuló en julio de 2025 en el caso AHA v. CFPB. El tribunal decidió que el CFPB se pasó de su autoridad. El CFPB no apeló y argumentó que la decisión debía anular las protecciones estatales, un argumento que los fiscales generales de varios estados han rechazado. A febrero de 2026, la regla no está en vigor."),
        ("¿Mi estado me protege de la deuda médica en mi informe de crédito?", "Es posible. Al menos 10 estados tienen leyes que limitan el reporte de deuda médica más allá de las reglas federales: California, Nueva York, Washington y Minnesota lo prohíben por completo; Colorado y Nevada protegen las deudas menores de $2,500; Connecticut protege las menores de $1,000; Illinois y Oregón protegen a pacientes con ingresos menores de 400% del Nivel Federal de Pobreza; y Maryland restringe las medidas de cobro contra pacientes de menores ingresos."),
        ("¿Cuánto baja mi puntaje de crédito la deuda médica?", "Una investigación del CFPB encontró una baja promedio de 22 puntos. El efecto real depende de su perfil de crédito y del modelo de puntaje que se use. Con FICO 9 y VantageScore 4.0, las cuentas médicas pagadas se ignoran. Con FICO 8 (todavía común en hipotecas), las cuentas médicas pesan casi igual que otras cuentas en cobros. Esos 22 puntos pueden hacer la diferencia entre niveles de tasa hipotecaria, con un costo de $20,000 a $40,000 en un préstamo de 30 años."),
        ("¿Cómo quito la deuda médica de mi informe de crédito?", "Primero verifique si la deuda se elimina automáticamente (pagada, menor de $500 o de menos de 12 meses). Si ya debería haber desaparecido, presente una disputa ante cada agencia que muestre el dato. Para deudas válidas de más de $500, puede intentar una negociación de pay-for-delete o simplemente pagar la deuda (las cuentas médicas pagadas se eliminan según la política de las agencias). Si su estado prohíbe el reporte de deuda médica, cite la ley específica en su disputa."),
        ("¿Debo pagar una cuenta médica en cobros para quitarla de mi informe?", "Según las reglas actuales de las agencias, pagar una cuenta médica en cobros activa su eliminación. Con FICO 9 y VantageScore 4.0, se ignora una vez pagada. Pero antes de pagar, verifique que la factura sea correcta. Si los cargos originales estaban mal, puede deber menos. También revise si la deuda se puede quitar sin pagar (menor de $500, de menos de 12 meses o protegida por ley estatal)."),
    ],
    "sources": [
        ("CFPB: Final Rule to Remove Medical Debt from Credit Reports (January 2025)", "https://www.consumerfinance.gov/about-us/newsroom/cfpb-finalizes-rule-to-remove-medical-debt-from-credit-reports/"),
        ("CFPB: Medical Debt Burden in the United States (Research Report)", "https://www.consumerfinance.gov/data-research/research-reports/medical-debt-burden-in-the-united-states/"),
        ("Equifax, Experian, TransUnion: Joint Announcement on Medical Collection Reporting Changes (2022)", "https://www.equifax.com/newsroom/all-news/equifax-experian-transunion-support-consumers-with-changes-to-medical-collection-debt-reporting/"),
        ("AnnualCreditReport.com: Free Weekly Credit Reports", "https://www.annualcreditreport.com"),
        ("myFICO: FICO Score Versions and How They Treat Medical Debt", "https://www.myfico.com/credit-education/credit-scores/fico-score-versions"),
        ("FTC: Fair Credit Reporting Act (FCRA)", "https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act"),
        ("KFF: The Burden of Medical Debt in the United States", "https://www.kff.org/health-costs/issue-brief/the-burden-of-medical-debt-in-the-united-states/"),
    ],
}

GUIDES = [FINANCIAL_ASSISTANCE, CANT_AFFORD, CREDIT_REPORT]
