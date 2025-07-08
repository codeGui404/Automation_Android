from adbutils import device
import uiautomator2
import time

d = uiautomator2.connect()

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

#Fechamento do primeiro anúncio
device(text="Ir para o app").click()
time.sleep(2)

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
    time.sleep(10)  # Espera 10 segundos antes de iniciar o próximo ciclo
    # Clica em "Fazer Check in novamente"
    if device(text="Fazer Check in novamente").exists:
        device(text="Fazer Check in novamente").click()
        print(" Clique em 'Fazer Check in novamente'")
    else:
        print(" Botão 'Fazer Check in novamente' não encontrado.")
        continue  # pula para o próximo ciclo

    time.sleep(5)  # tempo para o anúncio carregar

    # Aguarda o botão "Recompensa concedida" por até 60 segundos
    if device(text="Recompensa concedida").wait(timeout=60):
        device(text="Recompensa concedida").click()
        print(" Recompensa concedida clicada.")
        time.sleep(10)
    else:
        print(" Botão 'Recompensa concedida' não apareceu após o anúncio.")
        time.sleep(5)
