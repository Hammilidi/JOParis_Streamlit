import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Charger les données
df = pd.read_csv("data/parisOlympics.csv")


# Fonction pour afficher la page d'accueil avec une image et une description
def accueil():
    st.title("Page d'Accueil")
    
    # Afficher une image (ajustez le chemin de l'image selon votre emplacement)
    st.image("images/joParis.jpg", caption="Logo du projet", use_container_width=True)
    
    # Ajouter une description du projet
    st.markdown("""
    ## Description du Projet
    
    Ce projet analyse les performances des pays lors des derniers Jeux Olympiques. Il offre des visualisations interactives pour examiner la répartition des médailles par pays, la comparaison des résultats par type de médaille et la corrélation entre les différentes catégories de médailles. 
    
    Les objectifs de ce projet sont les suivants :
    - Analyser les tendances des performances olympiques à travers les médailles d'or, d'argent et de bronze.
    - Comparer les résultats de différents pays et comprendre les facteurs qui influencent leur succès.
    - Offrir des visualisations claires et interactives pour mieux comprendre les données olympiques.
    
    Ce projet utilise des données détaillées des derniers Jeux Olympiques pour créer des graphiques et des analyses permettant de mieux comprendre la répartition et la concurrence entre les pays.
    """)

# Fonction pour afficher les conclusions
def conclusions():
    st.title("Conclusions")

    st.markdown("""
    ## Synthèse des Observations

    Après avoir exploré les différentes analyses des performances olympiques, voici les principales conclusions que nous pouvons tirer :

    1. **Les États-Unis dominent largement** dans les classements olympiques, notamment grâce à un grand nombre de médailles d'or. Ils sont suivis par la Chine, qui est également très compétitive dans toutes les catégories de médailles.
    
    2. **La Russie, l'Allemagne, le Royaume-Uni et le Japon** se distinguent dans le top 6 des pays ayant remporté le plus grand nombre de médailles. Cependant, il existe un écart considérable entre ces pays et les autres.
    
    3. **Les pays plus petits**, tels que la Hongrie, l'Ukraine et le Kazakhstan, parviennent à se distinguer par un nombre respectables de médailles, ce qui démontre que la compétition n'est pas uniquement dominée par les plus grandes puissances.
    
    4. **Corrélation forte** : Les pays les plus performants dans les médailles d'or tendent également à exceller dans les médailles d'argent et de bronze. Cela indique une domination générale de ces pays dans les compétitions sportives.
    
    5. **Comparaison avec la France** : La France, bien qu'elle soit loin des pays les plus médaillés, reste compétitive avec un nombre de médailles notables en comparaison avec d'autres pays.

    6. **Concentration des succès** : Le graphique de la répartition des médailles montre une forte concentration des succès parmi les superpuissances sportives. Il existe un petit nombre de pays qui remportent une large majorité des médailles, laissant peu de places pour les autres nations.

    ## Conclusion finale

    En résumé, les Jeux Olympiques montrent une domination des grandes puissances, notamment les États-Unis et la Chine, mais aussi des pays comme la Russie et l'Allemagne. Les données soulignent l'importance de l'investissement en sport de haut niveau pour la performance des pays, et les analyses mettent en évidence des tendances intéressantes pour de futures compétitions.
    """)

# Fonction pour l'analyse 1 : Dimension du dataset et informations générales
def analyse_1():
    st.title("Informations Générales sur le Dataset")

    # Affichage des 5 premières lignes du DataFrame
    st.subheader("Extrait du dataset")
    st.write(df.head())
    
    # Statistiques descriptives generales
    st.subheader("Statistiques Descriptives genérales")
    st.write(df.describe())
    
    # Afficher les informations générales du DataFrame
    st.subheader("Informations Générales")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)
    
    
    # Interprétation sous forme de liste
    st.subheader("Comprehension de Données")
    st.markdown("""
        - **Position**: Classement du pays
        - **Country**: Nom du pays
        - **Gold**: Nombre de médailles d'or
        - **Silver**: Nombre de médailles d'argent
        - **Bronze**: Nombre de médailles de bronze
        - **Total Medals**: Nombre total de médailles obtenues
    """)


