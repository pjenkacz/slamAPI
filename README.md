DIAGRAM SEKWENCJI 
sequenceDiagram
    autonumber
    participant C as Klient (Android)
    participant API as FastAPI 
    participant AUTH as get_current_user() 
    participant JWT as decode_access_token()
    participant DB as Baza danych 

    C->>API: HTTP GET /photos/get Authorization: Bearer <token>
    API->>AUTH: Depends(get_current_user)
    AUTH->>JWT: decode_access_token(token)
    JWT-->>AUTH: payload (sub=user)

    AUTH->>AUTH: Walidacja tokenu

    alt  token niepoprawny
        AUTH-->>API: HTTP 401 Unauthorized
        API-->>C: 401 + komunikat błędu
    else użytkownik poprawny
    AUTH->>DB: SELECT * FROM users WHERE id = sub
    DB-->>AUTH: User (ORM object) / None
        AUTH-->>API: current_user: models.User
        API->>DB: SELECT * FROM photos WHERE user_id = current_user.id
        DB-->>API: List[Photo]
        API-->>C: 200 OK\nPhotoUploadListResponse (JSON)
    end
