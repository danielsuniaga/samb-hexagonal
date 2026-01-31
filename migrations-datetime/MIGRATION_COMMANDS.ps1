# ========================================
# COMANDOS DE MIGRACION DATETIME
# Ejecutar cada comando INDIVIDUALMENTE
# ========================================

# COMANDO 1 - R_100 ST
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r100-st-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 2 - R_100 STRSI
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r100-strsi-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 3 - R_100 STSMA
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r100-stsma-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 4 - R_100 STRSISMA
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r100-strsisma-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 5 - R_75 ST
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r75-st-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 6 - R_75 STRSI
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r75-strsi-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 7 - R_75 STSMA
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r75-stsma-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 8 - R_75 STRSISMA
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r75-strsisma-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 9 - R_50 ST
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r50-st-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 10 - R_50 STRSI
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r50-strsi-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 11 - R_50 STSMA
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r50-stsma-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }

# COMANDO 12 - R_50 STRSISMA
Get-Content migrations-datetime/MIGRATION_SIMPLE.sql | docker exec -i r50-strsisma-database-1 mysql -uroot -p7CXIxo7b2MGC guarvzpf_dev 2>&1 | Where-Object { $_ -notmatch "Warning.*password" }
