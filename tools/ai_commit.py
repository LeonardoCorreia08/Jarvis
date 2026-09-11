import sys
import os
import subprocess
from google import genai

def get_git_diff():
    try:
        result = subprocess.run(['git', 'diff', '--cached'], capture_output=True, text=True, encoding='utf-8')
        return result.stdout
    except Exception as e:
        return f"Erro ao pegar diff: {e}"

def generate_commit_message(diff_text):
    if not diff_text.strip():
        return "chore: empty commit"
    
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
Você é um especialista em Git e Conventional Commits.

Analise o git diff abaixo e identifique a intenção principal da alteração.

O objetivo NÃO é simplesmente traduzir ou descrever o código alterado.

Determine:
1. O que mudou?
2. Qual é a intenção da alteração?
3. Qual é o impacto funcional?
4. Qual tipo de Conventional Commit representa melhor essa mudança?

Tipos permitidos:
feat
fix
refactor
perf
docs
test
build
ci
chore
style

Regras:
- Retorne APENAS uma única linha.
- Escreva em português.
- Não utilize markdown.
- Não utilize aspas.
- Não explique sua decisão.
- Não invente funcionalidades que não estejam evidentes no diff.
- Priorize a intenção da alteração.
- Seja objetivo.

Diff:
{diff_text}
"""
        
        # Usando exatamente o modelo que apareceu no seu terminal
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        # Removi o limite de caracteres do erro para, se der ruim, lermos tudo
        return f"chore: erro na ia - {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)
        
    commit_msg_filepath = sys.argv[1]
    
    diff = get_git_diff()
    ai_message = generate_commit_message(diff)
    
    with open(commit_msg_filepath, 'w', encoding='utf-8') as f:
        f.write(ai_message)