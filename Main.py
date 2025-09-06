from adbutils import device
import uiautomator2
import time

device = uiautomator2.connect()

#Pressiona o botão home
device.press("home")

# Pressiona o botão de apps recentes
device.press("recent")
time.sleep(2)

# Click do botão de fechar todos os apps
if device(textContains="Fechar tudo").exists:
    device(textContains="Fechar tudo").click()
    time.sleep(2)

# Abertura do app Veek
device.shell(f"am start -n br.com.veek.app/.MainActivity")

# Botão para fazer o check-in
device(text="Check-in").click()
time.sleep(2)

# Fazer o check-in
device(text="Fazer Check-in").click()
time.sleep(35)
# Fechar o anúncio
if device(text="Recompensa concedida").wait(timeout=60):
    device(text="Recompensa concedida").click()
    print(" Recompensa concedida clicada.")
else:
    print(" Botão 'Recompensa concedida' não apareceu após o anúncio.")
    time.sleep(10)

# Repetição do processo de check-in
for i in range(3):
    print(f"\n Iniciando ciclo {i+2} de 4")
    time.sleep(10)  # espera antes do próximo ciclo

    # Clica no botão azul usando a classe do elemento
    # Esta linha vai procurar o primeiro botão na tela
    primeiro_botao_encontrado = device(className="android.widget.Button")

    if primeiro_botao_encontrado.count > 0:
        primeiro_botao_encontrado[0].click()
        print(" Botão de check-in clicado.")
    else:
        print(" Nenhum botão foi encontrado.")
        break 
    device(text="Fazer um novo Check-in").click()    
    time.sleep(35)  

    # Aguarda o botão "Recompensa concedida"
    if device(text="Recompensa concedida").wait(timeout=60):
        device(text="Recompensa concedida").click()
        print(" Recompensa concedida clicada.")
        time.sleep(10)
    else:
        print(" Botão 'Recompensa concedida' não apareceu após o anúncio.")
        time.sleep(5)

    # === Final da automação ===
print("\n [INFO] Finalizando automação...")

# Pressiona o botão home
device.press("home")
time.sleep(1)

# Pressiona o botão de apps recentes
device.press("recent")
time.sleep(2)

# Clica no botão "Fechar tudo", se existir
if device(textContains="Fechar tudo").exists:
    device(textContains="Fechar tudo").click()
    print(" Todos os aplicativos foram fechados.")
    time.sleep(2)
else:
    print(" Botão 'Fechar tudo' não encontrado.")