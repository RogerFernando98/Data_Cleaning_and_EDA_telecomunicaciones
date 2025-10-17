# 01_data_cleaning_and_eda

## Sobre el conjunto de datos

**Contexto**
Una compañía ficticia de telecomunicaciones que ofrecía servicios de telefonía fija e Internet a 7043 clientes en California en el tercer trimestre.

**Descripción de los datos**
7043 observaciones con 33 variables

* **CustomerID**: Un ID único que identifica a cada cliente.

* **Count**: Un valor usado en reportes/dashboards para sumar el número de clientes en un conjunto filtrado.

* **Country**: País de residencia principal del cliente.

* **State**: Estado de residencia principal del cliente.

* **City**: Ciudad de residencia principal del cliente.

* **Zip Code**: Código postal de residencia principal del cliente.

* **Lat Long**: Latitud y longitud combinadas de la residencia principal del cliente.

* **Latitude**: Latitud de la residencia principal del cliente.

* **Longitude**: Longitud de la residencia principal del cliente.

* **Gender**: Género del cliente: Masculino, Femenino.

* **Senior Citizen**: Indica si el cliente tiene 65 años o más: Sí, No.

* **Partner**: Indica si el cliente tiene pareja: Sí, No.

* **Dependents**: Indica si el cliente vive con personas a cargo: Sí, No. Los dependientes pueden ser hijos, padres, abuelos, etc.

* **Tenure Months**: Indica el número total de meses que el cliente ha estado con la compañía hasta el final del trimestre mencionado.

* **Phone Service**: Indica si el cliente está suscrito al servicio de telefonía fija de la compañía: Sí, No.

* **Multiple Lines**: Indica si el cliente está suscrito a múltiples líneas telefónicas con la compañía: Sí, No.

* **Internet Service**: Indica si el cliente está suscrito al servicio de Internet de la compañía: No, DSL, Fibra Óptica, Cable.

* **Online Security**: Indica si el cliente está suscrito a un servicio adicional de seguridad en línea ofrecido por la compañía: Sí, No.

* **Online Backup**: Indica si el cliente está suscrito a un servicio adicional de respaldo en línea ofrecido por la compañía: Sí, No.

* **Device Protection**: Indica si el cliente está suscrito a un plan adicional de protección de dispositivos para su equipo de Internet ofrecido por la compañía: Sí, No.

* **Tech Support**: Indica si el cliente está suscrito a un plan adicional de soporte técnico con tiempos de espera reducidos ofrecido por la compañía: Sí, No.

* **Streaming TV**: Indica si el cliente usa su servicio de Internet para ver televisión en streaming de 
un proveedor externo: Sí, No. La compañía no cobra tarifa adicional por este servicio.

* **Streaming Movies**: Indica si el cliente usa su servicio de Internet para ver películas en streaming de un proveedor externo: Sí, No. La compañía no cobra tarifa adicional por este servicio.

* **Contract**: Indica el tipo de contrato actual del cliente: Mes a mes, Un año, Dos años.

* **Paperless Billing**: Indica si el cliente eligió facturación sin papel: Sí, No.

* **Payment Method**: Indica cómo paga el cliente su factura: Domiciliación bancaria, Tarjeta de crédito, Cheque enviado por correo.

* **Monthly Charge**: Indica el cargo mensual total actual del cliente por todos los servicios de la compañía.

* **Total Charges**: Indica el cargo total del cliente, calculado hasta el final del trimestre mencionado.

* **Churn Label**: Sí = el cliente dejó la compañía este trimestre. No = el cliente permaneció en la 
compañía. Relacionado directamente con *Churn Value*.

* **Churn Value**: 1 = el cliente dejó la compañía este trimestre. 0 = el cliente permaneció en la compañía. Relacionado directamente con *Churn Label*.

* **Churn Score**: Un valor entre 0 y 100 calculado usando la herramienta predictiva IBM SPSS Modeler. El modelo incorpora múltiples factores conocidos por causar cancelaciones. Cuanto más alto el puntaje, mayor la probabilidad de que el cliente se dé de baja.

* **CLTV**: *Customer Lifetime Value* (Valor de vida del cliente). Se calcula un CLTV estimado usando fórmulas corporativas y datos existentes. Cuanto mayor el valor, más valioso es el cliente. Los clientes de alto valor deben ser monitoreados para evitar cancelaciones.

* **Churn Reason**: Razón específica por la cual el cliente dejó la compañía. Relacionado directamente con *Churn Category*.
