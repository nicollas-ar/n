# Site Santa Teresinha

1. `pip install -r requirements.txt`
2. `python app.py`
3. Abra http://127.0.0.1:5000 (no celular: http://IP_DO_PC:5000, na mesma rede Wi-Fi)

Para ampliar o conteúdo, basta adicionar itens nos JSONs em `static/data/`:
- quiz.json: {"pergunta": "...", "opcoes": ["A","B","C","D"], "correta": 0, "explicacao": "..."}
- curiosidades.json: {"tipo": "Curiosidade", "texto": "..."}
(`correta` é o índice, começando em 0, da opção certa.)
