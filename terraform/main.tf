terraform {
  required_providers {
    google = {
        source  = "hashicorp/google"
        version = ">= 4.0"
    }
  }
  required_version = ">= 1.3.0"
}

provider "google" {
  project = "advance-display-462217-r9"
  region  = "northamerica-northeast2" 
}

resource "google_container_cluster" "primary" {
    name     = "ci-cd-gke-cluster"
    location = "northamerica-northeast2"

    remove_default_node_pool = true
    initial_node_count        = 1

    ip_allocation_policy {}
}

resource "google_container_node_pool" "primary_nodes" {
    name      = "default-pool"
    cluster   = google_container_cluster.primary.name
    location  = google_container_cluster.primary.location

    node_config {
        machine_type = "e2-medium"
    }

    initial_node_count = 2
}