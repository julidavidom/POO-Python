'''
Para correr el progrma hay que inicializar el ambient virtul
en el terminal de comandos
        python -m venv env
        env\Scripts\activate.bat
        pip install bokeh

'''

from bokeh.plotting import figure,output_file, show


if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig=figure()
    total_vals= int(input('Cuantos valores queires graficar'))
    x_val=list(range(total_vals))
    y_val=[]
    for x in x_val:
        val = int(input(f'Valor Y para {x} '))
        y_val.append(val)
    fig.line(x_val, y_val, line_width=2)
    show(fig)
