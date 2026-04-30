import os
import pandas as pd
import logging

def validate_data(df):
    errors = []
    
    # 1. Validación Estructural: Columnas obligatorias
    required_columns = ['UserID', 'Age', 'Gender', 'VRHeadset', 'Duration', 'MotionSickness', 'ImmersionLevel']
    for col in required_columns:
        if col not in df.columns:
            errors.append(f"Falta columna obligatoria: {col}")

    # 2. Validación Semántica: Rangos lógicos
    # Ejemplo: Edad entre 0 y 110
    invalid_age = df[(df['Age'] < 0) | (df['Age'] > 110)]
    if not invalid_age.empty:
        errors.append(f"Se encontraron {len(invalid_age)} registros con edades fuera de rango.")

    # Ejemplo: Duración no negativa
    invalid_duration = df[df['Duration'] < 0]
    if not invalid_duration.empty:
        errors.append(f"Se encontraron {len(invalid_duration)} registros con duración negativa.")

    # 3. Generar Reporte (Requerimiento del ejercicio)
    report_path = "data/reports/error_report.txt"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, "w") as f:
        if not errors:
            f.write("Validación exitosa: No se detectaron errores.")
        else:
            f.write("REPORTE DE ERRORES DE VALIDACIÓN\n")
            f.writelines([f"- {err}\n" for err in errors])
            
    logging.info(f"Reporte de validación generado en: {report_path}")
    return len(errors) == 0