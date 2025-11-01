# Mapeo de campos del JSON al modelo Django
FIELD_MAPPING = {
    "PlayerID": "player_id",
    "Team": "team",
    "Number": "number",
    "FirstName": "first_name",
    "LastName": "last_name",
    "Position": "position",
    "Status": "status",
    "Height": "height",  # Requiere procesamiento
    "Weight": "weight",
    "BirthDate": "birth_date",  # Requiere procesamiento
    "College": "college",
    "Experience": "experience",
    "FantasyPosition": "fantasy_position",
    "Active": "active",
    "PositionCategory": "position_category",
    "Name": "name",
    "Age": "age",
    "PhotoUrl": "photo_url",
    "ByeWeek": "bye_week",
    # Agregar más campos según necesites
}

# Campos que requieren procesamiento especial
SPECIAL_PROCESSING = {
    "BirthDate": "parse_date",
    "Height": "parse_height",
    "InjuryStartDate": "parse_date",
}
