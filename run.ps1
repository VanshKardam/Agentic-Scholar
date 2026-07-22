Write-Host "Activating Virtual Environment..."
. .\.venv\Scripts\Activate.ps1
Write-Host "Starting Streamlit App..."
streamlit run app.py