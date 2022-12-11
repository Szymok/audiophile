Audiophile End-To-End ELT Pipeline
Pipeline that extracts data from Crinacle's Headphone and InEarMonitor databases and finalizes data for a Metabase Dashboard.

Architecture
Architecture

Infrastructure provisioning through Terraform, containerized through Docker and orchestrated through Airflow. Created dashboard through Metabase.

DAG Tasks:

Scrape data from Crinacle's website to generate bronze data.
Load bronze data to AWS S3.
Initial data parsing and validation through Pydantic to generate silver data.
Load silver data to AWS S3.
Load silver data to AWS Redshift.
Load silver data to AWS RDS for future projects.
and 8. Transform and test data through dbt in the warehouse.
