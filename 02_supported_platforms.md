# HVR 6 Supported Platforms

Fuente: https://fivetran.com/docs/hvr6/supported-platforms

Este documento lista las plataformas soportadas para Fivetran HVR releases.

## Plataformas versionadas

La documentacion de soporte de plataformas esta disponible para las siguientes versiones de HVR:

- [Platform Support Matrix - 6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635)
- [Platform Support Matrix - 6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630)
- [Platform Support Matrix - 6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625)
- [Platform Support Matrix - 6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620)
- [Platform Support Matrix - 6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615)
- [Platform Support Matrix - 6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)

---

# Platform Support Matrix - 6.3.5

Esta seccion lista los sistemas operativos y tipos de ubicacion source/target (versiones DBMS) soportados por Fivetran HVR **6.3.5**.

Para informacion sobre las versiones DBMS que soportan **Capture**, **Integrate**, **Refresh**, **Compare**, **Repository Database** y otras funciones de HVR, consulte la seccion Capabilities o las release notes.

---

## Politica de Soporte para Bases de Datos Hospedadas (Hosted Database Support Policy)

A menudo, las ubicaciones source y target soportadas que se pueden instalar on-premises son hospedadas por terceros como proveedores de nube (entre otros) Alibaba, Amazon, Google, Microsoft, etc. Estos sistemas hospedados generalmente son soportados por HVR como sources y targets en la medida en que sean compatibles con sus contrapartes descargables. La certificacion de compatibilidad es responsabilidad del proveedor de hosting, no de HVR. Las plataformas se han documentado por separado cuando la compatibilidad no es comparable y HVR ha podido implementar cambios de codigo de interoperabilidad (por ejemplo, Amazon Aurora PostgreSQL).

Si un proveedor afirma compatibilidad, debe ofrecer las mismas llamadas SQL y API y respuestas que soporten las funciones indicadas en la documentacion de HVR para los requisitos del tipo de ubicacion correspondiente en las secciones source y target apropiadas. En casos donde la compatibilidad no es completa, el soporte no esta garantizado. Cualquier problema que se manifieste en la plataforma hospedada debe ser reproducible en una version descargable equivalente para ser considerado un error en el software HVR.

### Notas importantes

- HVR version 6.x no es compatible con versiones 5.x y 4.x. Por lo tanto, asegurese de que la version 6.x este instalada tanto en las maquinas Hub como Agent.
- Solo la instalacion de **HVR Agent** es soportada en las siguientes plataformas:
  - Linux PPC: **linux_glibc2.28-ppc64-64bit**
  - Unix: **aix_7.1-powerpc-64bit**, **solaris_10-x64-64bit**, **solaris_11-sparcv9-64bit**

---

## Plataformas soportadas

A continuacion se detallan todas las plataformas soportadas en HVR 6.3.5, con sus sistemas operativos y versiones compatibles.

---

### Actian Vector / Vector(H)

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Vector: 6.0, Vector(H): 4.x |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Vector: 6.0 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Vector: 6.0, Vector(H): 4.x |

---

### Amazon S3

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | Supported |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **solaris_11-sparcv9-64bit** | Solaris para SPARC: 11 | Supported |
| **solaris_10-x64-64bit** | Solaris para Intel/AMD: 10, 11.x | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

---

### Apache HDFS

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 3.3.6+ |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 3.3.6+ |

---

### Apache Kafka

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 0.8+ |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 0.8+ |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 0.8+ |

---

### Aurora MySQL

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 1, 2, 3 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 1, 2, 3 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 1, 2, 3 |

---

### Aurora PostgreSQL

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 11, 12, 13, 14, 15, 16, 17, 18^2^ |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 11, 12, 13, 14, 15, 16, 17, 18^2^ |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 11, 12, 13, 14, 15, 16, 17, 18^2^ |

---

### Azure Blob Storage

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

---

### Azure Data Lake Storage

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Gen2: Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Gen2: Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Gen2: Supported |

---

### Azure SQL Database

**Capacidad:** Capture (deprecado), Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

> **Nota:** El soporte para Capture desde Azure SQL Database ha sido deprecado.