# Fonction pour l'analyse 2 : Répartition des Médailles par Pays
def analyse_2():
    st.title("Répartition des Médailles par Pays")
    
    # Graphique de la répartition des médailles
    st.write("Répartition des médailles par pays (top 20) :")
    fig, ax = plt.subplots(figsize=(10, 7))
    df.head(20).set_index('Country')[['Gold', 'Silver', 'Bronze']].plot(kind='bar', stacked=True, ax=ax, title="Répartition des Médailles par Pays")
    st.pyplot(fig)
    
    # Interprétation
    st.markdown("""

Le graphique montre la répartition des médailles d'or, d'argent et de bronze entre les différents pays. Quelques observations clés :

- Les États-Unis ont le plus grand nombre de médailles au total, avec une avance dominante sur les médailles d'or. 
- La Chine suit de près les États-Unis au total des médailles, avec de bonnes performances dans les trois catégories.
- Les athlètes russes ont le troisième total le plus élevé, principalement grâce aux médailles d'argent et de bronze.
- L'Allemagne, le Royaume-Uni et le Japon complètent le top 6 des pays au total des médailles.
- Il y a un écart important entre les premiers pays et le reste, indiquant une forte concentration des succès en médailles.
- Certains pays plus petits comme la Hongrie, le Kazakhstan et l'Ukraine se sont taillé une place respectable en médailles.
- Le graphique offre une perspective visuelle claire sur les hiérarchies de médailles et les forces nationales dans les différentes compétitions sportives.
        """)

# Fonction pour l'analyse 3 : Total des Médailles par Pays
def analyse_3():
    st.title("Total des Médailles par Pays")
    
    # Graphique des totaux des médailles par pays
    st.write("Total des médailles par pays (top 40) :")
    fig, ax = plt.subplots(figsize=(10, 7))
    df[['Country', 'Total Medals']].head(40).plot(x='Country', y='Total Medals', kind='bar', ax=ax, title="Total des Médailles par Pays", legend=False)
    st.pyplot(fig)
    
    # Interprétation
    st.markdown("""Analyse du graphique "Total des Médailles par Pays":

- Les États-Unis dominent largement avec plus de 100 médailles au total, suivis de loin par la Chine qui en totalise environ 90.
- La Russie complète le podium avec environ 75 médailles.
- L'Allemagne, le Royaume-Uni et le Japon forment le reste du top 6 des pays les plus médaillés.
- Il y a un écart significatif entre les pays les mieux classés et le reste du tableau.
- Certains pays plus petits comme la Hongrie, l'Ukraine et le Kazakhstan parviennent à se distinguer avec un nombre respectable de médailles.
- Ce graphique offre une vue d'ensemble claire de la répartition totale des médailles entre les différentes nations participantes.

En résumé, ce graphique met en évidence les principaux pays dominants ainsi que le niveau de concentration des succès olympiques.""")


# Fonction pour l'analyse 5 : Répartition des médailles (Sous-graphiques)
def analyse_4():
    st.title("Répartition des Médailles par Type")

    # Création des DataFrames triés pour Gold, Silver, Bronze
    gold_rank = df.sort_values(by='Gold', ascending=False)[['Country', 'Gold']].reset_index(drop=True)
    silver_rank = df.sort_values(by='Silver', ascending=False)[['Country', 'Silver']].reset_index(drop=True)
    bronze_rank = df.sort_values(by='Bronze', ascending=False)[['Country', 'Bronze']].reset_index(drop=True)

    # Création des sous-graphiques
    fig, axs = plt.subplots(3, 1, figsize=(12, 16))

    # 1er sous-graphe : Médailles d'or
    axs[0].bar(gold_rank["Country"].head(10), gold_rank["Gold"].head(10), color="#e7bb19")
    axs[0].set_title("Top 10 pays Médailles d'or")
    axs[0].set_xlabel("Pays")
    axs[0].set_ylabel("Nombre de Médailles d'or")
    axs[0].tick_params(axis='x', rotation=90)

    # 2ème sous-graphe : Médailles d'argent
    axs[1].bar(silver_rank["Country"].head(10), silver_rank["Silver"].head(10), color="#c1bfb7")
    axs[1].set_title("Top 10 pays Médailles d'argent")
    axs[1].set_xlabel("Pays")
    axs[1].set_ylabel("Nombre de Médailles d'argent")
    axs[1].tick_params(axis='x', rotation=90)

    # 3ème sous-graphe : Médailles de bronze
    axs[2].bar(bronze_rank["Country"].head(10), bronze_rank["Bronze"].head(10), color="#a05c05")
    axs[2].set_title("Top 10 pays Médailles de Bronze")
    axs[2].set_xlabel("Pays")
    axs[2].set_ylabel("Nombre de Médailles de bronze")
    axs[2].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    st.pyplot(fig)
    
    # Interprétation
    st.markdown("""Analyse du graphique des médailles d'or, d'argent et de bronze :

Pour les médailles d'or, les États-Unis dominent largement avec plus de 39 médailles, suivis de la Chine avec environ 32 et du Japon avec 27. 

En médailles d'argent, la hiérarchie est similaire, avec les États-Unis en tête, la Chine seconde et la Russie troisième.

Concernant les médailles de bronze, les États-Unis, la Chine et la Russie restent dans le top 3, avec une forte présence des équipes chinoises et américaines en particulier.

Dans l'ensemble, ce graphique met en évidence la supériorité des grandes puissances sportives traditionnelles comme les États-Unis, la Chine et la Russie, qui trustent la majorité des médailles dans les trois catégories.
""")


