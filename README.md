API de Conversão de PDF para MP3

**Descrição**

Esta API permite a conversão de arquivos PDF para MP3. O texto do PDF é extraído e convertido em áudio usando o motor de síntese de voz PyTTSx3.

**Requisitos**

Python 3.8 ou superior Flask Flask-RESTful PyPDF2 pyttsx3

**Instalação**

pip install -r requirements.txt

**Execução**

python main.py

**Rotas**

/convert

Método: POST

Descrição: Converte um arquivo PDF para MP3.

**Parâmetros:**

file_path: Caminho do arquivo PDF a ser convertido. Retorno:

output_path: Caminho do arquivo MP3 gerado.

**Próximos passos**

Adicionar mais informações à documentação, como o formato do arquivo PDF ou os requisitos de hardware e software necessários.
Implementar suporte para outros formatos de arquivo, como DOCX, PPT e XLSX.
Aperfeiçoar a qualidade do áudio gerado.
Implementar um banco de dados
