def render_user_profile(user):
    # Representa una lista de dulcees como una lista de diccionarios
    return {
            "id": user.id,
            "Username": user.username,
            "Password": user.password_hash,
            "Roles": user.roles,
    }