# Fonction pour l'analyse  : Comparaison avec la France
def analyse_5():
    st.title("Comparaison des Médailles avec la France")
    
    # Filtrer les données pour la France
    france_data = df[df['Country'] == 'France (FRA)']
    other_countries_data = df[df['Country'] != 'France (FRA)']

    # Comparaison des médailles par pays
    fig, axs = plt.subplots(4, 1, figsize=(18, 30))

    # Comparaison des Médailles d'or
    axs[0].bar(other_countries_data['Country'], other_countries_data['Gold'], color='lightblue')
    axs[0].bar(france_data['Country'], france_data['Gold'], color='blue')
    axs[0].set_title("Comparaison des Médailles d'or")
    axs[0].set_xlabel("Country")
    axs[0].set_ylabel("Médailles d'or")
    axs[0].tick_params(axis='x', rotation=90)

    # Comparaison des Médailles d'argent
    axs[1].bar(other_countries_data['Country'], other_countries_data['Silver'], color='lightgrey')
    axs[1].bar(france_data['Country'], france_data['Silver'], color='white', edgecolor='black')
    axs[1].set_title("Comparaison des Médailles d'argent")
    axs[1].set_xlabel("Country")
    axs[1].set_ylabel("Médailles d'argent")
    axs[1].tick_params(axis='x', rotation=90)

    # Comparaison des Médailles de bronze
    axs[2].bar(other_countries_data['Country'], other_countries_data['Bronze'], color='lightcoral')
    axs[2].bar(france_data['Country'], france_data['Bronze'], color='red')
    axs[2].set_title("Comparaison des Médailles de bronze")
    axs[2].set_xlabel("Country")
    axs[2].set_ylabel("Médailles de bronze")
    axs[2].tick_params(axis='x', rotation=90)

    # Comparaison du Total des Médailles
    axs[3].bar(other_countries_data['Country'], other_countries_data['Total Medals'], color='grey')
    axs[3].bar(france_data['Country'], france_data['Total Medals'], color='blue')
    axs[3].set_title("Comparaison du Total des Médailles")
    axs[3].set_xlabel("Country")
    axs[3].set_ylabel("Total des Médailles")
    axs[3].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    st.pyplot(fig)
    
    # Interprétation
    st.markdown("""Voici une analyse concise des graphiques de comparaison des médailles :

- Les États-Unis dominent largement en médailles d'or, suivis de la Chine et du Japon.
- La Russie obtient de très bons résultats en médailles d'argent et de bronze.
- La France est nettement distancée par les pays leaders.
- Il y a un écart important entre les principaux pays médaillés et les autres.
- Des pays plus petits comme la Hongrie, l'Ukraine et le Kazakhstan obtiennent des médailles respectives.

Ces données soulignent la concentration du succès olympique parmi les superpuissances sportives que sont les États-Unis, la Chine et la Russie.""")

