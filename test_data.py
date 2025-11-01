#!/usr/bin/env python3
"""
Script de prueba para verificar la estructura de datos sin Django
"""
import json
from datetime import datetime


def parse_date(date_string):
    """Convierte fecha del JSON a formato datetime de Python"""
    if date_string:
        try:
            return datetime.fromisoformat(date_string.replace("T00:00:00", ""))
        except:
            return None
    return None


def parse_height(height_string):
    """Convierte altura del formato 6'6" a pulgadas"""
    if height_string:
        try:
            parts = height_string.replace('"', "").split("'")
            feet = int(parts[0])
            inches = int(parts[1]) if len(parts) > 1 else 0
            return (feet * 12) + inches
        except:
            return None
    return None


def test_data_processing():
    """Prueba el procesamiento de los primeros 5 jugadores"""
    json_file = "/home/devmadhardy/projects/draftpy/src/allPlayers.json"

    with open(json_file, "r", encoding="utf-8") as file:
        players_data = json.load(file)

    print(f"Total de jugadores: {len(players_data)}")
    print("\nPrimeros 5 jugadores procesados:")
    print("-" * 50)

    for i, player in enumerate(players_data[:5]):
        print(f"\nJugador {i+1}:")
        print(f"  Nombre: {player.get('Name')}")
        print(f"  Equipo: {player.get('Team')}")
        print(f"  Posición: {player.get('Position')}")
        print(
            f"  Altura: {player.get('Height')} -> {parse_height(player.get('Height'))} pulgadas"
        )
        print(f"  Peso: {player.get('Weight')} lbs")
        print(
            f"  Fecha nacimiento: {player.get('BirthDate')} -> {parse_date(player.get('BirthDate'))}"
        )
        print(f"  Activo: {player.get('Active')}")


if __name__ == "__main__":
    test_data_processing()
