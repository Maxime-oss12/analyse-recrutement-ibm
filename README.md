# Analyse des Données de Recrutement IBM

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![Licence MIT](https://img.shields.io/badge/Licence-MIT-green)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

Ce projet propose un script Python complet pour analyser les données de recrutement d'IBM à partir de 4 fichiers CSV : candidatures, coûts, entretiens et postes. Il permet d'obtenir des statistiques, des analyses avancées et des visualisations pour mieux comprendre le processus de recrutement.

## Fonctionnalités principales

- **Chargement automatique** des 4 fichiers CSV avec `pandas`
- **Aperçu** des premières lignes de chaque table
- **Statistiques descriptives** sur toutes les données
- **Analyses avancées** :
  - Corrélation entre le score de CV et la note d'entretien
  - Analyse des coûts par canal de recrutement
  - Taux de conversion par département
  - Durée moyenne des entretiens par type
- **Visualisations** (matplotlib & seaborn) :
  - Histogramme des scores de CV
  - Box plot des coûts par statut
  - Scatter plot score de CV vs note d'entretien
  - Bar chart des candidatures par canal
- **Résumé automatique** des points clés de l'analyse

## 📊 Aperçu des résultats
![Graphiques d'analyse](analyse_recrutement_ibm.png)

## Prérequis

- Python 3.8 ou supérieur
- Les fichiers CSV suivants dans le même dossier :
  - `Candidatures.CSV`
  - `couts.CSV`
  - `Entretiens.CSV`
  - `postes.CSV`

## Installation

1. Clonez ce dépôt ou copiez les fichiers dans un dossier local.
2. Installez les dépendances Python :

```bash
pip install -r requirements.txt
```

## Utilisation

Lancez simplement le script principal :

```bash
python analyse_recrutement_ibm.py
```

Le script :
- Affichera les résultats dans le terminal (statistiques, analyses, résumé)
- Générera un fichier `analyse_recrutement_ibm.png` avec les 4 graphiques principaux

## Structure des fichiers CSV

- **Candidatures.CSV** : informations sur chaque candidature (id, poste, canal, score CV, statut, etc.)
- **couts.CSV** : coûts associés à chaque candidature (sourcing, entretiens, onboarding, total)
- **Entretiens.CSV** : détails de chaque entretien (type, durée, note, recruteur)
- **postes.CSV** : informations sur les postes ouverts (département, niveau, salaire, manager)

## Exemples de visualisations

- Histogramme de la distribution des scores de CV
- Box plot des coûts par statut de candidature
- Nuage de points score de CV vs note d'entretien
- Barres du nombre de candidatures par canal de recrutement

---

N'hésitez pas à forker, adapter ou améliorer ce script pour vos propres analyses RH ! 