---

### Azure SQL Managed Instance

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

---

### Azure Synapse Analytics

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

---

### Databricks

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 10.x, 11.x, 12.x, 13.x, 14.x |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 10.x, 11.x, 12.x, 13.x, 14.x |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 10.x, 11.x, 12.x, 13.x, 14.x |

---

### Db2 for i

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 7.2, 7.3, 7.4, 7.5, 7.6^3^ |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 7.2, 7.3, 7.4, 7.5, 7.6^3^ |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 7.2, 7.3, 7.4, 7.5, 7.6^3^ |

---

### Db2 for LUW

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | 10.5, 11.1, 11.5, 12.1 |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 10.5, 11.1, 11.5 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 11.1, 11.5 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022 | 10.5, 11.1, 11.5 |

---

### Db2 for z/OS

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | 11.1, 12.1, 13.1 |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 11.1, 12.1, 13.1 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 11.1, 12.1, 13.1 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 11.1, 12.1, 13.1 |

---

### File, FTP, SFTP

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | Local, FTP/FTPS, SFTP |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Local, FTP/FTPS, SFTP |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Local, FTP/FTPS, SFTP |
| **solaris_11-sparcv9-64bit** | Solaris para SPARC: 11 | Local, FTP/FTPS, SFTP |
| **solaris_10-x64-64bit** | Solaris para Intel/AMD: 10, 11.x | Local, FTP/FTPS, SFTP |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Local, FTP/FTPS, SFTP |

---

### Google BigQuery

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 2.3 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 2.3 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 2.3 |

---

### Google Cloud Storage

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | Supported |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **solaris_11-sparcv9-64bit** | Solaris para SPARC: 11 | Supported |
| **solaris_10-x64-64bit** | Solaris para Intel/AMD: 10, 11.x | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

---

### Greenplum

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 5.5.x, 5.10.x+, 6.0.x-6.9.x |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 6.0.x-6.9.x |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 5.5.x, 5.10.x+, 6.0.x-6.9.x |

---

### Ingres

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | 10.0, 10.1, 10.2, 11.0 |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 10.0, 10.1, 10.2, 11.0, 11.1, 11.2, 12.0 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 11.0, 11.1, 11.2 (con patch 15820+), 12.0 |
| **solaris_11-sparcv9-64bit** | Solaris para SPARC: 11 | 10.0, 10.1, 10.2, 11.0, 11.1, 11.2, 12.0 |
| **solaris_10-x64-64bit** | Solaris para Intel/AMD: 10, 11.x | 10.2, 11.0, 11.1, 11.2 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 10.0, 10.1, 10.2, 11.0, 11.1, 11.2, 12.0 |

---

### MariaDB

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 10.3, 10.4, 10.5, 10.6, 10.11 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 10.4, 10.5, 10.6, 10.11 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 10.3, 10.4, 10.5, 10.6, 10.11 |

---

### MySQL

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 5.6, 5.7, 8 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 5.7, 8 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 5.6, 5.7, 8 |

---

### Oracle

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | 11.2, 12.1, 12.2, 19c |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 11.1, 11.2, 12.1, 12.2, 18c, 19c, 21c, Exadata |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 11.2, 12.1, 12.2, 18c, 19c, 21c, Exadata |
| **solaris_11-sparcv9-64bit** | Solaris para SPARC: 11 | 11.1, 11.2, 12.1, 12.2, 19c |
| **solaris_10-x64-64bit** | Solaris para Intel/AMD: 10, 11.x | 11.2, 12.1, 12.2 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 11.1, 11.2, 12.1, 12.2, 18c, 19c, 21c |

---

### PostgreSQL

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18^2^ |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18^2^ |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18^2^ |

---

### Redshift

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

---

### SAP HANA

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 2.0 SPS: 00, 01, 02, 03, 04, 05, 06, 07, 08 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 2.0 SPS: 00, 01, 02, 03, 04, 05, 06, 07, 08 |
| **linux_glibc2.27-ppc64-64bit** | Linux (PowerPC 64-bit) basado en GLIBC 2.27+ | 2.0 SPS: 00, 01, 02, 03, 04, 05, 06, 07 |
| **linux_glibc2.28-ppc64-64bit** | Linux (PowerPC 64-bit) basado en GLIBC 2.28+ | 2.0 SPS: 00, 01, 02, 03, 04, 05, 06, 07 |

