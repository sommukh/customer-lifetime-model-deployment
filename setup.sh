mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = 5000\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
