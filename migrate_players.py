#!/usr/bin/env python3
"""
Script para migrar datos de allPlayers.json a la base de datos Django
"""
import os
import sys
import json
import django
from datetime import datetime

# Configurar Django
sys.path.append("/ruta/a/tu/proyecto/django")  # Cambiar por la ruta real
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tu_proyecto.settings"
)  # Cambiar por tu proyecto
django.setup()

# Importar tus modelos después de configurar Django
# from tu_app.models import Player  # Cambiar por tu modelo real


def parse_date(date_string):
    """Convierte fecha del JSON a formato datetime de Python"""
    if date_string:
        try:
            return datetime.fromisoformat(date_string.replace("T00:00:00", ""))
        except:
            return None
    return None


def parse_height(height_string):
    """Convierte altura del formato 6'6" a centímetros o número"""
    if height_string:
        try:
            parts = height_string.replace('"', "").split("'")
            feet = int(parts[0])
            inches = int(parts[1]) if len(parts) > 1 else 0
            return (feet * 12) + inches  # Total en pulgadas
        except:
            return None
    return None


def load_players_from_json():
    """Carga y procesa los datos del JSON"""
    json_file = "/home/devmadhardy/projects/draftpy/src/allPlayers.json"

    with open(json_file, "r", encoding="utf-8") as file:
        players_data = json.load(file)

    print(f"Encontrados {len(players_data)} jugadores en el JSON")
    return players_data


def migrate_players():
    """Función principal de migración"""
    players_data = load_players_from_json()

    created_count = 0
    updated_count = 0
    error_count = 0

    for player_data in players_data:
        try:
            # Datos básicos del jugador
            player_id = player_data.get("PlayerID")

            # Verificar si el jugador ya existe
            # player, created = Player.objects.get_or_create(
            #     player_id=player_id,
            #     defaults={
            #         'team': player_data.get('Team'),
            #         'number': player_data.get('Number'),
            #         'first_name': player_data.get('FirstName'),
            #         'last_name': player_data.get('LastName'),
            #         'position': player_data.get('Position'),
            #         'status': player_data.get('Status'),
            #         'height': parse_height(player_data.get('Height')),
            #         'weight': player_data.get('Weight'),
            #         'birth_date': parse_date(player_data.get('BirthDate')),
            #         'college': player_data.get('College'),
            #         'experience': player_data.get('Experience'),
            #         'fantasy_position': player_data.get('FantasyPosition'),
            #         'active': player_data.get('Active', False),
            #         'position_category': player_data.get('PositionCategory'),
            #         'name': player_data.get('Name'),
            #         'age': player_data.get('Age'),
            #         'photo_url': player_data.get('PhotoUrl'),
            #         'bye_week': player_data.get('ByeWeek'),
            #         # Agregar más campos según tu modelo
            #     }
            # )

            # Por ahora solo imprimimos para testing
            print(f"Procesando: {player_data.get('Name')} (ID: {player_id})")

            # if created:
            #     created_count += 1
            # else:
            #     updated_count += 1

        except Exception as e:
            print(f"Error procesando jugador {player_data.get('Name', 'Unknown')}: {e}")
            error_count += 1

    print(f"\nMigración completada:")
    print(f"Creados: {created_count}")
    print(f"Actualizados: {updated_count}")
    print(f"Errores: {error_count}")


if __name__ == "__main__":
    migrate_players()