---

### SAP NetWeaver

**Capacidad:** Capture

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 7.5+ |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 7.5+ |
| **linux_glibc2.27-ppc64-64bit** | Linux (PowerPC 64-bit) basado en GLIBC 2.27+ | 7.5+ |
| **linux_glibc2.28-ppc64-64bit** | Linux (PowerPC 64-bit) basado en GLIBC 2.28+ | 7.5+ |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 7.5+ |

---

### SingleStore

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 7.1 (solo 7.1.8+) |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 7.1 (solo 7.1.8+) |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 7.1 (solo 7.1.8+) |

---

### Snowflake

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Supported |

---

### SQL database in Microsoft Fabric

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Supported |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Supported |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025^1^ | Supported |

---

### SQL Server

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 2017, 2019, 2022, 2025^1^ |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 2017, 2019, 2022, 2025^1^ |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | 2012, 2014, 2016, 2017, 2019, 2022, 2025^1^ |

---

### Sybase ASE

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 16 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 16 |

---

### Teradata

**Capacidad:** Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **aix_7.1-powerpc-64bit** | AIX: 7.1+ | Teradata Database: 16.10, 16.20, 17.00, 17.05; Teradata Vantage: 16.20, 17.00, 17.05, 17.10, 17.20 |
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | Teradata Database: 16.10, 16.20, 17.00, 17.05; Teradata Vantage: 16.20, 17.00, 17.05, 17.10, 17.20 |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | Teradata Database: 16.10, 16.20, 17.00, 17.05; Teradata Vantage: 16.20, 17.00, 17.05, 17.10, 17.20 |
| **solaris_11-sparcv9-64bit** | Solaris para SPARC: 11 | Teradata Database: 16.10, 16.20; Teradata Vantage: 16.20 |
| **windows-x64-64bit** | Windows Server: 2012 R2, 2016, 2019, 2022, 2025 | Teradata Database: 16.10, 16.20, 17.00, 17.05; Teradata Vantage: 16.20, 17.00, 17.05, 17.10, 17.20 |

---

### YugabyteDB

**Capacidad:** Capture, Integrate

| Plataforma | Sistema Operativo | Estado / Version |
|---|---|---|
| **linux_glibc2.12-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.12+. Incluye: Amazon Linux 2023, RHEL 6.x+, SUSE 12.x, 15.x | 2024.1.x |
| **linux_glibc2.28-x64-64bit** | Linux (x86-64 bit) basado en GLIBC 2.28+. Incluye: Amazon Linux 2023, RHEL 8.x+, SUSE 15.x+ | 2024.1.x |

---

## Notas al pie

- **^1^** - Soportado desde HVR 6.3.5/2
- **^2^** - Soportado desde HVR 6.3.5/3
- **^3^** - Soportado desde HVR 6.3.5/5

---

## Resumen de plataformas

En total, HVR 6.3.5 soporta **34 plataformas** como source y/o target:

1. Actian Vector / Vector(H)
2. Amazon S3
3. Apache HDFS
4. Apache Kafka
5. Aurora MySQL
6. Aurora PostgreSQL
7. Azure Blob Storage
8. Azure Data Lake Storage
9. Azure SQL Database
10. Azure SQL Managed Instance
11. Azure Synapse Analytics
12. Databricks
13. Db2 for i
14. Db2 for LUW
15. Db2 for z/OS
16. File, FTP, SFTP
17. Google BigQuery
18. Google Cloud Storage
19. Greenplum
20. Ingres
21. MariaDB
22. MySQL
23. Oracle
24. PostgreSQL
25. Redshift
26. SAP HANA
27. SAP NetWeaver
28. SingleStore
29. Snowflake
30. SQL database in Microsoft Fabric
31. SQL Server
32. Sybase ASE
33. Teradata
34. YugabyteDB
