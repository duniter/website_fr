Title: Architecture
Order: 10
Date: 2017-10-09
Slug: architecture
Authors: vit

## Architecture réseau des clients

Voici un aperçu de l'architecture de Duniter entre les clients et un serveur.

::uml:: format="svg" alt="architecture clients"

@startuml

title Architecture clients de Duniter

node "Duniter" {

    interface "HTTP" as HTTP_duniter

    HTTP_duniter - [Basic Merkle Api]
}

database "Elastic Search" as ES {

    interface "HTTP" as HTTP_ES

    frame "Duniter4j Plugin" {

        [Sync] -- HTTP_duniter
    }

    [Members Profiles Index]
    [Companies Registry Index]
    [Market Place Index]
}


package "Cesium" {

    interface "client BMA" as client_bma

    frame "ES Data Store Plugin" {
        interface "client ES" as client_es

        [Members Profiles]
        [Companies Registry]
        [Market Place]
        client_es --- HTTP_ES
    }

    client_bma -- HTTP_duniter

}

package "Duniter Android App" {

    frame "Duniter4j API" {
        interface "client BMA" as client_android_bma

        client_android_bma --- HTTP_duniter
    }
}

package "Sakia" {

    frame "Duniter Python API" {
        interface "client BMA" as client_sakia

        client_sakia --- HTTP_duniter
    }
}

@enduml

::end-uml::
