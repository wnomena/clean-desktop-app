# Clean Desktop App

## 📋 Présentation

Application desktop robuste en cours de développement, conçue pour la gestion locale de données d'une application web en déploiement. Cette solution permet une synchronisation efficace entre les données locales et la plateforme web, tout en offrant des capacités de traitement avancées.

## 🎯 Objectif

Fournir une application desktop complète d'administration pour gérer des données sensibles localement, avec synchronisation transparente vers le serveur web. Optimisée pour la performance et la facilité d'utilisation.

## 🛠️ Stack Technique

- **Framework UI** : PySide6 6.10.1 (Qt pour Python)
- **Framework Web** : Flask
- **ORM** : SQLAlchemy 2.0.45
- **Base de Données** : MySQL (via PyMySQL 1.1.2, aiomysql 0.3.2)
- **Traitement de Données** : Pandas
- **Asynchrone** : aioschedule 0.5.2
- **Requêtes HTTP** : httpx 0.28.1, requests 2.32.5
- **Notifications** : Plyer 2.1.0
- **Support Async** : asyncio

## 📦 Composants du Projet

### Architecture Client-Serveur

- **Interface Graphique** : Interface desktop moderna avec PySide6
- **Synchronisation Async** : Gestion asynchrone avec aioschedule pour les tâches planifiées
- **Persistance Locale** : SQLAlchemy pour ORM avec support MySQL
- **Notifications Système** : Intégration Plyer pour alertes desktop
- **Traitement de Données** : Pandas pour manipulation de fichiers Excel et données structurées
- **Communication Web** : Requêtes HTTP pour synchronisation avec serveur

## 🎯 Fonctionnalités Principales

✅ Gestion des données en local avec SQLAlchemy
✅ Synchronisation automatique avec serveur web
✅ Interface graphique professionnelle avec PySide6
✅ Support Excel/Pandas pour import/export de données
✅ Notifications système en temps réel
✅ Opérations asynchrones et planifiées
✅ Gestion robuste des erreurs de connexion

## 🔧 Installation & Utilisation

```bash
# Installation des dépendances
pip install -r requirements.txt

# Lancement de l'application
python main.py
