from nicegui import ui

def sumar():
    try:
        resultado.text = f'{float(numero1.value) + float(numero2.value)}'
    except:
        resultado.text = 'Ingresa numeros validos'

def limpiar():
    numero1.value = ''
    numero2.value = ''
    resultado.text = 'Resultado: 0'

with ui.column().classes('w-full h-screen items-center justify-center'):
    with ui.card().style('width:400px; background-color:purple').classes('items-center'):
        ui.label('Calculadora de Suma').style('color:white; font-size:24px; font-weight:bold; width:380px').classes('text-center')

        numero1 = ui.input('Numero 1').props('dark outlined').style('width:380px')
        numero2 = ui.input('Numero 2').props('dark outlined').style('width:380px')

        with ui.row().classes('w-full justify-center no-wrap').style('gap:10px;'):
            ui.button('SUMAR', icon='calculate', color='green', on_click=sumar).style('color:white; width:140px')
            ui.button('LIMPIAR', icon='delete', color='red', on_click=limpiar).style('color:white; width:140px')

        resultado = ui.label('Resultado: 0').style('color:white; font-size:20px')

ui.run()
