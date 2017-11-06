Title: 7. Base de données
Order: 1
Date: 2017-10-31
Slug: chapitre-7-bdd
Authors: cgeek

> <span class="icon">![](/images/icons/warning.png)</span> Page en cours de rédaction !
>
> Ce chapitre sera complété courant Novembre 2017.

## Introduction

Ce chapitre s'attarde à décrire la structure, les champs et les relations de la base de données de Duniter. Il s'agit d'une base de données SQLite, en un seul fichier.

Ainsi vous pourrez vous-même extraire des informations de la blockchain Duniter et de sa toile de confiance en rédigeant les requêtes SQL qui vous intéressent.

## Vue générale

::uml::

@startuml

database "\nBase de donnees Duniter (SQLite)" {

  package "INDEX de Blockchain" {
      component b_index
      component m_index
      component i_index
      component s_index
      component c_index
  }

  package "Piscines" {
      component idty
      component cert
      component membership
      component txs
  }

  package "Autre" {
      component block
      component peer
      component wallet
      component meta
  }
}

@enduml

::end-uml::


> Passer à la suite du tutoriel : [Chapitre 8 : Addons C/C++](../chapitre-8-addons).
