#Test_rapide.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuration du style moderne
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

print("🎨 ANALYSE AVANCÉE IBM - VERSION SEABORN")
print("=" * 60)

try:
    # Chargement des données
    candidatures = pd.read_csv('Candidatures.CSV', encoding='utf-8')
    postes = pd.read_csv('postes.CSV', encoding='utf-8')
    entretiens = pd.read_csv('Entretiens.CSV', encoding='utf-8')
    couts = pd.read_csv('couts.CSV', encoding='utf-8')
    
    print(f"✅ Toutes les données chargées")
    
    # Jointure pour analyses complètes
    df_complet = candidatures.merge(entretiens, on='id_candidature', how='left')
    df_complet = df_complet.merge(postes, on='id_poste', how='left')
    
    print("🔗 Jointures réalisées")
    print(f"Dataset complet : {len(df_complet)} lignes")
    
    # === GRAPHIQUE 1 : Distribution CV Scores (Style Pro) ===
    plt.figure(figsize=(14, 8))
    sns.histplot(data=candidatures, x='cv_score', bins=20, kde=True, 
                 alpha=0.7, color='royalblue')
    plt.axvline(candidatures['cv_score'].mean(), color='red', linestyle='--', 
                label=f'Moyenne: {candidatures["cv_score"].mean():.1f}')
    plt.title('📊 Distribution des CV Scores - IBM Consulting 2024', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('CV Score', fontsize=14)
    plt.ylabel('Nombre de Candidats', fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # === GRAPHIQUE 2 : Analyse Multi-Variables ===
    plt.figure(figsize=(15, 10))
    sns.scatterplot(data=candidatures, x='experience_annees', y='cv_score', 
                    hue='statut_actuel', size='cv_score', sizes=(50, 200),
                    alpha=0.8)
    plt.title('🎯 CV Score vs Expérience par Statut', fontsize=16, fontweight='bold')
    plt.xlabel('Années d\'Expérience', fontsize=14)
    plt.ylabel('CV Score', fontsize=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    
    # === GRAPHIQUE 3 : Heatmap des Corrélations ===
    plt.figure(figsize=(12, 8))
    # Sélection variables numériques
    numeric_cols = ['cv_score', 'experience_annees', 'note_sur_10', 'duree_minutes']
    df_numeric = df_complet[numeric_cols].dropna()
    
    correlation_matrix = df_numeric.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu_r', center=0,
                square=True, linewidths=0.5, fmt='.3f')
    plt.title('🔥 Matrice de Corrélations - Variables Clés', 
              fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()
    
    # === GRAPHIQUE 4 : Box Plot Moderne ===
    plt.figure(figsize=(14, 8))
    sns.boxplot(data=candidatures, x='statut_actuel', y='cv_score', 
                palette='Set2')
    sns.swarmplot(data=candidatures, x='statut_actuel', y='cv_score', 
                  color='black', alpha=0.6, size=4)
    plt.title('📦 Distribution CV Scores par Statut (Box + Swarm Plot)', 
              fontsize=16, fontweight='bold')
    plt.xlabel('Statut du Candidat', fontsize=14)
    plt.ylabel('CV Score', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # === GRAPHIQUE 5 : Violin Plot (Impossible en Power BI) ===
    plt.figure(figsize=(14, 8))
    sns.violinplot(data=candidatures, x='statut_actuel', y='cv_score', 
                   palette='viridis', inner='box')
    plt.title('🎻 Densité des CV Scores par Statut (Violin Plot)', 
              fontsize=16, fontweight='bold')
    plt.xlabel('Statut du Candidat', fontsize=14)
    plt.ylabel('CV Score', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # === ANALYSES STATISTIQUES EXCLUSIVES ===
    print("\n🔬 ANALYSES STATISTIQUES AVANCÉES")
    print("=" * 50)
    
    # Corrélation CV Score vs Note Entretien
    if 'note_sur_10' in df_complet.columns:
        correlation = df_complet['cv_score'].corr(df_complet['note_sur_10'])
        print(f"📊 Corrélation CV Score ↔ Note Entretien: {correlation:.3f}")
        
        if correlation > 0.7:
            print("   ✅ Forte corrélation positive!")
        elif correlation > 0.3:
            print("   ⚠️ Corrélation modérée")
        else:
            print("   ❌ Faible corrélation")
    
    # Analyse par statut
    print(f"\n🎯 INSIGHTS BUSINESS:")
    embauches = candidatures[candidatures['statut_actuel'] == 'Embauché']
    if len(embauches) > 0:
        seuil_80 = embauches['cv_score'].quantile(0.2)
        print(f"   🏆 80% des embauchés ont CV Score > {seuil_80:.0f}")
        
        canal_perf = candidatures.groupby('canal_recrutement')['statut_actuel'].apply(
            lambda x: (x == 'Embauché').sum() / len(x) * 100
        ).sort_values(ascending=False)
        
        print(f"   📈 Meilleur canal: {canal_perf.index[0]} ({canal_perf.iloc[0]:.1f}% conversion)")
    
    print("\n✨ Analyse Seaborn terminée!")
    print("Ferme les graphiques pour voir les suivants...")
    
except Exception as e:
    print(f"❌ Erreur: {e}")