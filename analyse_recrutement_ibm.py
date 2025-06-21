#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'analyse des données de recrutement IBM
Auteur: Assistant IA
Date: 2024
Description: Analyse complète des données de candidatures, coûts, entretiens et postes
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configuration pour l'affichage en français
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

def charger_donnees():
    """
    Charge les 4 fichiers CSV dans des DataFrames pandas
    """
    print("=" * 60)
    print("CHARGEMENT DES DONNÉES")
    print("=" * 60)
    
    try:
        # Chargement des fichiers CSV
        candidatures = pd.read_csv('Candidatures.CSV')
        couts = pd.read_csv('couts.CSV')
        entretiens = pd.read_csv('Entretiens.CSV')
        postes = pd.read_csv('postes.CSV')
        
        print("✅ Tous les fichiers ont été chargés avec succès!")
        print(f"📊 Candidatures: {len(candidatures)} lignes")
        print(f"💰 Coûts: {len(couts)} lignes")
        print(f"🎯 Entretiens: {len(entretiens)} lignes")
        print(f"💼 Postes: {len(postes)} lignes")
        
        return candidatures, couts, entretiens, postes
    
    except FileNotFoundError as e:
        print(f"❌ Erreur: Fichier non trouvé - {e}")
        return None, None, None, None
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")
        return None, None, None, None

def afficher_premieres_lignes(candidatures, couts, entretiens, postes):
    """
    Affiche les premières lignes de chaque DataFrame
    """
    print("\n" + "=" * 60)
    print("APERÇU DES DONNÉES")
    print("=" * 60)
    
    print("\n📋 CANDIDATURES (5 premières lignes):")
    print(candidatures.head())
    
    print("\n💰 COÛTS (5 premières lignes):")
    print(couts.head())
    
    print("\n🎯 ENTRETIENS (5 premières lignes):")
    print(entretiens.head())
    
    print("\n💼 POSTES (5 premières lignes):")
    print(postes.head())

def statistiques_descriptives(candidatures, couts, entretiens, postes):
    """
    Affiche les statistiques descriptives pour chaque DataFrame
    """
    print("\n" + "=" * 60)
    print("STATISTIQUES DESCRIPTIVES")
    print("=" * 60)
    
    print("\n📊 CANDIDATURES - Statistiques numériques:")
    print(candidatures.describe())
    
    print("\n💰 COÛTS - Statistiques numériques:")
    print(couts.describe())
    
    print("\n🎯 ENTRETIENS - Statistiques numériques:")
    print(entretiens.describe())
    
    print("\n💼 POSTES - Statistiques numériques:")
    print(postes.describe())

def analyses_avancees(candidatures, couts, entretiens, postes):
    """
    Effectue des analyses avancées sur les données
    """
    print("\n" + "=" * 60)
    print("ANALYSES AVANCÉES")
    print("=" * 60)
    
    # 1. Corrélation entre cv_score et notes d'entretien
    print("\n1️⃣ CORRÉLATION CV_SCORE vs NOTES D'ENTRETIEN")
    print("-" * 40)
    
    # Fusion des données candidatures et entretiens
    candidatures_entretiens = candidatures.merge(entretiens, on='id_candidature', how='inner')
    
    # Calcul de la note moyenne par candidature
    notes_moyennes = candidatures_entretiens.groupby('id_candidature')['note_sur_10'].mean().reset_index()
    candidatures_avec_notes = candidatures.merge(notes_moyennes, on='id_candidature', how='inner')
    
    correlation = candidatures_avec_notes['cv_score'].corr(candidatures_avec_notes['note_sur_10'])
    print(f"Corrélation entre cv_score et note moyenne d'entretien: {correlation:.3f}")
    
    if correlation > 0.7:
        print("✅ Forte corrélation positive - Les CV scores prédisent bien les performances en entretien")
    elif correlation > 0.3:
        print("✅ Corrélation modérée positive")
    elif correlation > -0.3:
        print("⚠️ Corrélation faible")
    else:
        print("❌ Corrélation négative")
    
    # 2. Analyse des coûts par canal de recrutement
    print("\n2️⃣ ANALYSE DES COÛTS PAR CANAL DE RECRUTEMENT")
    print("-" * 40)
    
    candidatures_couts = candidatures.merge(couts, on='id_candidature', how='inner')
    couts_par_canal = candidatures_couts.groupby('canal_recrutement')['cout_total'].agg(['mean', 'sum', 'count']).round(2)
    couts_par_canal.columns = ['Coût moyen', 'Coût total', 'Nombre de candidatures']
    print(couts_par_canal.sort_values('Coût moyen', ascending=False))
    
    # 3. Taux de conversion par département
    print("\n3️⃣ TAUX DE CONVERSION PAR DÉPARTEMENT")
    print("-" * 40)
    
    candidatures_postes = candidatures.merge(postes, on='id_poste', how='inner')
    
    # Calcul du taux de conversion (Embauché / Total candidatures)
    conversion_par_dept = candidatures_postes.groupby('departement').agg({
        'id_candidature': 'count',
        'statut_actuel': lambda x: (x == 'Embauché').sum()
    }).rename(columns={'id_candidature': 'Total_candidatures', 'statut_actuel': 'Embauchés'})
    
    conversion_par_dept['Taux_conversion'] = (conversion_par_dept['Embauchés'] / conversion_par_dept['Total_candidatures'] * 100).round(2)
    print(conversion_par_dept.sort_values('Taux_conversion', ascending=False))
    
    # 4. Durée moyenne des entretiens par type
    print("\n4️⃣ DURÉE MOYENNE DES ENTRETIENS PAR TYPE")
    print("-" * 40)
    
    duree_par_type = entretiens.groupby('type_entretien')['duree_minutes'].agg(['mean', 'count']).round(2)
    duree_par_type.columns = ['Durée moyenne (min)', 'Nombre d\'entretiens']
    print(duree_par_type.sort_values('Durée moyenne (min)', ascending=False))

