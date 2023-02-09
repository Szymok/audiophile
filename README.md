# Audiophile End-To-End ELT Pipeline

This project is an end-to-end extract, load, and transform (ELT) pipeline that extracts data from Crinacle's Headphone and InEarMonitor databases and finalizes the data for use in a Metabase dashboard.

## Architecture

The pipeline is built using the following technologies:
- Infrastructure provisioning through Terraform
- Containerization through Docker
- Orchestration through Airflow
- Dashboard creation through Metabase

## DAG Tasks
1. Scrape data from Crinacle's website to generate the "bronze" data.
2. Load the bronze data to AWS S3.
3. Initial data parsing and validation through Pydantic to generate the "silver" data.
4. Load the silver data to AWS S3.
5. Load the silver data to AWS Redshift.
6. Load the silver data to AWS RDS for future projects.
7. Transform and test the data through dbt in the warehouse.

The pipeline is designed to be flexible, allowing for the easy addition or removal of tasks as needed. The use of containerization and orchestration through Airflow also allows for easy scaling and management of the pipeline.
 