# Fonction pour l'analyse 6 : Corrélation entre les médailles
def analyse_6():
    st.title("Corrélation entre les types de Médailles")
    
    # Calcul et affichage de la corrélation
    corr_matrix = df[['Gold', 'Silver', 'Bronze']].corr()
    st.write(corr_matrix)
    
    # Heatmap de la corrélation
    fig, ax = plt.subplots(figsize=(4, 4))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    ax.set_title("Corrélation entre les différents types de médailles")
    st.pyplot(fig)
    
    # Interprétation
    st.markdown("""La matrice de corrélation fournie montre les coefficients de corrélation entre les médailles d'or, d'argent et de bronze. Chaque coefficient de corrélation mesure la force et la direction de la relation linéaire entre deux variables. Ces valeurs sont comprises entre -1 et 1 :

- **1** signifie une corrélation parfaitement positive (les variables augmentent ensemble).
- **0** signifie aucune corrélation (aucune relation linéaire).
- **-1** signifie une corrélation parfaitement négative (l'une augmente tandis que l'autre diminue).

### Matrice de Corrélation :
|         | Gold  | Silver | Bronze |
|---------|-------|--------|--------|
| **Gold**  | 1.000 | 0.911  | 0.882  |
| **Silver**| 0.911 | 1.000  | 0.941  |
| **Bronze**| 0.882 | 0.941  | 1.000  |

### Interprétations :

1. **Corrélation entre les Médailles d'Or et d'Argent (0.911)** :
   - Il y a une forte corrélation positive (0.911) entre le nombre de médailles d'or et d'argent. Cela signifie que les pays qui gagnent beaucoup de médailles d'or ont tendance à gagner aussi beaucoup de médailles d'argent.
  
2. **Corrélation entre les Médailles d'Or et de Bronze (0.882)** :
   - La corrélation positive (0.882) entre les médailles d'or et de bronze est également élevée, bien qu'un peu plus faible que celle avec les médailles d'argent. Cela signifie que les pays qui remportent de nombreuses médailles d'or gagnent également un nombre important de médailles de bronze, bien que l'association soit légèrement moins forte.
  
3. **Corrélation entre les Médailles d'Argent et de Bronze (0.941)** :
   - La corrélation la plus élevée est entre les médailles d'argent et de bronze (0.941), indiquant une très forte relation positive. Cela signifie que les pays qui gagnent beaucoup de médailles d'argent ont presque systématiquement un nombre élevé de médailles de bronze.

### Conclusions :

1. **Performance Globale** :
   - Les fortes corrélations entre les différents types de médailles suggèrent que les pays performants dans une catégorie de médailles (or, argent ou bronze) tendent à être performants dans les autres catégories également. Autrement dit, les pays qui ont une forte performance olympique sont souvent capables de remporter des médailles dans toutes les couleurs.

2. **Dominance de Certains Pays** :
   - Les pays les plus performants tendent à accumuler des médailles de tous types, ce qui pourrait indiquer une domination générale dans les compétitions, indépendamment du niveau de la médaille.

3. **Stratégie de Compétition** :
   - Une autre conclusion possible est que les pays qui investissent dans le sport de haut niveau et qui sont bien préparés ont une meilleure chance de remporter des médailles, qu'elles soient d'or, d'argent ou de bronze. Les fortes corrélations pourraient refléter les efforts globaux de ces pays dans la préparation et la compétition.

4. **Pas de Spécialisation Marquée** :
   - Les fortes corrélations entre les médailles suggèrent qu'il n'y a pas de spécialisation marquée dans une seule couleur de médaille. Par exemple, un pays ne se spécialise pas uniquement dans l'obtention des médailles d'or au détriment des médailles d'argent ou de bronze, mais tend à être compétitif globalement.

En résumé, ces corrélations indiquent que les performances olympiques sont globales et non spécifiques à un type de médaille, les pays les plus performants ayant tendance à exceller dans toutes les catégories de médailles.
    """)







# Barre de navigation pour sélectionner l'analyse
analysis_options = [
    "Accueil", "Exploration", "Répartition des Médailles par pays",
    "Total des Médailles", "Répartition des Médailles par Type", 
    "Comparaison avec la France", "Corrélation entre les médailles", "Conclusions"
]

selected_analysis = st.sidebar.selectbox("Sélectionner l'analyse", analysis_options)

# Affichage de l'analyse ou de la page d'accueil
if selected_analysis == "Accueil":
    accueil()
elif selected_analysis == "Exploration":
    analyse_1()
elif selected_analysis == "Répartition des Médailles par pays":
    analyse_2()
elif selected_analysis == "Total des Médailles":
    analyse_3()
elif selected_analysis == "Répartition des Médailles par Type":
    analyse_4()
elif selected_analysis == "Comparaison avec la France":
    analyse_5()
elif selected_analysis == "Corrélation entre les médailles":
    analyse_6()
elif selected_analysis == "Conclusions":
    conclusions()