# SpotifyAnalysis

## Description

SpotifyAnalysis est un outil open-source permettant d'extraire et de visualiser des statistiques détaillées de votre compte Spotify. Grâce à l'API Spotify, l'utilisateur peut consulter :

- **Top Tracks** : vos morceaux les plus écoutés
- **Top Artists** : vos artistes favoris
- **Top Albums** : vos albums préférés
- **Analyse par période** : sur 4 semaines, 6 mois, 1 an ou une période personnalisée

L'objectif est de fournir un dashboard clair et interactif pour mieux comprendre vos habitudes d'écoute, découvrir des tendances et affiner vos recommandations musicales.

## Fonctionnalités principales

- Authentification OAuth 2.0 avec Spotify
- Récupération des données utilisateur (top tracks, artists, albums)
- Possibilité de choisir des plages de temps : `short_term` (4 semaines), `medium_term` (6 mois), `long_term` (1 an), ou intervalle personnalisé
- Visualisations graphiques (courbes, diagrammes en barres, nuages de points)
- Export des rapports au format CSV et JSON
- Génération de playlists basées sur vos morceaux top
- Statistiques complémentaires :
  - Répartition par genre musical
  - Analyse des caractéristiques audio (danceability, energy, valence…)
  - Heures et jours d’écoute les plus actifs
  - Comparaison multi-période

## Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/votre-utilisateur/SpotifyAnalysis.git
   cd SpotifyAnalysis
   ```
2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurer les variables d'environnement dans server.py**
   ```bash
   SPOTIFY_CLIENT_ID="votre_client_id"
   SPOTIFY_CLIENT_SECRET="votre_client_secret"
   SPOTIFY_REDIRECT_URI="http://localhost:8888/callback"
   ```

## Utilisation
Lorsque vous avez créé une application spotify sur https://developer.spotify.com/, et que vous avez spécifié la bonne adresse de callback, vous pouvez lancer l'application.

### Lancer l'application

```bash
python server.py
```

## Licence

MIT License © 2025

