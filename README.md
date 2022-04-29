# Python-Client-Template-for-gcp

This template helps in you to understand the python client template for GCP. This template consists of python code to list instacnes, list snapshot(no data source in terraform because of which it is very important), copy object between different buckets.

To use this first install the requirements for this python scripts using below commands:

    pip3 install -r requirements.txt

Now, after installing the requirements run, run below commands:

        export GOOGLE_APPLICATION_CREDENTIALS=path/to/service/account/file
        export GCP_PROJECT="project-id-of-gcp"

Also, check each source code and export required varibales.
After that run below commands:

    python3 path/to/file
