# Automation_Android

Este projeto contém um script em **Python** que utiliza a biblioteca [uiautomator2](https://github.com/openatx/uiautomator2) para automatizar interações com um celular Android.  
O código foi criado para realizar automaticamente o **check-in diário no aplicativo Veek**, fechando recompensas e repetindo o processo algumas vezes.


## 🚀 Funcionalidades
- Fecha todos os aplicativos em segundo plano  
- Abre o app **Veek**  
- Realiza automaticamente o **check-in**  
- Clica no botão de recompensa  
- Repete o processo 3 vezes  
- No final, retorna à tela inicial e fecha todos os apps abertos  


## 📋 Pré-requisitos
Antes de rodar o script, você precisa ter:

- **Python 3.10+**  
- **ADB** (Android Debug Bridge) configurado  
- Pacotes Python instalados: 
  pip install uiautomator2 adbutils

- **Depuração USB** ativada no celular  
  - Configurações > Opções do desenvolvedor > **Depuração USB**

## 📱 Observações
- Este código foi testado em um **Samsung Galaxy M34 5G**, mas deve funcionar em outros dispositivos Android.  
- Se você usa **gestos de navegação** em vez de botões, os comandos `device.press("home")` e `device.press("recent")` continuam funcionando normalmente via ADB.  

---

## 📜 Licença
Este projeto é open-source, feito apenas para fins de estudo e automação pessoal.
