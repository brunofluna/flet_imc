import flet as ft
''' Para gerar o executável do app:
pip install pyinstaller
pip install pillow
flet pack nome_arquivo.py --icon nome_icone.png
'''

def main(page: ft.Page):
    # evento
    def calcula_imc(e):
        try:
            peso_val = float(peso.value)
            altura_val = float(altura.value)
            imc_val = peso_val / (altura_val ** 2)
            imc.value = f"{imc_val:.2f}"

            if imc_val <= 16.9:
                resultado_imc = 'está muito abaixo do peso.'
            elif imc_val < 18.5:
                resultado_imc = 'está abaixo do peso.'
            elif imc_val < 25:
                resultado_imc = 'está no seu peso ideal.'
            elif imc_val < 30:
                resultado_imc = 'está acima do seu peso ideal.'
            elif imc_val < 40:
                resultado_imc = 'está com obesidade nível II.'
            else:
                resultado_imc = 'está com obesidade mórbida.'

            result.value = f"{nome.value} {resultado_imc}"
            nome.value = ""
            peso.value = ""
            altura.value = ""
            page.update()
        except ValueError:
            result.value = "Por favor, insira valores válidos para peso e altura."
            page.update()

    page.title = "CÁLCULO IMC"
    page.scroll = "adaptive"
    page.theme_mode= ft.ThemeMode.LIGHT
    nome = ft.TextField(label= "Nome")
    peso = ft.TextField(label="Peso",suffix_text="kg")
    altura = ft.TextField(label="Altura",suffix_text="m")
    imc = ft.Text(size=30)
    result = ft.Text(size=30)

    page.add(
        ft.Row(
            [ft.Text("IMC", size=40, weight= "bold")],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [peso],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [altura],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Calcular IMC", on_click=calcula_imc)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )

    )
    page.update()
ft.app(main)
