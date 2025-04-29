# API_tracking

📦 Shipment Tracking API
Shipment Tracking API est une application web développée avec Django REST Framework et conçue pour permettre aux utilisateurs de suivre en temps réel l’évolution de leurs colis maritimes ou aériens à l’aide d’un simple code de suivi.

Elle est destinée aux transitaires et aux clients finaux pour une gestion transparente des expéditions, avec une interface sécurisée pour l'administration.

✨ Fonctionnalités principales
🔐 Authentification sécurisée pour les administrateurs

🧾 Création, mise à jour et suppression de colis par les transitaires/admins

🔍 Suivi public d’un colis via un code de tracking

🗺️ Affichage de la position actuelle du colis sur une carte (Leaflet)

📈 Historique complet des mises à jour du colis

📤 API RESTful facilement consommable par un frontend (Vue.js, React, etc.)

🔧 Technologies utilisées
Backend : Django & Django REST Framework

Authentification : JWT / Session (au choix)

Base de données : SQLite (développement) / PostgreSQL (production possible)

Cartographie : Leaflet.js (pour l'affichage en frontend)

📁 Structure principale
bash
Copier
Modifier
shipment_tracking/
├── api/                 # App contenant les vues et serializers de l'API
├── TrackingShipment/    # App contenant les modèles et la logique métier
├── frontend/            # (optionnel) Frontend Vue.js ou autre
├── manage.py
└── README.md
🚀 À venir
Notifications (email/SMS) à chaque mise à jour de statut

Tableau de bord administrateur avec statistiques

Génération automatique de code de suivi

Géocodage automatique des adresses