def creer_graphiques(candidatures, couts, entretiens, postes):
    """
    Crée les 4 graphiques demandés
    """
    print("\n" + "=" * 60)
    print("CRÉATION DES GRAPHIQUES")
    print("=" * 60)
    
    # Configuration du style des graphiques
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Création d'une figure avec 2x2 sous-graphiques
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Analyse des Données de Recrutement IBM', fontsize=16, fontweight='bold')
    
    # 1. Histogramme des cv_scores
    print("📊 Création de l'histogramme des cv_scores...")
    axes[0, 0].hist(candidatures['cv_score'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Distribution des CV Scores', fontweight='bold')
    axes[0, 0].set_xlabel('CV Score')
    axes[0, 0].set_ylabel('Fréquence')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Ajout de la moyenne
    moyenne_cv = candidatures['cv_score'].mean()
    axes[0, 0].axvline(moyenne_cv, color='red', linestyle='--', label=f'Moyenne: {moyenne_cv:.1f}')
    axes[0, 0].legend()
    
    # 2. Box plot des coûts par statut
    print("💰 Création du box plot des coûts par statut...")
    candidatures_couts = candidatures.merge(couts, on='id_candidature', how='inner')
    
    # Filtrer les statuts avec suffisamment de données
    statuts_avec_couts = candidatures_couts.groupby('statut_actuel').filter(lambda x: len(x) >= 3)
    
    if len(statuts_avec_couts) > 0:
        sns.boxplot(data=statuts_avec_couts, x='statut_actuel', y='cout_total', ax=axes[0, 1])
        axes[0, 1].set_title('Distribution des Coûts par Statut', fontweight='bold')
        axes[0, 1].set_xlabel('Statut Actuel')
        axes[0, 1].set_ylabel('Coût Total (€)')
        axes[0, 1].tick_params(axis='x', rotation=45)
    else:
        axes[0, 1].text(0.5, 0.5, 'Données insuffisantes\npour le box plot', 
                       ha='center', va='center', transform=axes[0, 1].transAxes)
        axes[0, 1].set_title('Distribution des Coûts par Statut', fontweight='bold')
    
    # 3. Scatter plot cv_score vs note d'entretien
    print("🎯 Création du scatter plot cv_score vs note d'entretien...")
    
    # Calcul de la note moyenne par candidature
    notes_moyennes = entretiens.groupby('id_candidature')['note_sur_10'].mean().reset_index()
    candidatures_avec_notes = candidatures.merge(notes_moyennes, on='id_candidature', how='inner')
    
    axes[1, 0].scatter(candidatures_avec_notes['cv_score'], candidatures_avec_notes['note_sur_10'], 
                      alpha=0.6, color='green')
    axes[1, 0].set_title('CV Score vs Note d\'Entretien', fontweight='bold')
    axes[1, 0].set_xlabel('CV Score')
    axes[1, 0].set_ylabel('Note Moyenne d\'Entretien')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Ajout de la ligne de régression
    correlation = candidatures_avec_notes['cv_score'].corr(candidatures_avec_notes['note_sur_10'])
    z = np.polyfit(candidatures_avec_notes['cv_score'], candidatures_avec_notes['note_sur_10'], 1)
    p = np.poly1d(z)
    axes[1, 0].plot(candidatures_avec_notes['cv_score'], p(candidatures_avec_notes['cv_score']), 
                    "r--", alpha=0.8, label=f'Régression (r={correlation:.2f})')
    axes[1, 0].legend()
    
    # 4. Bar chart des candidatures par canal
    print("📈 Création du bar chart des candidatures par canal...")
    
    candidatures_par_canal = candidatures['canal_recrutement'].value_counts()
    
    bars = axes[1, 1].bar(candidatures_par_canal.index, candidatures_par_canal.values, 
                         color=sns.color_palette("husl", len(candidatures_par_canal)))
    axes[1, 1].set_title('Candidatures par Canal de Recrutement', fontweight='bold')
    axes[1, 1].set_xlabel('Canal de Recrutement')
    axes[1, 1].set_ylabel('Nombre de Candidatures')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    # Ajout des valeurs sur les barres
    for bar in bars:
        height = bar.get_height()
        axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                       f'{int(height)}', ha='center', va='bottom')
    
    # Ajustement de la mise en page
    plt.tight_layout()
    
    # Sauvegarde du graphique
    plt.savefig('analyse_recrutement_ibm.png', dpi=300, bbox_inches='tight')
    print("✅ Graphiques sauvegardés dans 'analyse_recrutement_ibm.png'")
    
    # Affichage du graphique
    plt.show()

def resume_analyse(candidatures, couts, entretiens, postes):
    """
    Affiche un résumé de l'analyse
    """
    print("\n" + "=" * 60)
    print("RÉSUMÉ DE L'ANALYSE")
    print("=" * 60)
    
    # Statistiques générales
    total_candidatures = len(candidatures)
    total_embauches = len(candidatures[candidatures['statut_actuel'] == 'Embauché'])
    taux_embauche_global = (total_embauches / total_candidatures * 100)
    
    print(f"\n📊 STATISTIQUES GÉNÉRALES:")
    print(f"   • Total candidatures: {total_candidatures}")
    print(f"   • Total embauches: {total_embauches}")
    print(f"   • Taux d'embauche global: {taux_embauche_global:.1f}%")
    
    # Canal le plus efficace
    candidatures_par_canal = candidatures.groupby('canal_recrutement').agg({
        'id_candidature': 'count',
        'statut_actuel': lambda x: (x == 'Embauché').sum()
    })
    candidatures_par_canal['taux_embauche'] = (candidatures_par_canal['statut_actuel'] / candidatures_par_canal['id_candidature'] * 100)
    canal_plus_efficace = candidatures_par_canal['taux_embauche'].idxmax()
    taux_canal_efficace = candidatures_par_canal['taux_embauche'].max()
    
    print(f"\n🎯 CANAL LE PLUS EFFICACE:")
    print(f"   • {canal_plus_efficace}: {taux_canal_efficace:.1f}% d'embauche")
    
    # Département avec le plus de candidatures
    candidatures_postes = candidatures.merge(postes, on='id_poste', how='inner')
    dept_plus_candidatures = candidatures_postes['departement'].value_counts().index[0]
    nb_candidatures_dept = candidatures_postes['departement'].value_counts().iloc[0]
    
    print(f"\n💼 DÉPARTEMENT LE PLUS POPULAIRE:")
    print(f"   • {dept_plus_candidatures}: {nb_candidatures_dept} candidatures")
    
    # CV score moyen
    cv_score_moyen = candidatures['cv_score'].mean()
    print(f"\n📝 CV SCORE MOYEN:")
    print(f"   • {cv_score_moyen:.1f}/100")
    
    # Coût moyen par embauche
    candidatures_couts = candidatures.merge(couts, on='id_candidature', how='inner')
    embauches_couts = candidatures_couts[candidatures_couts['statut_actuel'] == 'Embauché']
    cout_moyen_embauche = embauches_couts['cout_total'].mean()
    
    print(f"\n💰 COÛT MOYEN PAR EMBAUCHE:")
    print(f"   • {cout_moyen_embauche:.0f}€")

def main():
    """
    Fonction principale qui orchestre toute l'analyse
    """
    print("🚀 DÉBUT DE L'ANALYSE DES DONNÉES DE RECRUTEMENT IBM")
    print("=" * 60)
    
    # 1. Chargement des données
    candidatures, couts, entretiens, postes = charger_donnees()
    
    if candidatures is None:
        print("❌ Impossible de continuer sans les données")
        return
    
    # 2. Affichage des premières lignes
    afficher_premieres_lignes(candidatures, couts, entretiens, postes)
    
    # 3. Statistiques descriptives
    statistiques_descriptives(candidatures, couts, entretiens, postes)
    
    # 4. Analyses avancées
    analyses_avancees(candidatures, couts, entretiens, postes)
    
    # 5. Création des graphiques
    creer_graphiques(candidatures, couts, entretiens, postes)
    
    # 6. Résumé de l'analyse
    resume_analyse(candidatures, couts, entretiens, postes)
    
    print("\n" + "=" * 60)
    print("✅ ANALYSE TERMINÉE AVEC SUCCÈS!")
    print("=" * 60)
    print("📁 Fichiers générés:")
    print("   • analyse_recrutement_ibm.png (graphiques)")
    print("\n📊 Points clés de l'analyse:")
    print("   • Tous les graphiques ont été créés")
    print("   • Les analyses avancées ont été effectuées")
    print("   • Le résumé complet est disponible ci-dessus")

if __name__ == "__main__":
    main() 