## How to use 

### image build

- `docker build -t streamlit-demo .`

### conatiner run 

- `docker run --rm -it --name streamlit-demo -p 8501:8501 -v path:/app streamlit-demo /bin/bash`

### app start

### Table data dashboard
- `streamlit run table_data_dashboard.py <data_path>`

### Timeseries data dashboard
- `streamlit run timeseries_data_dashboard.py <data_path>`

### Model tuning
- `streamlit run model_tuning.py <data_and_model_path>`