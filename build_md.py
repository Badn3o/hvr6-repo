#!/usr/bin/env python3
"""
Build the capabilities markdown file from extracted content.
Reads content from individual files and assembles the final document.
"""
import os
import sys

OUTPUT_DIR = "/root/hvr-docs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "03_capabilities.md")

RELEASES = [
    ("635", "6.3.5"),
    ("630", "6.3.0"),
    ("625", "6.2.5"),
    ("620", "6.2.0"),
    ("615", "6.1.5"),
    ("610", "6.1.0"),
]

DATABASES = [
    "apache-kafka",
    "aurora-mysql",
    "aurora-postgresql",
    "azure-sql-database",
    "azure-sql-managed-instance",
    "azure-synapse-analytics",
    "bigquery",
    "databricks",
    "db2-for-i",
    "db2-for-linux-unix-and-windows",
    "db2-for-z-os",
    "greenplum",
    "ingres",
    "mariadb",
    "mysql",
    "oracle",
    "postgresql",
    "redshift",
    "sap-hana",
    "sap-netweaver-on-hana",
    "sap-netweaver-on-oracle",
    "singlestore",
    "snowflake",
    "sql-database-in-microsoft-fabric",
    "sql-server",
    "sybase-ase",
    "teradata",
    "vector",
    "yugabytedb",
]

def format_article_text(text, base_indent=""):
    """Format article text as proper markdown."""
    lines = text.split('\n')
    result = []
    in_table = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append('')
            continue
        
        # Check if this looks like a table row (contains tabs)
        if '\t' in stripped and not stripped.startswith('http'):
            # This is a table row
            cols = stripped.split('\t')
            if not in_table:
                # Start table
                result.append('| ' + ' | '.join(cols) + ' |')
                result.append('|' + '---|' * len(cols))
                in_table = True
            else:
                result.append('| ' + ' | '.join(cols) + ' |')
        else:
            in_table = False
            # Check if it's a heading-like line (all caps, short)
            if stripped.isupper() and len(stripped) < 100 and not stripped.startswith('HTTP'):
                result.append(f'### {stripped.title()}')
            else:
                result.append(stripped)
    
    return '\n'.join(result)

# Build the markdown
with open(OUTPUT_FILE, 'w') as f:
    f.write("""# HVR 6 Capabilities

This document contains the complete Capabilities section from Fivetran HVR 6 documentation, covering all supported releases and database platforms.

Source: https://fivetran.com/docs/hvr6/capabilities

---

""")

    for ver, label in RELEASES:
        # Write main page content
        main_file = os.path.join(OUTPUT_DIR, f"content_{ver}_main.txt")
        if os.path.exists(main_file):
            with open(main_file, 'r') as mf:
                content = mf.read()
            
            f.write(f"## Capabilities for {label} Release\n\n")
            f.write(f"Source: https://fivetran.com/docs/hvr6/capabilities/{ver}\n\n")
            f.write(content)
            f.write("\n\n---\n\n")
            
            # Write sub-page content
            for db in DATABASES:
                sub_file = os.path.join(OUTPUT_DIR, f"content_{ver}_{db}.txt")
                if os.path.exists(sub_file):
                    with open(sub_file, 'r') as sf:
                        sub_content = sf.read()
                    
                    db_name = db.replace('-', ' ').title()
                    f.write(f"### Capabilities for {db_name} ({label})\n\n")
                    f.write(f"Source: https://fivetran.com/docs/hvr6/capabilities/{ver}/capabilities-for-{db}\n\n")
                    f.write(sub_content)
                    f.write("\n\n")

            f.write("---\n\n")

print(f"Written to {OUTPUT_FILE}")
